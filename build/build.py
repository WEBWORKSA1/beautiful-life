# -*- coding: utf-8 -*-
"""Beautiful.Life static site generator.
Run:  python3 build/build.py   (from repo root)
Outputs plain HTML files that GitHub Pages serves directly from the main branch.
"""
import json, os, datetime, html
from content import PILLARS, ARTICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://beautiful.life"
NAME = "Beautiful.Life"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
INQUIRY_URL = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()
PILL = {p[0]: p for p in PILLARS}

TOOLS = [
    ("wheel-of-life", "Wheel of Life", "🎡", "Score 8 life areas and see your balance on an interactive chart.", "wheel"),
    ("happiness-check", "Life Satisfaction Check", "😊", "An 8-statement self-check with a personalised next step.", "quiz"),
    ("habit-tracker", "Habit Tracker", "✅", "Track daily habits and streaks. Private, no sign-up.", "habits"),
    ("gratitude-journal", "Gratitude Journal", "📓", "Three good things a day, with rotating prompts and export.", "gratitude"),
    ("sleep-calculator", "Sleep Cycle Calculator", "🌙", "Find bed and wake times that line up with sleep cycles.", "sleep"),
    ("life-in-weeks", "Your Life in Weeks", "⏳", "See every week of your life on one grid. A powerful perspective.", "weeks"),
    ("freedom-calculator", "Financial Freedom Calculator", "📈", "Find your freedom number and how long it will take.", "freedom"),
    ("breathing-coach", "Breathing Coach", "🌬️", "Animated box, 4-7-8 and coherent breathing guide.", "breath"),
]

LOGO_SVG = '<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b3fa0"/><stop offset=".55" stop-color="#e0607e"/><stop offset="1" stop-color="#f2a65a"/></linearGradient></defs><circle cx="20" cy="20" r="19" fill="url(#lg)"/><path d="M20 30s-9-5.6-9-12a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6.4-9 12-9 12z" fill="#fff"/><circle cx="20" cy="9.5" r="2.2" fill="#fff" opacity=".85"/></svg>'

def e(s): return html.escape(s, quote=True)

# ------------------------------------------------------------------ layout
def head(title, desc, path, base, extra_ld=None, og_type="website"):
    url = SITE + "/" + path.replace("index.html", "")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/",
           "potentialAction": {"@type": "SearchAction", "target": SITE + "/blog.html?q={q}", "query-input": "required name=q"}},
          {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE + "/", "logo": SITE + "/assets/img/logo.svg"}]
    if extra_ld: ld.append(extra_ld)
    full = title if title.startswith(NAME) else f"{title} | {NAME}"
    return f'''<!DOCTYPE html>
<html lang="en" data-base="{base}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#6b3fa0">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(full)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.svg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="{base}manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
{ADSENSE}
<script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("bl-theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(base, active=""):
    def a(href, label, key):
        return f'<a href="{base}{href}"{" class=on" if key == active else ""}>{label}</a>'
    topics = "".join(f'<a href="{base}topics/{p[0]}.html">{p[2]} {p[1]}</a>' for p in PILLARS)
    tools = "".join(f'<a href="{base}tools/{t[0]}.html">{t[2]} {t[1]}</a>' for t in TOOLS)
    return f'''<div class="topbar"><a href="{INQUIRY_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{base}index.html" aria-label="{NAME} home">{LOGO_SVG}<span>Beautiful<b>.Life</b></span></a>
<button class="icon-btn burger" aria-label="Menu" aria-expanded="false">&#9776;</button>
<nav class="nav" aria-label="Main">
<div class="dd"><button>Explore &#9662;</button><div class="menu">{topics}</div></div>
<div class="dd"><button>Tools &#9662;</button><div class="menu">{tools}<a href="{base}tools.html"><b>All tools &rarr;</b></a></div></div>
{a("blog.html","Articles","blog")}{a("good-news.html","Good News","news")}{a("videos.html","Videos","videos")}{a("contests.html","Contests","contests")}{a("support.html","Support","support")}
<button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">&#9790;</button>
<a class="btn sm" href="{base}get-matched.html">Get Matched</a>
</nav></div></header>
<main id="main">
'''

def footer(base):
    year = datetime.date.today().year
    return f'''</main>
<footer class="ftr"><div class="wrap">
<div class="cols">
<div><a class="logo" href="{base}index.html">{LOGO_SVG}<span>Beautiful<b>.Life</b></span></a>
<p style="margin-top:12px">Practical, research-informed guides and free tools for a calmer, healthier, richer and more meaningful life.</p>
<form class="newsletter" data-form="newsletter" data-subject="Newsletter" data-ok="You're in! Watch your inbox for the next Sunday letter.">
<label class="sr" for="nl-e">Email</label><input id="nl-e" type="email" name="email" placeholder="Your email" required><span class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></span><button class="btn sm" type="submit">Join</button><div class="form-msg"></div></form></div>
<div><h4>Explore</h4><ul>{"".join(f'<li><a href="{base}topics/{p[0]}.html">{p[1]}</a></li>' for p in PILLARS)}</ul></div>
<div><h4>Free tools</h4><ul>{"".join(f'<li><a href="{base}tools/{t[0]}.html">{t[1]}</a></li>' for t in TOOLS)}</ul></div>
<div><h4>Get involved</h4><ul>
<li><a href="{base}get-matched.html">Get Matched with an Expert</a></li><li><a href="{base}blueprint.html">Free 30-Day Blueprint</a></li>
<li><a href="{base}contests.html">Contests &amp; Prizes</a></li><li><a href="{base}support.html">Support / Donate</a></li>
<li><a href="{base}partners.html">Advertise &amp; Partner</a></li><li><a href="{base}careers.html">Careers &amp; Contributors</a></li>
<li><a href="{base}about.html">About</a></li><li><a href="{base}contact.html">Contact</a></li></ul></div>
</div>
<div class="legal">
<p><a href="{base}privacy.html">Privacy Policy</a> · <a href="{base}terms.html">Terms of Use</a> · <a href="{base}disclaimer.html">Disclaimer &amp; Trademark Notice</a> · <a href="{base}privacy.html#cookies">Cookies</a> · <a href="{base}sitemap.xml">Sitemap</a></p>
<p>&copy; <span data-year>{year}</span> {NAME}. All rights reserved. Original content on this site is protected by copyright. Beautiful.Life is an independent publication and is not affiliated with, endorsed by or connected to any company, product, app or trademark using similar names. Content is for general information only and is not medical, psychological, legal or financial advice.</p>
<p>This site uses cookies and displays advertising served by Google AdSense. <a href="{base}privacy.html#ads">Learn how Google uses data</a>.</p>
</div></div></footer>
<div class="cookie" role="dialog" aria-label="Cookie consent"><b>We value your privacy 🍪</b><p style="margin:6px 0 0">We use cookies for essential functions, analytics and to show personalised ads via Google AdSense. You can accept all or keep only essential cookies. See our <a href="{base}privacy.html#cookies">Privacy Policy</a>.</p><div class="acts"><button class="btn sm" data-consent="all">Accept all</button><button class="btn sm ghost" data-consent="essential">Essential only</button></div></div>
<div class="modal" role="dialog" aria-modal="true" aria-label="Free blueprint"><div class="box"><button class="x" aria-label="Close">&times;</button>
<span class="eyebrow">Free download</span><h3 style="font-size:1.7rem">The 30-Day Beautiful Life Blueprint</h3><p>One small action a day across all eight life areas. Printable checklist + weekly reflection prompts.</p>
<form class="form" data-form="blueprint" data-subject="Blueprint lead"><input name="name" placeholder="First name" required><input type="email" name="email" placeholder="Email address" required><span class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></span><button class="btn" type="submit">Send me the Blueprint</button><div class="form-msg"></div><p class="meta">No spam. Unsubscribe any time.</p></form></div></div>
<button class="icon-btn totop" aria-label="Back to top">&#8593;</button>
<script src="{base}config.js"></script>
<script src="{base}assets/js/main.js" defer></script>
<script src="{base}assets/js/tools.js" defer></script>
</body></html>
'''

def page(path, title, desc, body, active="", extra_ld=None, og_type="website"):
    depth = path.count("/")
    base = "../" * depth
    out = head(title, desc, path, base, extra_ld, og_type) + header(base, active) + body.replace("{B}", base) + footer(base)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(out)
    PAGES.append(path)

PAGES = []
HP = '<span class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></span>'

def phero(eyebrow, h1, p):
    return f'<section class="phero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{p}</p></div></section>'

def art_card(a, base="{B}"):
    p = PILL[a["cat"]]
    return f'''<a class="card art-card reveal" data-cat="{a["cat"]}" href="{base}articles/{a["slug"]}.html"><div class="cover c-{a["cat"]}">{a["emoji"]}</div>
