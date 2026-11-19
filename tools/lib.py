# Shared helpers for the page batches. Each batch file calls page(...) then save().
import json, os
UPDATED = "2026-11-19"
W = "https://wooter.com"
U = dict(
    builder=W + "/search?design_option=wooter_customizer", design=W + "/design-request/products",
    basketball=W + "/search/basketball", baseball=W + "/search/baseball", football=W + "/search/football",
    soccer=W + "/search/soccer", softball=W + "/search/softball", volleyball=W + "/search/volleyball",
    flag=W + "/search/flag-football", sevens=W + "/search/7v7-football", cheer=W + "/search/cheer",
    wrestling=W + "/search/wrestling", hoodies=W + "/search/custom-apparel/hoodies",
    jackets=W + "/search/custom-apparel/jackets", track=W + "/search/custom-apparel/track-jackets",
    bags=W + "/search/bags", compression=W + "/search/compression", apparel=W + "/search/custom-apparel",
    varsity=W + "/products/varsity-jacket-apparel", all=W + "/search",
    bbpackages=W + "/category/basketball", bspackages=W + "/search/baseball/packages",
    reversible=W + "/products/reversible-v-neck-basketball-jerseys-basketball",
    shooting=W + "/products/long-sleeved-shooting-shirts-basketball",
    singlets=W + "/products/wrestling-singlets-wrestling",
    fanshop=W + "/articles/what-is-a-team-store-one-link-individual-payments-direct-shipping/",
    sizing="https://wooterapparel.com/sizing",
)
MIN = "One on most items. Wooter's product pages list a minimum quantity of one, and the price per piece drops as the order grows."
SMALL = {"for", "with", "a", "of", "and", "to", "the", "in", "on"}
def tc(q):
    out = []
    for i, w in enumerate(q.split()):
        out.append(w if (w in SMALL and i) or w[0].isdigit() else w[0].upper() + w[1:])
    return " ".join(out)

