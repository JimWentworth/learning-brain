import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb15',n='15',title='Adult Plasticity and Belief: Earned, Specific, Kept by Use',h1='Adult plasticity and belief',em='Earned, specific, kept by use',read='8',mins='2 minutes',vtitle='Adult plasticity and belief',
dek='Adult brains do change with practice, but the change is earned, specific and kept by use. Believing ability can grow is true and worth saying. Brief mindset lessons alone, though, do little for grades.',
jumps='<span><a href="#kT">Watch a skill grow</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: an area in the temporal lobe that tracks visual motion, and the intraparietal sulcus. Both gained grey matter in adults who learned to juggle.',
hero_js="BR.R.tem.lab=[300,770];BR.R.tem.al='right';BR.R.ips.lab=[1000,-60];BR.R.ips.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['tem','ips'],labels:['tem','ips'],labelT:{tem:0.8,ips:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.kkey{display:grid;grid-template-columns:repeat(9,minmax(0,1fr));gap:4px;width:100%;max-width:520px;border:2px solid #8FA3C2;border-radius:10px;padding:6px;background:#0F2240}
.kkey[hidden]{display:none}
.kkey div{display:flex;flex-direction:column;align-items:center;gap:2px;color:#fff;font:800 18px var(--body)}
.kkey svg,.ksym svg{display:block}
.ksym{min-height:96px;display:flex;align-items:center;justify-content:center}
.kpad{display:grid;grid-template-columns:repeat(9,minmax(0,1fr));gap:6px;width:100%;max-width:520px}
.kpad[hidden]{display:none}
.kpad button{min-height:48px;border-radius:10px;border:2px solid #8FA3C2;background:#1B2E50;color:#fff;font:800 20px var(--body);cursor:pointer;padding:0}
.kpad button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
@media (max-width:520px){.kpad{grid-template-columns:repeat(5,minmax(0,1fr))}.kkey div{font-size:16px}}
.kfb{min-height:1.4em;font-size:18px;color:#E9EEF6;text-align:center;margin:0}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>Adults with no juggling experience spent three months learning a three-ball cascade. Brain scans showed more grey matter in an area that tracks visual motion. Three months after they stopped practising, much of that increase had faded.</p>
    <p>So adult brains do change, as <a href="@@LB:lb01@@">the neuroplasticity page</a> shows. But notice three things. The change was specific: a motion area, for a motion skill. It took months of effortful practice. And without use, it receded.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>3 months</strong><span>of juggling practice before the grey-matter change showed</span></div>
      <div role="listitem"><strong>12,490</strong><span>ninth graders in the largest trial of a brief growth-mindset programme</span></div>
      <div role="listitem"><strong>0.10</strong><span>grade points gained, on average, by the lower-achieving students in that trial</span></div>
      <div role="listitem"><strong>d = 0.02</strong><span>the effect in the highest-quality studies of one 2023 review: about zero</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Plasticity</span>Earned, specific, kept by use</h2>
    <p>Some windows also narrow with age, such as learning a new language without an accent. Adult plasticity is real, but it is earned through practice, specific to what is practised, and kept by continued use.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>Watch a skill grow</h2>
      <p>A key pairs nine symbols with the numbers 1 to 9. Each symbol that appears, press its number, as fast as you can while staying accurate. Four 30-second rounds with the key, then one round without it. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <div class="kkey" id="kKey" hidden aria-label="Key"></div>
          <div class="ksym" id="kSym" aria-live="polite"></div>
          <p class="kfb" id="kFb" aria-live="polite"></p>
          <div class="kpad" id="kPad" hidden role="group" aria-label="Number keys 1 to 9"></div>
          <div class="tbar" aria-hidden="true"><i id="kTb" style="width:0"></i></div>
          <p class="prog" id="kProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="kPhase">Ready</p>
          <p class="mtitle" id="kTitle">How fast does practice pay?</p>
          <p class="mtext" id="kText" aria-live="polite">Use the number keys on your keyboard, or tap the buttons. The pairing of symbols and numbers is new each time.</p>
          <div id="kRes"></div>
          <div class="mrow"><button class="nbtn" id="kGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Belief</span>Mindset: true, but not magic</h2>
    <p>Growth mindset is the idea that ability can be developed, and in one sense it is simply true: skills grow with practice, as the task above shows for most people. But do brief mindset lessons raise grades? In the largest trial, published in 2019 by David Yeager and colleagues, 12,490 ninth graders across the United States took two 25-minute online sessions. Lower-achieving students earned about a tenth of a grade point more in core subjects; higher-achieving students’ grades didn’t change.</p>
    <p>Reviews find small average effects. In 2018, Victoria Sisk, Brooke Macnamara and colleagues found the overall effect of mindset interventions on achievement was weak. In a 2023 review, Macnamara and Alexander Burgoyne found that when only the highest-quality studies were kept, the effect was close to zero. Another 2023 review found effects that ranged from negative to positive, depending on the setting.</p>
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
    <h2 class="sec"><span class="n">Some caution</span>Careful in both directions</h2>
    <p>Don’t promise that belief alone produces learning. And don’t tell students their abilities are fixed. Both claims are wrong.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Tell the honest version</h3>
      <p>Skills grow with the right kind of practice, over time. Praise strategy and progress, not effort alone: effort that isn’t working needs a new strategy, not more of the same. Show students their own growth, early work beside later work. And design courses where improvement is possible, with chances to revise and try again.</p>
    </aside>
  </div>
''',
tips_h='Belief opens the door; practice, strategy and time do the work',
tips='''      <li><b>The honest version</b><span>Skills grow with the right practice, over time.</span></li>
      <li><b>Praise strategy and progress</b><span>Not effort alone.</span></li>
      <li><b>Show the growth</b><span>Early work beside later work, with chances to revise.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/427311a">Draganski, B., et al. (2004). Neuroplasticity: Changes in grey matter induced by training. <i>Nature</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6786290/">Yeager, D. S., et al. (2019). A national experiment reveals where a growth mindset improves achievement. <i>Nature</i>.</a></li>
        <li><a href="https://englelab.gatech.edu/articles/2018/Sisk,%20Burgoyne%20et%20al.%20(2018)%20-%20Mindset%20and%20Academic%20Achievement.pdf">Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., &amp; Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? <i>Psychological Science</i>.</a></li>
        <li><a href="https://news.gatech.edu/news/2022/11/07/researchers-find-education-intervention-doesnt-live-promise">Georgia Tech on Macnamara, B. N., &amp; Burgoyne, A. P. (2023). Do growth mindset interventions impact students’ academic achievement? <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/2023-90931-004.pdf">Macnamara, B. N., &amp; Burgoyne, A. P. (2023). A spotlight on bias in the growth mindset intervention literature (reply discussing Burnette et al., 2023). <i>Psychological Bulletin</i>.</a></li>''',
quiz='''[
 {q:'What happened to the juggling-related brain change after people stopped practising?',o:['Much of it faded','It kept growing','It stayed exactly the same'],a:0,f:'Adult plasticity is kept by use.'},
 {q:'In the largest growth-mindset trial, who gained in grades?',o:['Lower-achieving students, by about 0.1 grade points','All students, by a full grade','No one'],a:0,f:'Higher-achieving students’ grades didn’t change.'},
 {q:'What should you praise?',o:['Strategy and progress','Effort alone','Natural talent'],a:0,f:'Effort that isn’t working needs a new strategy, not more of the same.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- watch a skill grow ----------
   9 symbols mapped to 1-9 at random. Rounds 1-4: 30 s each with the key shown; round 5: 30 s without it.
   A symbol is shown; a correct press moves on; a wrong press flags an error and keeps the symbol. Count correct per round. */
const SH={circle:'<circle cx="20" cy="20" r="13"/>',triangle:'<path d="M20 6 L34 33 L6 33 Z"/>',square:'<rect x="8" y="8" width="24" height="24"/>',diamond:'<path d="M20 5 L35 20 L20 35 L5 20 Z"/>',
 cross:'<path d="M9 9 L31 31 M31 9 L9 31"/>',plus:'<path d="M20 6 V34 M6 20 H34"/>',bar:'<path d="M8 20 H32 M8 12 H32 M8 28 H32"/>',arc:'<path d="M7 28 Q20 2 33 28"/>',zigzag:'<path d="M5 26 L13 12 L20 26 L27 12 L35 26"/>'};
const NAMES=Object.keys(SH);
const svg=(n,s)=>`<svg width="${s}" height="${s}" viewBox="0 0 40 40" aria-hidden="true" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">${SH[n]}</svg>`;
$('kPad').innerHTML=[1,2,3,4,5,6,7,8,9].map(d=>`<button type="button" data-d="${d}">${d}</button>`).join('');
let kr=null;
function kTimer(sec,me){const t0=performance.now();const tick=()=>{if(!kr||kr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('kTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
function press(d){if(!kr||!kr.live)return;if(d===kr.map[kr.cur]){kr.n++;kr.fb='';nextSym()}else{kr.err++;$('kFb').textContent='Not that one.'}}
function nextSym(){let s;do{s=NAMES[Math.floor(Math.random()*9)]}while(s===kr.cur);kr.cur=s;$('kSym').innerHTML=svg(s,84);$('kSym').setAttribute('aria-label',s);$('kFb').textContent=''}
$('kPad').addEventListener('click',e=>{const b=e.target.closest('button');if(b)press(+b.dataset.d)});
addEventListener('keydown',e=>{if(!kr||!kr.live)return;if(/^[1-9]$/.test(e.key)){e.preventDefault();press(+e.key)}});
function kWait(label){return new Promise(res=>{const b=$('kGo');b.textContent=label;b.disabled=false;b.focus();b.onclick=()=>{b.onclick=null;b.disabled=true;b.textContent='In progress';res()}})}
async function round(sec){kr.n=0;kr.err=0;kr.live=true;$('kPad').hidden=false;nextSym();if(kr.kb===false)$('kPad').querySelector('button').focus();const me=Symbol();kr.tok=me;kTimer(sec,me);await sw(sec*1000);if(!kr)return null;kr.live=false;kr.tok=null;$('kTb').style.width='0';$('kPad').hidden=true;$('kSym').innerHTML='';$('kSym').removeAttribute('aria-label');$('kFb').textContent='';return{n:kr.n,err:kr.err}}
$('kGo').addEventListener('click',async()=>{if(kr||$('kGo').onclick)return;kr={};const g=$('kGo');g.disabled=true;g.textContent='In progress';$('kRes').innerHTML='';
 const digits=shuf([1,2,3,4,5,6,7,8,9]);kr.map={};NAMES.forEach((n,i)=>kr.map[n]=digits[i]);
 $('kKey').innerHTML=[...NAMES].sort((a,b)=>kr.map[a]-kr.map[b]).map(n=>`<div aria-label="${n} is ${kr.map[n]}">${svg(n,30)}<span aria-hidden="true">${kr.map[n]}</span></div>`).join('');
 const R=[];
 for(let r=0;r<5;r++){const keyOn=r<4;$('kKey').hidden=!keyOn;
  $('kPhase').textContent=`Round ${r+1} of 5`;$('kTitle').textContent=keyOn?'With the key':'Without the key';$('kText').textContent=keyOn?'Press the number for each symbol, as fast as you can while staying accurate.':'The key is gone. Press the number for each symbol from memory.';
  $('kProg').textContent=r===0?'Get ready…':'Next round…';
  if(r>0){await kWait(keyOn?'Start the next round':'Start the last round');if(!kr)return}else{await sw(1200);if(!kr)return}
  $('kProg').textContent=`Round ${r+1}: 30 seconds`;const res=await round(30);if(!kr)return;R.push(res);
  $('kProg').textContent=`Round ${r+1}: ${res.n} correct${res.err?`, ${res.err} wrong press${res.err>1?'es':''}`:''}.`}
 $('kKey').hidden=true;$('kSym').textContent='';$('kPhase').textContent='Your results';
 const mx=Math.max(...R.map(x=>x.n),1);
 const row=(l,x,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${x.n/mx*100}%;background:${c}"></i></div><b>${x.n}</b></div>`;
 $('kRes').innerHTML=`<div class="res wl2">${R.slice(0,4).map((x,i)=>row(`Round ${i+1}`,x,['#C9D3E3','#9FB9DA','#7DB8FF','#FCB316'][i])).join('')}${row('No key',R[4],'#FF8A3D')}</div>`;
 const a=R[0].n,b=R[3].n,nk=R[4].n,gain=a?Math.round((b-a)/a*100):(b>0?100:0);
 const nkTxt=b>0?(nk>=0.7*b?` Without the key you still managed ${nk}: much of the key had moved into memory.`:nk>0?` Without the key you managed ${nk}: some of the key had moved into memory, but you still leaned on it.`:' Without the key, you couldn’t get any: you were still reading the key each time.'):'';
 let title,text;
 if(a+b<4){title='Too few answers to compare';text=`You got ${a} in the first round and ${b} in the fourth. Try again, pressing the number for each symbol as quickly as you can.`}
 else if(gain>=20){title='Your skill grew';text=`${a} correct in the first round, ${b} in the fourth: ${gain}% more in two minutes of practice.${nkTxt} Show students this kind of curve with their own work: early attempts beside later ones.`}
 else if(gain>-10){title='Steady this time';text=`${a} correct in the first round, ${b} in the fourth.${nkTxt} Some people start fast and level off quickly. Real skills take far longer than two minutes; the juggling change took three months.`}
 else{title='Slower by the end';text=`${a} correct in the first round, ${b} in the fourth.${nkTxt} Tiredness or lost focus can hide learning in the short run. That’s why progress is best judged over days and weeks, not minutes.`}
 $('kTitle').textContent=title;$('kText').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();kr=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['Adults after three months of learning to juggle',['More grey matter in a visual-motion area','No measurable change','Less grey matter'],0,'The change was specific to a motion area, for a motion skill.'],
 ['The same adults three months after they stopped juggling',['Much of the increase had faded','The increase kept growing','It stayed exactly the same'],0,'Plasticity is kept by use.'],
 ['Lower-achieving ninth graders after two 25-minute growth-mindset sessions',['About 0.1 grade points higher','About a full grade higher','No change'],0,'A small but real average gain in the largest trial.'],
 ['Higher-achieving ninth graders in the same trial',['No change in grades','A large gain in grades','Lower grades'],0,'Their grades didn’t change.'],
 ['Growth-mindset interventions across 43 studies, in a 2018 review',['Weak overall effects on achievement','Large effects','Harmful effects'],0,'The overall effect was weak.'],
 ['Only the highest-quality studies, in a 2023 review',['An effect close to zero','A large positive effect','A large negative effect'],0,'d = 0.02 across six high-quality studies.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: the brain changes with sustained, specific practice; a brief belief lesson alone does little.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb15/template.html','w').write(page(o))
