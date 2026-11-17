# Beautiful.Life

A life-design and wellbeing hub built with Jekyll, which GitHub Pages builds automatically on the free plan. It has 8 life pillars, 12 long-form guides, 8 private interactive tools, an expert-matching lead funnel, a self-updating good-news feed, a video library, monthly contests, a supporter/donation page, careers, partnerships and full legal pages.

## Publish (one time)
Settings → Pages → Build and deployment → Source: **Deploy from a branch** → Branch: **main** / **(root)** → Save.
The site goes live at `https://webworksa1.github.io/beautiful-life/`.

## Custom domain (beautiful.life)
1. Point DNS: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (and `www` CNAME → `webworksa1.github.io`).
2. Settings → Pages → Custom domain → `beautiful.life` → Enforce HTTPS.
3. In `_config.yml` change `baseurl: "/beautiful-life"` to `baseurl: ""`.

## Structure
- `_articles/`: one HTML file per article (front matter: title, description, cat, emoji, mins, date). Add a file and it appears everywhere automatically.
- `_data/pillars.yml`, `_data/tools.yml`: the navigation, pillar pages and tool cards.
- `_layouts/`, `_includes/`: the shared header, footer, AdSense tag, cookie banner and lead-gen box.
- `topics/`, `tools/`: pillar pages and interactive tool pages.
- `assets/js/main.js`: forms, live news feed, videos and UI. `assets/js/tools.js`: the interactive tools.
- `data/news.json`, `data/videos.json`: seed and fallback content. Visitors' browsers fetch live news on top of it.
- `config.js`: optional PayPal, Stripe, Ko-fi or Buy Me a Coffee links. A button appears only once its link is filled in.
- `automation/update-content.yml`: optional daily server-side refresh. See the comments in the file to enable it.

## Forms
All forms post through a secure relay. The destination address is encoded in `assets/js/main.js` and is never rendered on any page. The first submission triggers a one-time activation email from FormSubmit, and the link in it must be confirmed.

## Monetisation
Google AdSense Auto Ads (`ca-pub-6620975821265271`) loads in every page `<head>`, and `ads.txt` is included. Further revenue comes from lead generation, sponsorships, contests and reader support.

## Trademark
Beautiful.Life is an independent publication and is not affiliated with any brand using similar names. See `disclaimer.html`.
