import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a07',n='7',label='The Learning Brain · Generative AI · Topic 7',epi='The Learning Brain, Generative AI, episode 7',
title='Automation Bias: Why Even Experts Follow a Wrong Machine',h1='Automation bias',em='Practise disagreeing',read='7',mins='2 minutes',vtitle='Automation bias',
dek='When an AI suggestion was deliberately wrong, radiologists reading mammograms followed it, and the most experienced were not immune. Committing to your own answer first is a defence we can teach.',
jumps='<span><a href="#dT">Which side has more?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the occipital lobe, at the back, where vision is processed, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.occ.lab=[900,760];BR.R.occ.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','occ'],labels:['pfc','occ'],labelT:{pfc:0.8,occ:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.ai{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:10px 14px;max-width:42ch;width:100%;margin:0;color:#E9EEF6;font-size:18px;line-height:1.45;text-align:center}
.ai b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:2px}
.ai[hidden]{display:none}
.dpair{display:flex;gap:14px;justify-content:center;width:100%}
.dpair figure{margin:0;text-align:center}
.dpair figcaption{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-top:4px}
.dpair svg{width:min(150px,38vw);height:min(150px,38vw);background:#0F2240;border:1px solid #3A4E72;border-radius:10px;display:block}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>Twenty-seven radiologists read 50 mammograms, each with a rating suggested by what they were told was an AI system. In 12 of the cases, the suggestion was deliberately wrong. Thomas Dratsch and colleagues reported the results in 2023.</p>
    <p>When the AI was right, all three experience groups were about 80% accurate. When it was wrong, inexperienced readers fell to about 20%, moderately experienced readers to about 25%, and even very experienced readers, with more than 15 years on average, to about 45%.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>27</strong><span>radiologists reading 50 mammograms with a purported AI</span></div>
      <div role="listitem"><strong>12</strong><span>cases where the AI’s suggestion was deliberately wrong</span></div>
      <div role="listitem"><strong>~80%</strong><span>accurate, in every group, when the AI was right</span></div>
      <div role="listitem"><strong>~20% to ~45%</strong><span>accurate when it was wrong, from least to most experienced</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Automation bias</span>The pull of the machine’s answer</h2>
    <p>This is automation bias: the pull to accept a machine’s answer over your own judgement. It shows up in two ways: acting on a wrong suggestion, and failing to notice what the system missed.</p>
    <p>It is a shortcut. Checking takes effort, and a confident suggestion lowers the felt need to check. Expertise helps, but it does not make anyone immune.</p>
  </div>

  <section class="night" aria-labelledby="dT">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Which side has more?</h2>
      <p>Two boxes of dots flash for one second. Which has more? A simulated assistant gives its answer too, and it is sometimes wrong. In the first round you see its answer first. In the second, you commit to your own answer first, then see the assistant’s and decide whether to change. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="dScreen">
          <p class="ai" id="dA" hidden aria-live="polite"></p>
          <div class="dpair" aria-hidden="true"><figure><svg id="dL" viewBox="0 0 150 150"></svg><figcaption>Left</figcaption></figure><figure><svg id="dR" viewBox="0 0 150 150"></svg><figcaption>Right</figcaption></figure></div>
          <p class="qq" id="dQ" aria-live="polite">Press Start.</p>
          <div class="jb" id="dB" hidden role="group" aria-label="Your answer"></div>
          <p class="prog" id="dProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="dPhase">Ready</p>
          <p class="mtitle" id="dTitle">Two rounds of 8</p>
          <p class="mtext" id="dText" aria-live="polite">Round 1: assistant first. Round 2: you first. The dots are not described for screen readers, so this activity needs sight.</p>
          <div id="dRes"></div>
          <div class="mrow"><button class="nbtn" id="dGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Safeguards</span>Training, feedback, and AI as a second check</h2>
    <p>An editorial alongside the study suggested safeguards: training; accountability, with regular feedback on performance; transparent and validated systems; and AI that runs in the background as a second check, rather than speaking first.</p>
    <h2 class="sec"><span class="n">A caution</span>One experiment, decades of evidence</h2>
    <p>This was one experiment, with a purported AI and a small number of readers. But automation bias itself has been studied for decades, from aviation to medicine.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Teach students to disagree</h3>
      <p>Have students commit to their own answer before they see the AI’s. Seed some AI suggestions with deliberate errors, and debrief who caught them. And give feedback on how often students overrode the AI when they should have.</p>
    </aside>
  </div>
''',
tips_h='Expertise does not switch off automation bias',
tips='''      <li><b>Commit first</b><span>Students answer before they see the AI’s answer.</span></li>
      <li><b>Seed errors</b><span>And debrief who caught them.</span></li>
      <li><b>Feedback on overrides</b><span>How often did they disagree when they should have?</span></li>''',
sources='''        <li><a href="https://doi.org/10.1148/radiol.222176">Dratsch, T., Chen, X., Rezazade Mehrizi, M., et al. (2023). Automation bias in mammography: The impact of artificial intelligence BI-RADS suggestions on reader performance. <i>Radiology, 307</i>(4), e222176.</a></li>''',
quiz='''[
 {q:'When the purported AI was wrong, very experienced radiologists…',o:['Fell to about 45% accuracy','Stayed at about 80%','Fell to 0%'],a:0,f:'Less experienced readers fell further, to about 20%.'},
 {q:'Automation bias shows up as…',o:['Acting on a wrong suggestion, and missing what the system missed','Refusing to use machines','Checking everything twice'],a:0,f:'A confident suggestion lowers the felt need to check.'},
 {q:'Which is a defence we can teach?',o:['Committing to your own answer before seeing the AI’s','More experience alone','Hiding the AI’s confidence'],a:0,f:'Expertise helps, but it does not make anyone immune.'}]''',
js=BASE+r'''
/* ---------- which side has more? ----------
   Two rounds of 8 trials. Dots flash for 1 s (counts differ by 4 to 6). The simulated assistant is wrong on 2 trials per round.
   Round 1: assistant's answer shown first, then dots, then you choose.
   Round 2: dots, you commit, then the assistant's answer; if it disagrees, keep or switch. */
const NS='http://www.w3.org/2000/svg';
function dots(svg,n){svg.innerHTML='';const pts=[];let tries=0;while(pts.length<n&&tries<5000){tries++;const x=10+Math.random()*130,y=10+Math.random()*130;if(pts.every(([a,b])=>(a-x)**2+(b-y)**2>130))pts.push([x,y])}
 pts.forEach(([x,y])=>{const c=document.createElementNS(NS,'circle');c.setAttribute('cx',x.toFixed(1));c.setAttribute('cy',y.toFixed(1));c.setAttribute('r','4');c.setAttribute('fill','#FCB316');svg.appendChild(c)})}
const clr=()=>{$('dL').innerHTML='';$('dR').innerHTML=''};
let dr=null;
const wait=ms=>new Promise(r=>{dr.tm=setTimeout(r,ms)});
function dChoose(opts){return new Promise(res=>{dr.res=res;const b=$('dB');b.innerHTML=opts.map(([k,t],j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${k}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('dB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!dr||!dr.res)return;const r=dr.res;dr.res=null;$('dB').hidden=true;r(b.dataset.v)});
function dNext(label){return new Promise(res=>{const g=$('dGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
function trials(){const wrong=shuf([1,2,3,4,5,6,7]).slice(0,2);return Array.from({length:8},(_,i)=>{const lo=20+Math.floor(Math.random()*6),d=4+Math.floor(Math.random()*3),more=Math.random()<.5?'L':'R';return{nL:more==='L'?lo+d:lo,nR:more==='R'?lo+d:lo,more,ai:wrong.includes(i)?(more==='L'?'R':'L'):more}})}
const side=k=>k==='L'?'Left':'Right';
const LR=[['L','Left has more'],['R','Right has more']];
$('dGo').addEventListener('click',async()=>{if(dr||$('dGo').onclick)return;dr={};const g=$('dGo');g.disabled=true;g.textContent='In progress';$('dRes').innerHTML='';
 const R=[{okR:0,nR:0,okW:0,folW:0},{okR:0,nR:0,okW:0,folW:0,first:0,toWrong:0,toRight:0}];
 for(let r=0;r<2;r++){
  $('dPhase').textContent=r?'Round 2: you first':'Round 1: assistant first';$('dTitle').textContent=r?'Commit, then compare':'The assistant speaks first';
  $('dText').textContent=r?'Pick your answer before you see the assistant’s.':'Read the assistant’s answer, then watch the dots.';
  if(r===1){$('dQ').textContent='Round 2: you’ll answer first, then see the assistant’s answer.';$('dA').hidden=true;clr();await dNext('Start round 2');if(!dr)return}
  const T=trials();
  for(let i=0;i<8;i++){const t=T[i];$('dProg').textContent=`Round ${r+1}, trial ${i+1} of 8`;clr();$('dA').hidden=true;
   if(r===0){$('dA').innerHTML=`<b>Assistant</b>${side(t.ai)} has more.`;$('dA').hidden=false;$('dQ').textContent='Get ready…';await wait(1500);if(!dr)return}
   else{$('dQ').textContent='Get ready…';await wait(800);if(!dr)return}
   dots($('dL'),t.nL);dots($('dR'),t.nR);$('dQ').textContent='Look!';await wait(1000);if(!dr)return;clr();
   $('dQ').textContent='Which side had more dots?';let c=await dChoose(LR);if(!dr)return;
   if(r===1){if(c===t.more)R[1].first++;
    $('dA').innerHTML=`<b>Assistant</b>${side(t.ai)} has more.`;$('dA').hidden=false;
    if(c!==t.ai){$('dQ').textContent=`You said ${side(c).toLowerCase()}. The assistant disagrees.`;const k=await dChoose([['K','Keep my answer'],['S','Switch to the assistant’s']]);if(!dr)return;
     if(k==='S'){if(c===t.more)R[1].toWrong++;else R[1].toRight++;c=t.ai}}
    else{$('dQ').textContent='The assistant agrees with you.';await wait(900);if(!dr)return}}
   const ok=c===t.more,aiOk=t.ai===t.more;
   if(aiOk){R[r].nR++;if(ok)R[r].okR++}else{if(ok)R[r].okW++;if(c===t.ai)R[r].folW++}}}
 clr();$('dA').hidden=true;$('dQ').textContent='Done.';$('dProg').textContent='';$('dPhase').textContent='Your results';
 const [a,b]=R;
 $('dRes').innerHTML=`<div class="res wl2"><p class="gh">Round 1: assistant first</p>${barRow('Assistant right',a.okR,6,a.okR+' of 6','#7DD3A8')}${barRow('Assistant wrong',a.okW,2,a.okW+' of 2','#FFB38A')}<p class="gh">Round 2: you first</p>${barRow('Assistant right',b.okR,6,b.okR+' of 6','#7DD3A8')}${barRow('Assistant wrong',b.okW,2,b.okW+' of 2','#FFB38A')}</div>`;
 let title,text;
 const sw=b.toWrong?` In round 2 you changed ${b.toWrong===1?'a right answer to the assistant’s wrong one':b.toWrong+' right answers to the assistant’s wrong ones'}.`:'';
 if(a.folW>b.folW){title='Committing first helped';text=`With the assistant first, you went with ${a.folW===2?'both of its wrong answers':'one of its 2 wrong answers'}. Committing first, you went with ${b.folW===0?'none':'one'}.`+sw+' Your own answer gave you something to compare against.'}
 else if(a.folW===2&&b.folW===2){title='The pull is strong';text='You went with the assistant’s wrong answer every time, in both rounds.'+sw+' On a hard, fast judgement, a confident suggestion is very persuasive. That is automation bias.'}
 else if(a.folW===0&&b.folW===0){title='You held your ground';text=`You didn’t follow any of the assistant’s wrong answers. You were right ${a.okR+b.okR} of 12 times when it was right.`+sw+' In the study, even very experienced radiologists followed wrong suggestions more than half the time.'}
 else if(b.folW>a.folW){title='No benefit this time';text=`With the assistant first, you went with ${a.folW===0?'none':'one'} of its 2 wrong answers; committing first, with ${b.folW===2?'both':'one'}.`+sw+' With only 2 wrong answers a round, chance plays a big part. Changing your answer to match a confident machine is exactly the pull the study measured.'}
 else{title='The same in both rounds';text=`You went with one of the assistant’s 2 wrong answers in each round.`+sw+' With so few trials, chance plays a big part. Try again: the dots change each time.'}
 $('dTitle').textContent=title;$('dText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();dr=null});
'''+grid('''[
 ['Radiologists’ accuracy when the purported AI was right',['About 80%, in every experience group','About 50%','Close to 100%'],0,'Dratsch and colleagues, 2023.'],
 ['Inexperienced readers, when the AI was wrong',['About 20%','About 60%','About 80%'],0,'They followed the wrong suggestion most of the time.'],
 ['Very experienced readers, when the AI was wrong',['About 45%','About 80%','About 20%'],0,'Expertise helps, but it does not make anyone immune.'],
 ['Automation bias shows up as…',['Acting on a wrong suggestion, and missing what the system missed','Ignoring every suggestion','Working more slowly'],0,'Two kinds of error.'],
 ['One safeguard suggested in the editorial',['AI that runs in the background as a second check','Hiding the AI from experts','Removing feedback'],0,'Along with training, feedback and validated systems.'],
 ['How long has automation bias been studied?',['Decades, from aviation to medicine','Only since 2022','It hasn’t been'],0,'This study is new; the bias is not.']]''','The pattern: a confident machine pulls everyone toward its answer, experts included. Committing first and practising disagreement are the defences.'))
open('a07/template.html','w').write(page(o))
