'use client';
import {Fragment,useState} from 'react';
import Image from 'next/image';
import Link from 'next/link';
import Artwork from '@/components/Artwork';
import {useCollection} from '@/components/CollectionProvider';
import {species} from '@/lib/species';

export default function PrintPage(){
 const {data}=useCollection();
 const [selected,setSelected]=useState<string[]>(species.map(s=>s.slug));
 const [paper,setPaper]=useState<'letter'|'a4'>('letter');
 const [fieldGuide,setFieldGuide]=useState(true);
 const [colored,setColored]=useState(false);
 const toggle=(slug:string)=>setSelected(v=>v.includes(slug)?v.filter(x=>x!==slug):[...v,slug]);
 const printSelected=()=>{let style=document.getElementById('selected-paper-size') as HTMLStyleElement|null;if(!style){style=document.createElement('style');style.id='selected-paper-size';document.head.append(style);}style.textContent=`@media print { @page { size: ${paper==='a4'?'A4':'letter'}; margin: 0; } }`;window.print();};
 return <main className="wrap interior print-page">
  <p className="eyebrow">Stillness in Flight · The printable edition</p>
  <div className="page-intro"><div><h1>Make room to color.</h1><p>Three Ecuador butterflies in a quiet book you can print or open in a tablet coloring app.</p></div></div>
  <div className="print-hero"><div><p className="eyebrow">The complete sampler</p><h2>Three butterflies. Three moments to pause.</h2><p>A full-color photographic cover, three two-page field guide and coloring spreads, a matching black-and-white back cover, and credited sources.</p><a className="button primary" href="/downloads/the-butterfly-book-volume-01.pdf" download>Download Ecuador sampler PDF ↓</a><small>US Letter · 10 pages · vector coloring art</small></div><div className="print-preview"><div className="print-preview-photo"><Image src={species[2].photo.src} alt={species[2].photo.alt} fill sizes="(max-width: 700px) 100vw, 40vw"/></div><span>Stillness in Flight · Butterflies of Ecuador</span></div></div>
  <section className="print-options"><div className="section-heading"><div><p className="eyebrow">Your own selection</p><h2>Print the pages you want.</h2></div><p>Choose paper, the photographic field guide, and your saved colors.</p></div><div className="option-row"><label>Paper size<select value={paper} onChange={e=>setPaper(e.target.value as 'letter'|'a4')}><option value="letter">US Letter</option><option value="a4">A4</option></select></label><label className="check-row"><input type="checkbox" checked={fieldGuide} onChange={e=>setFieldGuide(e.target.checked)}/>Include field guide pages</label><label className="check-row"><input type="checkbox" checked={colored} onChange={e=>setColored(e.target.checked)}/>Print my colors</label></div><div className="print-select">{species.map(s=><label key={s.slug} className="print-select-card"><input type="checkbox" checked={selected.includes(s.slug)} onChange={()=>toggle(s.slug)}/><span className="print-choice-photo"><Image src={s.photo.src} alt={s.photo.alt} fill sizes="100px"/></span><span>{s.commonName}</span></label>)}</div><button className="button outline" disabled={!selected.length} onClick={printSelected}>Print {selected.length} selected {selected.length===1?'spread':'spreads'} ↗</button>{!selected.length&&<p className="hint">Choose at least one butterfly to print.</p>}</section>
  <p className="print-credits-link">Photographers, licenses, and research links appear in the book and on <Link prefetch={false} href="/credits">Sources &amp; credits ↗</Link>.</p>
  <div className={`print-sheets ${paper}`}>{species.filter(s=>selected.includes(s.slug)).map((s,i)=><Fragment key={s.slug}>{fieldGuide&&<article className="print-sheet field-guide-sheet"><header><span>Stillness in Flight · Ecuador</span><span>{String(i+1).padStart(2,'0')} / field guide</span></header><h2>{s.commonName}</h2><p><i>{s.scientificName}</i></p><div className="field-guide-photo"><Image src={s.photo.src} alt={s.photo.alt} fill sizes="100vw" unoptimized/></div><small>Photographed in {s.photo.location||'Ecuador'} · {s.photo.credit} · {s.photo.license}</small><p className="field-guide-elevation">Elevation: {s.elevation}</p><h3>Three things to notice</h3><ol>{s.fieldNotes.map(note=><li key={note}>{note}</li>)}</ol><p className="field-guide-prompt">{s.reflection}</p><div className="journal-lines">____________________________________________________________<br/>____________________________________________________________</div><footer>Look closely. Color slowly. Notice more.</footer></article>}<article className="print-sheet art-guide-sheet"><header><span>Stillness in Flight · Ecuador</span><span>{String(i+1).padStart(2,'0')} / coloring canvas</span></header><h2>{s.commonName}</h2><p><i>{s.scientificName}</i></p><Artwork species={s} colors={colored?(data.artworkBySpecies[s.slug]?.colors||{}):{}}/><footer>Date: ____________________  My notes: ____________________________</footer></article></Fragment>)}</div>
 </main>
}
