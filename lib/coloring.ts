import type {Species} from './species';
export type Colors = Record<string,string>;
export const isColor = (value:string) => /^#[0-9a-fA-F]{6}$/.test(value);
export function paint(species:Species, colors:Colors, id:string, color:string, symmetry:boolean):Colors {
 if(!isColor(color)) return colors;
 const region=species.regions.find(r=>r.id===id); if(!region)return colors;
 return {...colors,[id]:color,...(symmetry&&region.mirrorId?{[region.mirrorId]:color}:{})};
}
export function naturalColors(species:Species):Colors {return Object.fromEntries(species.regions.map(r=>[r.id,r.naturalFill]));}
export function renderSvg(species:Species,colors:Colors):string {
 return species.svg.replace(/<(path|circle|ellipse)([^>]*?)data-region="([^"]+)"([^>]*?)\/>/g,(all,tag,before,id,after)=>{
  const fill=colors[id];return fill&&isColor(fill)?`<${tag}${before.replace(/fill="[^"]*"/,`fill="${fill}"`)}data-region="${id}"${after}/>`:all;
 });
}
export function exportSvg(species:Species,colors:Colors):string {
 return renderSvg(species,colors).replace('<svg ','<svg width="2000" height="1733" ').replace(/<svg([^>]*)>/,'<svg$1><rect width="300" height="260" fill="#ffffff"/>');
}
export function downloadBlob(blob:Blob,name:string){const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);}
export function downloadSvg(species:Species,colors:Colors){downloadBlob(new Blob([exportSvg(species,colors)],{type:'image/svg+xml'}),`${species.slug}.svg`);}
export async function downloadPng(species:Species,colors:Colors){const svg=exportSvg(species,colors);const url=URL.createObjectURL(new Blob([svg],{type:'image/svg+xml'}));try{const img=new Image();img.src=url;await img.decode();const canvas=document.createElement('canvas');canvas.width=2000;canvas.height=1733;const ctx=canvas.getContext('2d');if(!ctx)throw Error('Canvas unavailable');ctx.fillStyle='#ffffff';ctx.fillRect(0,0,2000,1733);ctx.drawImage(img,0,0,2000,1733);const blob=await new Promise<Blob>((resolve,reject)=>canvas.toBlob(b=>b?resolve(b):reject(Error('PNG failed')),'image/png'));downloadBlob(blob,`${species.slug}.png`);}finally{URL.revokeObjectURL(url);}}
