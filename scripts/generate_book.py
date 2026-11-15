"""Generate the ten-page Ecuador sampler PDF from species data and vector art."""
import io
import json
from pathlib import Path

import pymupdf
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ['eighty-eight', 'glasswing', 'blue-morpho']
SPECIES = [json.loads((ROOT / f'lib/species-{slug}.json').read_text()) for slug in SLUGS]
OUT = ROOT / 'public/downloads/the-butterfly-book-volume-01.pdf'
INK = (.14, .16, .14)
MUTED = (.37, .4, .36)
RULE = (.81, .83, .79)


def write(page, at, value, size=11, font='helv', color=INK):
    page.insert_text(at, value.replace('–', '-').replace('—', '-').encode('latin-1', 'replace').decode('latin-1'), fontsize=size, fontname=font, color=color)


def line(page, y):
    page.draw_line((45, y), (567, y), color=RULE, width=.65)


def artwork(page, species, rect):
    source = pymupdf.open(stream=species['svg'].encode(), filetype='svg')
    pdf = pymupdf.open('pdf', source.convert_to_pdf())
    page.show_pdf_page(rect, pdf, 0, keep_proportion=True)


def photo(page, species, rect):
    with Image.open(ROOT / 'public' / species['photo']['src'].lstrip('/')) as img:
        img = ImageOps.exif_transpose(img).convert('RGB')
        img = ImageOps.fit(img, (int(rect.width * 3), int(rect.height * 3)), method=Image.Resampling.LANCZOS)
        data = io.BytesIO()
        img.save(data, 'JPEG', quality=88, optimize=True)
    page.insert_image(rect, stream=data.getvalue(), keep_proportion=False)


def footer(page, number):
    line(page, 752)
    write(page, (45, 768), 'STILLNESS IN FLIGHT  /  BUTTERFLIES OF ECUADOR', 7, color=MUTED)
    write(page, (552, 768), f'{number:02}', 7, color=MUTED)


def wrap(value, limit):
    result = ['']
    for word in value.split():
        candidate = (result[-1] + ' ' + word).strip()
        if len(candidate) > limit:
            result.append(word)
        else:
            result[-1] = candidate
    return result


def leaves(page):
    for x, y, sign in [(42, 602, 1), (563, 222, -1), (46, 271, 1), (554, 636, -1)]:
        shape = page.new_shape()
        shape.draw_line((x, y), (x + sign * 35, y - 48))
        for dy in (12, 26, 39):
            bx = x + sign * dy * .72
            by = y - dy * 1.1
            shape.draw_bezier((bx, by), (bx + sign * 19, by - 7), (bx + sign * 23, by - 24), (bx + sign * 2, by - 15))
        shape.finish(color=(.69, .71, .66), width=.5)
        shape.commit()


book = pymupdf.open()
cover = book.new_page(width=612, height=792)
write(cover, (45, 55), 'THE BUTTERFLY BOOK  /  ECUADOR SAMPLER', 9, color=MUTED)
write(cover, (45, 117), 'Stillness in Flight', 44, font='tiro')
write(cover, (45, 150), 'Butterflies of Ecuador', 17, font='tiro')
photo(cover, SPECIES[2], pymupdf.Rect(45, 184, 567, 606))
write(cover, (45, 625), 'BLUE MORPHO  /  MORPHO HELENOR  /  ECUADOR', 8, color=MUTED)
write(cover, (45, 667), 'Photography, field notes, and coloring for a quieter afternoon.', 10)
footer(cover, 1)

intro = book.new_page(width=612, height=792)
write(intro, (45, 59), 'A SMALL INVITATION', 9, color=MUTED)
write(intro, (45, 111), 'Begin with wonder.', 32, font='tiro')
line(intro, 137)
for i, sentence in enumerate([
    'Three butterflies, each photographed in Ecuador.',
    'On each left page, study the real butterfly and its field notes.',
    'On the facing page, color an original black and white drawing.',
    'Choose natural colors, or follow your own curiosity.',
    'Pause for a prompt. Write a thought, memory, or observation.',
    'Print one-sided or use the PDF in a tablet coloring app.',
]):
    write(intro, (45, 194 + i * 54), sentence, 12)
write(intro, (45, 582), 'Looking closely', 17, font='tiro')
for i, sentence in enumerate([
    'The 88 pattern is shown from below. The clearwing and morpho',
    'drawings interpret the upper wings. Photographs may show a',
    'different angle or form. These pages invite observation; they',
    'are not a substitute for a regional identification guide.',
]):
    write(intro, (45, 609 + i * 17), sentence, 10)
