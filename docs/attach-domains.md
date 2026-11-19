# Attaching GoDaddy domains to the Replit deployment

All 95 domains in `data/domains.txt` were attached on 2026-11-19 through Replit's Domains panel and GoDaddy Domain Connect (Entri). About 45 seconds per domain once the loop is stable.

## What each domain needs

1. Replit, Tools, Domains: type the domain under "Use a domain you already own", press Next.
2. The Entri modal opens. "Continue with GoDaddy" opens GoDaddy Domain Connect. Cmd+click it so it opens as a tab instead of a popup.
3. On GoDaddy, press Connect. It sets the A record (34.111.179.208) and the verification TXT. Close the tab.
4. Back in Replit the modal shows a free-domain offer. Press "No, thanks." Never "Claim domain for free".
5. The domain shows as a row. The dot goes amber to green when DNS verifies.

## Things that cost time

- Every add triggers a republish. While it runs, the Domains panel is stale and Next does nothing. Replit shows a toast: "This app is already published. Reopen the Domains tab and try again." Fix: click Publishing, then Domains, before every add.
- Sometimes the row does not appear after Connect. Add the same domain again. DNS is already set, so no modal opens and the row appears.
- GoDaddy sometimes answers "There was an error processing your request." Reload that tab and Connect appears.
- One republish failed at the Promote step during the run ("built successfully but failed to start", flagged by Replit as a likely platform issue). The earlier deployment kept serving and the status went back to live on its own. The health check noise in the logs (`healthcheck / returned status 500`, `connection refused`) also shows on successful deploys.
- `DATABASE_URL` in the deployment points at the dev database host, so analytics falls back to memory until a production Postgres is provisioned.

## After attaching

- Domains with a page in `sites/` serve it. The rest serve a 503 holding page with noindex and `Disallow: /`.
- Add each domain to Search Console and submit its sitemap once its page is live.