<div class="meta"><span class="tag">{p[1]}</span><span>{a["mins"]} min read</span></div><h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p></a>'''

def tool_card(t):
    return f'<a class="card reveal" href="{{B}}tools/{t[0]}.html"><div class="pill-ico">{t[2]}</div><h3>{t[1]}</h3><p>{t[3]}</p><span class="more">Open tool &rarr;</span></a>'

LEADBOX = f'''<div class="leadbox reveal">
<div><span class="eyebrow" style="color:#fff">Free · 2-minute match</span><h2>Get matched with a vetted life coach, therapist-referral service, financial planner or wellness retreat.</h2>
<p>Tell us what you want to change. We'll connect you with up to three trusted professionals who fit your goals, budget and location — free, with no obligation.</p>
<ul><li>✔ Life &amp; career coaching</li><li>✔ Financial planning &amp; money coaching</li><li>✔ Fitness, nutrition &amp; wellness</li><li>✔ Retreats, relationship &amp; family support</li></ul></div>
<form class="form" data-form="lead-quick" data-subject="Quick match lead" data-ok="Thank you! A matching specialist will email you within 1–2 business days.">
<h3 style="margin:0">Start your free match</h3>
<div><label for="lq-goal">I want help with</label><select id="lq-goal" name="goal" required><option value="">Choose one…</option><option>Life direction &amp; purpose</option><option>Career change</option><option>Money &amp; financial planning</option><option>Fitness &amp; nutrition</option><option>Stress &amp; burnout</option><option>Relationships</option><option>Wellness retreat</option></select></div>
<div class="row"><div><label for="lq-n">First name</label><input id="lq-n" name="name" required></div><div><label for="lq-c">Country / city</label><input id="lq-c" name="location" required></div></div>
<div><label for="lq-e">Email</label><input id="lq-e" type="email" name="email" required></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="{{B}}privacy.html">Privacy Policy</a>.</label>{HP}
<button class="btn" type="submit">Find my match &rarr;</button><div class="form-msg"></div>
<p class="meta">Prefer more detail? <a href="{{B}}get-matched.html">Use the full matching form</a>.</p></form></div>'''

# ------------------------------------------------------------------ HOME
def build_home():
    latest = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    body = f'''
<section class="hero"><div class="wrap">
<div><span class="eyebrow">Live well · Love well · Do well</span>
<h1>Design a life that feels <em>beautiful</em> — from the inside out.</h1>
<p class="lead">Research-informed guides, free interactive tools and real-world experts to help you sleep better, stress less, grow your money and spend more time on what matters.</p>
<div class="cta-row"><a class="btn" href="{{B}}tools/wheel-of-life.html">Take the free Life Check &rarr;</a><a class="btn ghost" href="#" data-open-modal>Get the 30-Day Blueprint</a></div>
<div class="stats"><div><b data-count="8">8</b>life areas</div><div><b data-count="8">8</b>free tools</div><div><b data-count="{len(ARTICLES)}">{len(ARTICLES)}</b>in-depth guides</div><div><b>Daily</b>good-news updates</div></div></div>
<div class="quote-card reveal" data-quote><span class="chip">✨ Quote of the day · <span data-today></span></span><p class="q">“Very little is needed to make a happy life.”</p><p class="a">— Marcus Aurelius</p>
<div class="today"><span class="chip">🎯 Today's beautiful action</span><p style="margin:10px 0 0;font-weight:600" data-action>Take a 10-minute walk outside without your phone.</p></div></div>
</div></section>

<section><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">The 8 pillars</span><h2>Every part of a beautiful life</h2></div><p>Balance comes from tending all eight areas. Start where you need it most.</p></div>
<div class="grid g4">{"".join(f'<a class="card reveal" href="{{B}}topics/{p[0]}.html"><div class="pill-ico c-{p[0]}">{p[2]}</div><h3>{p[1]}</h3><p>{p[3]}</p></a>' for p in PILLARS)}</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Free interactive tools</span><h2>Measure it. Improve it. Enjoy it.</h2></div><a class="btn ghost sm" href="{{B}}tools.html">All tools &rarr;</a></div>
<div class="grid g4">{"".join(tool_card(t) for t in TOOLS)}</div>
</div></section>

<section><div class="wrap">{LEADBOX}</div></section>

<section><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Latest guides</span><h2>Read something that helps today</h2></div><a class="btn ghost sm" href="{{B}}blog.html">All articles &rarr;</a></div>
<div class="grid g3">{"".join(art_card(a) for a in latest[:6])}</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Updated automatically every day</span><h2>Today's good news</h2></div><a class="btn ghost sm" href="{{B}}good-news.html">More good news &rarr;</a></div>
<div class="grid g3" data-news="6"><p>Loading uplifting stories…</p></div>
</div></section>

<section><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Watch &amp; be inspired</span><h2>Ideas worth watching</h2></div><a class="btn ghost sm" href="{{B}}videos.html">Video library &rarr;</a></div>
<div class="grid g3" data-videos="3"></div>
</div></section>

<section class="alt"><div class="wrap grid g3">
<div class="card reveal"><div class="pill-ico">🏆</div><h3>Beautiful Moments Contest</h3><p>Share a photo or story of a beautiful moment. Monthly winners receive prizes and are featured on the site.</p><a class="more" href="{{B}}contests.html">Enter this month &rarr;</a></div>
<div class="card reveal"><div class="pill-ico">💛</div><h3>Support our mission</h3><p>Reader support keeps our tools free and ad load light. Every contribution funds new guides, tools and community prizes.</p><a class="more" href="{{B}}support.html">Become a supporter &rarr;</a></div>
<div class="card reveal"><div class="pill-ico">🤝</div><h3>Partner with us</h3><p>Coaches, wellness brands, retreats and financial firms: reach a values-driven audience with sponsorships and listings.</p><a class="more" href="{{B}}partners.html">Advertise &amp; partner &rarr;</a></div>
</div></section>

<section><div class="wrap faq prose">
<div class="center"><span class="eyebrow">FAQ</span><h2>Questions, answered</h2></div>
<details><summary>Is Beautiful.Life free?</summary><p>Yes. All articles and tools are free. The site is supported by advertising, partners and optional reader contributions.</p></details>
<details><summary>Do your tools store my data?</summary><p>No. The Wheel of Life, habit tracker, gratitude journal and other tools save information only in your own browser. We never see it.</p></details>
<details><summary>How does "Get Matched" work?</summary><p>You tell us your goal, budget and location. We review your request and introduce you to suitable professionals from our partner network. It's free and you're never obliged to hire anyone.</p></details>
<details><summary>Is this medical or financial advice?</summary><p>No. Our content is general information. Always consult a qualified professional about your specific circumstances.</p></details>
</div></section>
'''
    page("index.html", "Beautiful.Life — Guides, Tools & Experts for a Beautiful Life",
         "Free research-informed guides and interactive tools for wellbeing, sleep, money, relationships and purpose — plus expert matching to help you design a beautiful life.", body, "home")

# ------------------------------------------------------------------ ARTICLES
def build_articles():
    ordered = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    for a in ARTICLES:
        p = PILL[a["cat"]]
        related = [x for x in ARTICLES if x["slug"] != a["slug"] and x["cat"] == a["cat"]][:2]
        related += [x for x in ordered if x["slug"] != a["slug"] and x not in related][:3 - len(related)]
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
              "datePublished": a["date"], "dateModified": a["date"], "author": {"@type": "Organization", "name": "Beautiful.Life Editorial Team"},
              "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.svg"}},
              "mainEntityOfPage": f'{SITE}/articles/{a["slug"]}.html'}
        date_h = datetime.date.fromisoformat(a["date"]).strftime("%B %d, %Y")
        body = f'''<div class="read-progress" style="position:fixed;top:0;left:0;height:3px;background:var(--grad);z-index:60;width:0"></div>
