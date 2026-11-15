"""Generate the ten-page, US Letter Butterfly Book from the app's species data."""
import io
import json
import re
from pathlib import Path

import pymupdf
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ['monarch', 'blue-morpho', 'eastern-tiger-swallowtail', 'common-buckeye', 'zebra-longwing', 'painted-lady']
SPECIES = [json.loads((ROOT / f'lib/species-{slug}.json').read_text()) for slug in SLUGS]
OUT = ROOT / 'public/downloads/the-butterfly-book-volume-01.pdf'
INK = (.13, .15, .13)
MUTED = (.37, .4, .36)
RULE = (.81, .83, .79)


def write(page, at, value, size=11, font='helv', color=INK):
    page.insert_text(at, value, fontsize=size, fontname=font, color=color)


def line(page, y):
    page.draw_line((45, y), (567, y), color=RULE, width=.65)


def artwork(page, species, rect):
    svg = species['svg']
    svg = re.sub(r'fill="#[0-9A-Fa-f]{6}"([^>]*?)data-region=', r'fill="#FFFFFF"\1data-region=', svg)
    source = pymupdf.open(stream=svg.encode(), filetype='svg')
    pdf = pymupdf.open('pdf', source.convert_to_pdf())
    page.show_pdf_page(rect, pdf, 0, keep_proportion=True)


def photo(page, species, rect):
    with Image.open(ROOT / 'public' / species['photo']['src'].lstrip('/')) as img:
        img = ImageOps.exif_transpose(img).convert('RGB')
        target = (int(rect.width * 3), int(rect.height * 3))
        img = ImageOps.fit(img, target, method=Image.Resampling.LANCZOS)
        data = io.BytesIO()
        img.save(data, 'JPEG', quality=86, optimize=True)
    page.insert_image(rect, stream=data.getvalue(), keep_proportion=False)


def footer(page, number):
    line(page, 752)
    write(page, (45, 768), 'THE BUTTERFLY BOOK  /  VOLUME 01', 7, color=MUTED)
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


book = pymupdf.open()
cover = book.new_page(width=612, height=792)
write(cover, (45, 56), 'A COLORING FIELD GUIDE  /  VOL. 01', 9, color=MUTED)
write(cover, (45, 128), 'The Butterfly', 50, font='tiro')
write(cover, (45, 181), 'Book', 54, font='tiro')
photo(cover, SPECIES[0], pymupdf.Rect(45, 215, 567, 571))
write(cover, (45, 593), 'MONARCH  /  DANAUS PLEXIPPUS', 8, color=MUTED)
write(cover, (45, 638), 'Color. Discover. Explore.', 20, font='tiro')
write(cover, (45, 661), 'Six remarkable butterflies. A quieter way to look closer.', 10)
footer(cover, 1)

intro = book.new_page(width=612, height=792)
write(intro, (45, 62), 'FIELD NOTES  /  HOW TO USE THIS BOOK', 9, color=MUTED)
write(intro, (45, 126), 'An invitation to look closer.', 30, font='tiro')
line(intro, 151)
for i, sentence in enumerate([
    'Choose a butterfly and color its wings however you wish.',
    'The small photograph offers a view of the real species.',
    'The large black and white drawing is yours to imagine.',
    'Look for the field marks and facts beside each page.',
    'Take the book outside and note butterflies you notice.',
    'Print one-sided on US Letter paper for the most room to color.',
]):
    write(intro, (45, 205 + i * 46), sentence, 12)
write(intro, (45, 577), 'A note on the illustrations', 17, font='tiro')
write(intro, (45, 609), 'The coloring pages are original, simplified dorsal views. The photos', 10)
write(intro, (45, 627), 'show living butterflies; their angle, sex, and individual markings may', 10)
write(intro, (45, 645), 'differ. Use a regional field guide for reliable identification.', 10)
footer(intro, 2)

for i, species in enumerate(SPECIES):
    page = book.new_page(width=612, height=792)
    write(page, (45, 51), f'SPECIES {i + 1:02}  /  06', 8, color=MUTED)
    write(page, (45, 97), species['commonName'], 30, font='tiro')
    write(page, (45, 119), species['scientificName'], 11, font='tiit', color=MUTED)
    line(page, 136)
    artwork(page, species, pymupdf.Rect(38, 146, 574, 560))
    line(page, 566)
    photo(page, species, pymupdf.Rect(45, 577, 163, 669))
    write(page, (177, 589), 'PHOTOGRAPHIC REFERENCE', 7, color=MUTED)
    for j, sentence in enumerate(wrap(species['fact'], 57)[:3]):
        write(page, (177, 610 + j * 14), sentence, 9)
    write(page, (177, 664), f"{species['region']}  /  {species['wingspan']}", 8, color=MUTED)
    write(page, (45, 691), f"Photo: {species['photo']['credit']}  /  {species['photo']['license']}", 7, color=MUTED)
    write(page, (45, 719), 'Date spotted: ___________________    Place: ______________________________', 9, color=MUTED)
    footer(page, i + 3)

journal = book.new_page(width=612, height=792)
write(journal, (45, 57), 'FIELD JOURNAL', 9, color=MUTED)
write(journal, (45, 112), 'What did you notice?', 31, font='tiro')
write(journal, (45, 139), 'A quiet space for your own observations.', 11, color=MUTED)
for i in range(4):
    y = 180 + i * 137
    line(journal, y)
    write(journal, (45, y + 24), 'Date  ____________________    Butterfly  ______________________________', 9)
    write(journal, (45, y + 55), 'Place  ___________________________________________________________', 9)
    write(journal, (45, y + 86), 'Notes  ___________________________________________________________', 9)
    write(journal, (45, y + 113), '          ___________________________________________________________', 9)
footer(journal, 9)

credits = book.new_page(width=612, height=792)
write(credits, (45, 55), 'SOURCES & CREDITS', 9, color=MUTED)
write(credits, (45, 105), 'A little more to explore.', 30, font='tiro')
line(credits, 127)
for i, species in enumerate(SPECIES):
    y = 155 + i * 89
    write(credits, (45, y), species['commonName'], 13, font='tiro')
    write(credits, (45, y + 20), 'Species: ' + species['source']['title'], 9)
    credits.insert_link({'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, y + 9, 567, y + 25), 'uri': species['source']['url']})
    write(credits, (45, y + 37), f"Photo: {species['photo']['credit']}  /  {species['photo']['license']}", 9)
    write(credits, (45, y + 53), 'View photograph and license on Wikimedia Commons', 8, color=MUTED)
    credits.insert_link({'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, y + 43, 567, y + 58), 'uri': species['photo']['sourceUrl']})
write(credits, (45, 707), 'Original coloring artwork adapted from the supplied prototype.', 9)
write(credits, (45, 723), 'Photo licenses and research sources checked 15 November 2026.', 9)
footer(credits, 10)

OUT.parent.mkdir(parents=True, exist_ok=True)
book.save(OUT, garbage=4, deflate=True)
print(f'{OUT}: {len(book)} pages, {OUT.stat().st_size} bytes')
