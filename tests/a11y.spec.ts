import {test,expect} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
test.use({browserName:'webkit'});
const base=process.env.BASE_URL||'http://localhost:3000';
for(const width of [390,1280])test(`WCAG checks at ${width}px`,async({page})=>{await page.setViewportSize({width,height:800});for(const path of ['/','/butterflies/eighty-eight','/collection','/print']){await page.goto(base+path);const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();expect(result.violations.map(v=>`${v.id}: ${v.nodes.length}`),`${width}px ${path}`).toEqual([]);}});
