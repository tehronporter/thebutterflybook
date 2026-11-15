# The Butterfly Book — Codex Master Build Prompt

## Role and mission
Act as a senior product designer, full-stack engineer, accessibility specialist, and natural-history editorial designer. Build **The Butterfly Book**, a polished, mobile-first interactive butterfly coloring field guide and companion printable coloring book. The product originated from a mother’s idea: let people color real butterflies however they like, learn interesting facts, see their actual colors, and recognize them in the wild. Keep butterflies as the sole focus of the initial release. Build a functioning application, not a mockup or a landing page alone.

**Tagline:** Color. Discover. Explore.

## 1. Deliverables and workflow
- Inspect the existing repository before modifying anything. If starting from scratch, scaffold the stack below. If supplied, inspect `The_Butterfly_Book.html` and `The_Butterfly_Book.pdf` as prototype references; preserve their useful functionality, but improve their illustration quality and architecture. Do not assume those files are present.
- Implement the complete MVP, including the public website, interactive coloring studio, species field guide, local collection, and printable PDF edition.
- Create a README with local setup, commands, deployment, data provenance, artwork authoring instructions, and known limitations. Include tests and a short implementation report.
- Deploy to Vercel if the CLI/account is authorized and available. Use a public production deployment with no login wall; verify its URL in a fresh browser. Suggest `thebutterflybook.vercel.app` if available; never invent or claim a deployment URL. If credentials are unavailable, provide exact deployment commands.
- Start by briefly outlining implementation and inspecting files, then proceed through the build, tests, and fixes without unnecessary approval pauses. Do not overwrite unrelated work.

## 2. Product experience
Audience: adults who enjoy coloring and nature, families, children with supervision, and casual butterfly watchers. The app should feel gentle, editorial, and intuitive for an older adult using an iPhone. No mandatory account, ads, payment, or onboarding wall. The user can begin coloring in one tap. All core activities work without a backend.

Primary navigation: **Explore / Color / My Collection / Print**. On small screens use a compact accessible bottom navigation or simple header; avoid redundant navigation. Use meaningful URLs and support browser back/forward.

### Home / Explore (`/`)
- Small wordmark, spacious hero with one beautiful butterfly on pure white, title and tagline, primary CTA “Start coloring,” secondary CTA “Explore butterflies.”
- Display a responsive species gallery with accurate natural-color previews, common name, scientific name and optional habitat/region labels. Cards lead to species pages; no generic photos as placeholders for species.
- Search by common/scientific name and filter by region or color if useful; include clear empty states. Keep controls unobtrusive.
- Brief explanation of the three actions: color, learn, explore. Include a link to download the book.

### Species / Coloring Studio (`/butterflies/[slug]`)
Desktop: large drawing canvas on the left, species information and compact reference on the right. Mobile: name and compact reference, large drawing canvas, palette and tools within easy reach, followed by educational content. No horizontal page overflow.
- Show species number, common name, italic scientific name, natural-color thumbnail and a larger optional reference view. A reference photograph must be correctly licensed, attributed, and match the species and sex/form when known. Original scientifically reviewed reference art is acceptable if labeled.
- Show a large original line-art SVG on white. Every meaningful wing region must be independently fillable. Clicking/tapping a region applies the selected color immediately. Preserve outlines and boundaries; no accidental recoloring of background or neighboring cells.
- Species-specific natural palette plus a small shared creative palette, custom color picker, active-color indication and white/eraser tool. Users can use any color, not just real colors.
- Symmetry toggle on by default: paint the homologous region on the opposite wing; when off, paint only the selected region. Pair regions by explicit stable metadata, not visual coordinates or DOM order.
- Undo and redo, clear page (confirm when artwork would be lost), restore natural colors (undoable), reset to blank, previous/next butterfly, save/download PNG and SVG, print current page. Export the artwork with a white background and no UI chrome; ensure mobile download fallback works.
- Natural-color restoration must use accurate per-region colors, not a generic repeating palette. Keep natural reference separate from user artwork.
- Save artwork automatically per species; show clear saved state. Allow resuming later. Keyboard-accessible region interactions and an alternative region selector when direct SVG navigation is difficult.
- Below the canvas: “Did you know?”, “Where to find it”, “How to recognize it”, habitat, geographic range, approximate wingspan, host plants, and seasonal activity where verified. Note regional/sex/season variation as appropriate. Link to credible references.
- Mark as spotted / undo. Optionally add observation date, approximate location text and personal notes; do not require GPS, upload photos, or share locations. A sighting is a user record, not verified identification.

### My Collection (`/collection`)
- A calm gallery of butterflies with original reference and user artwork thumbnails, coloring progress, and spotted status. Distinguish colored, completed (explicit user action), and spotted.
- Filters: All / In progress / Completed / Spotted. Show simple counts, not competitive gamification.
- Resume coloring, view and edit personal sightings, download artwork. Include a graceful empty state.
- Provide export/import of versioned local JSON backup, with validation and confirmation before replacing data. Clearly explain progress is stored on this device/browser and is not automatically synced.