<section style="padding-top:40px"><div class="wrap"><article class="article">
<div class="crumbs"><a href="{{B}}index.html">Home</a> › <a href="{{B}}topics/{p[0]}.html">{p[1]}</a> › Article</div>
<span class="tag">{p[2]} {p[1]}</span>
<h1 style="margin-top:12px">{e(a["title"])}</h1>
<p class="lead">{e(a["desc"])}</p>
<div class="meta"><span>By Beautiful.Life Editorial Team</span><span>· {date_h}</span><span>· {a["mins"]} min read</span></div>
<div class="cover c-{a["cat"]}">{a["emoji"]}</div>
{a["body"].replace('href="../', 'href="{B}')}
<div class="share"><span class="meta" style="align-self:center">Share:</span><button class="btn sm ghost" data-share="x">X</button><button class="btn sm ghost" data-share="fb">Facebook</button><button class="btn sm ghost" data-share="li">LinkedIn</button><button class="btn sm ghost" data-share="wa">WhatsApp</button><button class="btn sm ghost" data-share="pin">Pinterest</button><button class="btn sm ghost" data-share="copy">Copy link</button></div>
<div class="callout" style="background:var(--grad);color:#fff;border:0"><h3 style="color:#fff">Want personal guidance?</h3><p style="color:#fff">Get free introductions to vetted coaches and specialists who match your goals.</p><a class="btn" style="background:#fff;color:var(--brand)!important" href="{{B}}get-matched.html">Get matched free &rarr;</a></div>
<div class="author"><div class="av">BL</div><div><b>Beautiful.Life Editorial Team</b><br><span class="meta">We write research-informed, practical guides and review them for accuracy and clarity. <a href="{{B}}about.html#editorial">Our editorial standards</a>.</span></div></div>
</article></div></section>
<section class="alt"><div class="wrap"><h2>Keep reading</h2><div class="grid g3">{"".join(art_card(r) for r in related)}</div></div></section>'''
        page(f'articles/{a["slug"]}.html', a["title"], a["desc"], body, "blog", ld, "article")

    filt = '<button class="on" data-f="all">All</button>' + "".join(f'<button data-f="{p[0]}">{p[2]} {p[1]}</button>' for p in PILLARS)
    body = phero("The library", "Articles &amp; guides", "Practical, research-informed reading on every part of a beautiful life.") + f'''
<section style="padding-top:20px"><div class="wrap"><div class="search"><label class="sr" for="q">Search articles</label><input id="q" type="search" placeholder="Search guides… e.g. sleep, money, friends" data-search="#arts"></div>
<div class="filters" data-filter-group="#arts">{filt}</div>
<div class="grid g3" id="arts">{"".join(art_card(a) for a in ordered)}</div></div></section>
<script>(function(){{var q=new URLSearchParams(location.search).get("q");if(q){{var i=document.getElementById("q");i.value=q;setTimeout(function(){{i.dispatchEvent(new Event("input"))}},50);}}}})();</script>'''
    page("blog.html", "Articles & Guides", "Browse Beautiful.Life's library of guides on mind, body, money, love, home, purpose, adventure and growth.", body, "blog")

# ------------------------------------------------------------------ TOPICS
TOPIC_TIPS = {
 "mind": ["Do one minute of slow breathing before checking your phone.", "Name your emotion precisely — it helps regulate it.", "Write three good things before bed.", "Schedule worry: 15 minutes, then park it."],
 "body": ["Keep a consistent wake time, even on weekends.", "Walk after meals for 10 minutes.", "Fill half your plate with vegetables.", "Stand up and move every hour."],
 "money": ["Automate saving on payday.", "Track spending for 30 days without judgment.", "Build a starter emergency buffer first.", "Spend on experiences and time, not clutter."],
 "love": ["Book recurring time with friends.", "Ask one deeper question per conversation.", "Express appreciation out loud, daily.", "Repair quickly after conflict."],
 "home": ["Clear one surface completely.", "Use warm, low lighting in the evening.", "Add one easy-care plant.", "Do a 10-minute evening reset."],
 "purpose": ["Write down your top five values.", "Notice what gives you energy this week.", "Run one small experiment toward a dream.", "Help someone with a skill you have."],
 "adventure": ["Try one new thing every month.", "Plan a micro-adventure this weekend.", "Watch a sunrise or sunset intentionally.", "Explore your city like a tourist."],
 "growth": ["Make new habits tiny — two minutes.", "Read ten pages a day.", "Review your week every Sunday.", "Learn in public: share what you learn."],
}
TOPIC_TOOL = {"mind": "breathing-coach", "body": "sleep-calculator", "money": "freedom-calculator", "love": "gratitude-journal",
              "home": "habit-tracker", "purpose": "life-in-weeks", "adventure": "life-in-weeks", "growth": "wheel-of-life"}

def build_topics():
    for slug, name, emo, tag, intro in PILLARS:
        arts = [a for a in ARTICLES if a["cat"] == slug] or ARTICLES[:3]
        t = next(x for x in TOOLS if x[0] == TOPIC_TOOL[slug])
        body = f'''<section class="phero c-{slug}" style="background:none"><div class="wrap"><div class="pill-ico c-{slug}" style="margin:0 auto 14px;width:80px;height:80px;font-size:2.4rem">{emo}</div><span class="eyebrow">Pillar</span><h1>{name}</h1><p>{intro}</p></div></section>
