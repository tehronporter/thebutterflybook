"""Reproducible nine-page US Letter PDF from app species data and vector SVG art."""
import json,re
from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
files=['monarch','blue-morpho','eastern-tiger-swallowtail','common-buckeye','zebra-longwing','painted-lady']
species=[json.loads((ROOT/f'lib/species-{slug}.json').read_text()) for slug in files]
OUT=ROOT/'public/downloads/the-butterfly-book-volume-01.pdf'
INK=(.125,.125,.125); MUTED=(.38,.38,.38); RULE=(.84,.84,.84)
def text(page,at,value,size=11,font='helv',color=INK):page.insert_text(at,value,fontsize=size,fontname=font,color=color)
def rule(page,y):page.draw_line((45,y),(567,y),color=RULE,width=.6)
def art(page,s,rect,natural=False):
 svg=s['svg']
 if natural:
  svg=re.sub(r'<(path|ellipse|circle)([^>]*?)fill="[^"]*"([^>]*?)data-region="([^"]+)"',lambda m:f'<{m.group(1)}{m.group(2)}fill="{next(r["naturalFill"] for r in s["regions"] if r["id"]==m.group(4))}"{m.group(3)}data-region="{m.group(4)}"',svg)
 doc=pymupdf.open(stream=svg.encode(),filetype='svg');pdf=pymupdf.open('pdf',doc.convert_to_pdf());page.show_pdf_page(rect,pdf,0,keep_proportion=True)
def footer(p,n):rule(p,752);text(p,(45,768),'THE BUTTERFLY BOOK  /  VOLUME 01',7,color=MUTED);text(p,(552,768),f'{n:02}',7,color=MUTED)
book=pymupdf.open()
p=book.new_page(width=612,height=792);text(p,(45,65),'A COLORING FIELD GUIDE  /  VOL. 01',9,color=MUTED);text(p,(45,143),'The Butterfly',51,font='tiro');text(p,(45,198),'Book',55,font='tiro')
for i,s in enumerate(species):art(p,s,pymupdf.Rect(45+(i%3)*177,267+(i//3)*149,207+(i%3)*177,398+(i//3)*149),True)
text(p,(45,636),'Color. Discover. Explore.',20,font='tiro');text(p,(45,660),'Six extraordinary butterflies from around the world.',10);footer(p,1)
p=book.new_page(width=612,height=792);text(p,(45,62),'FIELD NOTES  /  HOW TO USE THIS BOOK',9,color=MUTED);text(p,(45,126),'A small invitation to look closer.',30,font='tiro');rule(p,151)
lines=['Choose a butterfly. Color its wings however you wish.','The small illustration shows a simplified view of its natural colors.','The large drawing is yours to imagine. No colors are wrong.','Take the book outside and keep a note of butterflies you notice.','A sighting is a personal memory, not a verified identification.','Print one-sided on US Letter paper for the most room to color.']
for i,line in enumerate(lines):text(p,(45,205+i*45),line,12)
text(p,(45,585),'A note about the artwork',17,font='tiro');text(p,(45,615),'These are original, simplified dorsal-view illustrations based on the',10);text(p,(45,633),'field marks described by the sources on the final page. Real butterflies',10);text(p,(45,651),'vary by sex, place, season, and individual.',10);footer(p,2)
for i,s in enumerate(species):
 p=book.new_page(width=612,height=792);text(p,(45,51),f'SPECIES {i+1:02}  /  06',8,color=MUTED);text(p,(45,97),s['commonName'],30,font='tiro');text(p,(45,119),s['scientificName'],11,font='tiit',color=MUTED);rule(p,136)
 art(p,s,pymupdf.Rect(38,148,574,566));rule(p,571);art(p,s,pymupdf.Rect(45,579,155,677),True)
 text(p,(174,596),'NATURAL COLOR REFERENCE',7,color=MUTED)
 # Fit a compact verified fact within two lines.
 fact=s['fact']; words=fact.split();lines=[''];
 for w in words:
  candidate=(lines[-1]+' '+w).strip()
  if len(candidate)>58:lines.append(w)
  else:lines[-1]=candidate
 for j,line in enumerate(lines[:2]):text(p,(174,617+j*15),line,10)
 text(p,(174,664),s['region']+'  /  '+s['wingspan'],8,color=MUTED);text(p,(45,706),'Date spotted: ___________________    Place: ______________________________',9,color=MUTED);footer(p,i+3)
p=book.new_page(width=612,height=792);text(p,(45,57),'FIELD JOURNAL',9,color=MUTED);text(p,(45,112),'What did you notice?',31,font='tiro');text(p,(45,139),'A quiet space for your own observations.',11,color=MUTED)
for i in range(4):
 y=180+i*137;rule(p,y);text(p,(45,y+24),'Date  ____________________    Butterfly  ______________________________',9);text(p,(45,y+55),'Place  ___________________________________________________________',9);text(p,(45,y+86),'Notes  ___________________________________________________________',9);text(p,(45,y+113),'          ___________________________________________________________',9)
footer(p,9)
p=book.new_page(width=612,height=792);text(p,(45,55),'SOURCES & CREDITS',9,color=MUTED);text(p,(45,105),'A little more to explore.',30,font='tiro');rule(p,127)
for i,s in enumerate(species):
 y=161+i*79;text(p,(45,y),s['commonName'],13,font='tiro');text(p,(45,y+21),s['source']['title'],9);url=s['source']['url'];text(p,(45,y+38),url,8,color=MUTED);p.insert_link({'kind':pymupdf.LINK_URI,'from':pymupdf.Rect(45,y+24,567,y+44),'uri':url})
text(p,(45,662),'Original vector artwork adapted and redrawn from the supplied prototype.',9);text(p,(45,679),'Illustrations are simplified references, not definitive field identification.',9);text(p,(45,696),'Source pages checked 15 November 2026. Individual forms can vary.',9);footer(p,10)
# 10 pages: cover, instructions, six species, journal, sources.
OUT.parent.mkdir(parents=True,exist_ok=True);book.save(OUT,garbage=4,deflate=True);print(f'{OUT}: {len(book)} pages, {OUT.stat().st_size} bytes')
