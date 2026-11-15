# Implementation report

The initial release has six independent species pages and four public routes. Coloring uses stable region IDs, paired symmetry, undo/redo, natural colors, clear with confirmation, accessible region selection, and client-side persistence. The collection supports completion, private sightings, and validated versioned backups. The printable edition is a fixed vector PDF plus custom browser printing in US Letter or A4.

## QA run

- `python3 scripts/validate_art.py`: six SVGs parsed; IDs, mirrored pairs, colors, and metadata checked.
- `npm test`: four unit tests passed for pairs, fill logic, natural colors, SVG export, and backup validation.
- `npm run lint`, `npm run typecheck`, `npm run build`: passed.
- `npm run e2e`: Six WebKit tests passed locally (coloring, mobile layout, import, print, keyboard selector, and accessibility). All six tests passed against the final public production deployment, including WCAG scans at 390px and 1280px.
- PDF: 10 Letter pages, no raster images, all pages visually reviewed in a contact sheet.

## Artwork review checklist

- [x] Six separate silhouettes and patterns, each in blank and natural views.
- [x] Stable IDs and explicit bilateral pair mappings.
- [x] Black lines remain visible over custom colors.
- [x] Natural colors and broad field marks checked against named sources.
- [ ] Lepidopterist review of fine wing markings, form, and anatomical accuracy before commercial publication.
- [ ] Compare multiple licensed specimen photographs for each species and document the specimen form.

Public deployment: https://thebutterflybook.vercel.app (production deployment `dpl_4gyG5SUn1FtmCi2qAUtJo74njNxS`, Ready). All ten public paths returned HTTP 200; the live PDF opened as 10 pages.

The current art is provisional simplified coloring art, not a field identification plate. Flat SVG cannot depict the Blue Morpho's iridescence. The site embeds no third-party photos. Local progress is specific to one browser and can be moved with JSON backup.
