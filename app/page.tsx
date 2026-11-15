'use client';
import {useState} from 'react';
import Link from 'next/link';
import Image from 'next/image';
import Artwork from '@/components/Artwork';
import {species} from '@/lib/species';

export default function Home(){
 const [query,setQuery]=useState('');
 const [region,setRegion]=useState('All regions');
 const found=species.filter(s=>`${s.commonName} ${s.scientificName}`.toLowerCase().includes(query.toLowerCase())&&(region==='All regions'||s.region.includes(region)));
 const monarch=species[0];
 return <main>
  <section className="hero wrap">
   <div className="hero-copy">
    <p className="eyebrow">The Butterfly Book · Volume 01</p>
    <h1>A field guide for color &amp; curiosity.</h1>
    <p className="tagline">Color. Discover. Explore.</p>
    <p className="lead">Slow down with six remarkable butterflies. Color their intricate wings, compare them with real photographs, and take a little more wonder into the world.</p>
    <div className="hero-actions"><Link prefetch={false} className="button primary" href="/butterflies/monarch">Begin coloring <span aria-hidden="true">↗</span></Link><a className="text-link" href="#explore">Meet the butterflies ↓</a></div>
   </div>
   <figure className="hero-figure"><div className="hero-photo"><Image src={monarch.photo.src} alt={monarch.photo.alt} fill priority sizes="(max-width: 700px) 100vw, 52vw"/></div><figcaption><span>01 / Monarch · <i>Danaus plexippus</i></span><a href={monarch.photo.sourceUrl} target="_blank" rel="noopener noreferrer">Photo: {monarch.photo.credit} · {monarch.photo.license}</a></figcaption></figure>
  </section>
  <section className="wrap explore-section" id="explore">
   <div className="section-heading"><div><p className="eyebrow">Volume 01 · Six species</p><h2>Look closer.</h2></div><p>Each butterfly has a story, a photograph, and a detailed page for you to color.</p></div>
   <div className="filters"><label className="search-label">Search butterflies<input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Name or scientific name" type="search"/></label><label className="search-label">Region<select value={region} onChange={e=>setRegion(e.target.value)}><option>All regions</option><option>North America</option><option>Central and South America</option><option>Southern United States</option><option>Nearly worldwide</option></select></label></div>
   <div className="species-grid">{found.map(s=><Link prefetch={false} className="species-card" href={`/butterflies/${s.slug}`} key={s.slug}><div className="card-photo"><Image src={s.photo.src} alt={s.photo.alt} fill sizes="(max-width: 700px) 50vw, 33vw"/></div><div className="card-meta"><span>{s.id} / 06 · {s.region}</span><span aria-hidden="true">↗</span></div><h3>{s.commonName}</h3><p><i>{s.scientificName}</i></p><small>Photo: {s.photo.credit} · {s.photo.license}</small></Link>)}</div>
   {!found.length&&<p className="empty">No butterflies match that search. Try another name or region.</p>}
  </section>
  <section className="wrap how"><div><span className="step">01 / COLOR</span><h3>Settle in.</h3><p>Choose a shade and fill each wing section. Your work is saved on this device.</p></div><div><span className="step">02 / DISCOVER</span><h3>Look again.</h3><p>Compare your page with a real photograph and learn the field marks that make each species distinct.</p></div><div><span className="step">03 / EXPLORE</span><h3>Take note.</h3><p>Keep a private record of the butterflies you may have seen outside.</p></div></section>
  <section className="wrap book-cta"><div><p className="eyebrow">The printable edition</p><h2>Take the quiet with you.</h2><p>Six detailed black-and-white coloring pages, real photo references, an observation journal, and credited sources.</p><Link prefetch={false} className="button outline" href="/print">See the printable book ↗</Link></div><div className="book-art"><Artwork species={species[3]}/></div></section>
  <footer className="wrap footer">The Butterfly Book · Volume 01 <span><Link prefetch={false} href="/credits">Photographs &amp; sources</Link> · Made for curious eyes and colorful hands.</span></footer>
 </main>
}
