# Beautiful.Life

A static, AdSense-ready life-design and wellbeing hub. It ships with 8 life pillars, 12 long-form guides, 8 private interactive tools, an expert-matching lead funnel, a daily auto-updated good-news feed, a video library, monthly contests, a supporter/donation page, careers, partnerships and full legal pages.

## Structure
- `build/content.py`: pillars and articles. Add an article dict here.
- `build/build.py`: generates every HTML page, `sitemap.xml`, `robots.txt`, `ads.txt` and `manifest.json`. Run `python3 build/build.py`.
- `assets/`: CSS, JS (`main.js` for core behaviour and forms, `tools.js` for the interactive tools) and images.
- `data/news.json` and `data/videos.json`: refreshed daily by `.github/workflows/update-content.yml`, which runs `scripts/update_feeds.py`.
- `config.js`: optional PayPal, Stripe, Ko-fi or Buy Me a Coffee links for the Support page. A button only appears once its link is filled in.

## Hosting
GitHub Pages: Settings → Pages → Source: *Deploy from a branch* → `main` / root.
For the custom domain, add a `CNAME` file containing `beautiful.life` and point DNS at GitHub Pages (A records 185.199.108-111.153).

## Forms
All forms post via a secure relay. The destination address is encoded in `assets/js/main.js` and never appears in page content. The first submission triggers a one-time activation email from FormSubmit, and the link in it must be confirmed.

## Monetisation
Google AdSense Auto Ads (`ca-pub-6620975821265271`) loads in every page `<head>`, and `ads.txt` is included. Further revenue comes from lead generation, sponsorships, contests and reader support.

## Trademark
Beautiful.Life is an independent publication and is not affiliated with any brand using similar names. See `disclaimer.html`.
