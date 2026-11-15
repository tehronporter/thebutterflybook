import {notFound} from 'next/navigation';import {species,speciesBySlug} from '@/lib/species';import Studio from '@/components/Studio';
export function generateStaticParams(){return species.map(s=>({slug:s.slug}));}
export default async function Page({params}:{params:Promise<{slug:string}>}){const {slug}=await params;const item=speciesBySlug(slug);if(!item)notFound();return <Studio species={item}/>;}
