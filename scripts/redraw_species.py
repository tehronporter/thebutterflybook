"""Build the three hand-authored specimen-inspired coloring plates.

The editable region IDs stay stable so previously saved colors continue to load.
Photo sources and licenses are recorded in the species JSON files.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'lib'
INK = '#242521'
DETAIL = '#4a4b45'
BOTANICAL = '#8d9389'


def plate():
    return ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260">']


def add(parts, regions, rid, label, natural, path=None, tag='path', attrs='', mirror=None, width=1.35):
    if path is not None:
        attrs = f'd="{path}" {attrs}'
    parts.append(f'<{tag} {attrs} fill="white" stroke="{INK}" stroke-width="{width}" stroke-linejoin="round" data-region="{rid}" data-natural="{natural}" role="button" tabindex="0" aria-label="{label}"/>')
    regions.append({'id':rid,'mirrorId':mirror,'naturalFill':natural,'label':label})


def detail(parts, markup, color=DETAIL, width=.7):
    parts.append(f'<g fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" pointer-events="none">{markup}</g>')


def save(slug, parts, regions, view=None, photo_alt=None):
    path = ROOT / f'species-{slug}.json'
    data = json.loads(path.read_text())
    parts.append('</svg>')
    data['svg'] = ''.join(parts)
    data['regions'] = regions
    if view:
        data['view'] = view
    if photo_alt:
        data['photo']['alt'] = photo_alt
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(slug, len(regions), 'regions', len(data['svg']), 'SVG chars')


def eighty_eight():
    p = plate(); r = []
    # A sparse fern and two lanceolate leaves frame the insect without crossing it.
    detail(p, '<path d="M12 243 Q32 213 58 192 M21 232 Q13 222 10 211 M30 222 Q42 204 50 197 M37 215 Q52 214 66 219 M262 241 Q272 219 289 197 M273 222 Q261 208 251 204"/><path d="M19 228 Q8 226 10 211 Q22 213 19 228 M34 213 Q40 198 52 196 Q52 210 34 213 M41 217 Q54 209 67 219 Q53 227 41 217 M273 219 Q265 209 252 205 Q255 223 273 219 M281 209 Q282 198 291 197 Q295 207 281 209"/>', BOTANICAL, .68)
    # The narrow, pointed forewing sits behind the rounded numbered hindwing.
    add(p,r,'top-black','Dark forewing',' #242521'.strip(),'M72 145 Q83 104 119 67 C146 34 180 23 218 27 Q235 42 237 75 Q232 109 220 143 Q154 127 72 145 Z')
    add(p,r,'white-top','Pale stripes at the forewing tip','#f4f2e9','M171 35 Q198 20 217 29 Q229 42 232 59 Q213 44 197 46 Q187 55 181 68 Q180 47 171 35 Z')
    add(p,r,'red-band','Crimson forewing flash','#dc2736','M103 119 Q125 77 159 58 Q181 55 207 72 Q194 83 178 111 Q144 103 103 119 Z')
    add(p,r,'wing-base','Pale numbered hindwing','#faf8ed','M72 137 C89 104 126 99 153 103 Q207 100 236 124 C256 143 262 178 247 207 Q235 229 208 230 C168 231 115 205 84 169 Q70 154 72 137 Z')
    add(p,r,'center-band','Curved black band above the numerals','#262724','M83 131 Q113 106 157 109 Q207 108 235 132 Q219 133 201 146 Q176 130 144 127 Q109 128 86 148 Z')
    # The photo's markings are unequal, crooked 8-like loops, not concentric circles.
    add(p,r,'digit-0-outer','Upper irregular 8 outline','#252623','M128 135 C139 119 164 118 177 131 Q187 142 177 154 C188 166 178 185 160 190 Q138 192 129 177 Q120 161 132 153 Q120 146 128 135 Z')
    add(p,r,'digit-0-middle','Upper pale 8 interior','#faf8ed','M138 136 Q149 125 165 132 Q174 140 164 151 Q178 162 169 175 Q157 185 143 176 Q136 169 145 158 Q131 149 138 136 Z')
    add(p,r,'digit-0-inner','Upper small dark eye','#242521','M145 138 Q154 133 159 139 Q161 145 153 149 Q143 150 145 138 Z')
    add(p,r,'digit-0-core','Upper lower eye','#242521','M151 161 Q160 155 166 161 Q169 168 162 171 Q153 173 151 161 Z')
    add(p,r,'digit-1-outer','Lower irregular 8 outline','#252623','M187 148 Q202 139 216 148 Q226 155 222 167 Q239 175 232 197 Q224 215 204 216 Q187 215 185 198 Q182 183 193 175 Q181 163 187 148 Z')
    add(p,r,'digit-1-middle','Lower pale 8 interior','#faf8ed','M194 153 Q207 145 215 154 Q221 163 210 173 Q229 178 223 196 Q218 208 203 207 Q193 204 194 192 Q195 181 205 176 Q191 166 194 153 Z')
    add(p,r,'digit-1-inner','Lower upper dark eye','#242521','M199 155 Q207 150 212 155 Q215 162 207 167 Q198 169 199 155 Z')
    add(p,r,'digit-1-core','Lower bottom dark eye','#242521','M202 186 Q211 180 218 187 Q221 196 213 199 Q202 202 202 186 Z')
    add(p,r,'outer-rim','Irregular outer hindwing border','#262724','M85 164 Q118 206 167 224 Q211 240 237 215 Q224 222 203 222 Q165 221 131 198 Q108 185 85 164 Z')
    # Head and slender abdomen point left, as in the source photograph.
    add(p,r,'body','Striped thorax and abdomen','#6b6d62','M72 137 Q87 141 100 155 Q104 163 99 172 Q85 168 75 157 Q67 148 72 137 Z')
    add(p,r,'head','Butterfly head','#343631',tag='ellipse',attrs='cx="68" cy="138" rx="8" ry="8"')
    detail(p, '<path d="M63 133 Q38 102 25 91 M67 132 Q51 104 47 88 M68 145 Q48 165 39 186 M78 157 Q68 176 66 192 M88 160 Q77 177 76 193 M98 166 Q89 183 92 198"/><circle cx="25" cy="91" r="1.6"/><circle cx="47" cy="88" r="1.6"/><path d="M99 128 Q125 117 145 120 M100 135 Q122 129 141 136 M97 151 Q112 172 129 180 M112 177 Q134 195 159 205 M170 111 Q211 116 236 140 M236 144 Q250 167 244 191 M92 164 Q113 196 154 214"/>', DETAIL, .8)
    # A second-weight line gives the white hindwing its distinctive scalloped rim.
    detail(p, '<path d="M76 139 C89 115 122 105 152 107 Q206 106 235 128 C254 149 256 181 244 202"/><path d="M107 141 Q118 136 129 137 M111 150 Q124 151 132 159 M125 189 Q146 206 172 211"/>', '#33342e', .5)
    save('eighty-eight',p,r,'ventral side view','Eighty-eight butterfly photographed from below on a hand in Zamora, Ecuador, showing a red forewing and irregular 88-like hindwing markings')


def glasswing():
    p = plate(); r = []
    # The flowering stems and rays echo the white blossoms in the reference image.
    detail(p,'<path d="M258 247 Q260 193 253 146 M277 249 Q272 210 281 157 M252 207 Q239 195 230 192 M260 224 Q274 211 290 210"/><path d="M254 211 Q242 195 230 192 Q230 210 254 211 M263 224 Q277 209 291 210 Q286 226 263 224"/>',BOTANICAL,.7)
    for cx,cy in [(253,138),(283,153)]:
        for dx,dy in [(-11,-13),(-3,-18),(5,-17),(13,-11),(15,-2),(9,6),(-5,5),(-14,-3)]:
            detail(p,f'<path d="M{cx} {cy} Q{cx+dx*.75:.1f} {cy+dy*.7:.1f} {cx+dx} {cy+dy} Q{cx+dx*.25:.1f} {cy+dy*.4:.1f} {cx} {cy} Z"/>',BOTANICAL,.55)
        detail(p,f'<circle cx="{cx}" cy="{cy}" r="4"/>',BOTANICAL,.6)
    # Side view: long rounded forewing, shorter hindwing and a trailing abdomen.
    add(p,r,'left-fore','Brown outer forewing rim','#684231','M205 119 Q183 94 158 75 C124 47 84 22 54 22 Q24 25 21 52 C18 76 38 101 77 114 Q135 126 205 119 Z')
    add(p,r,'left-fore-window','Large transparent forewing cell','#dfe8dd','M191 111 Q149 78 111 61 Q71 43 45 50 Q36 69 58 90 Q104 110 191 111 Z')
    add(p,r,'left-fore-tip','Upper pale forewing mark','#f4f3ed','M47 37 Q58 29 76 34 Q89 39 104 50 Q85 48 66 57 Q52 54 47 37 Z')
    add(p,r,'right-fore','Rust brown apical band','#875136','M23 51 Q24 30 53 24 Q81 20 105 39 Q70 36 47 49 Q37 62 35 74 Q25 66 23 51 Z')
    add(p,r,'right-fore-tip','Broad ivory band at wing tip','#f3f2e9','M34 73 Q45 55 66 54 Q88 48 111 61 Q96 68 85 83 Q58 82 34 73 Z')
    add(p,r,'right-fore-window','Narrow transparent upper cell','#dce8db','M113 47 Q137 56 156 73 Q177 89 197 110 Q149 90 112 62 Z')
    add(p,r,'left-hind','Warm brown hindwing border','#704833','M203 119 Q165 112 119 112 Q91 113 87 139 C83 168 109 198 146 206 Q181 209 203 179 Q216 151 203 119 Z')
    add(p,r,'left-hind-window','Broad transparent hindwing panel','#dfe8dd','M196 130 Q163 121 125 122 Q105 125 102 143 Q101 170 136 190 Q167 198 190 171 Q203 151 196 130 Z')
    add(p,r,'left-hind-spot','Pale upper hindwing cell','#e8ede5','M124 124 Q146 117 166 125 Q152 137 136 143 Q118 144 108 140 Q112 129 124 124 Z')
    add(p,r,'right-hind','Dark hindwing cross vein','#684231','M127 147 Q164 143 198 133 Q202 136 203 141 Q166 151 132 155 Z')
    add(p,r,'right-hind-window','Lower transparent hindwing cell','#dfe8dd','M110 157 Q139 157 161 151 Q180 149 198 146 Q197 168 174 187 Q153 198 128 182 Q114 172 110 157 Z')
    add(p,r,'right-hind-spot','Small clear cell by hindwing edge','#e8ede5','M100 145 Q110 137 122 141 Q116 152 106 156 Q101 153 100 145 Z')
    add(p,r,'body','Slender thorax and long abdomen','#68554b','M201 116 Q210 110 218 122 Q220 146 209 176 Q207 200 207 230 Q202 235 199 229 Q193 186 199 149 Q191 130 201 116 Z')
    add(p,r,'head','Clearwing head','#403731',tag='ellipse',attrs='cx="209" cy="113" rx="7" ry="7"')
    detail(p,'<path d="M213 109 Q239 85 266 89 M214 114 Q238 102 260 104 M209 137 Q228 157 237 176 M205 143 Q211 173 207 202 M203 148 Q188 169 181 181 M203 161 Q230 178 242 186"/><circle cx="210" cy="112" r="1.3"/>',DETAIL,.8)
    # True cell boundaries follow the radiating veins visible in the reference.
    detail(p,'<path d="M199 116 Q153 99 84 45 M199 116 Q156 110 48 87 M198 116 Q160 80 115 44 M199 116 Q143 107 68 70 M193 129 Q152 129 108 143 M193 130 Q152 151 130 185 M193 132 Q185 162 173 189 M193 132 Q122 129 102 154"/><path d="M35 45 Q52 28 71 31 M24 57 Q33 78 58 89 M105 124 Q95 139 99 157 M113 179 Q134 195 155 200"/>', '#565047', .68)
    # Sparse little scale marks suggest texture without producing tiny regions.
    detail(p,'<path d="M43 39 l3 -2 M48 35 l3 -2 M53 32 l3 -1 M62 29 l3 0 M83 35 l3 2 M91 40 l3 2 M99 44 l3 3 M108 48 l3 3"/>','#6f5649',.55)
    save('glasswing',p,r,'side view','Andromica glasswing photographed from the side on white flowers in Mindo, Ecuador; transparent panels, ivory bands, and brown borders are visible')


def morpho():
    p = plate(); r = []
    detail(p,'<path d="M11 232 Q25 210 41 200 M20 221 Q11 212 9 202 M28 214 Q39 203 51 203 M282 230 Q273 212 257 200 M275 216 Q286 206 293 199"/><path d="M18 216 Q8 211 9 202 Q22 205 18 216 M30 212 Q39 200 51 203 Q46 214 30 212 M279 213 Q286 202 293 199 Q294 212 279 213"/>',BOTANICAL,.65)
    for side in ('left','right'):
        mirror = 'right' if side == 'left' else 'left'
        transform = 'translate(300 0) scale(-1 1)' if side == 'right' else ''
        p.append(f'<g transform="{transform}">')
        add(p,r,f'{side}-0',f'{side.title()} blue forewing','#1689dd','M147 108 Q120 87 88 68 Q53 47 28 49 C13 52 13 67 17 84 Q22 111 48 131 Q86 154 147 139 Z',mirror=f'{mirror}-0')
        add(p,r,f'{side}-1',f'{side.title()} blue hindwing','#1689dd','M146 137 Q105 126 69 133 Q43 147 40 175 Q36 198 54 215 Q70 232 98 232 Q126 232 147 201 Z',mirror=f'{mirror}-1')
        add(p,r,f'{side}-2',f'{side.title()} dark forewing margin','#17243c','M29 49 Q57 45 94 69 Q125 91 147 110 Q126 103 111 95 Q73 67 39 63 Q28 67 31 81 Q33 98 50 115 Q34 105 23 88 Q11 67 18 55 Q21 50 29 49 Z',mirror=f'{mirror}-2')
        add(p,r,f'{side}-3',f'{side.title()} scalloped hindwing margin','#17243c','M41 172 Q34 185 42 203 Q46 215 57 222 Q67 232 78 230 Q88 238 99 233 Q115 239 126 226 Q140 214 147 197 Q124 221 101 223 Q74 223 57 205 Q45 191 41 172 Z',mirror=f'{mirror}-3')
        add(p,r,f'{side}-4',f'{side.title()} luminous blue basal wing','#75c9f2','M143 111 Q110 90 79 76 Q105 87 130 119 Q112 137 78 145 Q117 145 145 135 Z',mirror=f'{mirror}-4')
        spot_positions=[(25,63,3.0),(26,78,2.8),(32,94,2.7),(43,109,2.5),(52,208,2.8),(68,220,2.7)]
        for i,(cx,cy,rad) in enumerate(spot_positions,1):
            label=f'{side.title()} {"forewing" if i<=4 else "hindwing"} border spot {i}'
            add(p,r,f'{side}-border-spot-{i}',label,'#f7f1df',tag='circle',attrs=f'cx="{cx}" cy="{cy}" r="{rad}"',mirror=f'{mirror}-border-spot-{i}',width=.65)
        # Radiating veins and restrained scale hatching stay inside the wing contour.
        detail(p,'<path d="M145 121 Q105 93 34 60 M145 122 Q104 104 29 79 M145 123 Q103 119 45 113 M144 124 Q108 131 63 136 M143 143 Q97 143 55 159 M143 146 Q105 161 51 183 M143 151 Q118 182 73 214 M144 153 Q125 192 105 221"/><path d="M50 70 Q65 77 71 84 M57 81 Q73 87 79 94 M47 96 Q59 103 66 109 M71 145 Q80 149 85 154 M57 172 Q69 174 76 181 M65 200 Q78 197 85 204"/>','#4c5353',.65)
        p.append('</g>')
    add(p,r,'body','Segmented butterfly body','#17243c',tag='ellipse',attrs='cx="150" cy="153" rx="6" ry="45"')
    detail(p,'<path d="M147 111 Q139 91 133 84 M153 111 Q161 91 167 84 M145 135 Q155 138 155 139 M145 148 Q155 151 155 152 M145 161 Q155 164 155 165 M145 174 Q155 177 155 178 M147 187 Q153 190 153 191"/><circle cx="133" cy="84" r="1.8"/><circle cx="167" cy="84" r="1.8"/>',DETAIL,.78)
    save('blue-morpho',p,r,'dorsal view','Blue morpho photographed with wings spread in Ecuador, showing luminous blue wing fields, dark scalloped margins, and pale edge spots')


if __name__ == '__main__':
    eighty_eight(); glasswing(); morpho()
