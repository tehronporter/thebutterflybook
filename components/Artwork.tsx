'use client';
import {useMemo} from 'react';
import type {Species} from '@/lib/species';
import {renderSvg,type Colors} from '@/lib/coloring';
export default function Artwork({species,colors={},onRegion,className='',label}: {species:Species;colors?:Colors;onRegion?:(id:string)=>void;className?:string;label?:string}){
 const svg=useMemo(()=>{const markup=renderSvg(species,colors);return onRegion?markup:markup.replace(/ role="button" tabindex="0" aria-label="[^"]*"/g,'');},[species,colors,onRegion]);
 const find=(target:EventTarget|null)=>{const el=(target as Element)?.closest?.('[data-region]');return el?.getAttribute('data-region');};
 return <div className={`artwork ${className}`} role={onRegion?'group':'img'} aria-label={label||`${species.commonName} butterfly, ${species.view}`} onClick={onRegion?e=>{const id=find(e.target);if(id)onRegion(id);}:undefined} onKeyDown={onRegion?e=>{if(e.key==='Enter'||e.key===' '){const id=find(e.target);if(id){e.preventDefault();onRegion(id);}}}:undefined} dangerouslySetInnerHTML={{__html:svg}}/>;
}