# Default "who it fits / what it lacks" rows for the other companies, by sport cluster.
# Every claim here traces to data/products.json sources.
R = {
 "general": {
  "boombah": ("Teams that want a sublimated uniform built online and bought straight from the maker.", "Lead times and minimums differ from page to page on its site."),
  "customink": ("Small groups that want names and numbers printed on a stock jersey in about two weeks.", "Mostly stock garments with your print added, not a jersey built from your pattern."),
  "champro": ("Programs that order through a local team dealer and want cut-and-sew sublimation.", "Orders go through a dealer account. There is no public checkout."),
  "niketeam": ("Schools and clubs that want Nike and work with an authorized dealer.", "Build-to-order uniforms take 30, 60 or 90 days.")},
 "basketball": {
  "boombah": ("Teams that want reversible jerseys and shorts built online by a maker with its own factories.", "Three weeks standard on its basketball page, and other pages quote different times. Confirm before you order."),
  "customink": ("Small groups that need names and numbers on a stock jersey or reversible tank in about two weeks.", "Mostly stock garments with your print added, so the cut and panels are fixed."),
  "champro": ("Programs with a team dealer that want cut-and-sew Juice sublimation.", "A dealer account places the order. There is no public checkout."),
  "niketeam": ("Schools and clubs that want Nike and already work with an authorized dealer.", "Build-to-order uniforms take 30, 60 or 90 days.")},
 "baseball": {
  "boombah": ("Baseball teams that want sublimated jerseys and pants from one maker's own factories.", "Its baseball pages quote different lead times. Get the date in writing."),
  "champro": ("Teams with a local dealer that want a cut-and-sew Juice jersey or a lower-cost Splash one.", "Ordered through a dealer account, with lead time confirmed after artwork approval."),
  "customink": ("Rec and company teams that need a printed button-front jersey in about two weeks.", "Stock garments with your print added, not a jersey built from your pattern."),
  "niketeam": ("School programs that want Nike and plan a season ahead with a dealer.", "Build-to-order takes 30, 60 or 90 days. Personalized stock arrives within three weeks.")},
 "softball": {
  "boombah": ("Fastpitch and slowpitch teams that want sublimated jerseys from a company whose range is deepest on the diamond.", "Lead times and minimums vary by product page. Check the one you choose."),
  "champro": ("Softball programs that buy through a team dealer.", "No public price list. Your dealer sets the price and places the order."),
  "customink": ("Rec and coed teams that want a printed jersey fast, with a group order form for sizes.", "Decorated stock apparel, so there is no custom cut and no matching pants."),
  "niketeam": ("School softball programs that want Nike through an authorized dealer.", "Not built for a team that needs uniforms next month.")},
 "soccer": {
  "customink": ("Rec and small-sided teams that want names and numbers on a stock kit, with free standard shipping.", "The design choices stop at the print. The jersey itself is a stock style."),
  "champro": ("Clubs that order through a dealer and want cut-and-sew sublimated kits.", "Dealer ordering only, with no public price list."),
  "boombah": ("Teams that like building a sublimated uniform online. Each one is printed, cut and sewn to order.", "Soccer is a smaller part of its range than baseball and softball."),
  "niketeam": ("Clubs that want Nike and can plan around a dealer's timeline.", "Build-to-order kits take 30, 60 or 90 days.")},
 "football": {
  "champro": ("Programs with a team dealer that want a fitted, cut-and-sew Juice jersey.", "A dealer account places the order, and lead time is confirmed after artwork approval."),
  "customink": ("Flag, intramural and club teams that want sublimated or printed jerseys with free shipping.", "Its sublimated football styles come from other brands' catalogs, so designs start from their templates."),
  "niketeam": ("School programs that want Nike and order a season ahead.", "Build-to-order takes 30, 60 or 90 days, and pricing comes from the dealer.")},
 "flag": {
  "customink": ("Rec leagues that want flag jerseys with names and numbers and free shipping. Its page lists flag jerseys from around $40 a piece at volume.", "Styles come from stock and partner-brand catalogs, not a pattern drawn for your team."),
  "champro": ("Teams with a dealer that want a Juice sublimated 7v7 jersey.", "Ordered through a dealer, with no public checkout.")},
 "volleyball": {
  "boombah": ("Teams that want to build sublimated volleyball jerseys online and buy from the maker.", "Volleyball is a smaller line for it than baseball and fastpitch."),
  "customink": ("Rec and club teams that want fitted performance jerseys printed with names and numbers.", "Stock styles with decoration. No libero jersey cut from your own pattern."),
  "champro": ("School programs that order volleyball uniforms through a team dealer.", "Dealer pricing and dealer ordering."),
  "niketeam": ("Programs that want Nike and have a dealer.", "30 to 90 days on build-to-order uniforms.")},
 "cheer": {
  "varsityspirit": ("School and All Star programs that want a local rep to design the uniform and size the athletes in person.", "No public pricing or online checkout for custom uniforms. Everything runs through the rep."),
  "omnicheer": ("Squads that want in-stock shells and skirts quickly, or a sublimated set built in an online studio.", "Sublimated pieces need a minimum of six and take 4 to 6 weeks."),
  "flyathletics": ("All Star gyms that want couture detail such as rhinestone patterns and custom stitching.", "Six to eight weeks to produce, with a minimum of six uniforms per design."),
  "customink": ("Rec and school squads that want sublimated shells, skirts and skorts with volume pricing shown upfront.", "A catalog of set styles in ladies and girls cuts, recolored rather than drawn for you.")},
 "wrestling": {
  "cliffkeen": ("Programs that want singlets made in Ann Arbor, Michigan, with men's, women's and international cuts.", "A minimum of six on most custom products, and 3 to 5 weeks after art approval."),
  "allsports": ("Teams that want DAWG singlets from an online builder, with one and two week rush when the season is close.", "Small orders of women's singlets carry a per-singlet fee."),
  "boombah": ("Teams already buying Boombah for other sports that want a sublimated singlet from the same maker.", "Wrestling is a small part of what it makes.")},
 "varsity": {
  "jostens": ("High school students who want a traditional letter jacket with school and activity patches.", "A base jacket starts around $200 before patches, embroidery or leather sleeves."),
  "rushordertees": ("Groups that want a printed or embroidered logo on a stock letterman jacket, some with no minimum.", "Stock jackets from brands like Sport-Tek and Augusta, decorated rather than made to your design.")},
 "apparel": {
  "customink": ("Groups of any size that want hoodies, jackets or bags printed or embroidered, with free shipping.", "Mostly decorated stock apparel. Its fully sublimated outerwear comes from one partner brand's collection."),
  "boombah": ("Baseball and softball teams that want hoodies, jackets, warm-ups and pullovers alongside their uniforms.", "The apparel range is built around its diamond sports."),
  "rushordertees": ("Groups that want a logo printed or embroidered on a stock jacket, often with no minimum for print.", "Stock styles only. Embroidery usually needs six pieces.")},
}
_cluster = ["general"]
def use(c): _cluster[0] = c
def rk(i, fit=None, lacks=None, note=None, c=None):
    d = R[c or _cluster[0]].get(i) or R["general"].get(i) or (None, None)
    assert (fit or d[0]) and (lacks or d[1]), i
    out = {"id": i, "fit": fit or d[0], "lacks": lacks or d[1]}
    if note: out["note"] = note
    return out