footer(intro, 2)

for i, species in enumerate(SPECIES):
    left = book.new_page(width=612, height=792)
    write(left, (45, 54), f'FIELD GUIDE  /  {i+1:02} OF 03', 9, color=MUTED)
    write(left, (45, 99), species['commonName'], 30, font='tiro')
    write(left, (45, 120), species['scientificName'], 11, font='tiit', color=MUTED)
    photo(left, species, pymupdf.Rect(45, 148, 567, 424))
    write(left, (45, 441), f"PHOTOGRAPHED IN {species['photo']['location'].upper()}", 8, color=MUTED)
    write(left, (45, 457), f"Photo: {species['photo']['credit']} / {species['photo']['license']}", 8, color=MUTED)
    write(left, (45, 484), f"Elevation: {species['elevation']}", 9)
    line(left, 499)
    write(left, (45, 523), 'THREE THINGS TO NOTICE', 8, color=MUTED)
    y = 546
    for j, note in enumerate(species['fieldNotes']):
        for k, sentence in enumerate(wrap(f'{j+1:02}  {note}', 82)):
            write(left, (45, y + k * 14), sentence, 10)
        y += 37
    line(left, 664)
    write(left, (45, 685), species['reflection'], 11, font='tiro')
    write(left, (45, 710), '____________________________________________________________________________', 8, color=MUTED)
    write(left, (45, 728), '____________________________________________________________________________', 8, color=MUTED)
    footer(left, len(book))

    right = book.new_page(width=612, height=792)
    write(right, (45, 54), f'THE COLORING CANVAS  /  {i+1:02} OF 03', 9, color=MUTED)
    write(right, (45, 103), species['commonName'], 29, font='tiro')
    write(right, (45, 124), species['scientificName'], 11, font='tiit', color=MUTED)
    line(right, 139)
    leaves(right)
    artwork(right, species, pymupdf.Rect(38, 174, 574, 653))
    write(right, (45, 706), 'Date: ___________________   My colors / notes: _____________________________', 9, color=MUTED)
    footer(right, len(book))

back = book.new_page(width=612, height=792)
write(back, (45, 55), 'THE BUTTERFLY BOOK  /  BACK COVER', 9, color=MUTED)
write(back, (45, 116), 'A second look.', 39, font='tiro')
write(back, (45, 145), 'The Blue Morpho, now waiting for your colors.', 12)
leaves(back)
artwork(back, SPECIES[2], pymupdf.Rect(43, 205, 569, 619))
write(back, (45, 669), 'Stillness in Flight  /  Butterflies of Ecuador', 16, font='tiro')
footer(back, len(book))

credits = book.new_page(width=612, height=792)
write(credits, (45, 55), 'PHOTOGRAPHY & RESEARCH', 9, color=MUTED)
write(credits, (45, 105), 'Sources & credits.', 30, font='tiro')
line(credits, 128)
for i, species in enumerate(SPECIES):
    y = 168 + i * 145
    write(credits, (45, y), species['commonName'], 15, font='tiro')
    write(credits, (45, y + 25), f"Photo: {species['photo']['credit']} / {species['photo']['license']}", 9)
    write(credits, (45, y + 42), 'Photograph and license on Wikimedia Commons', 9, color=MUTED)
    credits.insert_link({'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, y + 30, 567, y + 48), 'uri': species['photo']['sourceUrl']})
    write(credits, (45, y + 62), 'Biology: ' + species['source']['title'], 9)
    credits.insert_link({'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, y + 49, 567, y + 68), 'uri': species['source']['url']})
    if species.get('additionalSource'):
        write(credits, (45, y + 79), 'Additional research: ' + species['additionalSource']['title'], 8)
        credits.insert_link({'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, y + 68, 567, y + 84), 'uri': species['additionalSource']['url']})
    write(credits, (45, y + 98), 'Photograph resized and cropped for this book and website.', 8, color=MUTED)
    line(credits, y + 117)
write(credits, (45, 656), 'Illustrations are original simplified coloring art, not diagnostic plates.', 9)
write(credits, (45, 676), 'Elevation notes reflect the cited records; exact photo elevation may be unknown.', 9)
write(credits, (45, 696), 'Photo licenses and research reviewed 15 November 2026.', 9)
footer(credits, len(book))

OUT.parent.mkdir(parents=True, exist_ok=True)
book.save(OUT, garbage=4, deflate=True)
print(f'{OUT}: {len(book)} pages, {OUT.stat().st_size} bytes')