<section style="padding-top:20px"><div class="wrap">
<div class="grid g4">{"".join(f'<div class="card reveal"><span class="chip">Quick win {i+1}</span><p style="margin-top:10px;font-weight:600;color:var(--ink)">{tip}</p></div>' for i, tip in enumerate(TOPIC_TIPS[slug]))}</div>
<div class="sec-head mt"><h2>{name} guides</h2></div>
<div class="grid g3">{"".join(art_card(a) for a in arts)}</div>
<div class="sec-head mt"><h2>Recommended tool</h2></div>
<div class="grid g2">{tool_card(t)}<a class="card reveal" href="{{B}}get-matched.html"><div class="pill-ico">🧭</div><h3>Talk to a {name.lower()} specialist</h3><p>Free introductions to vetted professionals who match your goals and budget.</p><span class="more">Get matched &rarr;</span></a></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Watch</h2><div class="grid g3" data-videos="3"></div></div></section>'''
        page(f"topics/{slug}.html", f"{name}: {tag}", f"{intro[:150]}", body)

# ------------------------------------------------------------------ TOOLS
TOOL_BODY = {
"wheel": '''<div class="tool" data-tool="wheel"><div class="grid g2" style="align-items:center"><div class="sliders"></div><canvas width="460" height="460" style="width:100%;max-width:460px;margin:auto" aria-label="Wheel of Life chart"></canvas></div><div class="result"></div></div>''',
"quiz": '''<form class="tool" data-tool="quiz"><p>Rate how much you agree with each statement. Be honest — results are private and stay on your device.</p><div class="qs"></div><button class="btn" type="submit">See my result</button><div class="result" hidden></div></form>''',
"habits": '''<div class="tool" data-tool="habits"><form class="newsletter" style="margin:0 0 18px"><label class="sr" for="nh">New habit</label><input id="nh" placeholder="Add a habit, e.g. 'Meditate 5 minutes'" maxlength="40"><button class="btn sm" type="submit">Add</button></form><div class="table" style="overflow:auto"></div><div class="result"></div></div>''',
"gratitude": '''<div class="tool" data-tool="gratitude"><p><b>Today's prompt:</b> <span class="prompt"></span></p><form class="form"><input name="a" placeholder="1. I'm grateful for…" required><input name="b" placeholder="2. I'm grateful for…" required><input name="c" placeholder="3. I'm grateful for…" required><button class="btn" type="submit">Save entry</button></form><p class="mt"><b class="count">0</b> days journaled · <button class="btn sm ghost" data-export>Export entries</button></p><div class="entries"></div></div>''',
"sleep": '''<div class="tool" data-tool="sleep"><div class="grid g2"><div><label for="wake">I want to wake up at</label><input type="time" id="wake" value="07:00"><button class="btn mt" data-wake>Calculate bedtimes</button></div><div><label>Going to bed now?</label><p class="meta">Find the best times to set your alarm.</p><button class="btn ghost" data-now>Calculate wake times</button></div></div><div class="result"></div></div>''',
"weeks": '''<div class="tool" data-tool="weeks"><div class="grid g2"><div><label for="dob">Your date of birth</label><input type="date" id="dob"></div><div><label for="exp">Years to plan for</label><input type="number" id="exp" value="85" min="40" max="110"></div></div><button class="btn mt">Show my life in weeks</button><div class="result"></div><div class="weeks" aria-hidden="true"></div><p class="meta mt">Each square is one week. Pink = lived, orange = this week, grey = still to come.</p></div>''',
"freedom": '''<div class="tool" data-tool="freedom"><div class="grid g2"><div><label for="f-exp">Monthly living expenses</label><input type="number" id="f-exp" value="3500" min="0"></div><div><label for="f-saved">Already invested</label><input type="number" id="f-saved" value="25000" min="0"></div><div><label for="f-mon">Monthly savings</label><input type="number" id="f-mon" value="1200" min="0"></div><div><label for="f-ret">Expected real annual return %</label><input type="number" id="f-ret" value="5" step="0.5"></div><div><label for="f-wr">Safe withdrawal rate %</label><input type="number" id="f-wr" value="4" step="0.25"></div></div><div class="result"></div></div>''',
"breath": '''<div class="tool center" data-tool="breath"><label for="pattern">Technique</label><select id="pattern" style="max-width:320px;margin:auto"><option value="box">Box breathing (4-4-4-4)</option><option value="relax">4-7-8 relaxing breath</option><option value="calm">Coherent breathing (5-5)</option></select><div class="breath">Ready</div><button class="btn" data-start>Start</button><p class="meta mt" style="justify-content:center">Rounds completed: <b class="rounds">0</b></p></div>''',
}
TOOL_ABOUT = {
"wheel": "The Wheel of Life is a classic coaching exercise. Rate your satisfaction in eight areas from 1 to 10. The shape of the wheel reveals imbalances that an overall average hides. Re-score monthly to track progress — your scores are saved privately in this browser.",
"quiz": "This quick self-check is a reflection tool, not a clinical assessment. It looks across satisfaction, energy, connection, finances, meaning, savouring and growth to suggest where to focus next.",
"habits": "Track up to 12 habits over a rolling seven-day window and watch streaks grow. Research on habit formation suggests consistency matters more than perfection, so aim for around 80%.",
"gratitude": "Write three specific things you're grateful for. Gratitude journaling is one of the most studied positive-psychology practices. Entries are stored only on your device; export them any time.",
"sleep": "Sleep moves in cycles of roughly 90 minutes. Waking at the end of a cycle often feels easier. This calculator adds about 15 minutes to fall asleep. Most adults need at least seven hours.",
"weeks": "A full human life fits on a single page when measured in weeks. Seeing it is a gentle, powerful prompt to spend time on what matters most.",
"freedom": "Your 'freedom number' is the invested amount that could cover your expenses using a chosen withdrawal rate. This simplified model assumes constant real returns and is for illustration, not financial advice.",
"breath": "Follow the expanding circle to slow your breathing. Lengthening the exhale is widely used to promote calm. Stop if you feel light-headed.",
}

def build_tools():
    for slug, name, emo, desc, key in TOOLS:
        ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "applicationCategory": "LifestyleApplication",
              "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"{SITE}/tools/{slug}.html"}
        others = [t for t in TOOLS if t[0] != slug][:4]
        body = phero(f"{emo} Free tool", name, desc) + f'''<section style="padding-top:10px"><div class="wrap">{TOOL_BODY[key]}
<div class="prose mt"><h2>About this tool</h2><p>{TOOL_ABOUT[key]}</p><p class="meta">Privacy: nothing you enter here is sent to us. Data is stored only in your browser's local storage.</p></div>
</div></section><section><div class="wrap">{LEADBOX}</div></section>
<section class="alt"><div class="wrap"><h2>More free tools</h2><div class="grid g4">{"".join(tool_card(t) for t in others)}</div></div></section>'''
        page(f"tools/{slug}.html", f"{name} — Free Online Tool", desc, body, "", ld)
    body = phero("Free · private · no sign-up", "Interactive life tools", "Measure what matters, build better habits and plan your future. Everything runs in your browser and your data stays on your device.") + f'''
<section style="padding-top:10px"><div class="wrap"><div class="grid g4">{"".join(tool_card(t) for t in TOOLS)}</div></div></section><section><div class="wrap">{LEADBOX}</div></section>'''
    page("tools.html", "Free Interactive Life Tools", "Free Wheel of Life, habit tracker, gratitude journal, sleep calculator, life-in-weeks, freedom calculator and breathing coach.", body)

# ------------------------------------------------------------------ FEEDS
def build_feeds():
    cats = [("all","All"),("world","World"),("health","Health"),("planet","Planet"),("science","Science"),("kindness","Kindness")]
    filt = "".join(f'<button{" class=on" if c=="all" else ""} data-f="{c}">{n}</button>' for c, n in cats)
    body = phero("Refreshed automatically every day", "Today's Good News", "A daily dose of uplifting, solutions-focused stories from trusted sources around the world, to balance out the doom-scroll.") + f'''
<section style="padding-top:10px"><div class="wrap"><p class="meta" style="justify-content:center">Last updated: <span data-news-updated>today</span></p>
<div class="filters" data-filter-group="#news" style="justify-content:center">{filt}</div>
<div class="grid g3" id="news" data-news="36"><p>Loading…</p></div>
<p class="meta mt">Headlines and short summaries link to the original publishers. All rights in linked content belong to their respective owners.</p></div></section>
<section class="alt"><div class="wrap">{LEADBOX}</div></section>'''
    page("good-news.html", "Today's Good News — Uplifting Stories Updated Daily", "Daily uplifting, positive and solutions-focused news stories from around the world, updated automatically.", body, "news")

    vc = [("all","All"),("mind","Mind"),("love","Love"),("growth","Growth"),("purpose","Purpose"),("body","Body"),("money","Money")]
    filt = "".join(f'<button{" class=on" if c=="all" else ""} data-f="{c}">{n}</button>' for c, n in vc)
    body = phero("Curated · refreshed weekly", "The Beautiful.Life video library", "Talks and lessons on happiness, purpose, relationships, health and growth from the world's best thinkers.") + f'''
<section style="padding-top:10px"><div class="wrap"><div class="filters" data-filter-group="#vids" style="justify-content:center">{filt}</div>
<div class="grid g3" id="vids" data-videos="60"></div>
<p class="meta mt">Videos are embedded from YouTube using privacy-enhanced mode and load only when you press play. All rights belong to their creators.</p>
<div class="card mt center"><h3>Are you a creator?</h3><p>Suggest a video or channel for the library, or partner with us on original content.</p><a class="btn sm mt" href="{{B}}partners.html#form">Suggest or partner &rarr;</a></div></div></section>'''
    page("videos.html", "Inspiring Videos on Happiness, Purpose & Growth", "A curated, regularly refreshed library of talks on happiness, purpose, relationships, health and personal growth.", body, "videos")