### Print (`/print`)
- Download full Volume 01 PDF, print/download individual blank or colored species pages, and optionally select multiple species to assemble a custom print selection.
- Offer US Letter and A4 print layouts. Default to ink-friendly pure white, black line art, with a small natural-color reference (optional black-and-white/reference-off mode).
- Printable book: cover, brief instructions, one page per butterfly, observation journal, and sources/credits. Each species page has title, scientific name, large fillable-looking line drawing, small accurate reference, short fact, habitat, and page number. Ensure artwork is never clipped; no blank trailing pages or app chrome. Prefer one-sided printing guidance.
- Generate a real downloadable static PDF for the initial edition, using the same source artwork/data as the web app. Include it in the repository and expose via a working link. Use vector art in PDF where practical. Do not merely open a print dialog for the full book download.

## 3. Visual design system
A modern natural history field guide meets a premium minimalist coloring book. Use **pure white (#FFFFFF)** as the main background on all pages. Butterflies are the dominant color. No gradients, heavy shadows, dark backgrounds, loud UI colors, textured paper, decorative clutter or cartoonish branding. Avoid generic dashboard aesthetics.
- Typography: editorial serif for large headings (e.g. Instrument Serif or a similarly restrained serif), legible sans-serif for interface and body (e.g. Inter), optional small uppercase tracking for metadata. Self-host licensed fonts or use robust fallbacks.
- Ink #202020, secondary text #626262, subtle rules #E5E5E5; ensure contrast. Use color sparingly for actual palette swatches and butterfly art.
- Spacious margins, thin rules, 8–12px restrained radii, generous touch targets (44px minimum), and clean responsive layouts. Desktop maximum content width around 1200px; mobile padding 16–20px. Avoid fixed heights that clip at text zoom.
- Use clear text labels alongside icons, visible focus states, accessible dialogs, semantic headings, reduced-motion support, no information conveyed solely by color. Test at 320px width, 200% zoom and typical iPhone sizes.
- Make the coloring surface as large as possible. Avoid a tiny preview trapped inside a card. Reference and canvas should be easy to compare without compromising coloring space.

## 4. Volume 01 content and artwork
Launch with **six complete species**, not dozens of incomplete placeholders. Expand the catalog only after the initial set is excellent. The following are starting editorial directions, not a substitute for verifying facts and taxonomy:

| Common name | Scientific name | Visual identification | Fact direction | Habitat direction |
|---|---|---|---|---|
| Monarch | Danaus plexippus | Orange wings, black veins and white border spots | Some populations migrate thousands of miles; milkweed hosts caterpillars | North American meadows, gardens and milkweed patches |
| Blue Morpho | Morpho peleides | Brilliant blue upper wings, dark edges; brown underside with eyespots | Structural coloration creates its iridescence | Tropical forests of Central and South America |
| Eastern Tiger Swallowtail | Papilio glaucus | Yellow wings with black tiger stripes and hindwing tails; some females dark | Female color forms differ | Eastern North American woodlands and gardens |
| Common Buckeye | Junonia coenia | Brown wings, bold eyespots, orange markings | Eyespots may help deter predators | Sunny open fields and paths in North America |
| Zebra Longwing | Heliconius charithonia | Elongated black wings with pale yellow stripes | Communal nighttime roosting | Warm thickets in southern US and tropical Americas |
| Painted Lady | Vanessa cardui | Orange-brown, black and white markings, small hindwing eyespots | Broad distribution and migratory behavior | Open habitats across much of the world |

Verify all scientific names (including potential synonyms or taxonomic changes), facts, distribution and imagery using authoritative sources such as Smithsonian, university extension programs, Butterflies and Moths of North America, Natural History Museum, and relevant museum or conservation databases. Store source URL, title, attribution, access date, and license where appropriate. Do not fabricate links, facts, photo rights or species artwork. Do not present simplified art as definitive identification guidance. If a detail cannot be verified, omit it or explicitly label uncertainty.

### SVG artwork requirements — critical
- Create six distinct anatomically plausible butterfly silhouettes and patterns based on reputable visual references. Do not reuse one wing template with superficial color substitutions. No generic butterfly icon, emoji, random mandala or arbitrary pattern.
- Use original paths or properly licensed reusable assets with recorded provenance. Respect photo/art licenses; reference does not authorize tracing copyrighted artwork. Do not hotlink random images.
- Design clean, closed, non-overlapping regions with stable IDs, explicit left/right pairing, natural fill values, and enough detail to be satisfying while remaining easy to tap. Aim for roughly 20–60 meaningful regions per species as appropriate, not an arbitrary required count. Maintain black outlines on a separate non-interactive layer if needed. Include antennae and body. Use correct species-specific shape and markings; label dorsal/ventral view and sex/form where relevant.
- Render blank, natural-color and user-colored versions from the same geometry. Use a consistent SVG viewBox and generous export padding. Make every interactive region discoverable and fillable; no external SVG scripts or unsafe markup.
- Store artwork in structured, typed data or validated local SVG assets. Include a validation script for duplicate IDs, missing mirror pairs, missing natural fills, invalid colors, and missing metadata. Add a visual review checklist. If scientific accuracy cannot be confirmed, label artwork provisional and identify what requires review before commercial publication.

## 5. Recommended technical architecture
Use Next.js (App Router), TypeScript strict mode, React, and Tailwind CSS or equivalent maintainable styling. Choose compatible stable versions after inspecting existing dependencies; do not blindly replace an established stack. Use static data and client-side state for core functionality. Deploy as a static-friendly Vercel app where practical. No Supabase, authentication, paid APIs, AI image calls or unnecessary server infrastructure in MVP.

Suggested structure (adapt to repository conventions):
```
app/page.tsx
app/butterflies/[slug]/page.tsx
app/collection/page.tsx
app/print/page.tsx
components/ButterflyCanvas.tsx
components/ColorPalette.tsx
components/ColoringToolbar.tsx
components/SpeciesCard.tsx
components/SpeciesReference.tsx
components/SightingEditor.tsx
lib/species.ts
lib/coloring.ts
lib/storage.ts
lib/export.ts
content/species/
public/butterflies/
public/downloads/
scripts/generate-book.*
tests/
```

Data model (adapt as needed):
- `Species`: id, slug, commonName, scientificName, description, view, form, regions/geographicRange, habitat, identification, wingspan, hostPlants, season, facts, sources, artwork, palette.
- `WingRegion`: stable id, SVG geometry or path reference, mirrorId (optional for centerline), naturalFill, accessibleLabel.
- `ArtworkState`: speciesId, regionColors keyed by region ID, updatedAt, completed; separate undo/redo history per session.
- `Sighting`: id, speciesId, observedAt, optional locationText and notes.
- `LocalCollection`: schemaVersion, artworkBySpecies, sightings, settings.

Use localStorage or IndexedDB with guarded reads, versioned schema and migration handling. Handle malformed JSON, unavailable storage, quota errors and SSR hydration. Do not silently erase user progress. Keep history bounded and clear redo on new edits. Symmetry edits and bulk actions are single undoable transactions. Render state declaratively rather than mutating the DOM as primary state. Use static data and local assets to minimize network requirements. Optional service worker/PWA only if it can be tested properly; offline support beyond local persistence is not required for MVP.

For PNG export, serialize sanitized SVG with explicit dimensions, rasterize to a canvas at high resolution (e.g. 2000px wide), and create a downloadable Blob. Verify no cross-origin canvas taint. For printable PDF, use a reproducible generation script with embedded fonts/vector artwork where feasible, or a carefully tested browser PDF pipeline. Use dedicated print CSS with page breaks and margins. Keep build dependencies documented.

## 6. Quality, accessibility and verification
Implement unit tests for fill, symmetry, undo/redo, natural colors, completion, schema validation and persistence. Add Playwright end-to-end coverage for desktop and mobile:
1. Open home, select each species and confirm accurate distinct artwork and content.
2. Pick a color; tap region; verify only intended region(s) change; toggle symmetry and test again.
3. Undo/redo individual and bulk actions; clear and restore colors.
4. Switch species and reload; verify artwork and collection persist independently.
5. Record/edit/remove sighting; verify counts and notes persist.
6. Export PNG/SVG, confirm contents and dimensions, download and open the PDF; verify page count, margins and no clipped art.
7. Test backup export/import and invalid data handling.
8. Check keyboard navigation, focus, screen reader labels, reduced motion, contrast and mobile touch targets. Run automated accessibility checks where available.
9. Test narrow/mobile, tablet and desktop viewports, no overflow or inaccessible toolbar; test iOS Safari where tooling permits and disclose if not tested on an actual device.
10. Run lint, typecheck, tests and production build. Fix errors; do not claim checks passed unless executed. Verify no console errors, broken routes, missing assets or dead buttons.

## 7. Scope and future roadmap
MVP is free, public, six species, complete coloring/learning/collection/print experience. Do not add payment, social feeds, AI identification, native app wrappers, GPS maps, or cloud sync prematurely. Architect for later volumes (Backyard, Tropical, Rare & Unusual, North America), expanded species, optional accounts and cross-device sync, photo-assisted identification with uncertainty, mobile app/PWA, multilingual content and commercial printable editions. Treat nature identification and conservation/location privacy responsibly.

## 8. Definition of done
The application is ready when a first-time visitor can open a public link on an iPhone, select a butterfly, color its wings, compare it with its real appearance, read verified facts, save progress, mark it as spotted, and download or print the book without needing an account. Every initial species must have its own functional artwork and source-backed content. No fake controls, placeholder artwork represented as finished, mock downloads, or imaginary deployment links.

At completion provide: actual verified URL if deployed, local run instructions, repository/file summary, PDF path, test results, source/artwork review status, and unresolved issues. If deployment is blocked, give exact next commands (`npm install`, `npm run dev`, `npm run build`, `npx vercel --prod` as appropriate to the project) and disclose the blocker. Prioritize a shareable, polished experience for the mother who inspired the idea.