S = []
ORDER = ["domain", "cluster", "template", "query", "site_name", "title", "updated", "published", "verdict", "cta", "cta2",
         "steps_title", "steps", "generator", "sections", "ranking", "pub_title", "why", "criteria", "faq", "related"]
def page(domain, cluster, template, query, verdict, ranking=None, why=None, criteria=None, faq=None, cta=None, cta2=None,
         steps=None, steps_title=None, sections=None, generator=None, title=None, pub_title=None):
    x = dict(domain=domain, cluster=cluster, template=template, query=query, site_name=tc(query),
             title=title or tc(query) + " (2026)", updated=UPDATED, verdict=verdict, ranking=ranking or [], why=why or [],
             criteria=[{"name": n, "text": t} for n, t in (criteria or [])], faq=[{"q": q, "a": a} for q, a in faq], related=[])
    if cta: x["cta"] = {"url": cta[0], "text": cta[1]}
    if cta2: x["cta2"] = {"url": cta2[0], "text": cta2[1]}
    if steps: x["steps"] = [{"name": n, "text": t} for n, t in steps]
    if steps_title: x["steps_title"] = steps_title
    if sections: x["sections"] = sections
    if generator: x["generator"] = generator
    if pub_title: x["pub_title"] = pub_title
    assert len(verdict) >= 2 and len(x["faq"]) >= 4, domain
    S.append(x)

MINV = [MIN,
 "No real minimum. Most Wooter product pages allow an order of one, though the per-piece price is far lower at team quantity.",
 "Most Wooter products can be ordered one at a time. The price breakdown on each page shows how the cost falls as you add pieces.",
 "Wooter lists a minimum quantity of one on most products. Small orders are welcome and cost more per piece than large ones."]
LEAD0 = "Three to four weeks after you approve the design at Wooter, with rush production offered."
LEADV = [LEAD0,
 "Wooter's product pages quote three to four weeks from design approval, and rush production is available.",
 "Plan on three to four weeks from the day you approve the proof. Wooter offers rush production if you are short on time.",
 "About three to four weeks once the design is approved. Ask Wooter about rush production for a tighter date."]
def vary(x):
    # The two stock answers appear on many pages. Rotate the wording by domain so pages do not share sentences.
    h = sum(map(ord, x["domain"]))
    for f in x["faq"]:
        if f["a"] == MIN: f["a"] = MINV[h % 4]
        if LEAD0 in f["a"]: f["a"] = f["a"].replace(LEAD0, LEADV[(h // 4) % 4])

def save():
    doms = {l.strip() for l in open("data/domains.txt") if l.strip()}
    for x in S:
        assert x["domain"] in doms, x["domain"]
        vary(x)
        f = "sites/" + x["domain"] + ".json"
        x["published"] = json.load(open(f)).get("published", UPDATED) if os.path.exists(f) else UPDATED
        json.dump({k: x[k] for k in ORDER if k in x}, open(f, "w"), indent=2, ensure_ascii=False)
    print(len(S), "sites written")