# ------------------------------------------------------------------ LEAD GEN
def build_leadgen():
    body = phero("Free · no obligation · 2 minutes", "Get matched with the right expert", "Coaches, financial planners, wellness specialists and retreats. Tell us what you need and we'll introduce you to up to three trusted professionals.") + f'''
<section style="padding-top:10px"><div class="wrap grid g2" style="align-items:start">
<form class="tool form" data-form="lead-full" data-steps data-subject="Full match lead" data-ok="You're all set! A matching specialist will email your introductions within 1–2 business days.">
<div class="steps"><span></span><span></span><span></span><span></span></div>
<div class="step"><h3>1. What would you like help with?</h3><div class="opts">
{"".join(f'<label class="opt"><input type="radio" name="service" value="{s}" required><span>{s}</span></label>' for s in ["🧭 Life coaching","💼 Career coaching","💰 Financial planning","🏋️ Fitness & nutrition","🧘 Stress & burnout","💞 Relationship coaching","🌴 Wellness retreat","🧠 Therapist referral service"])}
</div><button class="btn" data-next>Continue &rarr;</button></div>
<div class="step"><h3>2. Tell us a little more</h3>
<div><label for="g-goal">Your main goal (one or two sentences)</label><textarea id="g-goal" name="goal" required placeholder="e.g. I want to change careers within 12 months without losing financial stability."></textarea></div>
<div class="row"><div><label for="g-time">When do you want to start?</label><select id="g-time" name="timeline" required><option value="">Choose…</option><option>Immediately</option><option>Within a month</option><option>1–3 months</option><option>Just researching</option></select></div>
<div><label for="g-budget">Monthly budget</label><select id="g-budget" name="budget" required><option value="">Choose…</option><option>Under $100</option><option>$100–$300</option><option>$300–$750</option><option>$750+</option><option>Not sure yet</option></select></div></div>
<div class="row"><div><label for="g-fmt">Preferred format</label><select id="g-fmt" name="format"><option>Online / video</option><option>In person</option><option>Either</option></select></div><div><label for="g-loc">Country / city</label><input id="g-loc" name="location" required></div></div>
<div class="row"><button class="btn ghost" data-prev>&larr; Back</button><button class="btn" data-next>Continue &rarr;</button></div></div>
<div class="step"><h3>3. Where should we send your matches?</h3>
<div class="row"><div><label for="g-n">Full name</label><input id="g-n" name="name" required autocomplete="name"></div><div><label for="g-p">Phone (optional)</label><input id="g-p" name="phone" type="tel" autocomplete="tel"></div></div>
<div><label for="g-e">Email</label><input id="g-e" type="email" name="email" required autocomplete="email"></div>
<div><label for="g-c">Best way to reach you</label><select id="g-c" name="contact_pref"><option>Email</option><option>Phone</option><option>WhatsApp</option></select></div>
<div class="row"><button class="btn ghost" data-prev>&larr; Back</button><button class="btn" data-next>Review &rarr;</button></div></div>
<div class="step"><h3>4. Confirm</h3><p>We'll review your request and send personalised introductions. You're never obliged to hire anyone.</p>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that Beautiful.Life may share my request with up to three matching professionals and contact me about it. I accept the <a href="{{B}}privacy.html">Privacy Policy</a>.</label>
<label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Send me the free Sunday letter and the 30-Day Blueprint.</label>{HP}
<div class="row"><button class="btn ghost" data-prev>&larr; Back</button><button class="btn" type="submit">Get my free matches ✨</button></div><div class="form-msg"></div></div>
</form>
<div><div class="card"><h3>How it works</h3><ol><li><b>Tell us your goal</b> — two minutes, no account.</li><li><b>We hand-match</b> professionals by speciality, budget, format and location.</li><li><b>You choose</b> — compare introductions and book only if it feels right.</li></ol></div>
<div class="card mt"><h3>Why people use it</h3><ul><li>Saves hours of searching and comparing</li><li>Free for you — partners fund the service</li><li>Your details go only to relevant matches</li></ul></div>
<div class="card mt"><h3>Are you a professional?</h3><p>Coaches, planners, therapists' practices and retreats can apply to receive qualified client introductions.</p><a class="btn sm mt" href="{{B}}partners.html#form">Join the partner network &rarr;</a></div>
<p class="meta mt">Beautiful.Life is an introduction service, not a provider of medical, psychological or financial services. In an emergency, contact local emergency services.</p></div>
</div></section>'''
    page("get-matched.html", "Get Matched with a Coach, Planner or Wellness Expert — Free", "Free, no-obligation matching with vetted life coaches, financial planners, wellness specialists and retreats.", body)

    days = ["Write a one-line vision for your life","Drink water before coffee","10-minute phone-free walk","Clear one surface at home","Message an old friend","Check one subscription","Lights out 20 minutes earlier","Three good things journal","Cook one simple healthy meal","Box breathing x4","Write your top 5 values","Read 10 pages","Compliment someone sincerely","Move your body for 20 minutes","Plan a micro-adventure","Automate a small saving","Declutter one drawer","Call a family member","Learn one new skill for 15 minutes","Eat one meal mindfully","Wheel of Life check-in","Do something kind anonymously","Spend an hour in nature","Write a gratitude letter","Set one 90-day goal","Digital sunset after 9pm","Try something new","Review your money for 15 minutes","Celebrate a win","Write a letter to your future self"]
    rows = "".join(f'<label class="check" style="font-size:1rem;color:var(--ink);padding:8px 0;border-bottom:1px solid var(--line)"><input type="checkbox"> <b>Day {i+1}:</b>&nbsp;{d}</label>' for i, d in enumerate(days))
    body = phero("Free · printable", "The 30-Day Beautiful Life Blueprint", "One small action a day across all eight life areas. Tick them off, reflect weekly and watch your Wheel of Life grow.") + f'''
<section style="padding-top:10px"><div class="wrap prose">
<div id="bp-locked" class="leadbox" style="grid-template-columns:1fr"><form class="form" data-form="blueprint" data-subject="Blueprint lead"><h3 style="margin:0">Unlock the Blueprint (free)</h3><div class="row"><input name="name" placeholder="First name" required><input type="email" name="email" placeholder="Email" required></div><label class="check"><input type="checkbox" name="consent" value="yes" required> Send me the Blueprint and the Sunday letter. Unsubscribe anytime.</label>{HP}<button class="btn" type="submit">Unlock now</button><div class="form-msg"></div></form></div>
<div id="bp" hidden><div class="card"><div class="sec-head"><h2 style="margin:0">Your 30 days</h2><button class="btn sm" onclick="window.print()">Print</button></div>{rows}</div>
<div class="card mt"><h3>Weekly reflection (days 7, 14, 21, 28)</h3><ul><li>What gave me the most energy this week?</li><li>Which action felt hardest — and why?</li><li>What will I keep doing after the 30 days?</li></ul></div></div>
</div></section>
<script>try{{if(localStorage.getItem("bl-blueprint")||location.hash==="#unlocked"){{document.getElementById("bp").hidden=false;document.getElementById("bp-locked").hidden=true;}}}}catch(e){{}}</script>'''
    page("blueprint.html", "Free 30-Day Beautiful Life Blueprint", "A free, printable 30-day plan with one small action a day across mind, body, money, love, home, purpose, adventure and growth.", body)

