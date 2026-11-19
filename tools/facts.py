# Adds the category specialists to data/products.json. Run after batch1.py.
# Every line comes from the company's own pages, listed under sources. Checked 2026-11-19.
import json
p = json.load(open("data/products.json"))
p["wooter"]["sources"] += ["https://wooter.com/category/basketball", "https://wooter.com/products/wrestling-singlets-wrestling/904/003",
    "https://wooter.com/packages/cheerleading-uniform", "https://wooter.com/products/varsity-jacket-apparel", "https://wooter.com/category/compression"]
p["wooter"]["verified"] = "2026-11-19"
p.update({
 "varsityspirit": {"name": "Varsity Spirit", "url": "https://www.varsity.com/uniforms", "type": "Cheer uniforms ordered through a local rep",
  "what": "Varsity Spirit has made cheer uniforms since 1979, for school and All Star programs. A local Varsity rep guides the order, helps design the uniform and sizes the athletes in person.",
  "fit": "School and All Star programs that want a rep to run the process.", "pricing": "Quoted through your rep. There is no public checkout for custom uniforms.",
  "turnaround": "Set with your rep once the design and sizing are done.",
  "sources": ["https://varsity.com/uniforms", "https://www.varsity.com/school/spirit-fashion/vsfuniforms/", "https://www.varsity.com/school/spirit-fashion/juniorvarsity/"], "verified": "2026-11-19"},
 "omnicheer": {"name": "Chassé at Omni Cheer", "url": "https://www.omnicheer.com", "type": "Cheer uniforms with an online design studio",
  "what": "Omni Cheer sells Chassé uniforms: in-stock shells and skirts that ship ready to wear, and sublimated uniforms you build in its online design studio.",
  "fit": "Squads that want stock uniforms fast or a sublimated set designed online.", "pricing": "Prices are on each product page. Sublimated pieces carry a minimum quantity of six.",
  "turnaround": "Its customization page lists 4 to 6 weeks for sublimation and 3 to 4 weeks for lettering on stock uniforms.",
  "sources": ["https://www.omnicheer.com/Customization-Mascots", "https://www.omnicheer.com/collections/chasse-uniforms", "https://www.omnicheer.com/sublimation/"], "verified": "2026-11-19"},
 "flyathletics": {"name": "Fly Athletics", "url": "https://flyathletics.com/custom-cheer-uniforms/", "type": "Custom cheer uniforms for All Star and school teams",
  "what": "Fly Athletics makes fully custom cheer uniforms, from fabric and colors to rhinestone patterns and stitching, and has a cheer design app.",
  "fit": "Gyms that want a couture competition look.", "pricing": "Quoted per design. A minimum of six uniforms per design, with no minimum on reorders.",
  "turnaround": "First designs in 24 to 48 hours. Production in six to eight weeks.",
  "sources": ["https://flyathletics.com/custom-cheer-uniforms/"], "verified": "2026-11-19"},
 "cliffkeen": {"name": "Cliff Keen", "url": "https://cliffkeen.com/pages/design-lab", "type": "Wrestling singlets made in Ann Arbor, Michigan",
  "what": "Cliff Keen builds custom sublimated singlets from templates in its uniform builder, in men's, women's and international cuts. All of its singlets are produced in Ann Arbor, Michigan.",
  "fit": "Wrestling programs that want a specialist.", "pricing": "Singlet templates list from $84.50 to $98.50, with a minimum order of six on most custom products.",
  "turnaround": "Orders usually ship within 3 to 5 weeks of final art approval. Some product pages estimate 4 to 6.",
  "sources": ["https://cliffkeen.com/pages/design-lab", "https://cliffkeen.com/products/the-ck-deluxe", "https://cliffkeen.com/products/template-43", "https://cliffkeen.com/products/leg-bands-t-back"], "verified": "2026-11-19"},
 "allsports": {"name": "All Sports Uniforms", "url": "https://allsportsuniforms.net/wrestling/", "type": "DAWG wrestling singlets with an online builder",
  "what": "All Sports Uniforms sells DAWG sublimated singlets, women's singlets, rashguards, fight shorts and warmups, designed in its Wrestling Uniform Builder or from your own artwork.",
  "fit": "Clubs and schools that want a builder and a rush option.", "pricing": "Quoted by order. Orders of one to six women's singlets carry a $20 per-singlet fee, and reorders have no minimum.",
  "turnaround": "Standard production is three weeks, with one and two week rush.",
  "sources": ["https://allsportsuniforms.net/wrestling/", "https://allsportsuniforms.net/custom-wrestling-uniforms/", "https://allsportsuniforms.net/custom-womens-wrestling-singlets/"], "verified": "2026-11-19"},
 "jostens": {"name": "Jostens", "url": "https://www.jostens.com", "type": "School letter jackets with patches",
  "what": "Jostens sells letter jackets through an online builder that walks you through each step, with more than 100 patches for sports and activities.",
  "fit": "Students marking a varsity letter.", "pricing": "A base letterman jacket starts around $200. Patches, embroidery and leather sleeves are priced as add-ons.",
  "sources": ["https://jostens-auth.dotcms.cloud/apparel/jackets-and-patches/letter-jackets"], "verified": "2026-11-19"},
 "rushordertees": {"name": "RushOrderTees", "url": "https://www.rushordertees.com/jackets/letterman-varsity", "type": "Printed and embroidered jackets on stock styles",
  "what": "RushOrderTees decorates stock letterman and varsity jackets from brands like Sport-Tek and Augusta Sportswear with your print or embroidery, designed in its online studio.",
  "fit": "Groups that want a logo on a ready-made jacket.", "pricing": "Volume pricing is shown per style. No minimum for printed jackets and six pieces for most embroidery.",
  "sources": ["https://www.rushordertees.com/jackets/letterman-varsity", "https://www.rushordertees.com/custom/varsity-letterman-jackets"], "verified": "2026-11-19"},
})
json.dump(p, open("data/products.json", "w"), indent=2, ensure_ascii=False)
print(len(p), "products")
