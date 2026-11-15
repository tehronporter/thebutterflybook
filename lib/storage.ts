import {speciesForStorage} from './species';
import {isColor,type Colors} from './coloring';
export type Artwork={colors:Colors;updatedAt:string;completed:boolean};
export type Sighting={id:string;speciesId:string;observedAt:string;locationText:string;notes:string};
export type Collection={schemaVersion:1;artworkBySpecies:Record<string,Artwork>;sightings:Sighting[]};
export const emptyCollection=():Collection=>({schemaVersion:1,artworkBySpecies:{},sightings:[]});
const key='butterfly-book-v1';
export function validateCollection(value:unknown):value is Collection {
 if(!value||typeof value!=='object')return false;const x=value as Partial<Collection>;
 if(x.schemaVersion!==1||!x.artworkBySpecies||typeof x.artworkBySpecies!=='object'||!Array.isArray(x.sightings))return false;
 for(const [slug,a] of Object.entries(x.artworkBySpecies)){const s=speciesForStorage.find(v=>v.slug===slug);if(!s||!a||typeof a!=='object'||typeof a.completed!=='boolean'||typeof a.updatedAt!=='string'||!a.colors||typeof a.colors!=='object')return false;for(const [id,c] of Object.entries(a.colors))if(!s.regions.some(r=>r.id===id)||!isColor(c))return false;}
 return x.sightings.every(v=>v&&typeof v.id==='string'&&speciesForStorage.some(s=>s.slug===v.speciesId)&&typeof v.observedAt==='string'&&typeof v.locationText==='string'&&typeof v.notes==='string');
}
export function loadCollection():Collection {return readCollection().data;}
export function readCollection():{data:Collection;error:string} {try{const raw=localStorage.getItem(key);if(!raw)return {data:emptyCollection(),error:''};const parsed:unknown=JSON.parse(raw);return validateCollection(parsed)?{data:parsed,error:''}:{data:emptyCollection(),error:'Stored progress could not be read. Import a valid backup before making changes; your existing data has been preserved.'};}catch{return {data:emptyCollection(),error:'Browser storage is unavailable or contains unreadable progress. Your existing data has been preserved.'};}}
export function saveCollection(data:Collection):boolean {try{localStorage.setItem(key,JSON.stringify(data));window.dispatchEvent(new Event('butterfly-storage'));return true;}catch{return false;}}
