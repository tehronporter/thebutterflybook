'use client';
import {useEffect,useState} from 'react';
import Link from 'next/link';
import Image from 'next/image';
import Artwork from '@/components/Artwork';
import {species} from '@/lib/species';

export default function Home(){
 const [ready,setReady]=useState(false);
 useEffect(()=>setReady(true),[]);
 const [query,setQuery]=useState('');
 const found=species.filter(s=>`${s.commonName} ${s.scientificName}`.toLowerCase().includes(query.toLowerCase()));
 const hero=species[2];
 return <main>
  <section className="hero wrap">
   <div className="hero-copy">
    <p className="eyebrow">The Butterfly Book · Ecuador sampler</p>
    <h1>Stillness in flight.</h1>
    <p className="tagline">Butterflies of Ecuador</p>
    <p className="lead">A quiet field guide and coloring space inspired by three extraordinary butterflies. Study real photographs, notice the details, then make each wing your own.</p>
    <div className="hero-actions"><Link prefetch={false} className="button primary" href="/butterflies/eighty-eight">Begin coloring <span aria-hidden="true">↗</span></Link><a className="text-link" href="#explore">Meet the butterflies ↓</a></div>
   </div>
   <figure className="hero-figure"><div className="hero-photo"><Image src={hero.photo.src} alt={hero.photo.alt} fill priority sizes="(max-width: 700px) 100vw, 52vw"/></div><figcaption><span>Blue Morpho · <i>{hero.scientificName}</i> · Ecuador</span><a href={hero.photo.sourceUrl} target="_blank" rel="noopener noreferrer">Photo: {hero.photo.credit} · {hero.photo.license}</a></figcaption></figure>
  </section>
  <section className="wrap explore-section" id="explore">
   <div className="section-heading"><div><p className="eyebrow">Three butterflies · one country</p><h2>Look closer.</h2></div><p>Each chapter pairs an Ecuador photograph with field notes and an original coloring canvas.</p></div>
   <div className="filters"><label className="search-label">Find a butterfly<input disabled={!ready} value={query} onChange={e=>setQuery(e.target.value)} placeholder="Name or scientific name" type="search"/></label></div>
   <div className="species-grid">{found.map(s=><Link prefetch={false} className="species-card" href={`/butterflies/${s.slug}`} key={s.slug}><div className="card-photo"><Image src={s.photo.src} alt={s.photo.alt} fill sizes="(max-width: 700px) 50vw, 33vw"/></div><div className="card-meta"><span>{s.id} / 03 · {s.region}</span><span aria-hidden="true">↗</span></div><h3>{s.commonName}</h3><p><i>{s.scientificName}</i></p><small>Photo: {s.photo.credit} · {s.photo.license}</small></Link>)}</div>
   {!found.length&&<p className="empty">No butterflies match that search. Try another name.</p>}
  </section>
  <section className="wrap how"><div><span className="step">01 / OBSERVE</span><h3>See the real thing.</h3><p>Start with photographs made in Ecuador. Notice shape, color, and the setting around each butterfly.</p></div><div><span className="step">02 / COLOR</span><h3>Settle in.</h3><p>Fill detailed wings in your own palette. Your work saves on this device.</p></div><div><span className="step">03 / REFLECT</span><h3>Stay curious.</h3><p>Read three biological notes and leave a line or two of your own observations.</p></div></section>
  <section className="wrap book-cta"><div><p className="eyebrow">The printable edition</p><h2>A small book for a slower afternoon.</h2><p>Three two-page spreads: a photographic field guide on the left and a botanical coloring canvas on the right. Print at home or use the PDF in an iPad coloring app.</p><Link prefetch={false} className="button outline" href="/print">Explore the printable book ↗</Link></div><div className="book-art"><Artwork species={species[1]}/></div></section>
  <footer className="wrap footer">Stillness in Flight · The Butterfly Book <span><Link prefetch={false} href="/credits">Photographs &amp; sources</Link> · Ecuador sampler</span></footer>
 </main>
}
