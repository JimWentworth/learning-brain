import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb04',n='4',title='The Power of Prediction: Learning from the Gap',h1='The power of prediction',em='Learning from the gap',read='8',mins='2 minutes',vtitle='The power of prediction',
dek='Your brain is always guessing what comes next. When the guess is wrong, the gap between expected and actual is the signal that drives learning. Once something is fully predicted, there is nothing left to learn.',
jumps='<span><a href="#rwT">Nothing left to learn</a></span><span><a href="#pdT">Predict, then see</a></span>',
hero_aria='Drawing of the brain with two areas glowing orange and labelled: the visual cortex at the back, where predictions shape what we see, and the midbrain dopamine area, deep in the brain, whose cells signal prediction errors about reward.',
hero_js="BR.R.v1.lab=[960,-60];BR.R.v1.al='right';BR.R.vta.lab=[360,720];BR.R.vta.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.52,cy:H*0.44,s:fitS(W,H,1.32),t,active:['v1','vta'],labels:['v1','vta'],labelT:{v1:0.8,vta:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.rwset{display:grid;gap:12px;margin:0 0 14px}
.rwset fieldset{border:0;margin:0;padding:0}
.rwset legend{font-size:16px;font-weight:700;color:#fff;margin-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{display:flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border:2px solid #8FA3C2;border-radius:22px;color:#fff;font-weight:700;font-size:16px;cursor:pointer}
.chips input{width:20px;height:20px;accent-color:#FF5F05}
@media (min-width:901px){.rwlab{grid-template-columns:minmax(0,1.5fr) minmax(260px,1fr)}}
#rwC{width:100%;max-width:640px;height:auto;aspect-ratio:600/420;display:block}
.demo{border-top:1px solid var(--rule);padding:18px 0}
.demo:first-child{border-top:0;padding-top:0}
.demo h3{font-family:var(--display);font-size:22px;margin:0 0 6px}
.demo canvas{width:100%;max-width:560px;height:auto;aspect-ratio:600/300;display:block;background:#F3F6FA;border-radius:8px;margin:10px 0}
.demo fieldset{border:0;margin:0;padding:0}
.demo legend{font-weight:700;font-size:17px;margin-bottom:8px}
.demo .opts2{display:flex;flex-wrap:wrap;gap:8px}
.demo .opts2 label{display:flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border:2px solid #5A6B82;border-radius:22px;font-weight:700;font-size:16px;cursor:pointer}
.demo .opts2 input{width:20px;height:20px;accent-color:#13294B}
.demo .ex{font-size:17px;line-height:1.5;margin:10px 0 0}
.demo .ex b.y{color:#1F5C3F}.demo .ex b.n{color:#A3262F}''',
body='''  <div class="col lede">
    <p>Watch a ball roll toward the edge of a table. Before it falls, you have already pictured where it will land. The brain doesn’t just take in the world. It is constantly guessing what comes next.</p>
    <p>One influential theory, predictive coding, says perception works this way. In a 1999 model of the visual cortex, Rajesh Rao and Dana Ballard proposed that higher areas send predictions down to lower ones, and only the residual error, the part the prediction got wrong, travels back up. Whether the whole brain works like this is still debated. But in one place, the evidence for prediction errors is strong: learning from reward.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1972</strong><span>the Rescorla–Wagner model: learning in proportion to surprise</span></div>
      <div role="listitem"><strong>1999</strong><span>the Rao–Ballard model of prediction in the visual cortex</span></div>
      <div role="listitem"><strong>3 ways</strong><span>to present a classroom demo: not at all, just watch, or predict first</span></div>
      <div role="listitem"><strong>0</strong><span>left to learn once the outcome is fully predicted</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>Cells that signal surprise</h2>
    <p>In monkeys, dopamine cells in the midbrain fire when juice arrives unexpectedly. After the monkey learns that a light comes first, the cells fire at the light instead and barely respond to the juice. And if the expected juice never comes, they go quiet at the moment it was due. They signal the difference between what was expected and what happened (see <a href="@@LB:rew@@">The reward system</a>).</p>
    <h2 class="sec"><span class="n">The rule</span>Learning in proportion to error</h2>
    <p>Decades before those recordings, in 1972, Robert Rescorla and Allan Wagner proposed a model of classical conditioning built on the same idea. On each trial, how much an animal learns depends on how surprising the outcome was. A big error makes a big update. A small error makes a small one. When the outcome is fully predicted, the error is zero, and nothing more is learned.</p>
    <p>The model explained a puzzle Leon Kamin had found: blocking. If an animal has already learned that a light means food, adding a tone alongside the light teaches it almost nothing about the tone. The food is no longer a surprise.</p>
  </div>

  <section class="night" aria-labelledby="rwT">
    <div class="col">
      <h2 class="sec" id="rwT"><span class="n">Try it</span>Nothing left to learn</h2>
      <p>Train a simulated animal with the Rescorla–Wagner rule. First it sees a light followed by food. Then it sees the light and a tone together, followed by food. How much will it learn about the tone? Make a prediction, then run it.</p>
    </div>
    <div class="wide">
      <div class="lab rwlab">
        <div class="mscreen"><canvas id="rwC" width="600" height="420" role="img" aria-label="Chart of how strongly the animal expects food from the light and from the tone, trial by trial."></canvas><p class="prog" id="rwProg" aria-live="polite">Choose the settings, make a prediction, then press Run.</p></div>
        <div>
          <div class="rwset">
            <fieldset><legend>Stage 1: light, then food, how many times?</legend><div class="chips">
              <label><input type="radio" name="rwN" value="0">None</label><label><input type="radio" name="rwN" value="2">2</label><label><input type="radio" name="rwN" value="15" checked>15</label></div></fieldset>
            <fieldset><legend>Stage 2 is always 10 trials of light + tone, then food. Afterwards, how strongly will the tone alone predict food?</legend><div class="chips">
              <label><input type="radio" name="rwP" value="hi">Strongly</label><label><input type="radio" name="rwP" value="mid">Somewhat</label><label><input type="radio" name="rwP" value="lo">Hardly at all</label></div></fieldset>
          </div>
          <div class="mrow"><button class="nbtn" id="rwGo">Run</button></div>
          <p class="mtext" id="rwText" aria-live="polite" style="margin-top:14px"></p>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">In the classroom</span>Watching isn’t enough</h2>
    <p>Prediction errors aren’t just for animals learning about food. In 2004, Catherine Crouch, Adam Fagen, Paul Callan and Eric Mazur compared ways of running physics demonstrations in a large Harvard course. Students who simply watched a demonstration and heard it explained understood the underlying concept no better than students who never saw it at all. Students who first predicted the outcome showed significantly greater understanding.</p>
    <p>A prediction gives the brain something to be wrong about. Without one, the result of a demonstration is just one more thing to see.</p>
  </div>

  <section aria-labelledby="pdT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="pdT"><span class="n">Try it</span>Predict, then see</h2>
      <p>Three classic physics questions. Commit to a prediction for each, then run the demonstration.</p>
    </div>
    <div class="wide"><div class="lbox" id="pdBox"></div><p class="pmsg" id="pdSum" aria-live="polite"></p></div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Some caution</span>Strong evidence, open theory</h2>
    <p>The evidence for reward prediction errors in dopamine cells is strong. The idea that the whole brain runs on prediction is still a theory, and an actively debated one. And the classroom gains from predicting were real, but modest.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Ask for a guess</h3>
      <p>Before you reveal a result, a demonstration, a worked problem or the answer to a question, have learners commit to a prediction, ideally in writing. A wrong guess isn’t wasted. It’s the signal that tells the brain to update.</p>
    </aside>
  </div>
''',
tips_h='The brain learns from the gap',
tips='''      <li><b>Predict first</b><span>Have learners commit to a prediction before any demonstration or reveal.</span></li>
      <li><b>Write it down</b><span>A written guess is harder to quietly revise after the fact.</span></li>
      <li><b>Value the miss</b><span>A wrong prediction is where the learning signal is biggest.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/10195184/">Rao, R. P. N., &amp; Ballard, D. H. (1999). Predictive coding in the visual cortex. <i>Nature Neuroscience</i>.</a></li>
        <li><a href="https://www.its.caltech.edu/~jkenny/nb250c/papers/Schultz-1997.pdf">Schultz, W., Dayan, P., &amp; Montague, P. R. (1997). A neural substrate of prediction and reward. <i>Science</i>.</a></li>
        <li><a href="https://brainhealth.rutgers.edu/wp-content/uploads/2022/04/CH18_Gluck_Bowerbook2007.pdf">Gluck &amp; Bower: Rescorla and Wagner’s (1972) error-correction model of classical conditioning.</a></li>
        <li><a href="https://gershmanlab.opalstacked.com/textbook/chapter10.pdf">Gershman: the Rescorla–Wagner model and Kamin blocking.</a></li>
        <li><a href="https://works.swarthmore.edu/fac-physics/203">Crouch, C. H., Fagen, A. P., Callan, J. P., &amp; Mazur, E. (2004). Classroom demonstrations: learning tools or entertainment? <i>American Journal of Physics</i>.</a></li>''',
quiz='''[
 {q:'In the Rescorla–Wagner model, what decides how much is learned on a trial?',o:['How surprising the outcome was','How many trials there have been','How strong the light is'],a:0,f:'Big error, big update. No error, no update.'},
 {q:'An animal already knows a light means food. Then a tone is added alongside the light. What does it learn about the tone?',o:['Almost nothing','As much as about the light','More than about the light'],a:0,f:'This is blocking: the food is already predicted, so there is no error to drive learning.'},
 {q:'In the physics course, which students understood the demonstrations better?',o:['Those who predicted the outcome first','Those who just watched','Neither: all groups were the same'],a:0,f:'Watching alone did no better than not seeing the demonstration at all.'}]''',
js=r'''
/* ---------- nothing left to learn (Rescorla–Wagner) ----------
   Rate 0.3, maximum 1. Stage 1: N trials of light -> food (N = 0, 2 or 15). Stage 2: 10 trials of light + tone -> food.
   Each trial: error = 1 - (sum of strengths of cues present); each present cue gains 0.3 x error.
   Tone result: under 0.2 = "hardly at all", 0.2-0.7 = "somewhat", over 0.7 = "strongly". */
const RC=$('rwC'),RX=RC.getContext('2d');let rwRun=null;
function rwSim(N){let L=0,T=0;const h=[];for(let i=0;i<N;i++){const e=1-L;L+=0.3*e;h.push({L,T,e,st:1})}for(let i=0;i<10;i++){const e=1-(L+T);L+=0.3*e;T+=0.3*e;h.push({L,T,e,st:2})}return h}
function rwDraw(h,n,N){const W=600,H=420,l=70,t=40,pw=510,ph=250;RX.clearRect(0,0,W,H);RX.font='600 24px '+BODY;
 RX.strokeStyle='#3A4E72';RX.lineWidth=1;for(let v=0;v<=1.001;v+=0.5){const y=t+ph-v*ph;RX.beginPath();RX.moveTo(l,y);RX.lineTo(l+pw,y);RX.stroke();RX.fillStyle='#C9D3E3';RX.textAlign='right';RX.fillText(v.toFixed(1),l-8,y+8)}
 const tot=N+10,xw=pw/tot,X=i=>l+xw*(i+0.5);
 if(N>0){RX.fillStyle='rgba(233,238,246,0.06)';RX.fillRect(l,t,xw*N,ph)}
 RX.fillStyle='#C9D3E3';RX.textAlign='center';if(N>2)RX.fillText('Stage 1',l+xw*N/2,t+ph+32);RX.fillText('Stage 2',l+xw*(N+5),t+ph+32);
 RX.textAlign='left';RX.fillText('Expected food',l,t-12);
 for(let i=0;i<n;i++){const s=h[i];RX.fillStyle='rgba(252,179,22,0.55)';const eh=Math.max(0,s.e)*ph;RX.fillRect(X(i)-xw*0.35,t+ph-eh,xw*0.7,eh)}
 const line=(k,col)=>{RX.strokeStyle=col;RX.lineWidth=4;RX.beginPath();let st=false;for(let i=0;i<n;i++){const v=h[i][k];if(k==='T'&&h[i].st===1)continue;const x=X(i),y=t+ph-v*ph;st?RX.lineTo(x,y):RX.moveTo(x,y);st=true}RX.stroke()};
 line('L','#7DB8FF');line('T','#FF8A3D');
 RX.font='700 24px '+BODY;RX.fillStyle='#7DB8FF';RX.fillText('— Light',l,t+ph+76);RX.fillStyle='#FF8A3D';RX.fillText('— Tone',l+150,t+ph+76);RX.fillStyle='#FCB316';RX.fillText('▮ Error',l+290,t+ph+76)}
rwDraw([],0,15);
$('rwGo').addEventListener('click',()=>{const N=+document.querySelector('input[name="rwN"]:checked').value;const pSel=document.querySelector('input[name="rwP"]:checked');
 if(!pSel){$('rwText').textContent='First, make a prediction about the tone.';return}
 const h=rwSim(N),T=h[h.length-1].T,L=h[h.length-1].L,cat=T<0.2?'lo':T<=0.7?'mid':'hi',lab={lo:'hardly at all',mid:'somewhat',hi:'strongly'};
 $('rwGo').disabled=true;document.querySelectorAll('.rwset input').forEach(i=>i.disabled=true);let n=0;const me=Symbol();rwRun=me;
 const finish=()=>{rwDraw(h,h.length,N);const ok=pSel.value===cat;
  let why;if(N===0)why=`With no first stage, light and tone were learned together and split the credit: each ended near ${T.toFixed(2)}.`;
  else why=`After ${N} light-only trials, the light already predicted the food at ${h[N-1].L.toFixed(2)}, so the stage 2 errors were small (the first was ${h[N].e.toFixed(2)}). The tone gained only ${T.toFixed(2)}. That’s blocking: with little surprise left, there was little to learn.`;
  $('rwText').innerHTML=`<b>${ok?'Your prediction was right.':'Not what you predicted.'}</b> The tone alone predicts food ${lab[cat]} (${T.toFixed(2)} out of 1). ${why}${ok?'':' A wrong prediction is exactly where learning starts.'} Try another stage 1 setting.`;
  $('rwProg').textContent=`Done: light ${L.toFixed(2)}, tone ${T.toFixed(2)}.`;$('rwGo').disabled=false;document.querySelectorAll('.rwset input').forEach(i=>i.disabled=false)};
 if(RM){finish();return}
 const step=()=>{if(rwRun!==me)return;n++;rwDraw(h,n,N);$('rwProg').textContent=`Trial ${n} of ${h.length}`;if(n<h.length)setTimeout(step,140);else finish()};step()});

/* ---------- predict, then see ---------- */
const DEMOS=[
 {id:'tube',t:'The curved tube',q:'A ball rolls fast through a curved tube lying flat on a table, seen from above. Which path does it take after it leaves the tube?',o:['It keeps curving','It goes in a straight line','It curves the other way'],a:1,ex:'Once it leaves the tube, nothing pushes it sideways any more, so it moves in a straight line in the direction it was going at the exit. A common intuition says objects “remember” curved motion, but they don’t.'},
 {id:'cart',t:'The moving cart',q:'A cart moves to the right at a steady speed and drops a ball. Ignoring air, where does the ball land?',o:['Behind the point where it was dropped','Exactly below where it was dropped','Ahead of the drop point, below the cart'],a:2,ex:'The ball keeps the cart’s sideways speed as it falls, so it stays under the cart and lands ahead of the drop point. Many people expect it to fall straight down, or to drift behind.'},
 {id:'drop',t:'Heavy and light',q:'A 1 kg ball and a 10 kg ball are dropped together from the same height, with no air. Which lands first?',o:['The heavy one','They land together','The light one'],a:1,ex:'Without air, all objects fall with the same acceleration, so they land together. In real air, very light objects like a feather fall more slowly because of air resistance, not because they weigh less.'}];
const box2=$('pdBox');const pdState={};
box2.innerHTML=DEMOS.map((d,i)=>`<div class="demo" id="dm_${d.id}"><h3>${i+1}. ${d.t}</h3><canvas width="600" height="300" id="dc_${d.id}" role="img" aria-label="${d.t}: demonstration, before it runs."></canvas><fieldset><legend>${d.q}</legend><div class="opts2">${d.o.map((o,j)=>`<label><input type="radio" name="dp_${d.id}" value="${j}">${o}</label>`).join('')}</div></fieldset><div class="qrow"><button class="pbtn" id="db_${d.id}">Run it</button></div><p class="ex" id="dx_${d.id}" aria-live="polite"></p></div>`).join('');
function pdFrame(d,p){const c=$('dc_'+d.id),g=c.getContext('2d');g.clearRect(0,0,600,300);g.font='600 24px '+BODY;g.textAlign='center';
 const ball=(x,y,r,col)=>{g.fillStyle=col;g.beginPath();g.arc(x,y,r,0,7);g.fill()};
 if(d.id==='tube'){g.lineCap='butt';g.strokeStyle='#5A6B82';g.lineWidth=30;g.beginPath();g.arc(300,300,220,Math.PI,1.5*Math.PI);g.stroke();g.strokeStyle='#F3F6FA';g.lineWidth=20;g.beginPath();g.arc(300,300,220,Math.PI,1.5*Math.PI);g.stroke();
  g.fillStyle='#3D4A5C';g.fillText('Seen from above',460,250);
  let x,y;if(p<=0.55){const a=Math.PI+(p/0.55)*0.5*Math.PI;x=300+Math.cos(a)*220;y=300+Math.sin(a)*220}else{x=300+(p-0.55)/0.45*270;y=80}
  if(p>0.55){g.setLineDash([8,8]);g.strokeStyle='#B84300';g.lineWidth=3;g.beginPath();g.moveTo(300,80);g.lineTo(x,y);g.stroke();g.setLineDash([])}
  ball(x,y,11,'#B84300')}
 else if(d.id==='cart'){p=p*0.75;g.strokeStyle='#5A6B82';g.lineWidth=3;g.beginPath();g.moveTo(10,272);g.lineTo(590,272);g.stroke();
  const cx=p=>40+420*p+45;const cxx=cx(p);g.fillStyle='#13294B';g.fillRect(cxx-45,222,90,36);ball(cxx-28,262,9,'#5A6B82');ball(cxx+28,262,9,'#5A6B82');g.fillRect(cxx-3,90,6,132);
  const xd=cx(0.25);if(p>=0.25){g.setLineDash([6,6]);g.strokeStyle='#5A6B82';g.lineWidth=2;g.beginPath();g.moveTo(xd,80);g.lineTo(xd,272);g.stroke();g.setLineDash([]);g.fillStyle='#3D4A5C';g.fillText('drop point',xd-60,140)}
  let bx,by;if(p<0.25){bx=cxx;by=80}else if(p<0.75){const q=(p-0.25)/0.5;bx=cxx;by=80+(260-80)*q*q}else{bx=cx(0.75);by=260}
  ball(bx,by,11,'#B84300');g.fillStyle='#3D4A5C';g.fillText('→',cxx+70,245)}
 else{g.strokeStyle='#5A6B82';g.lineWidth=3;g.beginPath();g.moveTo(60,272);g.lineTo(540,272);g.stroke();
  const y=40+(272-22-40)*Math.min(1,p)*Math.min(1,p);ball(220,Math.min(y+10,260),12,'#5A6B82');ball(380,Math.min(y,250),22,'#13294B');
  g.fillStyle='#3D4A5C';g.fillText('1 kg',160,Math.min(y+18,268));g.fillText('10 kg',460,Math.min(y+10,262));g.fillText('No air',300,30)}}
let pdDone=0,pdRight=0;
DEMOS.forEach(d=>{pdFrame(d,0);$('db_'+d.id).addEventListener('click',()=>{const sel=document.querySelector(`input[name="dp_${d.id}"]:checked`);
 if(!sel){$('dx_'+d.id).textContent='Choose a prediction first.';return}
 $('db_'+d.id).disabled=true;document.querySelectorAll(`input[name="dp_${d.id}"]`).forEach(i=>i.disabled=true);$('dx_'+d.id).textContent='';
 const done=()=>{pdFrame(d,1);const ok=+sel.value===d.a;pdDone++;if(ok)pdRight++;
  $('dc_'+d.id).setAttribute('aria-label',`${d.t}: result. ${d.o[d.a]}.`);
  $('dx_'+d.id).innerHTML=`<b class="${ok?'y':'n'}">${ok?'Your prediction was right.':'Not what you predicted.'}</b> Answer: ${d.o[d.a].toLowerCase()}. ${d.ex}`;
  if(pdDone===DEMOS.length)$('pdSum').textContent=pdRight===DEMOS.length?'You predicted all three correctly. Notice how a correct prediction felt: confirming, with little surprise.':`You predicted ${pdRight} of 3 correctly. The ones you got wrong are the ones most likely to stick, because the gap between your guess and the result is the learning signal.`};
 if(RM){done();return}const t0=performance.now();const tick=now=>{const p=Math.min(1,(now-t0)/2200);pdFrame(d,p);if(p<1)requestAnimationFrame(tick);else done()};requestAnimationFrame(tick)})});
''')
open('lb04/template.html','w').write(page(o))
