#!/usr/bin/env python3
"""Self-updating content for Beautiful.Life (run daily by GitHub Actions).
- Pulls uplifting news from public RSS feeds  -> data/news.json
- Pulls new talks from YouTube channel feeds  -> data/videos.json (merged with curated list)
- Refreshes sitemap <lastmod> dates
Standard library only. Failures in any single source are ignored so the site never breaks.
"""
import json, os, re, datetime, html, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (BeautifulLife feed bot; +https://beautiful.life)"}

NEWS_FEEDS = [
    ("Good News Network", "https://www.goodnewsnetwork.org/feed/"),
    ("Good News Network", "https://www.goodnewsnetwork.org/category/news/health/feed/"),
    ("Positive News", "https://www.positive.news/feed/"),
    ("Reasons to be Cheerful", "https://reasonstobecheerful.world/feed/"),
    ("Greater Good Magazine", "https://greatergood.berkeley.edu/site/rss/articles"),
]
YT_CHANNELS = [
    ("TED", "UCAuUUnT6oDeKwE6v1NGQxug"),
    ("TEDx Talks", "UCsT0YIqwnpJCM-mx7-gSA4Q"),
]
SKIP = re.compile(r"horoscope|good news in history|astrology|shooting|killed|murder|war\b", re.I)
CATS = [
    ("health", r"health|medic|patient|doctor|cancer|disease|hospital|treatment|sleep|mental|brain"),
    ("planet", r"climate|wildlife|species|ocean|forest|river|energy|solar|green|nature|bird|whale|bear|animal|plant|reef"),
    ("science", r"scien|research|discover|space|mars|astronom|study|tech|robot|ai\b"),
    ("kindness", r"kind|donat|rescue|volunteer|neighbo|stranger|hero|gift|charity|help"),
]
VID_KEYS = re.compile(r"happ|life|love|purpose|mind|stress|sleep|habit|meaning|friend|relationship|money|wellbeing|well-being|calm|anxiety|joy|gratitude|kind|health|brain|grow|learn|success|fear|courage|lonel", re.I)
VID_CAT = [("love", r"love|friend|relationship|lonel|kind"), ("money", r"money|wealth|rich|financ"), ("body", r"sleep|health|body|exercise|food"),
           ("purpose", r"purpose|meaning|work|career"), ("growth", r"habit|learn|grow|success|fear|courage"), ("mind", r".")]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

def clean(s, n=220):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"The post .* appeared first on .*$", "", s).strip()
    return (s[:n].rsplit(" ", 1)[0] + "…") if len(s) > n else s

def parse_date(s):
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            d = datetime.datetime.strptime((s or "").strip(), fmt)
            if d.tzinfo is None: d = d.replace(tzinfo=datetime.timezone.utc)
            return d.isoformat()
        except Exception: pass
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def categorize(text, table, default):
    for c, rx in table:
        if re.search(rx, text, re.I): return c
    return default

def update_news():
    path = os.path.join(ROOT, "data", "news.json")
    old = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {"items": []}
    items, seen = [], set()
    for source, url in NEWS_FEEDS:
        try:
            root = ET.fromstring(fetch(url))
            for it in root.iter("item"):
                title = clean(it.findtext("title"), 160); link = (it.findtext("link") or "").strip()
                if not title or not link or link in seen or SKIP.search(title): continue
                summary = clean(it.findtext("description"))
                seen.add(link)
                items.append({"title": title, "link": link, "summary": summary, "source": source,
                              "date": parse_date(it.findtext("pubDate")), "cat": categorize(title + " " + summary, CATS, "world")})
        except Exception as ex:
            print("news source failed:", url, ex)
    if len(items) < 6:  # keep previous content if sources were unreachable
        items += [o for o in old.get("items", []) if o["link"] not in seen]
    items.sort(key=lambda x: x["date"], reverse=True)
    json.dump({"updated": datetime.datetime.now(datetime.timezone.utc).isoformat(), "items": items[:60]},
              open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("news items:", len(items[:60]))

def update_videos():
    path = os.path.join(ROOT, "data", "videos.json")
    data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {"items": []}
    curated = [v for v in data["items"] if v.get("curated")]
    fresh, ids = [], {v["id"] for v in curated}
    ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
    for name, cid in YT_CHANNELS:
        try:
            root = ET.fromstring(fetch(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"))
            for en in root.findall("a:entry", ns):
                vid = en.findtext("yt:videoId", namespaces=ns); title = en.findtext("a:title", namespaces=ns) or ""
                if vid and vid not in ids and VID_KEYS.search(title) and "#shorts" not in title.lower():
                    ids.add(vid)
                    fresh.append({"id": vid, "title": html.unescape(title), "channel": name, "cat": categorize(title, VID_CAT, "mind"),
                                  "date": en.findtext("a:published", namespaces=ns)})
        except Exception as ex:
            print("video source failed:", cid, ex)
    previous = [v for v in data["items"] if not v.get("curated") and v["id"] not in ids]
    auto = (fresh + previous)[:24]
    # newest auto picks first, then the evergreen curated library
    json.dump({"updated": datetime.datetime.now(datetime.timezone.utc).isoformat(), "items": auto + curated},
              open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("videos:", len(auto) + len(curated))

def touch_sitemap():
    p = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(p):
        s = open(p, encoding="utf-8").read()
        today = datetime.date.today().isoformat()
        s = re.sub(r"(<loc>https://beautiful\.life/(?:good-news\.html)?</loc><lastmod>)[^<]+", r"\g<1>" + today, s)
        open(p, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    update_news(); update_videos(); touch_sitemap()
