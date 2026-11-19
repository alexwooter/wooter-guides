# Wooter guides

One codebase that serves a separate page on each exact-match domain in `data/domains.txt`. The server reads the request's hostname and serves `dist/<domain>/`. Adding a domain is adding a JSON file in `sites/`. Forked from `alexwooter/best-guides`; PLAYBOOK.md is the full runbook.

## Status (18 Nov 2026)

- Search terms: 479 ranked from Google Ads Keyword Planner (wooterapparel.com account, US). GoDaddy bulk check the same day: 315 open at standard price, 54 premium, 110 taken.
- First batch: 95 standard-price names, listed in `research/first-95.csv`.
- Pending before pages are written: bought list, Wooter legal entity name (publisher.json carries the site footer's "Wooter Apparel"), one production time, the competitor set.

## Page types

- Buyer's guide: ranked, Wooter first, alternatives described from their own sites.
- Design tool: opens the Wooter builder for that sport.
- Tool / info: working generator or size chart on the page.
- Local and fundraising guides.

One real page per intent. Variant domains 301 to the closest page.

## Rules

- Publisher disclosure in every footer. No other company's trademark in a domain.
- Competitor facts come from their own public pages, with a `verified` date. Prices only when verified.
- Related links only to pages that are built.

## Facts to refresh

`data/products.json` is the single place for Wooter's and competitors' facts. Rebuild and redeploy; every page updates.

## Pages

All 95 domains in `data/domains.txt` have a page in `sites/`. They come in three kinds:

- Buyer's guides (layouts `ledger`, `terminal`, `paper`, `brief`): a ranked comparison with Wooter first and the reason stated.
- Design-tool pages (`studio`, `bench`): steps first, then the tools compared.
- Info and tool pages (`field`): name generators, size charts, number fonts, fundraising and design ideas. No ranking.

The pages are written in `tools/batch*.py` and the fact sheet in `tools/batch1.py` and `tools/facts.py`. Edit there, then run `./tools/build_all.sh`, which regenerates `sites/*.json`, sets related links and builds `dist/`.

Every claim about another company comes from that company's own pages, listed under `sources` in `data/products.json`. Wooter prices quoted on pages were read from wooter.com in November 2026 and say so.
