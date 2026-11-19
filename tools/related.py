# Sets each site's related links: the next five in its own cluster, then two or three general hubs.
# Run last, after every batch. Keeps cross-linking modest on purpose.
import json, glob
order = [l.strip() for l in open("data/domains.txt") if l.strip()]
sites = {d: json.load(open(f"sites/{d}.json")) for d in order}
HUBS = ["bestcustomjerseys.com", "customjerseybuilder.com", "jerseysizechart.com", "randomteamnamegenerator.com", "jerseydesignideas.com", "cheapcustomjerseys.com", "fundraisingideasforsportsteams.com"]
by = {}
for d in order: by.setdefault(sites[d]["cluster"], []).append(d)
for n, d in enumerate(order):
    c = by[sites[d]["cluster"]]; i = c.index(d)
    rel = [c[(i + k) % len(c)] for k in range(1, min(6, len(c)))]
    for k in range(len(HUBS)):
        h = HUBS[(n + k) % len(HUBS)]
        if len(rel) >= 7: break
        if h != d and h not in rel: rel.append(h)
    sites[d]["related"] = rel
    json.dump(sites[d], open(f"sites/{d}.json", "w"), indent=2, ensure_ascii=False)
print(len(order), "sites linked")
