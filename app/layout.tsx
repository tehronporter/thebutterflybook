import type {Metadata} from 'next';
import './globals.css';import Nav from '@/components/Nav';import {CollectionProvider} from '@/components/CollectionProvider';
export const metadata:Metadata={title:'Stillness in Flight — The Butterfly Book',description:'An Ecuador butterfly field guide with real photography, biological notes, mindful reflections, detailed coloring canvases, and a printable book.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><CollectionProvider><Nav/>{children}</CollectionProvider></body></html>}
