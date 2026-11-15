import type {Metadata} from 'next';
import './globals.css';import Nav from '@/components/Nav';import {CollectionProvider} from '@/components/CollectionProvider';
export const metadata:Metadata={title:'The Butterfly Book — Color. Discover. Explore.',description:'An interactive coloring field guide with real butterfly photography, detailed black-and-white line art, fascinating facts, and a printable book.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><CollectionProvider><Nav/>{children}</CollectionProvider></body></html>}
