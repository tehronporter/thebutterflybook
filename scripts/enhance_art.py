"""Add original fine wing engraving to the six hand-authored fill regions.

The engraved strokes are non-interactive and clipped to each butterfly's wing
silhouette. Fillable region IDs remain unchanged, so saved coloring persists.
"""
from pathlib import Path
import json,xml.etree.ElementTree as ET
NS='http://www.w3.org/2000/svg'; Q=lambda tag:f'{{{NS}}}{tag}'
base=[
 'M145 119 Q105 68 25 35',
 'M144 123 Q98 87 20 67',
 'M144 127 Q100 112 28 103',
 'M141 132 Q104 129 51 132',
 'M144 144 Q95 144 43 157',
 'M143 149 Q94 168 48 188',
 'M142 152 Q107 196 79 218',
 'M145 158 Q130 204 110 221',
 'M82 65 Q78 76 76 88',
 'M101 81 Q97 93 94 104',
 'M117 101 Q113 110 110 122',
 'M62 172 Q72 178 78 188',
 'M80 191 Q89 193 95 204',
]
extra={
 'monarch':[
  'M28 58 Q56 61 83 76','M33 85 Q72 96 111 117',
  'M58 146 Q89 151 113 147','M72 173 Q102 165 127 151',
  'M38 47 l-6 13 M48 51 l-5 13 M60 57 l-4 13 M73 64 l-4 13',
  'M54 197 Q70 204 87 211','M84 215 Q101 212 116 200',
  'M43 164 Q49 180 63 190','M45 190 Q64 205 76 208',
  'M115 136 Q90 122 66 119',
 ],
 'blue-morpho':[
  'M35 46 Q59 49 81 62','M40 74 Q72 81 99 98',
  'M33 105 Q69 111 99 123','M51 142 Q75 139 96 141',
  'M45 163 Q57 181 78 192','M60 204 Q86 211 105 201',
  'M89 212 Q115 202 128 181','M94 83 Q106 92 115 105',
  'M61 118 Q90 123 113 132','M70 151 Q100 155 124 148',
  'M67 179 Q86 172 104 162',
 ],
 'eastern-tiger-swallowtail':[
  'M30 43 Q48 42 65 53','M33 78 Q52 87 68 102',
  'M49 115 Q76 120 101 127','M58 148 Q81 147 106 148',
  'M50 165 Q64 182 84 192','M72 205 Q90 211 106 205',
  'M90 217 Q89 234 84 247','M106 220 Q119 199 130 172',
  'M45 149 Q33 172 46 189','M48 198 Q65 215 80 216',
  'M120 105 Q111 112 105 122',
 ],
 'common-buckeye':[
  'M31 43 Q53 50 70 62','M39 72 Q59 84 73 98',
  'M51 105 Q78 110 105 121','M56 134 Q79 133 100 138',
  'M44 153 Q48 173 57 188','M60 194 Q77 209 92 213',
  'M90 219 Q114 214 132 183','M110 162 Q121 169 128 180',
  'M25 64 Q30 82 38 96','M74 143 Q91 150 108 150',
  'M52 185 Q62 182 70 177',
 ],
 'zebra-longwing':[
  'M19 38 Q33 44 46 49','M27 73 Q49 86 75 94',
  'M38 110 Q65 123 97 131','M53 141 Q76 146 103 148',
  'M48 161 Q64 174 83 181','M63 191 Q81 189 99 181',
  'M84 199 Q113 187 135 161','M76 73 Q95 86 114 103',
  'M65 103 Q91 114 112 124','M71 151 Q91 154 114 149',
  'M101 135 Q121 137 139 137',
 ],
 'painted-lady':[
  'M25 41 Q43 48 57 60','M30 73 Q53 89 72 98',
  'M45 116 Q72 124 97 131','M52 139 Q83 140 110 140',
  'M47 155 Q53 177 68 190','M68 202 Q90 215 108 213',
  'M89 219 Q112 211 133 182','M109 92 Q104 107 112 121',
  'M60 178 Q79 174 97 163','M53 197 Q65 207 78 210',
  'M122 153 Q130 162 137 176',
 ],
}
for slug,additional in extra.items():
 p=Path('lib')/f'species-{slug}.json';s=json.loads(p.read_text());root=ET.fromstring(s['svg'])
 # Regeneration is safe: remove previous engraved layers and clipping paths.
 for el in list(root):
  if el.attrib.get('data-butterfly-detail')=='true':root.remove(el)
 defs=ET.Element(Q('defs'),{'data-butterfly-detail':'true'});clip=ET.SubElement(defs,Q('clipPath'),{'id':f'{slug}-wing-clip'})
 for wing in list(root[0])[:2]:ET.SubElement(clip,Q('path'),{'d':wing.attrib['d']})
 root.insert(0,defs)
 for g in [el for el in root if el.tag==Q('g')][:2]:
  for el in list(g):
   if el.attrib.get('class')=='wing-engraving':g.remove(el)
  detail=ET.Element(Q('g'),{'class':'wing-engraving','clip-path':f'url(#{slug}-wing-clip)','fill':'none','stroke':'#252525','stroke-width':'.65','stroke-linecap':'round','stroke-linejoin':'round','pointer-events':'none','opacity':'.9'})
  if slug=='zebra-longwing':
   strokes=[
    'M145 119 Q100 81 25 39','M145 126 Q98 102 40 88',
    'M144 132 Q100 125 65 118','M142 146 Q99 140 60 145',
    'M143 152 Q94 164 58 170','M140 157 Q105 178 79 190',
    'M19 38 Q33 44 46 49','M76 73 Q95 86 114 103',
    'M65 103 Q91 114 112 124','M71 151 Q91 154 114 149',
    'M101 135 Q121 137 139 137',
   ]
  else:strokes=base+additional
  for d in strokes:ET.SubElement(detail,Q('path'),{'d':d})
  if slug!='zebra-longwing':
   hatch=ET.SubElement(detail,Q('g'),{'stroke-width':'.45','opacity':'.52'})
   for j in range(7):
    x=38+j*13
    ET.SubElement(hatch,Q('path'),{'d':f'M{x} {77+j*5} l5 8 M{x+5} {157+j*4} l5 7'})
  g.insert(2,detail)
 s['svg']=ET.tostring(root,encoding='unicode').replace('ns0:','').replace(':ns0','')
 p.write_text(json.dumps(s,ensure_ascii=False))
 print(slug,len(base+additional)+14,'fine strokes per wing')
