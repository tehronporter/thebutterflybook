import type {Metadata} from 'next';
import './globals.css';import Nav from '@/components/Nav';import {CollectionProvider} from '@/components/CollectionProvider';
export const metadata:Metadata={title:'The Butterfly Book — Color. Discover. Explore.',description:'A gentle, interactive butterfly coloring field guide. Color six real species, discover their stories, and print your own book.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><CollectionProvider><Nav/>{children}</CollectionProvider></body></html>}
