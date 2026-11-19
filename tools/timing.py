# Final wording pass on sites/*.json for Wooter's lead time.
# Facts, confirmed by Alex on 2026-11-19: three weeks is the average, and rush turnaround
# in one to two weeks costs extra. The batch files say "three weeks" in many places, so this pass
# (1) softens Wooter's "three weeks" to "about three weeks" and
# (2) adds the rush option to FAQ answers about timing that do not mention it yet.
# Sentences about other companies are left alone. Run with -v to print every change.
import glob, json, re, sys

V = "-v" in sys.argv
OTHERS = ["Boombah", "Custom Ink", "Champro", "Nike", "Omni", "Fly Athletics", "Varsity Spirit",
          "Cliff Keen", "All Sports", "Jostens", "RushOrderTees", "DAWG"]
RUSH = ["Rush turnaround in one to two weeks costs extra.",
        "A one to two week rush is available for an added fee.",
        "Paid rush cuts that to one to two weeks.",
        "If the date is tight, rush production takes one to two weeks and costs more.",
        "Wooter also offers a one to two week rush at extra cost.",
        "For a closer deadline, pay for rush and get the order in one to two weeks."]
TIMING_Q = re.compile(r"how long|how early|how far ahead|how fast|how soon|when will|when should|arrive|turnaround", re.I)
SPLIT = re.compile(r"(?<=[.!?])\s+")

def wooters(s):
    return re.search(r"three weeks", s, re.I) and not any(o in s for o in OTHERS)

def soften(text, log):
    out = []
    for s in SPLIT.split(text):
        if wooters(s) and not re.search(r"average|about three weeks", s, re.I):
            t = re.sub(r"\bThree weeks\b", "About three weeks", s)
            t = re.sub(r"(?<!About )\bthree weeks\b", "about three weeks", t)
            log.append((s, t)); s = t
        out.append(s)
    return " ".join(out)

def add_rush(answer, pick, log):
    if re.search(r"one to two", answer): return answer
    parts = SPLIT.split(answer)
    for i, s in enumerate(parts):
        if wooters(s):
            parts.insert(i + 1, pick)
            log.append((answer, " ".join(parts)))
            return " ".join(parts)
    return answer

n_soft = n_rush = 0
for f in sorted(glob.glob("sites/*.json")):
    x = json.load(open(f)); log = []; rlog = []
    h = sum(map(ord, x["domain"]))
    for key in ("verdict", "why"):
        x[key] = [soften(p, log) for p in x.get(key, [])]
    for c in x.get("criteria", []): c["text"] = soften(c["text"], log)
    for st in x.get("steps", []): st["text"] = soften(st["text"], log)
    for sec in x.get("sections", []):
        if "p" in sec: sec["p"] = [soften(p, log) for p in sec["p"]]
        if "list" in sec: sec["list"] = [soften(p, log) if isinstance(p, str) else p for p in sec["list"]]
    for r in x.get("ranking", []):
        if r["id"] != "wooter": continue
        for k in ("fit", "lacks", "note"):
            if r.get(k): r[k] = soften(r[k], log)
    for i, q in enumerate(x.get("faq", [])):
        q["a"] = soften(q["a"], log)
        if TIMING_Q.search(q["q"]): q["a"] = add_rush(q["a"], RUSH[(h + i) % len(RUSH)], rlog)
    n_soft += len(log); n_rush += len(rlog)
    if V:
        for a, b in log: print(x["domain"], "| SOFT |", b)
        for a, b in rlog: print(x["domain"], "| RUSH |", b)
    json.dump(x, open(f, "w"), indent=2, ensure_ascii=False)
print(f"timing pass: {n_soft} sentences softened, {n_rush} answers given the rush option")
