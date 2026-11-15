import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
if '--force' not in sys.argv and list(Path('lib').glob('species-*.json')):
 raise SystemExit('Species JSON already exists. This one-time prototype import would overwrite edited artwork; use --force only if intentional.')
s=Path('The_Butterfly_Book.html').read_text()
data=json.loads(re.search(r'const data=(\[.*?\]);let i=',s).group(1))
urls=[
'https://www.butterfliesandmoths.org/species/Danaus-plexippus',
'https://ask.ifas.ufl.edu/publication/IN1101',
'https://www.butterfliesandmoths.org/species/Papilio-glaucus',
'https://www.butterfliesandmoths.org/species/Junonia-coenia',
'https://ask.ifas.ufl.edu/publication/in805',
'https://www.butterfliesandmoths.org/species/Vanessa-cardui']
extra=[
('North America','Meadows, roadsides and gardens with milkweed','8.6–12.4 cm','Milkweeds','Spring to fall in temperate North America','Orange wings with dark veins and black, white-spotted borders.','Some North American monarch populations migrate thousands of miles.'),
('Central and South America','Tropical forests and forest edges','about 12–20 cm','Various legumes','Year-round in tropical habitats','Brilliant blue upper wings with dark edges; brown, eyespotted undersides.','The brilliant blue comes from microscopic wing-scale structures rather than blue pigment.'),
('Eastern North America','Deciduous woods, forest edges and gardens','6.2–11.4 cm','Wild cherry, tulip tree and other broadleaf trees','Spring through fall; timing varies by latitude','Yellow wings with black tiger stripes and a tail on each hindwing. Some females are dark.','Females occur in yellow and dark forms.'),
('North America','Sunny open ground, fields and roadsides','4.2–7 cm','Plantains, snapdragons and related plants','Spring through fall; year-round in the far south','Brown upper wings with large eyespots and orange bars.','Its large eyespots may startle predators.'),
('Southern United States and tropical Americas','Woodland edges, shrubby thickets and gardens','7.2–10 cm','Passionflower vines','Year-round in much of Florida and the tropics','Long, narrow black wings crossed by pale yellow bands.','Adults may gather in small communal roosts at night.'),
('Nearly worldwide','Open fields, dunes, roadsides and gardens','5.1–7.3 cm','Thistles, mallows and many others','Seasonal migrants in temperate regions','Orange-brown upper wings, black tips with white spots, and small hindwing spots.','More than 100 caterpillar host plants have been recorded.')]
ns='{http://www.w3.org/2000/svg}'
for i,d in enumerate(data):
 root=ET.fromstring(d['blank'])
 regions=[]
 for gi,g in enumerate(root.findall(f'{ns}g')):
  side='left' if gi==0 else 'right' if gi==1 else 'center'
  for el in g.iter():
   old=el.attrib.get('data-region')
   if old is None: continue
   if el.attrib.get('data-natural')=='none':
    for key in ('data-region','data-natural'):el.attrib.pop(key,None)
    continue
   rid=f'{side}-{old}' if side!='center' else 'body'
   el.set('data-region',rid)
   natural=el.attrib.get('data-natural','#ffffff')
   label=('Body' if side=='center' else f'{side.title()} wing, area {int(old)+1}')
   el.set('role','button');el.set('tabindex','0');el.set('aria-label',label)
   regions.append({'id':rid,'mirrorId':(f'{"right" if side=="left" else "left"}-{old}' if side!='center' else None),'naturalFill':natural,'label':label})
 # ElementTree preserves the SVG namespace from the source.
 # ElementTree's namespace serialization is verbose but safe and valid.
 svg=ET.tostring(root,encoding='unicode').replace('ns0:','').replace(':ns0','')
 slug=d['name'].lower().replace(' ','-')
 region,habitat,wingspan,hosts,season,ident,fact=extra[i]
 out={'id':str(i+1).zfill(2),'slug':slug,'commonName':d['name'],'scientificName':d['latin'],'region':region,'habitat':habitat,'wingspan':wingspan,'hostPlants':hosts,'season':season,'identification':ident,'fact':fact,'view':'Simplified dorsal view','form':'Representative form; individual colors and markings vary','palette':d['palette'],'source':{'title':'Butterflies and Moths of North America' if i in (0,2,3,5) else 'University of Florida / IFAS Extension','url':urls[i],'accessed':'2026-11-15'},'svg':svg,'regions':regions}
 Path(f'lib/species-{slug}.json').write_text(json.dumps(out,ensure_ascii=False))
 print(slug,len(regions))
