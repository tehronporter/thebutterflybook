'use client';
import {createContext,useContext,useEffect,useState, type ReactNode} from 'react';
import {emptyCollection,readCollection,saveCollection,type Collection} from '@/lib/storage';
type Value={data:Collection;ready:boolean;error:string;update:(fn:(old:Collection)=>Collection)=>void;replace:(data:Collection)=>void};
const Context=createContext<Value|null>(null);
export function CollectionProvider({children}:{children:ReactNode}){const [data,setData]=useState<Collection>(emptyCollection);const [ready,setReady]=useState(false);const [error,setError]=useState('');useEffect(()=>{const result=readCollection();setData(result.data);setError(result.error);setReady(true);},[]);const replace=(next:Collection)=>{setData(next);if(!saveCollection(next))setError('Could not save on this device. Check available browser storage.');else setError('');};const update=(fn:(old:Collection)=>Collection)=>{if(error)return;replace(fn(data));};return <Context.Provider value={{data,ready,error,update,replace}}>{error&&<div className="storage-alert" role="alert">{error}</div>}{children}</Context.Provider>}
export function useCollection(){const v=useContext(Context);if(!v)throw Error('CollectionProvider missing');return v;}
