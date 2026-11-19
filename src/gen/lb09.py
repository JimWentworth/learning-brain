import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb09',n='9',title='Memory Systems and Automaticity: How Skills Run on Their Own',h1='Memory systems and automaticity',em='How skills run on their own',read='9',mins='2½ minutes',vtitle='Memory systems and automaticity',
dek='Knowing that and knowing how are handled by different brain systems. Practice moves a skill from slow and effortful to fast and automatic, which frees the mind for what comes next. But automatic skills hide their own steps, even from experts.',
jumps='<span><a href="#wT">Predict the weather</a></span><span><a href="#sT">Can you stop reading?</a></span>',
hero_aria='Drawing of the side of the brain with three structures glowing orange and labelled: the hippocampus, needed for memories of facts and events, and the striatum, part of the basal ganglia, and the cerebellum, which support skills and habits.',
hero_js="BR.R.hip.lab=[700,740];BR.R.hip.al='left';BR.R.str.lab=[300,-70];BR.R.str.al='right';BR.R.cer.lab=[1000,-70];BR.R.cer.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.44,s:fitS(W,H,1.32),t,active:['hip','str','cer'],labels:['hip','str','cer'],labelT:{hip:0.8,str:1.0,cer:1.2},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.wcards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;width:100%;max-width:460px}
.wcard{aspect-ratio:3/4;border-radius:10px;border:2px dashed #3A4E72;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.wcard.on{border:3px solid #fff;background:#1B2E50}
.wcard b{font-size:clamp(34px,6vw,52px);line-height:1;color:#fff}
.wcard small{font-size:15px;color:#E9EEF6}
.wfb{font:800 clamp(22px,3vw,28px)/1.3 var(--body);color:#fff;text-align:center;min-height:1.3em}
.wfb .ok{color:#7DD3A8}.wfb .no{color:#FFB38A}
.wq{display:grid;gap:12px;margin:6px 0 14px}
.wq[hidden]{display:none}
.wq fieldset{border:1px solid var(--night-line);border-radius:8px;padding:8px 12px;margin:0;display:flex;align-items:center;gap:14px;flex-wrap:wrap;color:#fff}
.wq legend{font-size:17px;font-weight:700;padding:0 4px}
.wq label{display:flex;align-items:center;gap:6px;font-size:17px;min-height:36px}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}
.sp{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:30px 10px;border-radius:10px;background:#F3F6FA;min-height:180px}
.sp:focus-visible{outline:3px solid #13294B;outline-offset:3px}
.sp .bx{min-height:120px;border:4px solid #13294B;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;font:800 clamp(26px,5vw,40px)/1 var(--body);color:#13294B;letter-spacing:.04em}
.sp .fx{grid-column:1/-1;text-align:center;font:800 32px/1 var(--body);color:#13294B;min-height:1em}
.smsg{text-align:center;font-size:17px;margin:12px 0 0;min-height:1.5em}''',
body='''  <div class="col lede">
    <p>After brain surgery in 1953 to stop his seizures, a man known as H.M. could no longer form new memories of facts or events. The psychologist Brenda Milner gave him a hard task: trace a star while watching only its reflection in a mirror. Over three days, he got steadily better. Yet each day, he had no memory of ever doing it before.</p>
    <p>H.M. showed that memory is not one system. He could learn a skill without being able to remember learning it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>3 days</strong><span>of mirror tracing: H.M. improved, but never remembered practising</span></div>
      <div role="listitem"><strong>50 → 65%</strong><span>roughly, the rise from chance in the weather task over 50 trials, for amnesic patients and healthy people alike</span></div>
      <div role="listitem"><strong>2002</strong><span>expert golfers putted worse when told to attend to each step of the stroke</span></div>
      <div role="listitem"><strong>76%</strong><span>of 67 high-school maths teachers wrongly expected equations to be easiest for algebra students</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Two systems</span>Knowing that, knowing how</h2>
    <p>Declarative memory holds facts and events: things you can put into words. It depends on the hippocampus, which is what H.M. had lost. Procedural memory holds skills and habits. It runs without awareness and leans on the basal ganglia, including the striatum, and the cerebellum.</p>
    <p>In 1996, Barbara Knowlton, Jennifer Mangels and Larry Squire pulled the two apart. People learned to predict the weather from patterns of cards, where each card was linked to rain or sun only some of the time. Amnesic patients learned the task as well as anyone, yet could hardly answer questions about the training session. Patients with Parkinson’s disease, which affects the basal ganglia, showed the reverse: they remembered the session but failed to learn the task.</p>
  </div>

  <section class="night" aria-labelledby="wT">
    <div class="col">
      <h2 class="sec" id="wT"><span class="n">Try it</span>Predict the weather</h2>
      <p>Each round, one to three cards appear. Guess rain or sun, and you’ll be told what happened. No card is a sure sign, so you’ll often be “wrong” even with a good guess. 60 rounds, then four quick questions. About 4 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="wScreen">
          <div class="wcards" id="wCards" aria-live="polite"></div>
          <div class="keys" id="wKeys" hidden><button type="button" id="wRain">Rain<small>key R</small></button><button type="button" id="wSun">Sun<small>key S</small></button></div>
          <div class="wfb" id="wFb" aria-live="polite"></div>
          <p class="prog" id="wProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="wPhase">Ready</p>
          <p class="mtitle" id="wTitle">Can you learn the pattern?</p>
          <p class="mtext" id="wText" aria-live="polite">Just go with your gut. You’ll get a score for each block of 20 rounds: how often you picked the more likely weather.</p>
          <form id="wQ" class="wq" hidden></form>
          <div id="wRes"></div>
          <div class="mrow"><button class="nbtn" id="wGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Practice</span>From slow to automatic</h2>
    <p>With practice, a skill shifts from slow and effortful to fast and automatic. That frees working memory for the next layer. A beginning reader sounds out each letter; a fluent reader stops noticing letters and starts thinking about the argument. Once reading is automatic, though, it is hard to switch off, as the next task shows.</p>
  </div>

  <section aria-labelledby="sT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Can you stop reading?</h2>
      <p>A word appears in the left or the right box. Press the side it is on: the F key or left arrow for left, the J key or right arrow for right, or tap the box. Ignore what the word says. 36 rounds, about 1 minute.</p>
    </div>
    <div class="wide">
      <div class="lbox">
        <div class="sp" id="sBox" tabindex="0" role="group" aria-label="Side task. Press F or left arrow for left, J or right arrow for right." aria-describedby="sMsg"><div class="fx" id="sFx" aria-hidden="true"></div><div class="bx" id="sL"></div><div class="bx" id="sR"></div></div>
        <p class="smsg" id="sMsg" aria-live="polite">Press Start.</p>
        <div class="qrow" style="justify-content:center"><button class="pbtn" id="sGo">Start</button></div>
        <div id="sRes" aria-live="polite"></div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The cost</span>Automatic hides the steps</h2>
    <p>In 2002, Sian Beilock and colleagues asked golfers to putt while either attending to each step of the stroke or doing a distracting second task. Experienced golfers putted better when distracted and worse when attending to their stroke. Novices showed the opposite pattern.</p>
    <p>Experts also lose sight of what was once hard. Mitchell Nathan and Kenneth Koedinger asked high-school maths teachers to rank algebra problems by difficulty. Most expected bare equations to be easiest. For students, equations were the hardest: fewer than 30% solved them, while more than half solved matching word problems. In 2003, Nathan and Anthony Petrosino found that future teachers with more advanced maths training were more likely to make this mistake. They called it the expert blind spot.</p>
    <h2 class="sec"><span class="n">Some caution</span>Fluency is not understanding</h2>
    <p>A student can run a procedure automatically and still not know why it works, or when to use it. Speed is worth building, but only for the right pieces, and only tied to meaning.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Choose what to make automatic</h3>
      <p>Decide which pieces students should make automatic, such as notation, core facts or routine steps, and drill those deliberately, spaced over time. Keep the reasoning in view, so fast steps stay tied to meaning. And when you explain, slow down and unpack the steps you no longer notice yourself.</p>
    </aside>
  </div>
''',
tips_h='Practice moves a skill out of the spotlight',
tips='''      <li><b>Choose what to automate</b><span>Notation, core facts, routine steps.</span></li>
      <li><b>Drill it, spaced</b><span>Short, deliberate practice across days and weeks.</span></li>
      <li><b>Unpack your own steps</b><span>The steps you no longer notice are the ones students need to see.</span></li>''',
sources='''        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC33639">Squire, L. R., &amp; Zola, S. M. (1996). Structure and function of declarative and nondeclarative memory systems. <i>PNAS</i>. (Weather task: about 50% to 65% over 50 trials.)</a></li>
        <li><a href="https://synapsesocial.com/papers/W1979455727">Knowlton, B. J., Mangels, J. A., &amp; Squire, L. R. (1996). A neostriatal habit learning system in humans. <i>Science</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/12009178/">Beilock, S. L., Carr, T. H., MacMahon, C., &amp; Starkes, J. L. (2002). When paying attention becomes counterproductive. <i>Journal of Experimental Psychology: Applied</i>.</a></li>
        <li><a href="https://website.education.wisc.edu/~mnathan/Publications_files/2004_Nathan_PME2004_TPDforBeliefChange.pdf">Nathan, M. J. (2004), summarizing Nathan &amp; Koedinger (2000): 76% of 67 high-school teachers expected equations to be easiest.</a></li>
        <li><a href="https://website.education.wisc.edu/~mnathan/Publications_files/2001_NathanEtAl_ICCS_EBS.pdf">Nathan, M. J., Koedinger, K. R., &amp; Alibali, M. W. (2001). Expert blind spot: When content knowledge eclipses pedagogical content knowledge.</a></li>
        <li><a href="https://core.ac.uk/display/79899049">Nathan, M. J., &amp; Petrosino, A. (2003). Expert blind spot among preservice teachers. <i>American Educational Research Journal</i>.</a></li>''',
quiz='''[
 {q:'What did H.M. show by improving at mirror tracing?',o:['A skill can be learned without remembering the learning','Practice doesn’t help people with amnesia','The hippocampus stores skills'],a:0,f:'He got better over three days but never remembered practising.'},
 {q:'Patients with Parkinson’s disease, in the weather task:',o:['Remembered the session but didn’t learn the task','Learned the task but forgot the session','Did both normally'],a:0,f:'Amnesic patients showed the reverse pattern.'},
 {q:'What is the expert blind spot?',o:['Experts misjudge what novices will find hard','Experts can’t see their own mistakes','Experts learn more slowly'],a:0,f:'Teachers with more maths training expected equations to be easiest; for students they were hardest.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
const med=a=>{const s=[...a].sort((x,y)=>x-y),m=s.length>>1;return s.length?(s.length%2?s[m]:(s[m-1]+s[m])/2):0};
/* ---------- weather prediction ----------
   4 cards; chance of rain given each card = 0.8, 0.6, 0.4, 0.2, assigned to the symbols at random.
   Each round shows 1-3 cards; chance of rain = mean of the shown cards' values; outcome drawn from it.
   Best guess = the outcome with chance > 0.5 (rounds at exactly 0.5 are not scored).
   60 rounds in 3 blocks of 20; then 4 questions: does each card mostly mean rain or sun? */
const CARDS=[['●','circle'],['■','square'],['◆','diamond'],['▲','triangle']];
let wr=null;
function wDraw(set){$('wCards').innerHTML=CARDS.map((c,i)=>set&&set.includes(i)?`<div class="wcard on"><b aria-hidden="true">${c[0]}</b><small>${c[1]}</small></div>`:`<div class="wcard" aria-hidden="true"></div>`).join('');
 $('wCards').setAttribute('aria-label',set?'Cards: '+set.map(i=>CARDS[i][1]).join(', '):'')}
wDraw(null);
function wChoose(){return new Promise(res=>{wr.res=res;$('wKeys').hidden=false;if(wr.kb)$('wRain').focus()})}
const wPick=v=>{if(!wr||!wr.res)return;const r=wr.res;wr.res=null;r(v)};
$('wRain').addEventListener('click',()=>wPick(1));$('wSun').addEventListener('click',()=>wPick(0));
addEventListener('keydown',e=>{if(!wr||!wr.res||e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;const k=e.key.toLowerCase();if(k==='r'){e.preventDefault();wPick(1)}else if(k==='s'){e.preventDefault();wPick(0)}});
function wWait(label){return new Promise(res=>{const b=$('wGo');b.textContent=label;b.disabled=false;b.focus();b.onclick=()=>{b.onclick=null;b.disabled=true;b.textContent='In progress';res()}})}
$('wGo').addEventListener('click',async e=>{if(wr||$('wGo').onclick)return;wr={kb:e.detail===0};const g=$('wGo');g.disabled=true;g.textContent='In progress';$('wRes').innerHTML='';$('wQ').hidden=true;
 const P=shuf([0.8,0.6,0.4,0.2]);const best=[[],[],[]];let lastRain=0;
 const sets=[];for(let m=1;m<15;m++){const s=[0,1,2,3].filter(i=>m>>i&1);if(s.length<4)sets.push(s)}
 for(let t=0;t<60;t++){const blk=Math.floor(t/20);$('wPhase').textContent=`Block ${blk+1} of 3`;$('wTitle').textContent='Rain or sun?';$('wText').textContent='Go with your gut. You’ll learn from the outcome.';
  const s=sets[Math.floor(Math.random()*sets.length)];const p=s.reduce((x,i)=>x+P[i],0)/s.length;
  wDraw(s);$('wFb').textContent='';$('wProg').textContent=`Round ${t+1} of 60`;
  const c=await wChoose();if(!wr)return;$('wKeys').hidden=true;
  const rain=Math.random()<p;if(blk===2&&c===1)lastRain++;if(Math.abs(p-0.5)>1e-9)best[blk].push(c===(p>0.5?1:0));
  $('wFb').innerHTML=`${rain?'Rain':'Sun'}. <span class="${c===(rain?1:0)?'ok':'no'}">${c===(rain?1:0)?'You were right.':'You guessed '+(c?'rain':'sun')+'.'}</span>`;
  await sw(1100);if(!wr)return}
 wDraw(null);$('wFb').textContent='';$('wProg').textContent='Done.';
 $('wPhase').textContent='Four questions';$('wTitle').textContent='What did each card mean?';$('wText').textContent='For each card on its own, was the weather mostly rain or mostly sun?';
 $('wQ').innerHTML=CARDS.map((c,i)=>`<fieldset><legend>${c[0]} ${c[1]}</legend><label><input type="radio" name="wq${i}" value="1">Mostly rain</label><label><input type="radio" name="wq${i}" value="0">Mostly sun</label></fieldset>`).join('');
 $('wQ').hidden=false;$('wQ').querySelector('input').focus();
 await wWait('Check my answers');if(!wr)return;
 let ex=0,ans=0;CARDS.forEach((c,i)=>{const s=document.querySelector(`input[name="wq${i}"]:checked`);if(s){ans++;if(+s.value===(P[i]>0.5?1:0))ex++}});
 $('wQ').hidden=true;$('wPhase').textContent='Your results';
 const pc=a=>a.length?Math.round(100*a.filter(Boolean).length/a.length):0;const b=best.map(pc);
 const row=(l,n,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${n}%;background:${c}"></i></div><b>${n}%</b></div>`;
 const key=CARDS.map((c,i)=>`${c[1]}, ${P[i]>0.5?'rain':'sun'} ${Math.round((P[i]>0.5?P[i]:1-P[i])*100)}% of the time`).join('; ');
 $('wRes').innerHTML=`<div class="res wl2">${row('Rounds 1–20',b[0],'#C9D3E3')}${row('Rounds 21–40',b[1],'#7DB8FF')}${row('Rounds 41–60',b[2],'#FCB316')}${row('Card questions',ex*25,'#FF8A3D')}</div><p class="mtext">On its own, each card meant: ${key}.</p>`;
 const exTxt=`You answered ${ex} of 4 card questions correctly${ans<4?` (${4-ans} left blank)`:''}.`;
 let title,text;
 const one=Math.max(lastRain,20-lastRain);
 if(one>=18){title='Mostly one answer';text=`In the last block you chose ${lastRain>=10?'rain':'sun'} in ${one} of 20 rounds. Always giving the same answer scores whatever share of rounds happened to favour it, so these numbers can’t show learning. ${exTxt} Try again, and let each set of cards guide your guess.`}
 else if(b[2]>=70&&ex===4){title='You learned it, and you can say why';text=`Your best-guess rate was ${b[2]}% in the last block. ${exTxt} Many people find that their choices improve before they can explain the rule. In the 1996 study, amnesic patients learned the task normally while barely remembering the training.`}
 else if(b[2]>=70){title='You learned more than you can say';text=`Your best-guess rate was ${b[2]}% in the last block, but you got only ${ex} of 4 card questions right${ans<4?` (${4-ans} left blank)`:''}. Your choices picked up the pattern before you could put it into words: habit-like learning, built up slowly from feedback.`}
 else if(b[2]>=60){title='Starting to learn';text=`Your best-guess rate was ${b[0]}%, ${b[1]}% and ${b[2]}% across the three blocks. ${exTxt} In studies, people rise from about 50% to about 65% over 50 rounds. This kind of learning is gradual.`}
 else{title='Still close to chance';text=`Your best-guess rate was ${b[0]}%, ${b[1]}% and ${b[2]}% across the three blocks; 50% is guessing. ${exTxt} This task is hard and slow: in studies, people reach only about 65% after 50 rounds, and chance outcomes can hide a good strategy.`}
 $('wTitle').textContent=title;$('wText').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();wr=null});

/* ---------- can you stop reading? (spatial Stroop) ----------
   36 rounds: 12 matching (LEFT on left / RIGHT on right), 12 clashing, 12 neutral (####), random order.
   Fixation 500-900 ms, then the word in one box. Response: side. Median correct-response time per kind. */
let sr=null;
function sResp(side){if(!sr||!sr.wait)return;const r=sr.wait;sr.wait=null;r(side)}
$('sBox').addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(k==='f'||e.key==='ArrowLeft'){e.preventDefault();sResp(0)}else if(k==='j'||e.key==='ArrowRight'){e.preventDefault();sResp(1)}});
$('sL').addEventListener('pointerdown',()=>sResp(0));$('sR').addEventListener('pointerdown',()=>sResp(1));
$('sGo').addEventListener('click',async()=>{sr={};$('sGo').hidden=true;$('sRes').innerHTML='';$('sBox').focus();
 const T=shuf([...Array(12).fill('C'),...Array(12).fill('I'),...Array(12).fill('N')]);const R={C:[],I:[],N:[]},E={C:0,I:0,N:0};
 $('sMsg').textContent='Get ready…';await sw(1200);if(!sr)return;
 for(let i=0;i<36;i++){const k=T[i],side=Math.random()<0.5?0:1;const word=k==='N'?'####':(k==='C'?(side?'RIGHT':'LEFT'):(side?'LEFT':'RIGHT'));
  $('sL').textContent='';$('sR').textContent='';$('sFx').textContent='+';$('sMsg').textContent=`Round ${i+1} of 36`;
  await sw(500+Math.random()*400);if(!sr)return;$('sFx').textContent='';
  $(side?'sR':'sL').textContent=word;const t0=performance.now();
  const r=await new Promise(res=>{sr.wait=res;sr.to=setTimeout(()=>{if(sr&&sr.wait){sr.wait=null;res(-1)}},2500)});if(!sr)return;clearTimeout(sr.to);
  const rt=performance.now()-t0;
  if(r===side)R[k].push(rt);else{E[k]++;$('sMsg').textContent=r<0?'Too slow. Next one.':'Other side. Next one.';await sw(600);if(!sr)return}}
 $('sL').textContent='';$('sR').textContent='';$('sFx').textContent='';$('sMsg').textContent='Done.';
 const mN=med(R.N),mC=med(R.C),mI=med(R.I),mx=Math.max(mN,mC,mI)||1,f=x=>Math.round(x);
 const row=(l,m,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${m/mx*100}%;background:${c}"></i></div><b>${f(m)} ms</b></div>`;
 const d=mI-mC;const errs=E.C+E.I+E.N?` Mistakes or misses: ${E.C} when the word matched its side, ${E.I} when it clashed, ${E.N} with ####.`:'';
 let head,body;
 if(R.C.length<4||R.I.length<4){head='Too few correct answers to compare';body=`Most rounds were missed or went to the wrong side.${errs} Try again, pressing the side the word is on, as quickly as you can.`}
 else if(d>=30){head='Reading got in the way';body=`You took about ${f(mC)} ms when the word matched its side and ${f(mI)} ms when it clashed: ${f(d)} ms slower.${errs} You were told to ignore the word, but you read it anyway. That is what automatic means: fast, effortless, and hard to switch off. A child just learning to read wouldn’t show this.`}
 else if(d>-30){head='Little interference this time';body=`You took about ${f(mC)} ms when the word matched its side and ${f(mI)} ms when it clashed.${errs} Some people learn to look only at the position, and with 12 rounds of each, small effects can hide in the noise. The classic version, naming the ink colour of colour words, usually shows a clear slowdown.`}
 else{head='The clashing words were faster this time';body=`You took about ${f(mC)} ms when the word matched its side and ${f(mI)} ms when it clashed.${errs} With only 12 rounds of each, chance plays a part. In studies, clashing words usually slow people down, because reading runs on its own.`}
 $('sRes').innerHTML=`${R.C.length<4||R.I.length<4?'':`<div class="lres">${row('#### (no word)',mN,'#8FA3C2')}${row('Word matches side',mC,'#13294B')}${row('Word clashes',mI,'#B84300')}</div>`}<p class="pmsg"><b class="h">${head}</b>${body}</p>`;
 $('sGo').hidden=false;$('sGo').textContent='Try again';$('sGo').focus();sr=null});
''')
open('lb09/template.html','w').write(page(o))
