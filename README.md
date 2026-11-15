# The Butterfly Book

An interactive coloring field guide for six butterflies. Built with Next.js 15, React 19, TypeScript, local browser storage, editable SVG artwork adapted from the supplied prototype, and a reproducible vector PDF.

## Run locally

```bash
npm install
npm run dev
```

Open `http://localhost:3000`. No API keys, database, account, or external runtime service is required.

## Checks and build

```bash
npm run validate
npm test
npm run lint
npm run typecheck
npm run build
npm run e2e     # requires: npx playwright install webkit
npm run book    # requires Python 3 and pymupdf
```

The app has `/`, `/butterflies/[slug]`, `/collection`, and `/print`. `public/downloads/the-butterfly-book-volume-01.pdf` is a **10-page** US Letter PDF with cover, instructions, six species, journal, and sources. The Print page also lets visitors choose species, US Letter or A4, natural reference, and their own colors for browser printing.

## Data and artwork

Species data and wing geometry live in `lib/species-*.json`. Each region has a stable ID, paired region ID, accessible label, and natural color. `scripts/validate_art.py` checks IDs, pairs, metadata, and colors. `scripts/generate_book.py` builds the vector PDF from the same SVG geometry and content. `scripts/extract_reference.py` records how the original user-supplied HTML prototype was parsed; edited JSON is the current authoring source.

To revise artwork: edit the SVG and its `regions` array together, keep IDs stable so saved color work remains compatible, run `npm run validate`, `npm test`, regenerate the book, and visually inspect all six blank and natural views plus the resulting PDF. For publication review, compare dorsal wing shape, sex or form, markings, palette, and size against named specimen photographs and have a lepidopterist review the art. Current illustrations are **simplified and provisional**. They are coloring art and broad visual references, not definitive identification plates. No third-party photographs are embedded or hotlinked.

Source-backed facts and taxonomy use Butterflies and Moths of North America, University of Florida IFAS Extension, and Florida Museum of Natural History. Each species page links to its source; source URLs and the access date (15 November 2026) are in its JSON. `Morpho peleides` also appears in newer literature as `Morpho helenor peleides`; taxonomy merits editorial review before commercial publication. Source pages describe regional, sex, and seasonal variation, so range and flight seasons are approximate.

## Local data

Coloring, completion, and sighting notes are saved only in this browser's localStorage. The Collection page exports/imports versioned JSON backups. Import validates the schema and asks before replacement. Corrupted stored data is preserved and surfaced as an error. A sighting is a personal record, not verified identification. There is no cloud sync.

## Deploy

The source is hosted at [tehronporter/thebutterflybook](https://github.com/tehronporter/thebutterflybook). The `main` branch is connected to the new Vercel project `the-butterfly-book` for automatic production deploys. The earlier CLI deployment remains at [thebutterflybook.vercel.app](https://thebutterflybook.vercel.app). The project is static friendly and can also deploy directly to Vercel:

```bash
npx vercel --prod
```

Vercel requires no application environment variables. Verify public access to the four routes and PDF after deploying.

## Implementation notes and limits

- Six species have separate SVG geometry and natural palettes, mirrored coloring, undo and redo, erase, completion, sightings, PNG/SVG export, a local collection, backup, and printable pages.
- The natural color illustrations are source-informed simplifications; their small details and individual forms still need scientific art review. Blue Morpho dorsal color cannot reproduce true iridescence in flat SVG.
- Browser print output depends on the user's print settings. The downloadable edition is a fixed US Letter PDF; A4 is available for the custom browser print flow.
- Automated WebKit checks cover desktop and narrow/mobile layouts. Actual iPhone Safari hardware has not been tested.
