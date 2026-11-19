import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb05',n='5',title='Focused and Diffuse Modes: Why Stepping Away Helps',h1='Focused and diffuse modes',em='Why stepping away helps',read='8',mins='2 minutes',vtitle='Focused and diffuse modes',
dek='You give up on a problem, go for a walk, and the answer shows up. Hard focus and stepping away both play a part in solving problems. The evidence for breaks is real but modest, and the timing matters.',
jumps='<span><a href="#ratT">Stuck, then step away</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: the frontal lobe and the intraparietal sulcus, parts of the attention network that switches on during demanding tasks. The default mode network, more active at rest, lies mostly along the midline and is not visible from the side.',
hero_js="BR.R.ips.lab=[500,-70];BR.R.ips.al='left';BR.R.fro.lab=[200,-70];BR.R.fro.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.5,s:fitS(W,H,1.32),t,active:['ips','fro'],labels:['ips','fro'],labelT:{ips:0.8,fro:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.rat{font:800 clamp(26px,4.4vw,40px)/1.3 var(--body);color:#fff;text-align:center;letter-spacing:.02em;min-height:1.3em}
.rin{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.rin[hidden]{display:none}
.rin input{min-height:52px;width:220px;padding:0 12px;font:700 22px var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.rin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:120px;height:120px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>You’ve been stuck on a problem for an hour. You give up, go for a walk, and halfway down the block, the answer shows up. Why does that happen?</p>
    <p>One popular way to describe it uses two modes, from the engineering educator Barbara Oakley. Focused mode is tight and effortful: it follows familiar paths quickly, but only nearby. Diffuse mode is relaxed and wide: it makes long, loose jumps between distant ideas. This is a teaching metaphor, not a map of the brain. But it is loosely tied to something real.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2005</strong><span>brain networks for tasks and for rest shown to rise and fall in opposition</span></div>
      <div role="listitem"><strong>2009</strong><span>a meta-analysis found that breaks help problem solving, modestly</span></div>
      <div role="listitem"><strong>8 hours</strong><span>of sleep, wakefulness at night, or wakefulness by day in the classic insight study</span></div>
      <div role="listitem"><strong>59%</strong><span>of people who slept found a hidden shortcut, more than twice the rate of those who stayed awake</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The networks</span>Task and rest</h2>
    <p>During demanding tasks, a set of attention regions in the frontal and parietal lobes switches on. At rest, a different set, the default mode network, mostly along the brain’s midline, becomes more active. In 2005, Michael Fox, Marcus Raichle and colleagues showed that even at rest, with no task at all, these two networks tend to rise and fall in opposition. The default network is busy when the mind wanders, remembers the past and imagines the future.</p>
    <h2 class="sec"><span class="n">Breaks</span>Does stepping away help?</h2>
    <p>In 2009, Ut Na Sio and Thomas Ormerod pooled decades of experiments on incubation, the idea that setting a problem aside helps solve it. Breaks did help, modestly. They worked best after a longer first attempt, and when the break was filled with an easy task rather than a demanding one. For word puzzles, an easy task even beat simple rest.</p>
  </div>

  <section class="night" aria-labelledby="ratT">
    <div class="col">
      <h2 class="sec" id="ratT"><span class="n">Try it</span>Stuck, then step away</h2>
      <p>Each puzzle shows three words. Find one word that goes with all three, such as “cottage, swiss, cake”: cheese. You get 30 seconds each. Puzzles you don’t solve come back later: some straight away, some after a one-minute easy break. About 6 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="rScreen" aria-describedby="rProg">
          <div class="rat" id="rW" aria-live="polite"></div>
          <div class="tbar" aria-hidden="true"><i id="rT" style="width:0"></i></div>
          <form class="rin" id="rForm" hidden><label class="sr-only" for="rIn">Your answer</label><input id="rIn" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">Check</button><button class="nbtn ghost" type="button" id="rSkip">Skip</button></form>
          <button class="brk" id="rBrk" hidden aria-label="Tap when the circle is orange"></button>
          <p class="prog" id="rProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="rPhase">Ready</p>
          <p class="mtitle" id="rTitle">Does a break help?</p>
          <p class="mtext" id="rText" aria-live="polite">You’ll compare the puzzles you came back to straight away with the ones you came back to after a short, easy break.</p>
          <div id="rRes"></div>
          <div class="mrow"><button class="nbtn" id="rGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Sleep</span>Sleeping on it</h2>
    <p>Sleep may help too. In 2004, Ullrich Wagner, Jan Born and colleagues had people practise a number task with a hidden shortcut they weren’t told about. After training, they spent 8 hours either asleep at night, awake at night, or awake during the day. Then they practised again. Of those who had slept, 59% found the shortcut, more than twice as many as in the groups that stayed awake. Sleep didn’t help people who hadn’t trained on the task first.</p>
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
    <h2 class="sec"><span class="n">Some caution</span>A picture, not a mechanism</h2>
    <p>Some later sleep studies found smaller effects, or none. And creative thinking doesn’t simply flip between modes: in 2016, Roger Beaty and colleagues reviewed evidence that the default and control networks, which often work in opposition, tend to cooperate while people generate and evaluate creative ideas. Treat focused and diffuse as a useful picture, not a description of how the brain works.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Stuck is not failing</h3>
      <p>Give learners a hard problem early, let them work on it in earnest, then build in a gap, such as a break, a night or a different task, before coming back to it. And say plainly that being stuck is a normal stage, not a sign of failure.</p>
    </aside>
  </div>
''',
tips_h='Learning needs a rhythm',
tips='''      <li><b>Start hard problems early</b><span>So there is time to step away and come back.</span></li>
      <li><b>Work in earnest first</b><span>Breaks help most after a real attempt.</span></li>
      <li><b>Make the break easy</b><span>An undemanding task, a walk, or a night’s sleep, not another hard task.</span></li>''',
sources='''        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC1157105">Fox, M. D., Snyder, A. Z., Vincent, J. L., Corbetta, M., Van Essen, D. C., &amp; Raichle, M. E. (2005). The human brain is intrinsically organized into dynamic, anticorrelated functional networks. <i>PNAS</i>.</a></li>
        <li><a href="https://www.research.lancs.ac.uk/portal/en/publications/does-incubation-enhance-problem-solving-a-metaanalytic-review(ec023bd3-01e9-453e-854a-3dca00e2d146)/export.html">Sio, U. N., &amp; Ormerod, T. C. (2009). Does incubation enhance problem solving? A meta-analytic review. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://research.uni-luebeck.de/en/publications/sleep-inspires-insight/">Wagner, U., Gais, S., Haider, H., Verleger, R., &amp; Born, J. (2004). Sleep inspires insight. <i>Nature</i>.</a></li>
        <li><a href="https://develop.bigthink.com/?p=64710">Big Think: the science of sleeping on it (59% in the sleep group).</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5834438">Schönauer, M., et al. (2018). Sleep does not promote solving classical insight problems and magic tricks. <i>Frontiers in Human Neuroscience</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4724474">Beaty, R. E., Benedek, M., Silvia, P. J., &amp; Schacter, D. L. (2016). Creative cognition and brain network dynamics. <i>Trends in Cognitive Sciences</i>.</a></li>''',
quiz='''[
 {q:'What did the 2009 review find about taking a break from a stuck problem?',o:['It helps, modestly','It makes no difference','It always solves the problem'],a:0,f:'Breaks helped most after a longer first attempt, filled with an easy task.'},
 {q:'What should fill a break to help most?',o:['Something easy','Another demanding task','Nothing at all, always'],a:0,f:'Demanding tasks during the break gave smaller effects.'},
 {q:'How should “focused” and “diffuse” modes be treated?',o:['As a useful teaching picture, not a brain mechanism','As two separate brain areas','As proven brain states that switch on and off'],a:0,f:'The default and control networks often cooperate during creative thinking.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- stuck, then step away (compound remote associates) ----------
   8 puzzles drawn at random from 16. Round 1: up to 30 s each. Unsolved puzzles are split at random, alternately,
   into "straight away" and "after a break". Round 2: the "straight away" ones, 20 s each. Then a 60 s easy break
   (tap the circle when it turns orange). Round 3: the "after a break" ones, 20 s each.
   Result: share solved on return, for each group. */
const RAT=[['cottage','swiss','cake','cheese'],['cream','skate','water','ice'],['loser','throat','spot','sore'],['show','life','row','boat'],['night','wrist','stop','watch'],['duck','fold','dollar','bill'],['rocking','wheel','high','chair'],['dew','comb','bee','honey'],['fountain','baking','pop','soda'],['aid','rubber','wagon','band'],['flake','mobile','cone','snow'],['cracker','fly','fighter','fire'],['safety','cushion','point','pin'],['cane','daddy','plum','sugar'],['dream','break','light','day'],['fish','mine','rush','gold']];
let rr=null;
function rTimer(sec,me){const t0=performance.now();const tick=()=>{if(!rr||rr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('rT').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
function rAsk(item,sec,label){return new Promise(res=>{const me=Symbol();rr.tok=me;rr.res=res;rr.item=item;
 $('rW').textContent=item.slice(0,3).join(' · ');$('rForm').hidden=false;$('rIn').value='';$('rIn').focus();$('rProg').textContent=label;rTimer(sec,me);
 setTimeout(()=>{if(rr&&rr.tok===me){rr.tok=null;res(false)}},sec*1000)})}
const norm=s=>s.toLowerCase().trim().replace(/[^a-z]/g,'');
$('rForm').addEventListener('submit',e=>{e.preventDefault();if(!rr||!rr.tok)return;const v=norm($('rIn').value);if(!v)return;
 if(v===rr.item[3]||v===rr.item[3]+'s'){rr.tok=null;$('rProg').textContent=`Yes: ${rr.item[3]}.`;rr.res(true)}else{$('rProg').textContent=`Not “${v}”. Keep trying, or skip.`;$('rIn').select()}});
$('rSkip').addEventListener('click',()=>{if(rr&&rr.tok){rr.tok=null;rr.res(false)}});
async function rBreak(){$('rForm').hidden=true;$('rW').textContent='Easy break';$('rBrk').hidden=false;$('rBrk').focus();let on=false,hits=0;const me=Symbol();rr.btok=me;
 $('rProg').textContent='For one minute, tap the circle (or press Space) whenever it turns orange. Don’t think about the puzzles.';
 const brk=$('rBrk');brk.onclick=()=>{if(on){hits++;on=false;brk.classList.remove('on')}};
 const t0=performance.now();const me2=me;rTimer(60,me2);rr.tok=me2;
 while(performance.now()-t0<60000){await sw(1200+Math.random()*1800);if(!rr)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;rr.tok=null}
$('rBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('rBrk').click()}});
$('rGo').addEventListener('click',async()=>{rr={};$('rGo').disabled=true;$('rRes').innerHTML='';$('rPhase').textContent='Round 1 of 3';$('rTitle').textContent='Find the link';$('rText').textContent='Type one word that goes with all three. Skip if you’re stuck.';
 const items=shuf(RAT.map(x=>[...x])).slice(0,8);const uns=[];
 for(let i=0;i<8;i++){const ok=await rAsk(items[i],30,`Puzzle ${i+1} of 8`);if(!rr)return;if(!ok)uns.push(items[i]);await sw(ok?700:300)}
 shuf(uns);const now=uns.filter((_,i)=>i%2===0),later=uns.filter((_,i)=>i%2===1);
 const sNow=[],sLater=[];
 if(now.length){$('rPhase').textContent='Round 2 of 3';$('rTitle').textContent='Straight back to it';$('rText').textContent='These are some of the puzzles you didn’t solve. Another 20 seconds each, straight away.';
  for(let i=0;i<now.length;i++){const ok=await rAsk(now[i],20,`Straight back: ${i+1} of ${now.length}`);if(!rr)return;sNow.push(ok);await sw(ok?700:300)}}
 if(later.length){$('rPhase').textContent='Break';$('rTitle').textContent='Step away';$('rText').textContent='An easy, one-minute task.';await rBreak();if(!rr)return;
  $('rPhase').textContent='Round 3 of 3';$('rTitle').textContent='After the break';$('rText').textContent='The rest of the puzzles you didn’t solve. 20 seconds each.';
  for(let i=0;i<later.length;i++){const ok=await rAsk(later[i],20,`After the break: ${i+1} of ${later.length}`);if(!rr)return;sLater.push(ok);await sw(ok?700:300)}}
 $('rForm').hidden=true;$('rW').textContent='';$('rT').style.width='0';$('rProg').textContent='Done.';$('rPhase').textContent='Your results';
 const k1=8-uns.length,a=sNow.filter(Boolean).length,b=sLater.filter(Boolean).length;
 const row=(l,k,n,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${n?k/n*100:0}%;background:${c}"></i></div><b>${n?k+' of '+n:'—'}</b></div>`;
 $('rRes').innerHTML=`<div class="res">${row('First try',k1,8,'#7DB8FF')}${row('Straight back',a,now.length,'#C9D3E3')}${row('After the break',b,later.length,'#FCB316')}</div>`;
 const pa=now.length?a/now.length:0,pb=later.length?b/later.length:0;let title,text;
 if(uns.length<2){title=uns.length?'Almost nothing left to incubate':'You solved them all';text=`You solved ${k1} of 8 on the first try, so there weren’t enough unsolved puzzles to compare. Try again: you’ll get a different set.`}
 else if(a+b===0){title='Still stuck';text=`None of the returned puzzles fell, with or without a break. A minute’s break is short; in studies, longer gaps and sleep sometimes do more. Breaks help modestly on average, not every time.`}
 else if(pb>pa){title='The break helped this time';text=`You solved ${b} of ${later.length} after the break, compared with ${a} of ${now.length} when you went straight back. That fits the research: a short, easy break after a real attempt helps, modestly.`}
 else if(pb===pa){title='No difference this time';text=`You solved the same share either way (${a} of ${now.length} straight back, ${b} of ${later.length} after the break). With so few puzzles, chance plays a big part. Across many studies, breaks help modestly.`}
 else{title='Going straight back worked better this time';text=`You solved ${a} of ${now.length} straight back, and ${b} of ${later.length} after the break. With so few puzzles, chance plays a big part. Across many studies, breaks help modestly, and not for everyone every time.`}
 $('rTitle').textContent=title;$('rText').textContent=text;$('rGo').textContent='Try again';$('rGo').disabled=false;$('rGo').focus();rr=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['People stuck on a problem who took a break, compared with people who kept working',['Did better','Did the same','Did worse'],0,'Breaks helped, modestly, across the studies in the 2009 review.'],
 ['A break after a long first attempt, compared with a break after a short one',['Long attempt first helped more','No difference','Short attempt first helped more'],0,'Longer preparation before the break gave a bigger effect. A break helps most after a real attempt.'],
 ['A break filled with an easy task, compared with one filled with a demanding task',['Easy task helped more','No difference','Demanding task helped more'],0,'Demanding tasks during the break gave a smaller effect.'],
 ['For word puzzles, a break with an easy task, compared with simply resting',['Easy task helped more','No difference','Resting helped more'],0,'Surprisingly, an easy task beat rest for word-based insight problems.'],
 ['People who slept after practising a number task with a hidden shortcut, compared with people who stayed awake',['More found the shortcut','About the same','Fewer found the shortcut'],0,'59% of sleepers found it, more than twice the rate in the groups that stayed awake.'],
 ['Later studies of sleep and insight',['Mixed results, some found no benefit','All found a big benefit','All found that sleep hurt'],0,'Some later studies found smaller effects, or none.']];
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<6?` (${6-ans} left blank)`:''}. `)+'The pattern: work hard first, then step away into something easy, and expect a modest boost, not a guarantee.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb05/template.html','w').write(page(o))
