import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb13',n='13',title='Motivation and Reward: Make Them Want to Know',h1='Motivation and reward',em='Make them want to know',read='8',mins='2 minutes',vtitle='Motivation and reward',
dek='Dopamine neurons signal the gap between what we expected and what we got. Curiosity recruits the same circuit and helps memory. External rewards are trickier: expected prizes can drain interest, while informative feedback builds it.',
jumps='<span><a href="#cT">The curiosity test</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two deep structures glowing orange and labelled: the ventral tegmental area in the midbrain, where dopamine neurons signal reward prediction errors, and the striatum, which receives that signal.',
hero_js="BR.R.vta.lab=[260,760];BR.R.vta.al='left';BR.R.str.lab=[200,-60];BR.R.str.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['vta','str'],labels:['vta','str'],labelT:{vta:0.8,str:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.cq{font:800 clamp(22px,3.2vw,30px)/1.3 var(--body);color:#fff;text-align:center;max-width:28ch;min-height:2.6em;display:flex;align-items:center;justify-content:center}
.ca{font:700 clamp(20px,2.6vw,24px)/1.35 var(--body);color:#FCB316;text-align:center;max-width:32ch;min-height:1.4em}
.cbtns{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;width:100%;max-width:520px}
.cbtns[hidden]{display:none}
.cbtns button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 16px/1.2 var(--body);cursor:pointer;padding:4px}
.cbtns button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.cbtns button small{display:block;font-size:13px;color:#C9D3E3;font-weight:600}
.cknew{background:none;border:none;color:#E9EEF6;text-decoration:underline;font:600 16px var(--body);cursor:pointer;min-height:36px}
.cknew[hidden]{display:none}
.copts{display:grid;gap:8px;width:100%;max-width:440px}
.copts[hidden]{display:none}
.copts button{min-height:48px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 18px var(--body);cursor:pointer;text-align:left;padding:6px 14px}
.copts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
@media (max-width:520px){.cbtns{grid-template-columns:repeat(2,minmax(0,1fr))}}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:110px;height:110px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>A monkey gets an unexpected sip of juice, and dopamine neurons in its midbrain fire a burst. Once a light reliably comes before the juice, the burst moves to the light. And if the light comes but the juice doesn’t, the neurons dip below their usual rate, right when the juice was due.</p>
    <p>Wolfram Schultz and colleagues showed that these neurons are not simply signalling pleasure. They track the difference between what was expected and what arrived: a reward prediction error.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Burst · nothing · dip</strong><span>dopamine’s response to better than, as and worse than expected</span></div>
      <div role="listitem"><strong>2014</strong><span>study showing curiosity engages reward areas and helps memory</span></div>
      <div role="listitem"><strong>128</strong><span>experiments in a 1999 review of rewards and interest</span></div>
      <div role="listitem"><strong>2009</strong><span>study in which writing about relevance raised science grades</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The signal</span>Better, as expected, worse</h2>
    <p>Better than expected brings a burst; just as expected, nothing; worse than expected, a dip. It is the prediction signal from <a href="@@LB:lb04@@">the page on prediction</a>, tuned to what matters, and <a href="@@LB:rew@@">the reward system page</a> looks at it in more detail.</p>
    <h2 class="sec"><span class="n">Curiosity</span>Wanting to know</h2>
    <p>Curiosity recruits the same circuit. In 2014, Matthias Gruber, Bernard Gelman and Charan Ranganath had people read trivia questions, rate how curious they were, and wait a few seconds for each answer. The more curious they were, the more their midbrain reward areas and nucleus accumbens engaged, and the better they remembered the answers, both straight away and a day later. They even remembered better the unrelated faces shown during the wait.</p>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>The curiosity test</h2>
      <p>16 trivia questions. For each, say how curious you are about the answer, then wait a moment for it. After a short break, a surprise quiz. Does curiosity predict what you remember? About 5 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
          <div class="cq" id="cQ" aria-live="polite"></div>
          <div class="ca" id="cA" aria-live="polite"></div>
          <div class="cbtns" id="cRate" hidden role="group" aria-label="How curious are you? Keys 1 to 4"><button type="button" data-v="1">1<small>Not curious</small></button><button type="button" data-v="2">2<small>A little</small></button><button type="button" data-v="3">3<small>Quite</small></button><button type="button" data-v="4">4<small>Very</small></button></div>
          <button class="cknew" id="cKnew" type="button" hidden>I already know the answer</button>
          <div class="copts" id="cOpts" hidden role="group" aria-label="Choose the answer"></div>
          <div class="tbar" aria-hidden="true"><i id="cTb" style="width:0"></i></div>
          <button class="brk" id="cBrk" hidden aria-label="Tap when the circle is orange"></button>
          <p class="prog" id="cProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="cPhase">Ready</p>
          <p class="mtitle" id="cTitle">Does wanting to know help you remember?</p>
          <p class="mtext" id="cText" aria-live="polite">Rate honestly, and use the whole scale. Questions you already know the answer to are left out.</p>
          <div id="cRes"></div>
          <div class="mrow"><button class="nbtn" id="cGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Rewards</span>Prizes and praise are not the same</h2>
    <p>External rewards are trickier. In 1999, Edward Deci, Richard Koestner and Richard Ryan pooled 128 experiments. When people expected a tangible reward, such as money or a prize, for doing an interesting task, they later chose to keep doing it on their own less often. Positive, informative feedback did the opposite: it raised both free-choice time on the task and reported interest.</p>
    <h2 class="sec"><span class="n">Relevance</span>Why should I care?</h2>
    <p>In 2009, Chris Hulleman and Judith Harackiewicz asked high-school science students to write, during the term, about how the material connected to their own lives. Students who had expected to do poorly gained interest in science and earned higher grades than similar students who wrote summaries instead. A later study replicated the result.</p>
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
    <h2 class="sec"><span class="n">Some caution</span>Rewards are not all bad</h2>
    <p>The undermining effect applies to tasks people already find interesting, and to rewards that are expected and tangible. Rewards for dull tasks, or unexpected ones, behave differently. And curiosity studies use trivia; a classroom question has to be one students actually want answered.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Show the gap before you fill it</h3>
      <p>Open with a question students want answered, and pause before the reveal. Give feedback that informs, about strategy and progress, rather than points for everything. Ask students to connect the material to their own goals, and let surprise do some of the work.</p>
    </aside>
  </div>
''',
tips_h='The brain learns most when it cares about the answer',
tips='''      <li><b>Question first</b><span>Open with something students want to know, and pause.</span></li>
      <li><b>Feedback that informs</b><span>About strategy and progress, not points for everything.</span></li>
      <li><b>Connect it to them</b><span>Ask how the material links to their own lives.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.275.5306.1593">Schultz, W., Dayan, P., &amp; Montague, P. R. (1997). A neural substrate of prediction and reward. <i>Science</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4252494">Gruber, M. J., Gelman, B. D., &amp; Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning via the dopaminergic circuit. <i>Neuron</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/10589297/">Deci, E. L., Koestner, R., &amp; Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://openevo.eva.mpg.de/?p=15319">Hulleman, C. S., &amp; Harackiewicz, J. M. (2009). Promoting interest and performance in high school science classes. <i>Science</i>.</a></li>
        <li><a href="https://forrt.org/flora-replication-atlas/doi/10.1126/science.1177067/">Replication record: Hulleman et al. (2017), <i>Journal of Educational Psychology</i>.</a></li>''',
quiz='''[
 {q:'What do dopamine neurons do when an expected reward fails to arrive?',o:['Dip below their usual rate','Fire a burst','Nothing changes'],a:0,f:'Better than expected: burst. As expected: nothing. Worse: a dip.'},
 {q:'What did curiosity do in the 2014 trivia study?',o:['Improved memory for answers, and even for unrelated faces','Improved memory only for the answers','Made no difference to memory'],a:0,f:'Curiosity engaged reward areas and helped memory.'},
 {q:'Which tended to raise people’s later free choice to keep doing an interesting task?',o:['Positive, informative feedback','Expected tangible rewards','Both equally'],a:0,f:'Expected tangible rewards tended to lower it.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- curiosity test ----------
   16 trivia questions. Study: question, curiosity rating 1-4 (or "I already know": excluded), 3 s wait, answer 3 s.
   30 s easy task. Surprise 4-option quiz on all rated questions. Compare % correct for high (3-4) vs low (1-2) curiosity. */
const QS=[
 ['How many hearts does an octopus have?','Three. One pumps blood through the body; two serve the gills.',['Three','One','Two','Five']],
 ['Which letter of the alphabet appears in no US state’s name?','Q.',['Q','J','X','Z']],
 ['On which planet does one turn on its axis take longer than one trip around the Sun?','Venus.',['Venus','Mercury','Mars','Neptune']],
 ['What is the national animal of Scotland?','The unicorn.',['The unicorn','The red deer','The golden eagle','The Highland cow']],
 ['What colour is a polar bear’s skin, under the fur?','Black.',['Black','Pink','White','Grey']],
 ['Counting its overseas territories, which country spans the most time zones?','France, with 12.',['France','Russia','The United States','The United Kingdom']],
 ['What is a group of crows called?','A murder.',['A murder','A parliament','A pride','A pod']],
 ['Which metal is liquid at room temperature?','Mercury.',['Mercury','Lead','Tin','Sodium']],
 ['A cashew nut grows attached to what?','A fruit called the cashew apple.',['A fruit, the cashew apple','The plant’s roots, underground','A cone, like a pine nut','A pod, like a pea']],
 ['Which animal has fingerprints that are hard to tell apart from human ones?','The koala.',['The koala','The kangaroo','The sloth','The panda']],
 ['Botanically, which of these is a berry?','The banana.',['Banana','Strawberry','Raspberry','Cherry']],
 ['A sesquicentennial marks how many years?','150 years.',['150','75','125','200']],
 ['What is the smallest bone in the human body?','The stapes, in the middle ear.',['The stapes, in the ear','A bone in the little toe','A bone in the little finger','The tip of the tailbone']],
 ['Which gas makes up most of Earth’s atmosphere?','Nitrogen, about 78%.',['Nitrogen','Oxygen','Carbon dioxide','Argon']],
 ['What shape is wombat poo?','Cubes.',['Cubes','Spheres','Spirals','Flat discs']],
 ['What do sea otters often do while sleeping, so they don’t drift apart?','Hold paws.',['Hold paws','Hold each other’s tails','Climb onto rocks','Bury themselves in sand']]];
let cr=null;
function cTimer(sec,me){const t0=performance.now();const tick=()=>{if(!cr||cr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('cTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
async function hold(sec){const me=Symbol();cr.tok=me;cTimer(sec,me);await sw(sec*1000);if(!cr)return false;cr.tok=null;$('cTb').style.width='0';return true}
function rate(){return new Promise(res=>{cr.res=res;$('cRate').hidden=false;$('cKnew').hidden=false;$('cRate').querySelector('button').focus()})}
const pick=v=>{if(!cr||!cr.res)return;const r=cr.res;cr.res=null;$('cRate').hidden=true;$('cKnew').hidden=true;r(v)};
$('cRate').addEventListener('click',e=>{const b=e.target.closest('button');if(b)pick(+b.dataset.v)});
$('cKnew').addEventListener('click',()=>pick(0));
addEventListener('keydown',e=>{if(!cr||!cr.res||$('cRate').hidden)return;if(/^[1-4]$/.test(e.key)){e.preventDefault();pick(+e.key)}});
function choose(opts){return new Promise(res=>{const box=$('cOpts');box.innerHTML=opts.map((t,i)=>`<button type="button" data-i="${i}">${t}</button>`).join('');box.hidden=false;box.querySelector('button').focus();
 box.onclick=e=>{const b=e.target.closest('button');if(!b||!cr)return;box.onclick=null;box.hidden=true;res(+b.dataset.i)}})}
async function cBreak(){$('cQ').textContent='Easy break';$('cA').textContent='';$('cBrk').hidden=false;$('cBrk').focus();let on=false;const me=Symbol();cr.tok=me;
 $('cProg').textContent='For 30 seconds, tap the circle (or press Space) whenever it turns orange.';
 const brk=$('cBrk');brk.onclick=()=>{if(on){on=false;brk.classList.remove('on')}};const t0=performance.now();cTimer(30,me);
 while(performance.now()-t0<30000){await sw(1000+Math.random()*1800);if(!cr)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;cr.tok=null;$('cTb').style.width='0'}
$('cBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('cBrk').click()}});
$('cGo').addEventListener('click',async()=>{if(cr)return;cr={};const g=$('cGo');g.disabled=true;g.textContent='In progress';$('cRes').innerHTML='';
 const items=shuf(QS.map(q=>({q:q[0],a:q[1],o:q[2],r:0})));
 $('cPhase').textContent='Step 1 of 3 · Questions';$('cTitle').textContent='How curious are you?';$('cText').textContent='Rate each question from 1 (not curious) to 4 (very curious), using the buttons or keys 1 to 4. Then wait for the answer.';
 for(let i=0;i<items.length;i++){const it=items[i];$('cQ').textContent=it.q;$('cA').textContent='';$('cProg').textContent=`Question ${i+1} of ${items.length}`;
  it.r=await rate();if(!cr)return;
  if(it.r===0){$('cA').textContent='Skipped: you knew it.';if(!await hold(1))return;continue}
  $('cA').textContent='The answer is coming…';if(!await hold(3))return;$('cA').textContent=it.a;if(!await hold(3))return}
 $('cQ').textContent='';$('cA').textContent='';
 $('cPhase').textContent='Step 2 of 3 · Break';$('cTitle').textContent='Step away';$('cText').textContent='An easy, 30-second task.';await cBreak();if(!cr)return;
 const test=shuf(items.filter(x=>x.r>0));
 $('cPhase').textContent='Step 3 of 3 · Quiz';$('cTitle').textContent='Surprise quiz';$('cText').textContent='Choose the answer you were shown.';
 for(let i=0;i<test.length;i++){const it=test[i];$('cQ').textContent=it.q;$('cProg').textContent=`Question ${i+1} of ${test.length}`;
  const ord=shuf([0,1,2,3]);const c=await choose(ord.map(k=>it.o[k]));if(!cr)return;it.got=ord[c]===0}
 $('cQ').textContent='Done';$('cProg').textContent='Done.';$('cPhase').textContent='Your results';
 const hi=test.filter(x=>x.r>=3),lo=test.filter(x=>x.r<=2),pc=a=>a.length?Math.round(100*a.filter(x=>x.got).length/a.length):0;
 const known=items.length-test.length,pH=pc(hi),pL=pc(lo);
 const row=(l,a,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${pc(a)}%;background:${c}"></i></div><b>${a.filter(x=>x.got).length} of ${a.length}</b></div>`;
 $('cRes').innerHTML=`<div class="res wl2">${lo.length?row('Less curious (1–2)',lo,'#C9D3E3'):''}${hi.length?row('More curious (3–4)',hi,'#FCB316'):''}</div>`;
 const kTxt=known?` ${known} question${known>1?'s':''} you already knew ${known>1?'were':'was'} left out.`:'';
 let title,text;
 if(hi.length<3||lo.length<3){title='Not enough spread to compare';text=`You rated ${hi.length} question${hi.length===1?'':'s'} 3 or 4 and ${lo.length} rated 1 or 2, so one group is too small to compare.${kTxt} You got ${test.filter(x=>x.got).length} of ${test.length} right overall. Try again and use the whole scale.`}
 else if(pH>=90&&pL>=90){title='Near perfect on both';text=`You got ${pH}% of the questions you were curious about and ${pL}% of the others.${kTxt} A four-choice quiz a few minutes later is easy; in the 2014 study, curiosity also helped a day later.`}
 else if(pH-pL>=15){title='Curiosity helped';text=`You got ${pH}% of the questions you were curious about, and ${pL}% of the ones you weren’t.${kTxt} Wanting to know seems to put the brain in a state that is ready to learn.`}
 else if(pL-pH>=15){title='Less curious did better this time';text=`You got ${pL}% of the questions you weren’t curious about and ${pH}% of the ones you were.${kTxt} With so few questions in each group, chance plays a big part. In the 2014 study, higher curiosity went with better memory on average.`}
 else{title='About the same this time';text=`You got ${pH}% of the questions you were curious about and ${pL}% of the others.${kTxt} With so few questions, small effects can hide. In the 2014 study, higher curiosity went with better memory on average.`}
 $('cTitle').textContent=title;$('cText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();cr=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['A monkey’s dopamine neurons when juice arrives completely unexpectedly',['A burst of firing','No change','A dip in firing'],0,'Better than expected: a burst.'],
 ['The same neurons once a light reliably predicts the juice, when the juice arrives as expected',['Little or no response to the juice','A bigger burst','A dip'],0,'The burst moves to the light. As expected: nothing.'],
 ['The light comes on, but the juice never arrives',['A dip below the usual rate','A burst','No change'],0,'Worse than expected: a dip, right when the juice was due.'],
 ['Unrelated faces shown while people waited for an answer they were curious about',['Remembered better','Remembered worse','No difference'],0,'A curious state seemed to help learning in general.'],
 ['Expected tangible rewards for doing an interesting task',['Later free choice to do it dropped','Later free choice rose','No change'],0,'Across 128 experiments, expected tangible rewards tended to undermine interest.'],
 ['High-school students who expected to do poorly, after writing about the relevance of science',['Higher interest and higher grades','No change','Lower interest'],0,'The relevance writing helped these students most.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: the brain responds to surprise and to wanting to know; expected prizes can backfire, while informative feedback and relevance help.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb13/template.html','w').write(page(o))