# ------------------------------------------------------------------ COMMUNITY & REVENUE
def build_community():
    month = datetime.date.today().strftime("%B %Y")
    body = phero("Monthly contests · real prizes", "Contests &amp; prizes", "Share what makes your life beautiful. Every month we feature the best entries and award prizes funded by our supporters and sponsors.") + f'''
<section style="padding-top:10px"><div class="wrap">
<div class="grid g3">
<div class="card reveal"><div class="pill-ico">📸</div><h3>Beautiful Moments Photo</h3><p>A photo of a moment that made you stop and smile. Judged on emotion, originality and story.</p><p class="mt"><span class="chip">🥇 Featured + gift card</span></p></div>
<div class="card reveal"><div class="pill-ico">✍️</div><h3>Life-Changing Habit Story</h3><p>In 300 words or fewer, tell us about one habit that changed your life.</p><p class="mt"><span class="chip">🥇 Featured + coaching session</span></p></div>
<div class="card reveal"><div class="pill-ico">🧭</div><h3>Micro-Adventure Challenge</h3><p>Complete a micro-adventure and share what you did and what you discovered.</p><p class="mt"><span class="chip">🥇 Featured + adventure kit</span></p></div>
</div>
<div class="grid g2 mt" style="align-items:start">
<form class="tool form" data-form="contest" data-subject="Contest entry" data-ok="Your entry is in! Winners are announced in the first week of next month.">
<h3>Enter the {month} contest</h3>
<div><label for="c-cat">Category</label><select id="c-cat" name="category" required><option value="">Choose…</option><option>Beautiful Moments Photo</option><option>Life-Changing Habit Story</option><option>Micro-Adventure Challenge</option></select></div>
<div class="row"><div><label for="c-n">Name</label><input id="c-n" name="name" required></div><div><label for="c-e">Email</label><input id="c-e" type="email" name="email" required></div></div>
<div><label for="c-t">Title of your entry</label><input id="c-t" name="title" required></div>
<div><label for="c-s">Your story (max 300 words)</label><textarea id="c-s" name="story" required maxlength="2200"></textarea></div>
<div><label for="c-l">Link to your photo (Google Drive, Dropbox, Instagram…)</label><input id="c-l" type="url" name="photo_link" placeholder="https://"></div>
<div><label for="c-c">Country</label><input id="c-c" name="country" required></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I'm 18+ (or have parental consent), this is my original work, and I accept the contest rules below.</label>{HP}
<button class="btn" type="submit">Submit my entry</button><div class="form-msg"></div></form>
<div class="faq"><h3>Contest rules (summary)</h3>
<details open><summary>Who can enter?</summary><p>Anyone aged 18+ where such contests are legal. Under-18s need parental consent. No purchase necessary.</p></details>
<details><summary>How are winners chosen?</summary><p>An editorial panel scores entries on originality, emotional impact and alignment with the theme. Winners are notified by email and announced in the first week of the following month.</p></details>
<details><summary>What about rights?</summary><p>You keep copyright. By entering, you grant Beautiful.Life a non-exclusive licence to feature your entry on the site and our channels with credit.</p></details>
<details><summary>Prizes</summary><p>Prizes vary by month and sponsor and are listed when each contest opens. No cash alternative unless stated. Void where prohibited.</p></details>
<details><summary>Sponsor a contest</summary><p>Brands can sponsor prizes for exposure to an engaged audience. <a href="{{B}}partners.html#form">Become a prize sponsor</a>.</p></details></div>
</div></div></section>'''
    page("contests.html", "Contests & Prizes — Beautiful Moments", "Enter Beautiful.Life's monthly photo, story and micro-adventure contests for featured placement and prizes.", body, "contests")

    tiers = [("5","☕","A coffee"),("15","🌱","Seed supporter"),("50","🌸","Bloom patron"),("150","🌟","Guardian")]
    body = phero("Reader-supported", "Help keep Beautiful.Life free", "Your support funds new guides and tools, community contest prizes, promotion of our mission and the talented writers and developers who make it all possible.") + f'''
<section style="padding-top:10px"><div class="wrap">
<div class="card"><div class="sec-head" style="margin-bottom:10px"><h3 style="margin:0">This year's community goal</h3><b>62% funded</b></div><div class="progress"><i style="width:62%"></i></div><p class="meta mt">Goal: fund 4 new interactive tools, 12 monthly contests and 50 new expert-reviewed guides.</p></div>
<div class="grid g2 mt" style="align-items:start">
<div class="tool"><h3>Choose an amount</h3><div class="tiers">{"".join(f'<div class="tier" data-amt="{a}" role="button" tabindex="0"><span style="font-size:1.6rem">{i}</span><b>${a}</b><span class="meta" style="justify-content:center">{n}</span></div>' for a, i, n in tiers)}</div>
<div class="cta-row"><a class="btn" data-pay="paypal" hidden>Donate with PayPal</a><a class="btn" data-pay="stripe" hidden>Donate by card</a><a class="btn ghost" data-pay="kofi" hidden>Ko-fi</a><a class="btn ghost" data-pay="bmac" hidden>Buy me a coffee</a></div>
<form class="form mt" data-form="donation" data-subject="Donation pledge" data-ok="Thank you so much! We'll email you secure payment details and a receipt within 24 hours.">
<p class="meta">Pledge below and we'll send secure payment instructions (card, PayPal, Interac e-Transfer or bank transfer) by email.</p>
<div class="row"><div><label for="donation-amount">Amount (USD)</label><input id="donation-amount" name="amount" type="number" min="1" value="15" required></div><div><label for="d-f">Frequency</label><select id="d-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div><label for="d-p">Direct my support to</label><select id="d-p" name="purpose"><option>Where it's needed most (operations)</option><option>New tools &amp; guides</option><option>Contest prizes</option><option>Promotion &amp; outreach</option><option>Hiring writers &amp; developers</option></select></div>
<div class="row"><div><label for="d-n">Name</label><input id="d-n" name="name" required></div><div><label for="d-e">Email</label><input id="d-e" type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters' wall.</label>{HP}
<button class="btn" type="submit">Pledge my support 💛</button><div class="form-msg"></div></form></div>
<div><div class="card"><h3>Where your money goes</h3><ul><li><b>40%</b> — new tools, guides and fact-checking</li><li><b>20%</b> — community contests and prizes</li><li><b>20%</b> — hosting, operations and security</li><li><b>20%</b> — promotion, outreach and hiring talent</li></ul></div>
<div class="card mt"><h3>Other ways to help</h3><ul><li>Share an article with someone who needs it</li><li>Enter or sponsor a contest</li><li><a href="{{B}}careers.html">Contribute as a writer or volunteer</a></li><li><a href="{{B}}partners.html">Introduce us to a sponsor</a></li></ul></div>
<p class="meta mt">Beautiful.Life is not a registered charity; contributions are not tax-deductible.</p></div>
</div></div></section>'''
    page("support.html", "Support Beautiful.Life — Donate", "Support Beautiful.Life with a one-time or monthly contribution to keep our guides and tools free.", body, "support")

    body = phero("Advertise · sponsor · partner", "Partner with Beautiful.Life", "Reach people actively investing in their health, wealth, relationships and personal growth.") + f'''
<section style="padding-top:10px"><div class="wrap">
<div class="grid g4">
<div class="card reveal"><div class="pill-ico">📣</div><h3>Sponsored content</h3><p>Clearly labelled features, guides and newsletter placements.</p></div>
<div class="card reveal"><div class="pill-ico">🧭</div><h3>Lead partner network</h3><p>Coaches, planners and retreats receive qualified client introductions.</p></div>
<div class="card reveal"><div class="pill-ico">🏆</div><h3>Contest sponsorship</h3><p>Fund monthly prizes and get featured to every entrant and visitor.</p></div>
<div class="card reveal"><div class="pill-ico">🛠️</div><h3>Tool sponsorship</h3><p>Exclusive "presented by" placement on one of our interactive tools.</p></div>
</div>
<div class="grid g2 mt" style="align-items:start" id="form">
<form class="tool form" data-form="partner" data-subject="Partnership inquiry" data-ok="Thanks! Our partnerships team will reply within 2 business days with our media kit.">
<h3>Request the media kit</h3>
<div><label for="p-t">I'm interested in</label><select id="p-t" name="interest" required><option value="">Choose…</option><option>Joining the lead partner network (professionals)</option><option>Sponsored content / advertising</option><option>Contest or prize sponsorship</option><option>Tool sponsorship</option><option>Video / creator collaboration</option><option>Acquiring this website or domain</option><option>Other partnership</option></select></div>
<div class="row"><div><label for="p-n">Name</label><input id="p-n" name="name" required></div><div><label for="p-c">Company / practice</label><input id="p-c" name="company" required></div></div>
<div class="row"><div><label for="p-e">Work email</label><input id="p-e" type="email" name="email" required></div><div><label for="p-w">Website</label><input id="p-w" name="website" type="url" placeholder="https://"></div></div>
<div><label for="p-b">Budget range</label><select id="p-b" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Performance-based / per lead</option></select></div>
<div><label for="p-m">Tell us about your goals</label><textarea id="p-m" name="message" required></textarea></div>{HP}
<button class="btn" type="submit">Send inquiry</button><div class="form-msg"></div></form>
<div class="card"><h3>Our audience</h3><ul><li>Adults 25–55 investing in self-improvement</li><li>Strong interest in wellness, personal finance, relationships and travel</li><li>High-intent visitors using planning and assessment tools</li></ul><h3 class="mt">Editorial independence</h3><p>Sponsored content is always labelled. Partners never influence our independent guides or tool results.</p><p class="mt"><a href="https://web.works/contact" target="_blank" rel="noopener">Interested in this website or domain name? Contact us here.</a></p></div>
</div></div></section>'''
    page("partners.html", "Advertise, Sponsor & Partner", "Advertising, sponsorship, contest prizes and lead partnerships with Beautiful.Life.", body)

    roles = [("Wellness & Lifestyle Writer","Freelance · Remote","Write practical, research-informed guides. Experience in health, psychology or personal finance writing preferred."),
             ("Certified Coach / Expert Reviewer","Freelance · Remote","Review articles for accuracy in your field (coaching, nutrition, fitness, finance, psychology)."),
             ("Front-end Developer","Contract · Remote","Build new interactive tools in vanilla JavaScript. Accessibility and performance mindset."),
             ("Video Creator / Editor","Freelance · Remote","Produce short-form explainers for YouTube and social channels."),
             ("Community & Contest Manager","Part-time · Remote","Run monthly contests, moderate entries and grow our community."),
             ("Partnerships & Sales Lead","Commission · Remote","Grow our sponsor and lead-partner network.")]
    body = phero("We're hiring talent", "Careers &amp; contributors", "Help millions of people build more beautiful lives. Remote, flexible roles for writers, experts, developers and creators.") + f'''
<section style="padding-top:10px"><div class="wrap"><div class="grid g3">{"".join(f'<div class="card reveal"><span class="tag">{t}</span><h3 style="margin-top:10px">{r}</h3><p>{d}</p></div>' for r, t, d in roles)}</div>
<div class="grid g2 mt" style="align-items:start">
<form class="tool form" data-form="careers" data-subject="Job application" data-ok="Application received — thank you! We'll be in touch if there's a fit.">
<h3>Apply or introduce yourself</h3>
<div><label for="j-r">Role</label><select id="j-r" name="role" required><option value="">Choose…</option>{"".join(f"<option>{r}</option>" for r,_,_ in roles)}<option>Volunteer / other</option></select></div>
<div class="row"><div><label for="j-n">Full name</label><input id="j-n" name="name" required></div><div><label for="j-e">Email</label><input id="j-e" type="email" name="email" required></div></div>
<div class="row"><div><label for="j-p">Portfolio / LinkedIn</label><input id="j-p" type="url" name="portfolio" placeholder="https://" required></div><div><label for="j-l">Location / time zone</label><input id="j-l" name="location"></div></div>
<div><label for="j-m">Why you, in a few sentences</label><textarea id="j-m" name="message" required></textarea></div>{HP}
<button class="btn" type="submit">Submit application</button><div class="form-msg"></div></form>
<div class="card"><h3>How we work</h3><ul><li>100% remote, asynchronous-first</li><li>Paid per project or contract</li><li>Editorial standards: accuracy, kindness, clarity</li><li>Credit and bylines for contributors</li></ul><p class="meta">We welcome applicants of every background. We never charge fees to applicants.</p></div>
</div></div></section>'''
    page("careers.html", "Careers & Contributors — We're Hiring", "Remote roles for writers, expert reviewers, developers, video creators and community managers at Beautiful.Life.", body)

