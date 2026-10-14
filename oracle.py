import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round0(x): return jsnum(math.floor(x + 0.5))

TAKE_RATE = 0.9

def clove_plan(areaM2, spacingCm):
    if not (areaM2 > 0) or not (spacingCm > 0):
        return {"error": "the bed and the spacing must be positive"}
    cloves = math.ceil(areaM2 * 10000 / (spacingCm * spacingCm))
    if cloves <= 30: verdict = "a kitchen-row planting"
    elif cloves <= 100: verdict = "a raised-bed crop"
    else: verdict = "a market garden"
    return {"cloves": cloves, "verdict": verdict}

def harvest_plan(cloves, braidSize):
    if not (cloves > 0) or not (braidSize > 0):
        return {"error": "the cloves and the braid must be positive"}
    bulbs = round0(cloves * TAKE_RATE)
    braids = math.ceil(bulbs / braidSize)
    if bulbs <= 25: verdict = "a pantry shelf"
    elif bulbs <= 60: verdict = "a hanging row"
    else: verdict = "a pantry braid wall"
    return {"bulbs": bulbs, "braids": braids, "verdict": verdict}

def supply_plan(bulbs, perWeek):
    if not (bulbs > 0) or not (perWeek > 0):
        return {"error": "the bulbs and the pace must be positive"}
    weeks = math.floor(bulbs / perWeek)
    if weeks <= 13: verdict = "a season's worth"
    elif weeks <= 39: verdict = "through the winter"
    elif weeks <= 52: verdict = "a full year"
    else: verdict = "enough to share or replant"
    return {"weeks": weeks, "verdict": verdict}

def render_clove(r, areaM2, spacingCm):
    return ("Your " + fmt(areaM2) + " m2 bed at a labeled " + fmt(spacingCm) + " cm spacing takes "
            + plural(r["cloves"], "clove") + " - " + r["verdict"] + ".")

def render_harvest(r, cloves, braidSize):
    return (fmt(cloves) + " cloves at a labeled 90% take is " + plural(r["bulbs"], "bulb") + ", about "
            + plural(r["braids"], "braid") + " of " + fmt(braidSize) + " - " + r["verdict"] + ".")

def render_supply(r, bulbs, perWeek):
    return (plural(bulbs, "bulb") + " at " + fmt(perWeek) + " a week is " + plural(r["weeks"], "week")
            + " of garlic - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[2,15],[1,10],[5,15],[0.5,20],[3,12],[1.5,18],[4,10],[2.5,15],[0,15],[2,0]]:
    add("clovePlan", clove_plan, render_clove, a)
for a in [[89,12],[100,10],[30,12],[223,12],[13,8],[50,10],[75,12],[60,10],[0,12],[89,0]]:
    add("harvestPlan", harvest_plan, render_harvest, a)
for a in [[80,2],[100,3],[40,2],[26,1],[52,1],[90,1],[20,2],[60,4],[0,2],[80,0]]:
    add("supplyPlan", supply_plan, render_supply, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
