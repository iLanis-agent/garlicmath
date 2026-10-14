(function (root) {
  "use strict";
  var TAKE_RATE = 0.9; // labeled share of planted cloves that make a bulb

  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function clovePlan(areaM2, spacingCm) {
    if (!(areaM2 > 0) || !(spacingCm > 0)) return { error: "the bed and the spacing must be positive" };
    var cloves = Math.ceil(areaM2 * 10000 / (spacingCm * spacingCm));
    var verdict;
    if (cloves <= 30) verdict = "a kitchen-row planting";
    else if (cloves <= 100) verdict = "a raised-bed crop";
    else verdict = "a market garden";
    return { cloves: cloves, verdict: verdict };
  }

  function harvestPlan(cloves, braidSize) {
    if (!(cloves > 0) || !(braidSize > 0)) return { error: "the cloves and the braid must be positive" };
    var bulbs = Math.round(cloves * TAKE_RATE);
    var braids = Math.ceil(bulbs / braidSize);
    var verdict;
    if (bulbs <= 25) verdict = "a pantry shelf";
    else if (bulbs <= 60) verdict = "a hanging row";
    else verdict = "a pantry braid wall";
    return { bulbs: bulbs, braids: braids, verdict: verdict };
  }

  function supplyPlan(bulbs, perWeek) {
    if (!(bulbs > 0) || !(perWeek > 0)) return { error: "the bulbs and the pace must be positive" };
    var weeks = Math.floor(bulbs / perWeek);
    var verdict;
    if (weeks <= 13) verdict = "a season's worth";
    else if (weeks <= 39) verdict = "through the winter";
    else if (weeks <= 52) verdict = "a full year";
    else verdict = "enough to share or replant";
    return { weeks: weeks, verdict: verdict };
  }

  function renderClove(r, areaM2, spacingCm) {
    return "Your " + areaM2 + " m2 bed at a labeled " + spacingCm + " cm spacing takes "
      + plural(r.cloves, "clove") + " - " + r.verdict + ".";
  }

  function renderHarvest(r, cloves, braidSize) {
    return cloves + " cloves at a labeled 90% take is " + plural(r.bulbs, "bulb") + ", about "
      + plural(r.braids, "braid") + " of " + braidSize + " - " + r.verdict + ".";
  }

  function renderSupply(r, bulbs, perWeek) {
    return plural(bulbs, "bulb") + " at " + perWeek + " a week is " + plural(r.weeks, "week")
      + " of garlic - " + r.verdict + ".";
  }

  var api = { clovePlan: clovePlan, harvestPlan: harvestPlan, supplyPlan: supplyPlan, renderClove: renderClove, renderHarvest: renderHarvest, renderSupply: renderSupply };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.GarlicMath = api;
})(this);