# ------------------------------------------------------------------ INFO & LEGAL
def build_info():
    body = phero("About us", "Live well. Love well. Do well.", "Beautiful.Life is an independent publication helping people design calmer, healthier, richer and more meaningful lives.") + '''
<section style="padding-top:10px"><div class="wrap prose">
<h2>Our mission</h2><p>Self-improvement content online is often extreme, contradictory or designed to sell you something. We believe a beautiful life is built from small, sensible, evidence-informed choices across eight areas: mind, body, money, love, home, purpose, adventure and growth. Our job is to make those choices easier with clear guides, free tools and introductions to trustworthy experts.</p>
<h2>What we offer</h2><ul><li><b>Guides</b> — practical articles grounded in published research and expert consensus.</li><li><b>Free tools</b> — private, browser-based assessments, trackers and calculators.</li><li><b>Good news</b> — a daily, automatically refreshed feed of uplifting stories.</li><li><b>Expert matching</b> — free introductions to coaches, planners and wellness professionals.</li><li><b>Community</b> — monthly contests that celebrate real beautiful moments.</li></ul>
<h2 id="editorial">Editorial standards</h2><p>We write for clarity and accuracy, cite well-established research where relevant, avoid sensational claims and update content as evidence changes. Health and money articles are general information and always point readers to qualified professionals for personal advice. Sponsored content is always labelled and never influences our independent guides.</p>
<h2>How we're funded</h2><p>Beautiful.Life is free to read. We're funded by display advertising (Google AdSense), partner referrals from our matching service, sponsorships and voluntary reader support. Advertisers do not influence editorial content.</p>
<h2>Corrections</h2><p>Spotted an error? Please tell us via our <a href="{B}contact.html">contact page</a> and we'll review it promptly.</p>
</div></section>'''
    page("about.html", "About Beautiful.Life", "Beautiful.Life is an independent publication with guides, free tools and expert matching for a calmer, healthier, more meaningful life.", body)

    body = phero("We'd love to hear from you", "Contact us", "Questions, feedback, corrections, press or partnerships — send us a message and we'll reply within two business days.") + f'''
<section style="padding-top:10px"><div class="wrap grid g2" style="align-items:start">
<form class="tool form" data-form="contact" data-subject="Contact message">
<div class="row"><div><label for="ct-n">Name</label><input id="ct-n" name="name" required></div><div><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required></div></div>
<div><label for="ct-t">Topic</label><select id="ct-t" name="topic"><option>General question</option><option>Feedback or correction</option><option>Press / media</option><option>Advertising &amp; partnership</option><option>Website / domain inquiry</option><option>Technical issue</option><option>Privacy request</option></select></div>
<div><label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the processing of my message per the <a href="{{B}}privacy.html">Privacy Policy</a>.</label>{HP}
<button class="btn" type="submit">Send message</button><div class="form-msg"></div></form>
<div><div class="card"><h3>Other ways to connect</h3><ul><li><a href="{{B}}get-matched.html">Get matched with an expert</a></li><li><a href="{{B}}partners.html">Advertising &amp; partnerships</a></li><li><a href="{{B}}careers.html">Write or work with us</a></li><li><a href="{{B}}support.html">Support our mission</a></li></ul></div>
<div class="card mt"><h3>Interested in this website?</h3><p>For inquiries about acquiring this website or domain name, sponsorship, advertising or partnership:</p><a class="btn sm mt" href="https://web.works/contact" target="_blank" rel="noopener">Contact the owner &rarr;</a></div></div>
</div></section>'''
    page("contact.html", "Contact Beautiful.Life", "Contact the Beautiful.Life team with questions, feedback, corrections or partnership inquiries.", body)

    upd = datetime.date.today().strftime("%B %d, %Y")
    body = phero("Legal", "Privacy Policy", f"Last updated: {upd}") + '''<section style="padding-top:10px"><div class="wrap prose">
<p>This Privacy Policy explains how Beautiful.Life ("we", "us") collects, uses and protects information when you visit our website.</p>
<h2>Information we collect</h2><ul><li><b>Information you provide:</b> when you submit a form (newsletter, matching request, contest entry, donation pledge, application or contact message) we collect the details you enter, such as your name, email address and message. Form submissions are delivered to us through a third-party form-processing service.</li><li><b>Automatically collected information:</b> like most websites, our hosting provider and advertising partners may collect technical data such as IP address, browser type, device information and pages visited.</li><li><b>Tool data:</b> our interactive tools store your entries only in your browser's local storage. We cannot see this data. Clear your browser storage to delete it.</li></ul>
<h2>How we use information</h2><ul><li>To respond to inquiries and deliver what you requested.</li><li>To introduce matching requests to up to three relevant professionals, only with your consent.</li><li>To send newsletters you opted into (unsubscribe at any time).</li><li>To run contests, process pledges and evaluate applications.</li><li>To improve the site and maintain security.</li></ul>
<h2 id="ads">Advertising — Google AdSense</h2><p>We use Google AdSense to display advertisements. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to users based on their visits to this site and/or other sites on the Internet.</p><p>You may opt out of personalised advertising by visiting <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">www.aboutads.info</a>. Learn more about <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</p>
<h2 id="cookies">Cookies</h2><p>Cookies are small files stored on your device. We use essential storage (e.g. your theme and cookie choice), and our advertising partners use cookies as described above. Our cookie banner lets you accept all cookies or limit to essential cookies and non-personalised ads. You can also control cookies in your browser settings.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. Once played, YouTube may collect data according to its own privacy policy. Links to external news sources are governed by those sites' policies.</p>
<h2>Sharing</h2><p>We do not sell your personal information. We share it only with service providers that help operate the site (hosting, form processing, advertising), with professionals you ask to be matched with, or where required by law.</p>
<h2>Your rights</h2><p>Depending on where you live (including under GDPR, UK GDPR, PIPEDA, CCPA/CPRA and similar laws) you may have the right to access, correct, delete or restrict use of your personal information and to withdraw consent. To make a request, use our <a href="{B}contact.html">contact form</a> and choose "Privacy request".</p>
<h2>Children</h2><p>This site is intended for adults. We do not knowingly collect personal information from children under 13 (or the applicable age in your country).</p>
<h2>Data retention &amp; security</h2><p>We keep submissions only as long as needed for the purpose they were collected and use reasonable safeguards to protect them. No online transmission is completely secure.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above when we do.</p>
<h2>Contact</h2><p>Questions about this policy? <a href="{B}contact.html">Contact us</a>.</p>
</div></section>'''
    page("privacy.html", "Privacy Policy", "How Beautiful.Life collects, uses and protects your information, including cookies and Google AdSense advertising.", body)

    body = phero("Legal", "Terms of Use", f"Last updated: {upd}") + '''<section style="padding-top:10px"><div class="wrap prose">
<p>By using Beautiful.Life you agree to these Terms. If you do not agree, please do not use the site.</p>
<h2>Use of the site</h2><p>You may use the site for personal, non-commercial purposes. You agree not to misuse the site, attempt to disrupt it, scrape it at scale, submit unlawful or harmful content, or impersonate others.</p>
<h2>Content &amp; intellectual property</h2><p>Original text, design, tools and graphics on Beautiful.Life are protected by copyright. You may share links and short quotations with attribution. Third-party content (news headlines, embedded videos, quotations) remains the property of its respective owners.</p>
<h2>User submissions</h2><p>When you submit contest entries, stories or other content, you confirm you own it or have permission to share it, and you grant us a non-exclusive, worldwide, royalty-free licence to display it on the site and our channels with credit. You keep your copyright.</p>
<h2>No professional advice</h2><p>Content and tools are for general information and self-reflection only and are not medical, psychological, legal or financial advice. See our <a href="{B}disclaimer.html">Disclaimer</a>.</p>
<h2>Matching service</h2><p>Our matching service introduces you to independent third-party professionals. We do not provide their services, and we are not responsible for their advice, fees or conduct. Please conduct your own due diligence.</p>
<h2>Contests</h2><p>Contests are subject to the rules published on the <a href="{B}contests.html">Contests page</a>. Void where prohibited.</p>
<h2>Donations</h2><p>Contributions are voluntary, support site operations and are generally non-refundable. Beautiful.Life is not a registered charity.</p>
<h2>External links</h2><p>We link to third-party sites for convenience and are not responsible for their content or practices.</p>
<h2>Limitation of liability</h2><p>The site is provided "as is" without warranties. To the fullest extent permitted by law, we are not liable for any loss arising from your use of the site.</p>
<h2>Changes</h2><p>We may update these Terms at any time. Continued use means you accept the updated Terms.</p>
</div></section>'''
    page("terms.html", "Terms of Use", "Terms and conditions for using the Beautiful.Life website, tools, contests and matching service.", body)

    body = phero("Legal", "Disclaimer &amp; Trademark Notice", f"Last updated: {upd}") + '''<section style="padding-top:10px"><div class="wrap prose">
<h2 id="trademark">Trademark &amp; copyright disclosure</h2>
<p>"Beautiful.Life" is the name of this independent website, operated on the domain beautiful.life. The phrase "beautiful life" is a common English expression used descriptively here. <b>Beautiful.Life is not affiliated with, endorsed by, sponsored by or connected to any company, brand, product, app, film, song, publication or registered trademark that uses the same or similar wording</b>, including any mark written as a single word or with different spacing or capitalisation. Any such names are the property of their respective owners, and any reference is purely descriptive or nominative.</p>
<p>All other trademarks, service marks, logos and product names mentioned on this site (including Google, YouTube, PayPal and the names of news publishers and their content) belong to their respective owners. Their mention does not imply endorsement.</p>
<p>The Beautiful.Life logo, site design, original articles and interactive tools are original works &copy; Beautiful.Life. Quotations are attributed to their authors and, where historical, are in the public domain. News headlines and summaries link to and credit the original publishers. Embedded videos remain the property of their creators.</p>
<p>If you believe any content on this site infringes your rights, please <a href="{B}contact.html">contact us</a> with details and we will review and respond promptly.</p>
<h2>Health disclaimer</h2><p>Content on Beautiful.Life is for general informational and educational purposes only and does not constitute medical or psychological advice, diagnosis or treatment. Always seek the advice of a qualified healthcare provider with any questions about a medical or mental-health condition. If you are in crisis or think you may have an emergency, contact your local emergency services immediately.</p>
<h2>Financial disclaimer</h2><p>Money content and calculators are for illustration and education only and are not personalised financial, investment, tax or legal advice. Results are estimates based on simplified assumptions. Consult a qualified professional before making financial decisions.</p>
<h2>Affiliate &amp; advertising disclosure</h2><p>Beautiful.Life displays ads through Google AdSense and may receive referral fees from partners in our matching network or from sponsors. Sponsored content is clearly labelled. These relationships do not influence our independent editorial content.</p>
<h2>Accuracy</h2><p>We strive to keep information accurate and current but make no guarantees. Research evolves; content may be updated without notice.</p>
</div></section>'''
    page("disclaimer.html", "Disclaimer & Trademark Notice", "Beautiful.Life health, financial, affiliate and trademark/copyright disclaimers.", body)

    body = phero("404", "This page took a wrong turn", "Even beautiful lives have detours. Let's get you back on track.") + '''<section style="padding-top:0"><div class="wrap center"><a class="btn" href="{B}index.html">Back home</a> <a class="btn ghost" href="{B}tools.html">Explore free tools</a></div></section>'''
    page("404.html", "Page not found", "The page you were looking for could not be found.", body)

