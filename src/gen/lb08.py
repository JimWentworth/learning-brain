import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb08',n='8',title='Spatial Memory: Give Ideas a Place',h1='Spatial memory',em='Give ideas a place',read='8',mins='2 minutes',vtitle='Spatial memory',
dek='Your brain keeps a map of where things are, and that map can grow in adults. Memory champions borrow it to store lists. It may even help organize ideas that have nothing to do with space.',
jumps='<span><a href="#mT">Build a memory palace</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two deep structures glowing orange and labelled: the hippocampus, home of place cells, and the entorhinal cortex next to it, home of grid cells.',
hero_js="BR.R.hip.lab=[640,740];BR.R.hip.al='left';BR.R.ent.lab=[360,740];BR.R.ent.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.44,s:fitS(W,H,1.32),t,active:['hip','ent'],labels:['hip','ent'],labelT:{hip:0.8,ent:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.mword{font:800 clamp(28px,4.6vw,44px)/1.2 var(--body);color:#fff;text-align:center;min-height:1.2em}
.mcap{font-size:18px;color:#E9EEF6;text-align:center;margin:0;min-height:1.4em;max-width:36ch}
.house{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px;width:100%}
.house[hidden]{display:none}
.room{border:2px solid #8FA3C2;border-radius:8px;padding:8px 10px;background:#0F2240}
.room b{display:block;font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-bottom:6px}
.spot{display:flex;align-items:center;gap:8px;font-size:17px;color:#fff;padding:4px 6px;border-radius:6px;min-height:34px}
.spot i{font-style:normal;font-weight:800;width:24px;height:24px;border-radius:50%;background:#3A4E72;display:inline-flex;align-items:center;justify-content:center;font-size:14px;flex:none}
.spot.on{background:#FF8A3D;color:#13294B;font-weight:800}.spot.on i{background:#13294B;color:#fff}
.min{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%}
.min[hidden]{display:none}
.min textarea{width:100%;max-width:440px;min-height:110px;padding:10px 12px;font:600 19px/1.4 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;resize:vertical}
.min textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:110px;height:110px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>A rat explores a box. Deep in its brain, in the hippocampus, one cell fires only when the rat is in one corner. Another fires only by the far wall. Cell by cell, they build a map of the room.</p>
    <p>The brain is built to remember where. Teachers and memory champions can borrow that map for things that have nothing to do with places.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1971</strong><span>place cells first reported, in the hippocampus of rats</span></div>
      <div role="listitem"><strong>2014</strong><span>Nobel Prize for the discovery of place cells and grid cells</span></div>
      <div role="listitem"><strong>3–4 years</strong><span>for London taxi trainees to learn the city’s layout</span></div>
      <div role="listitem"><strong>26 → 62</strong><span>words out of 72 recalled after 40 days of memory-palace training</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The map</span>An inner positioning system</h2>
    <p>John O’Keefe and Jonathan Dostrovsky reported these place cells in 1971. In 2005, May-Britt and Edvard Moser’s lab found grid cells next door, in the entorhinal cortex. Each grid cell fires at many spots laid out in a repeating triangular pattern, like the lines of graph paper. Together, place cells and grid cells work like an inner GPS. The three shared the 2014 Nobel Prize in Physiology or Medicine.</p>
    <h2 class="sec"><span class="n">Adults</span>The map can grow</h2>
    <p>Trainee London taxi drivers spend 3 to 4 years learning the city’s 25,000 streets, known as “the Knowledge”, and only about half pass. Katherine Woollett and Eleanor Maguire scanned 79 trainees and 31 people who weren’t training, before and after. The trainees who qualified gained grey matter in the back of the hippocampus. Those who failed, and the comparison group, showed no such change.</p>
    <h2 class="sec"><span class="n">The method</span>A memory palace</h2>
    <p>An ancient memory method, the method of loci, borrows the map. You picture each item at a spot along a route you know well, then walk the route in your mind to bring the items back. In 2017, Martin Dresler and colleagues trained people with ordinary memories for 30 minutes a day. After 40 days, they went from recalling an average of 26 words out of 72 to 62. Four months later, without more training, they still recalled 22 more words than at the start.</p>
  </div>

  <section class="night" aria-labelledby="mT">
    <div class="col">
      <h2 class="sec" id="mT"><span class="n">Try it</span>Build a memory palace</h2>
      <p>Two rounds of 10 words, shown one at a time. In the first, remember them any way you like. In the second, you’ll place each word at a spot in a house. Each round ends with a 15-second easy task, then you type what you remember. About 4 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="mScreen">
          <div class="house" id="mHouse" hidden></div>
          <div class="mword" id="mWord" aria-live="polite"></div>
          <p class="mcap" id="mCap"></p>
          <div class="tbar" aria-hidden="true"><i id="mTb" style="width:0"></i></div>
          <form class="min" id="mForm" hidden><label class="sr-only" for="mIn">Type the words you remember</label><textarea id="mIn" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Type the words, in any order"></textarea><button class="nbtn" type="submit">Done</button></form>
          <button class="brk" id="mBrk" hidden aria-label="Tap when the circle is orange"></button>
          <p class="prog" id="mProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="mPhase">Ready</p>
          <p class="mtitle" id="mTitle">Does a route help?</p>
          <p class="mtext" id="mText" aria-live="polite">The memory-palace round always comes second, because once you know the method you can’t switch it off. That gives it a little practice, but also one list more to keep apart.</p>
          <div id="mRes"></div>
          <div class="mrow"><button class="nbtn" id="mGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Beyond space</span>A map for ideas</h2>
    <p>The map may reach beyond physical space. In 2016, Alexandra Constantinescu, Jill O’Reilly and Timothy Behrens taught people a set of cartoon birds that differed in neck length and leg length. Changing the bird felt like moving through a two-dimensional “bird space”. As people moved through it in their minds, brain scans showed a grid-like signal, much like the one seen during navigation.</p>
  </div>

  <section aria-labelledby="brT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="brT"><span class="n">Try it</span>Predict the findings</h2>
      <p>For each comparison from the research, predict what was found. Then check.</p>
    </div>
    <div class="wide">
      <form class="pgrid" id="pGrid"></form>
      <div class="qrow"><button class="pbtn" id="pCheck" type="button">Check my predictions</button><button class="pbtn" id="pReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="pSum" aria-live="polite"></p>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Some caution</span>Finding is not understanding</h2>
    <p>Memory palaces are strong for lists and sequences, such as the order of steps, names or dates. They don’t build understanding: a place helps you find an idea, but doesn’t explain it. And findings about the size of brain areas come from small groups, so treat them as a sign that the adult brain can change, not as a recipe.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Give ideas a consistent place</h3>
      <p>Keep the same board layout from week to week. Draw diagrams with stable positions and come back to them. Show a map of the course, so each topic sits somewhere. And let students lay out what they know in space, as a concept map or a timeline on the wall.</p>
    </aside>
  </div>
''',
tips_h='The brain remembers where',
tips='''      <li><b>Same place, every time</b><span>A stable board layout and stable diagrams.</span></li>
      <li><b>Map the course</b><span>So each topic has a place among the others.</span></li>
      <li><b>Let students lay it out</b><span>Concept maps and timelines turn ideas into places.</span></li>''',
sources='''        <li><a href="https://www.nobelprize.org/prizes/medicine/2014/summary/">The Nobel Prize in Physiology or Medicine 2014: John O’Keefe, May-Britt Moser and Edvard I. Moser.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3268356">Woollett, K., &amp; Maguire, E. A. (2011). Acquiring “the Knowledge” of London’s layout drives structural brain changes. <i>Current Biology</i>.</a></li>
        <li><a href="https://www.sciencedaily.com/releases/2017/03/170308131236.htm">ScienceDaily on Dresler, M., et al. (2017). Mnemonic training reshapes brain networks to support superior memory. <i>Neuron</i>.</a></li>
        <li><a href="https://neurosciencenews.com/memory-training-longevity-6221/">Neuroscience News: four months later, the trained group still recalled more than 22 more words.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5248972">Constantinescu, A. O., O’Reilly, J. X., &amp; Behrens, T. E. J. (2016). Organizing conceptual knowledge in humans with a gridlike code. <i>Science</i>.</a></li>''',
quiz='''[
 {q:'Which London taxi trainees gained grey matter in the back of the hippocampus?',o:['Those who qualified','All trainees, pass or fail','None of them'],a:0,f:'Trainees who failed, and the comparison group, showed no such change.'},
 {q:'What is a memory palace best for?',o:['Lists and sequences','Understanding why an idea works','Replacing practice'],a:0,f:'A place helps you find an idea, but doesn’t explain it.'},
 {q:'What did the bird study suggest?',o:['A grid-like brain signal may also map ideas, not just places','Birds have grid cells','People navigate better after looking at birds'],a:0,f:'People moving through an abstract “bird space” showed a grid-like signal.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- memory palace ----------
   20 words from 24 concrete nouns, two lists of 10. Round 1: plain list, one word every 4 s, 15 s easy task, free recall.
   Round 2: same timing, but each word appears at the next of 10 spots in a house (route shown first).
   15 s easy task, then free recall with the empty house shown. Scoring: words typed in any order;
   a plural or one-letter slip counts. */
const POOL=['trumpet','pineapple','scissors','penguin','bicycle','teapot','cactus','envelope','volcano','sandwich','octopus','telescope','balloon','pyramid','skateboard','lobster','compass','crown','tractor','parrot','toaster','hammock','lantern','dolphin'];
const ROOMS=[['Front hall',['doormat','coat hook']],['Kitchen',['sink','fridge']],['Living room',['sofa','fireplace']],['Stairs',['bottom step','top step']],['Bedroom',['bed','wardrobe']]];
const SPOTS=ROOMS.flatMap(r=>r[1]);
$('mHouse').innerHTML=ROOMS.map(([r,s],k)=>`<div class="room"><b>${r}</b>${s.map((p,j)=>`<div class="spot" id="sp${k*2+j}"><i>${k*2+j+1}</i><span>${p}</span></div>`).join('')}</div>`).join('');
function ed1(a,b){if(a===b)return true;if(Math.abs(a.length-b.length)>1)return false;let i=0,j=0,d=0;while(i<a.length&&j<b.length){if(a[i]===b[j]){i++;j++;continue}if(++d>1)return false;if(a.length>b.length)i++;else if(b.length>a.length)j++;else{i++;j++}}return d+(a.length-i)+(b.length-j)<=1}
const match=(t,w)=>t===w||t===w+'s'||t===w+'es'||(w.length>=5&&ed1(t,w));
const score=(txt,list)=>{const toks=[...new Set(txt.toLowerCase().split(/[^a-z]+/).filter(Boolean))];return new Set(toks.map(t=>list.find(w=>match(t,w))).filter(Boolean)).size};
let mr=null;
function mTimer(sec,me){const t0=performance.now();const tick=()=>{if(!mr||mr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('mTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
function spots(i,word){SPOTS.forEach((p,k)=>{const s=$('sp'+k);s.classList.toggle('on',k===i);s.querySelector('span').textContent=k===i&&word?`${p}: ${word}`:p})}
function mWait(label){return new Promise(res=>{const b=$('mGo');b.textContent=label;b.disabled=false;b.focus();b.onclick=()=>{b.onclick=null;b.disabled=true;b.textContent='In progress';res()}})}
function mRecall(){return new Promise(res=>{mr.res=res;$('mForm').hidden=false;$('mIn').value='';$('mIn').focus()})}
$('mForm').addEventListener('submit',e=>{e.preventDefault();if(!mr||!mr.res)return;const r=mr.res;mr.res=null;$('mForm').hidden=true;r($('mIn').value)});
async function mBreak(){$('mWord').textContent='Easy break';$('mCap').textContent='';$('mBrk').hidden=false;$('mBrk').focus();let on=false;const me=Symbol();mr.tok=me;
 $('mProg').textContent='For 15 seconds, tap the circle (or press Space) whenever it turns orange.';
 const brk=$('mBrk');brk.onclick=()=>{if(on){on=false;brk.classList.remove('on')}};const t0=performance.now();mTimer(15,me);
 while(performance.now()-t0<15000){await sw(1000+Math.random()*1500);if(!mr)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;mr.tok=null;$('mTb').style.width='0'}
$('mBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('mBrk').click()}});
async function show(list,palace){for(let i=0;i<10;i++){$('mWord').textContent=list[i];
  if(palace){spots(i,list[i]);$('mCap').textContent=`Spot ${i+1}, the ${SPOTS[i]}. Picture the ${list[i]} there, doing something strange.`}else $('mCap').textContent=`Word ${i+1} of 10`;
  const me=Symbol();mr.tok=me;mTimer(4,me);await sw(4000);if(!mr)return false}
 mr.tok=null;$('mWord').textContent='';spots(-1);$('mTb').style.width='0';return true}
$('mGo').addEventListener('click',async()=>{if(mr||$('mGo').onclick)return;mr={};const g=$('mGo');g.disabled=true;g.textContent='In progress';$('mRes').innerHTML='';
 const w=shuf([...POOL]).slice(0,20);const A=w.slice(0,10),B=w.slice(10);
 $('mPhase').textContent='Round 1 of 2';$('mTitle').textContent='A plain list';$('mText').textContent='Ten words, 4 seconds each. Remember them any way you like.';$('mHouse').hidden=true;$('mProg').textContent='';
 if(!await show(A,false))return;
 $('mPhase').textContent='Round 1 of 2 · Break';await mBreak();if(!mr)return;
 $('mTitle').textContent='Recall';$('mText').textContent='Type every word you remember, in any order.';$('mWord').textContent='Which words?';$('mProg').textContent='';
 const a=score(await mRecall(),A);if(!mr)return;$('mProg').textContent=`${a} of 10.`;
 $('mPhase').textContent='Round 2 of 2';$('mTitle').textContent='A memory palace';$('mText').textContent='Here is a house with 10 spots, in order: front hall, kitchen, living room, stairs, bedroom. Take a moment to walk through it in your mind. Each new word will appear at the next spot. Picture it there, as vivid and odd as you can.';
 $('mHouse').hidden=false;spots(-1);$('mWord').textContent='';$('mCap').textContent='Walk the route: doormat, coat hook, sink, fridge, sofa, fireplace, bottom step, top step, bed, wardrobe.';
 await mWait('Show the words');if(!mr)return;$('mProg').textContent='';
 if(!await show(B,true))return;
 $('mPhase').textContent='Round 2 of 2 · Break';$('mHouse').hidden=true;await mBreak();if(!mr)return;
 $('mHouse').hidden=false;$('mTitle').textContent='Walk the route';$('mText').textContent='Walk through the house in your mind, spot by spot, and type every word you find, in any order.';$('mWord').textContent='';$('mCap').textContent='What was at each spot?';$('mProg').textContent='';
 const b=score(await mRecall(),B);if(!mr)return;
 $('mHouse').hidden=true;$('mWord').textContent='Done';$('mCap').textContent='';$('mProg').textContent='Done.';$('mPhase').textContent='Your results';
 const row=(l,n,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${n*10}%;background:${c}"></i></div><b>${n} of 10</b></div>`;
 $('mRes').innerHTML=`<div class="res wl2">${row('Plain list',a,'#C9D3E3')}${row('Memory palace',b,'#FCB316')}</div>`;
 let title,text;
 if(a>=9&&b>=9){title='Both near perfect';text=`You recalled ${a} words from the plain list and ${b} from the memory palace. Ten words is a short list; the method pays off most with long lists, such as the 72-word lists in the 2017 training study.`}
 else if(b-a>=2){title='The route did the work';text=`You recalled ${a} of 10 from the plain list and ${b} of 10 using the house. Each spot gave you a place to look, so walking the route brought the words back. People who trained for 40 days went from 26 to 62 words out of 72.`}
 else if(a-b>=2){title='The plain list won this time';text=`You recalled ${a} of 10 from the plain list and ${b} of 10 using the house. A new house, learned in a minute, is a weak route; the method works best with a place you already know by heart, and with practice. The people in the 2017 study trained for 30 minutes a day for 40 days.`}
 else{title='About the same this time';text=`You recalled ${a} of 10 from the plain list and ${b} of 10 using the house. On a first try, with a house you have only just seen, the method may help only a little. It works best with a place you know by heart, and with practice.`}
 $('mTitle').textContent=title;$('mText').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();mr=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['London taxi trainees who qualified, before and after 3 to 4 years of training',['More grey matter in the back of the hippocampus','No change','Less grey matter'],0,'Those who qualified gained grey matter in the posterior hippocampus.'],
 ['Trainees who failed to qualify, and people who weren’t training',['No such change','The same gain as those who qualified','A bigger gain'],0,'The change was found only in those who qualified.'],
 ['How many of the taxi trainees in that study qualified?',['About half','Nearly all','Almost none'],0,'39 of the 79 trainees passed.'],
 ['People with ordinary memories, after 40 days of memory-palace training',['More than doubled their recall','Improved slightly','No change'],0,'From an average of 26 words out of 72 to 62.'],
 ['The same people, four months later, without more training',['Kept most of the gain','Fell back to where they started','Improved further'],0,'They still recalled more than 22 words more than before training.'],
 ['People imagining moving through a “bird space” of neck and leg lengths',['Showed a grid-like brain signal','Showed no spatial signal','Showed activity only in visual areas'],0,'The signal resembled the one seen during navigation.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: the brain’s map changes with long practice, can be borrowed to store lists, and may help organize ideas too.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb08/template.html','w').write(page(o))
