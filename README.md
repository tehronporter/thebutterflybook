# Stillness in Flight · The Butterfly Book

An interactive coloring field guide and printable Ecuador sampler. The featured species are the Eighty-eight Butterfly (*Diaethria clymena*), Andromica Glasswing (*Greta andromica*), and Blue Morpho (*Morpho helenor*). The app pairs photographs taken in Ecuador with short biological notes, elevation context, reflection prompts, and detailed vector coloring art.

## Run and verify

```bash
npm install
npm run dev
npm run lint
npm run typecheck
npm test
npm run build
BASE_URL=http://localhost:3000 npm run e2e
python3 scripts/validate_art.py
python3 scripts/generate_book.py
```

End-to-end tests need Playwright WebKit (`npx playwright install webkit`). PDF generation needs Python 3, Pillow, and PyMuPDF. The website itself needs no API keys, account, or server database.

## Product

- `/` introduces the three Ecuador butterflies and links to each coloring studio.
- `/butterflies/[slug]` provides a full photographic reference, three field notes, an elevation note, reflection prompt, saved coloring, page zoom, undo/redo, symmetry where applicable, natural colors, PNG/SVG download, and a private sighting journal. Larger color controls and named regions support phone and tablet coloring.
- `/collection` shows progress and offers versioned JSON backup/import.
- `/print` offers a ten-page US Letter PDF and custom browser printing with selectable species, field guide pages, saved colors, and US Letter or A4.
- `/credits` links every photographer, photo license, file page, and research source.

The PDF at `public/downloads/the-butterfly-book-volume-01.pdf` has a photographic front cover, introduction, three paired field-guide/coloring spreads, a matching line-art back cover, and sources. Each spread places the photograph and notes on the left and a botanical vector coloring page on the right. Tablet PDF apps can import it, though actual stylus behavior depends on the app.

## Data and rights

Species records and SVG artwork live in `lib/species-*.json`. The three active species are selected in `lib/species.ts`; earlier species records remain in the repository so existing saved browser data remains readable. `scripts/redraw_species.py` produces the reference-guided SVG paths while preserving existing color-region IDs. `scripts/validate_art.py` checks the active vector regions and paired coloring IDs. `scripts/generate_book.py` uses the same vector artwork for the PDF. Photographs live in `public/photos` and can be re-fetched using `scripts/prepare_photos.py`.

The photos are licensed CC BY-SA 4.0, CC BY-SA 2.0, and CC BY 4.0 respectively. Each transformed WebP retains its photo's license. Photographer and license attribution appear beside images, on `/credits`, and in the PDF. Commercial use is allowed under these licenses, with attribution and share-alike obligations where applicable. The copyright and license records were reviewed 15 November 2026. Species notes link to Butterflies and Moths of North America, Florida Museum of Natural History, and primary research articles. When an exact elevation for a photographed individual was unavailable, the app says so rather than assigning one.

The illustrations are creative interpretations, not diagnostic identification plates. They need expert review before scientific publication. The Blue Morpho art began with the supplied prototype; the Eighty-eight and Glasswing drawings were created for this sampler.

## Storage and deployment

Colors and sighting notes stay in this browser's localStorage. The Collection page can export and import a backup. Legacy records remain valid in storage even though the Ecuador sampler is now the featured edition. There is no cloud sync.

The repository is [tehronporter/thebutterflybook](https://github.com/tehronporter/thebutterflybook). The Git-connected Vercel project serves [the-butterfly-book.vercel.app](https://the-butterfly-book.vercel.app). The original shared address, [thebutterflybook.vercel.app](https://thebutterflybook.vercel.app), is a separate Vercel project and must be deployed separately after each change.