# ------------------------------------------------------------------ STATIC FILES
def build_static():
    def w(p, s):
        full = os.path.join(ROOT, p); os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f: f.write(s)
    urls = "".join(f'<url><loc>{SITE}/{p.replace("index.html", "")}</loc><lastmod>{TODAY}</lastmod><changefreq>{"daily" if p in ("index.html","good-news.html") else "weekly"}</changefreq><priority>{"1.0" if p=="index.html" else "0.7"}</priority></url>\n' for p in PAGES if p != "404.html")
    w("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    w("robots.txt", f"User-agent: *\nAllow: /\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    w("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    w(".nojekyll", "")
    w("manifest.json", json.dumps({"name": NAME, "short_name": NAME, "start_url": "./index.html", "display": "standalone",
                                   "background_color": "#fbf8f3", "theme_color": "#6b3fa0",
                                   "icons": [{"src": "assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))
    w("assets/img/logo.svg", '<svg xmlns="http://www.w3.org/2000/svg" ' + LOGO_SVG[5:])
    w("assets/img/og.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b3fa0"/><stop offset=".55" stop-color="#e0607e"/><stop offset="1" stop-color="#f2a65a"/></linearGradient></defs><rect width="1200" height="630" fill="url(#g)"/><text x="600" y="300" text-anchor="middle" font-family="Georgia,serif" font-size="110" font-weight="700" fill="#fff">Beautiful.Life</text><text x="600" y="390" text-anchor="middle" font-family="Arial,sans-serif" font-size="38" fill="#fff">Guides · Tools · Experts for a beautiful life</text></svg>')
    if not os.path.exists(os.path.join(ROOT, "config.js")):
        w("config.js", "/* Optional payment links for the Support page. Paste a URL to show the button; leave empty to hide it. */\nwindow.BL_CONFIG = {\n  paypal: \"\",   // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX\n  stripe: \"\",   // e.g. https://donate.stripe.com/XXXX\n  kofi: \"\",     // e.g. https://ko-fi.com/yourname\n  bmac: \"\"      // e.g. https://buymeacoffee.com/yourname\n};\n")

if __name__ == "__main__":
    build_home(); build_articles(); build_topics(); build_tools(); build_feeds()
    build_leadgen(); build_community(); build_info(); build_static()
    print(f"Built {len(PAGES)} pages")
