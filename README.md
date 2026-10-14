# Garlic math

Fall garlic planting arithmetic: the bed names the cloves, the cloves name the braids, and the braids name the winter.

Live at https://ilanis-agent.github.io/garlicmath/

## The three tools

- **Clove plan** - cloves = ceil(bed m2 x 10000 / spacing cm squared), with kitchen-row, raised-bed and market-garden bands.
- **Harvest plan** - bulbs = cloves x a labeled 90% take (round half up), braids = ceil(bulbs / braid size), with pantry-shelf, hanging-row and braid-wall bands.
- **Supply plan** - weeks = floor(bulbs / bulbs a week), with season's-worth, through-the-winter, full-year and share-or-replant bands.

## Formulas and limits

- Counts use ceiling for buying and floor for weeks of supply, mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: grid spacing, take rate, braid size.
- Illustrative planning arithmetic only. Plant cloves point-up, a knuckle deep, a few weeks before the ground freezes, and mulch after planting. Keep the best bulbs for next year's seed, and certified disease-free seed garlic beats any schedule this page can draw.

## Development

- `engine.js` - calculation and render engine (browser global `GarlicMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
