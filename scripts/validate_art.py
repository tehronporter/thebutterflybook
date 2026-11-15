import json,re,glob,xml.etree.ElementTree as ET
assert len(glob.glob('lib/species-*.json'))==6
for file in glob.glob('lib/species-*.json'):
 s=json.load(open(file));root=ET.fromstring(s['svg']);regions=s['regions'];ids=[r['id'] for r in regions];assert len(ids)==len(set(ids)),file
 assert len(regions)>=10,file
 assert all(re.fullmatch('#[0-9A-Fa-f]{6}',r['naturalFill']) for r in regions),file
 assert all(not r['mirrorId'] or r['mirrorId'] in ids for r in regions),file
 assert all(next((v['mirrorId'] for v in regions if v['id']==r['mirrorId']),None)==r['id'] for r in regions if r['mirrorId']),file
 assert {e.attrib['data-region'] for e in root.iter() if 'data-region' in e.attrib}==set(ids),file
 assert s['scientificName'] and s['source']['url'].startswith('https://'),file
 print(s['commonName'],len(regions),'regions OK')
