from wkit import *
o=wbase(6,'The Bilingual Advantage, Carefully','The bilingual advantage,','carefully',
'For years, headlines said that speaking two languages sharpens the mind’s control systems. Then researchers checked which studies got published. The story of the bilingual advantage is a lesson in how evidence can mislead.')
o['hero_aria'],o['hero_js']=hero(['pfc','tem'],{'pfc':([40,-60],'left'),'tem':([300,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, linked to executive control, and the temporal lobe, linked to language, glowing orange and labelled.')
screen='''            <svg id="pbSvg" viewBox="0 0 520 260" width="100%" style="max-width:540px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="pbD">
              <desc id="pbD">A chart of study results. Each dot is one small study comparing bilinguals with monolinguals. Dots to the right of the centre line favour bilinguals; dots to the left favour monolinguals. A vertical marker shows the average.</desc>
              <g id="pbG" font-family="Source Sans 3, sans-serif"></g>
            </svg>
            <p class="prog" id="pbP" aria-live="polite">&nbsp;</p>'''
student=lab(screen,'Ready','Run the studies, then publish','You will simulate 40 small studies of a bilingual advantage, in a world where there is no advantage at all. Then you will decide which ones get published.')
o.update(body=tabs('Run the studies, then publish','Simulate 40 small studies where the true effect is zero. Then see what readers would conclude if only the striking ones were published.',student,
 'About 10 minutes',
 ['Project the student version. Run the 40 studies and point out that the average sits near zero.',
  'Ask the class which studies they think would get published. Then publish only the striking ones.',
  'Ask: if you read only the published studies, what would you conclude?',
  'Connect to how students evaluate evidence: one study, or many? Published only, or all?'],
 ['Why did some studies show an advantage when the true effect was zero?',
  'What does the published literature look like if only striking results get out?',
  'How would you check for this when you read research?'],
 'Use this as a lesson in evaluating evidence, whatever the subject: single studies vary by chance, and what gets published can be a biased sample. Look for meta-analyses that check for publication bias, and for preregistered studies.',
 'The simulation is random, so each run differs. This is about how evidence can mislead, not a claim that bilingualism has no value: speaking two languages has obvious personal, social and professional benefits.')+'''
  <div class="col lede">
    <p>The idea was appealing: constantly managing two languages might train the brain’s executive functions, such as inhibiting distractions and switching between tasks. Many studies reported such an advantage. Others found none.</p>
    <p>In 2018, Minna Lehtonen and colleagues pooled 891 effect sizes from 152 studies of adults. Before correcting for publication bias, they found a very small bilingual advantage for inhibition, shifting and working memory. After correcting for it, no evidence for a bilingual advantage remained.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>152</strong><span>studies of adults, with 891 effect sizes, in the 2018 meta-analysis</span></div>
      <div role="listitem"><strong>None</strong><span>bilingual advantage remained after correcting for publication bias</span></div>
      <div role="listitem"><strong>104</strong><span>conference abstracts tracked to see which got published</span></div>
      <div role="listitem"><strong>~2×</strong><span>as likely to be published if they found a benefit</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Publication bias</span>Following studies from talk to journal</h2>
    <p>Angela de Bruin, Barbara Treccani and Sergio Della Sala looked at 104 conference abstracts on bilingualism and executive control from 1999 to 2012, and checked which studies were later published. Studies fully supporting a bilingual advantage were the most likely to be published, followed by those with mixed results; studies challenging it were least likely. The difference was not explained by sample size, tests used or statistical power.</p>
    <h2 class="sec"><span class="n">The details</span>A small disadvantage, too</h2>
    <p>Lehtonen and colleagues also found a disadvantage for verbal fluency, possibly reflecting less exposure to each language for people who use two. And their analyses of possible explanations did not support the theory behind the advantage.</p>
    <h2 class="sec"><span class="n">The lesson</span>How a literature can mislead</h2>
    <p>No one needs to cheat for this to happen. Small studies vary by chance; striking results are more exciting to write up and publish; and a reader who sees only the published studies sees a biased sample. The activity above shows how far that can shift the picture.</p>
    <h2 class="sec"><span class="n">For learning</span>Value bilingualism for the right reasons</h2>
    <p>Speaking more than one language opens communities, literatures and careers. Bilingual students don’t need a hidden brain-training benefit to justify supporting their languages. And this case is a good one for teaching students to read research critically.</p>
  </div>

'''+pgrid_html(),
tips_h='One study can mislead. So can only the published ones.',
tips='''      <li><b>Look for the whole body of evidence</b><span>Meta-analyses that check for publication bias.</span></li>
      <li><b>Prefer preregistered studies</b><span>Their results get reported whichever way they come out.</span></li>
      <li><b>Teach it</b><span>This case makes publication bias concrete for students.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/bul0000142">Lehtonen, M., Soveri, A., Laine, A., Järvenpää, J., de Bruin, A., &amp; Antfolk, J. (2018). Is bilingualism associated with enhanced executive functioning in adults? A meta-analytic review. <i>Psychological Bulletin, 144</i>(4), 394–425.</a></li>
        <li><a href="https://doi.org/10.1177/0956797614557866">de Bruin, A., Treccani, B., &amp; Della Sala, S. (2015). Cognitive advantage in bilingualism: An example of publication bias? <i>Psychological Science, 26</i>(1), 99–107.</a></li>''',
foot='The 40 studies in the activity are simulated, with a true effect of zero. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'After correcting for publication bias, the 2018 meta-analysis found…',o:['No evidence of a bilingual advantage','A large advantage','A large disadvantage'],a:0,f:'152 studies, 891 effect sizes.'},
 {q:'Which studies were most likely to be published?',o:['Those supporting the advantage','Those challenging it','Equally likely'],a:0,f:'de Bruin and colleagues, 2015.'},
 {q:'Publication bias means…',o:['Published studies are a skewed sample of all studies','Researchers falsify data','Journals publish everything'],a:0,f:'No cheating required.'}]''',
js=PANEL_JS+r'''
/* ---------- publication bias simulation ---------- */
const X=v=>260+v*380,Nn=40;
const randn=()=>{let u=0,v=0;while(!u)u=Math.random();while(!v)v=Math.random();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v)};
function axes(){return `<line x1="70" y1="225" x2="450" y2="225" stroke="#13294B"/><line x1="260" y1="20" x2="260" y2="225" stroke="#9AA6B8" stroke-dasharray="4 4"/>`+
 [-0.4,-0.2,0,0.2,0.4].map(v=>`<text x="${X(v)}" y="246" text-anchor="middle" font-size="14" fill="#13294B">${v>0?'+':''}${v}</text>`).join('')+
 `<text x="80" y="40" font-size="14" fill="#3D4A5C">favours monolinguals</text><text x="440" y="40" font-size="14" text-anchor="end" fill="#3D4A5C">favours bilinguals</text>`}
function plot(st,pubOnly){const m=a=>a.reduce((x,y)=>x+y.d,0)/a.length;const shown=pubOnly?st.filter(s=>s.pub):st;
 let h=axes()+st.map((s,i)=>{const faded=pubOnly&&!s.pub;return `<circle cx="${X(Math.max(-.6,Math.min(.6,s.d)))}" cy="${60+(i%16)*10}" r="6" fill="${faded?'#E3E8EF':(s.d>0?'#FF5F05':'#3E6B9E')}"/>`}).join('');
 const mean=m(shown);h+=`<line x1="${X(mean)}" y1="30" x2="${X(mean)}" y2="225" stroke="#2E7D32" stroke-width="4"/><text x="${X(mean)+6}" y="222" font-size="15" font-weight="700" fill="#2E7D32">average ${mean>=0?'+':''}${mean.toFixed(2)}</text>`;
 $('pbG').innerHTML=h;return mean}
startRun(async()=>{const st=[];$('pbG').innerHTML=axes();
 say('Step 1','Run 40 small studies','In this world, being bilingual makes no difference at all. Each small study still gets a slightly different result, by chance.');
 await nextBtn('Run the studies');if(!RUN)return;
 for(let i=0;i<Nn;i++){st.push({d:randn()*0.22});if(i%4===3){plot(st,false);await sw(90);if(!RUN)return}}
 const all=plot(st,false);$('pbP').textContent=`${st.filter(s=>s.d>0).length} of 40 studies happened to favour bilinguals.`;
 say(null,'All 40 studies',`Some favour bilinguals and some favour monolinguals, by chance. The average is ${all>=0?'+':''}${all.toFixed(2)}, close to the true value of zero.`);
 const a=await ask(['Mostly the ones showing an advantage','A fair mix of all of them','Mostly the ones showing no effect'],'Which studies do you think get published?');if(!RUN)return;hideCh();
 st.forEach(s=>{s.pub=s.d>0.2?true:Math.random()<(s.d>0?0.35:0.15)});
 const pub=plot(st,true);const np=st.filter(s=>s.pub).length;$('pbP').textContent=`${np} of 40 studies published (faded dots stay in file drawers).`;
 say('Step 2','Publish the striking ones',`Striking positive results always get published; others only sometimes. The published average is now ${pub>=0?'+':''}${pub.toFixed(2)}.`);
 const b=await ask(['Bilingualism gives an advantage','There is no real effect','Can’t tell from published studies alone'],'Reading only the published studies, what would you conclude?');if(!RUN)return;hideCh();
 say('What happened','A zero effect that looks real',`The true effect was zero, but the published studies average ${pub>=0?'+':''}${pub.toFixed(2)}. ${b===0?'Like many readers, you would have concluded there is an advantage. ':''}That is how a literature can show an effect that isn’t there. When researchers tracked conference abstracts on bilingualism and corrected meta-analyses for this bias, the advantage disappeared.`)});
'''+grid('''[
 ['How many studies of adults did Lehtonen and colleagues pool?',['152','15','1,520'],0,'With 891 effect sizes.'],
 ['Before correcting for publication bias, the advantage was…',['Very small','Large','Exactly zero'],0,'For inhibition, shifting and working memory.'],
 ['After correction?',['No evidence of an advantage remained','The advantage grew','It became a large disadvantage'],0,'The bias explained the apparent effect.'],
 ['How many conference abstracts did de Bruin and colleagues track?',['104','14','1,004'],0,'From 1999 to 2012.'],
 ['Was the publication difference explained by sample size or statistical power?',['No','Yes','Only sample size'],0,'Positive results were simply more likely to be published.']]''','The pattern: chance plus selective publication can create an effect that isn’t there.'))
write(o)
