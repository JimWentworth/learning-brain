import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a06',n='6',label='The Learning Brain · Generative AI · Topic 6',epi='The Learning Brain, Generative AI, episode 6',
title='Confident and Wrong: How AI Inflates Our Sense of Knowing',h1='Confident and wrong',em='Fluency is not understanding',read='7',mins='2 minutes',vtitle='Confident and wrong',
dek='With an AI assistant, people solved more reasoning problems, and thought they had solved even more. Judging your own accuracy is a skill, and AI can quietly switch it off.',
jumps='<span><a href="#cT">How sure are you?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0}
.ai{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;max-width:42ch;width:100%;margin:0;color:#E9EEF6;font-size:18px;line-height:1.45}
.ai b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin-bottom:4px}
.ai[hidden]{display:none}
.copts{display:grid;gap:8px;width:100%;max-width:520px}
.copts[hidden]{display:none}
.copts button{min-height:48px;padding:10px 14px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:600 17px/1.35 var(--body);text-align:left;cursor:pointer}
.copts button:hover{border-color:#FCB316}
.copts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.copts button[aria-pressed="true"]{border-color:#FCB316;background:#22375C}
.copts button:disabled:not([aria-pressed="true"]){opacity:.6;border-color:#8FA3C2;cursor:default}
.cconf{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;width:100%;max-width:520px}
@media (max-width:520px){.cconf{grid-template-columns:1fr}}
.cconf[hidden]{display:none}
.cconf button{min-height:48px;padding:8px 10px;border-radius:10px;border:2px solid #FCB316;background:transparent;color:#fff;font:700 16px/1.3 var(--body);cursor:pointer}
.cconf button small{display:block;font:500 13px var(--body);color:#C9D3E3}
.cconf button:focus-visible{outline:3px solid #fff;outline-offset:2px}
.clab{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin:0}
.clab[hidden]{display:none}
.rlist{margin:8px 0 14px;padding-left:20px;color:#E9EEF6;font-size:16px;line-height:1.5}
.rlist .ok{color:#7DD3A8}.rlist .no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Two hundred and forty-six people solved 20 logical-reasoning problems from the Law School Admission Test (LSAT), with an AI assistant. Their scores went up by about 3 points over a norm group. But they thought they had done about 4 points better than they actually did. Daniela Fernandes, Robin Welsch and colleagues reported this in 2026.</p>
    <p>Normally on this kind of task, the weakest performers overestimate themselves the most. That is the Dunning–Kruger pattern. With AI, it disappeared: everyone overestimated, by about the same amount.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>246</strong><span>people solving 20 LSAT reasoning problems with AI</span></div>
      <div role="listitem"><strong>+3 points</strong><span>in scores, against a norm group without AI</span></div>
      <div role="listitem"><strong>+4 points</strong><span>more than that, in how well they thought they had done</span></div>
      <div role="listitem"><strong>452</strong><span>people in a second study, which found the same pattern</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>How sure are you?</h2>
      <p>Eight short reasoning puzzles, each with an assistant’s answer. The answers were written for this page, not produced by a real AI, and some may be wrong. Pick your answer, then say how sure you are. You’ll see how you did at the end, not before. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
          <p class="qq" id="cQ" aria-live="polite">Press Start.</p>
          <p class="ai" id="cA" hidden></p>
          <div class="copts" id="cO" hidden role="group" aria-label="Your answer"></div>
          <p class="clab" id="cL" hidden>How sure are you?</p>
          <div class="cconf" id="cC" hidden role="group" aria-label="How sure are you?"><button type="button" data-c="0">Guessing<small>about 1 in 3</small></button><button type="button" data-c="1">Fairly sure<small>about 7 in 10</small></button><button type="button" data-c="2">Certain<small>no doubt</small></button></div>
          <p class="prog" id="cProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="cPhase">Ready</p>
          <p class="mtitle" id="cTitle">Answer, then rate</p>
          <p class="mtext" id="cText" aria-live="polite">At the end, you’ll see how many you expected to get right, and how many you did.</p>
          <div id="cRes"></div>
          <div class="mrow"><button class="nbtn" id="cGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Know-how</span>More AI literacy, less self-accuracy</h2>
    <p>People who knew more about how AI works were more confident, but less accurate about their own performance. That is the opposite of what you might expect.</p>
    <h2 class="sec"><span class="n">One prompt, no check</span>No feedback, no correction</h2>
    <p>Most people sent a single prompt per question and accepted the answer. Without testing the reasoning, they got no feedback on where they were wrong. And people working with the AI did not beat the AI working alone.</p>
    <h2 class="sec"><span class="n">Metacognition</span>Fluent answers feel like understanding</h2>
    <p>This is the metacognition problem from Series 1, sharpened. Our feeling of knowing tracks how fluent something feels, not how accurate it is. A smooth, confident answer feels like understanding. Judging your own accuracy is a skill, and AI can quietly switch it off.</p>
    <h2 class="sec"><span class="n">A caution</span>Puzzles, one model, online samples</h2>
    <p>These are reasoning puzzles, with one model, in online samples. But they fit a wider finding about fluency and the feeling of knowing.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Make reflection a routine</h3>
      <p>Before students see an AI answer, have them predict their confidence, then check. Ask them to explain the AI’s reasoning back, or find one flaw in it. On some tasks, grade calibration, not just correctness. And make it a routine, not a one-off.</p>
    </aside>
  </div>
''',
tips_h='AI can make students smarter on the task. Only reflection makes them wiser about it.',
tips='''      <li><b>Predict, then check</b><span>Confidence first, then the answer.</span></li>
      <li><b>Explain it back</b><span>Or find one flaw in the AI’s reasoning.</span></li>
      <li><b>Grade calibration</b><span>On some tasks, not just correctness.</span></li>''',
sources='''        <li><a href="https://arxiv.org/abs/2409.16708">Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., &amp; Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. <i>Computers in Human Behavior</i>. Preprint: arXiv:2409.16708.</a></li>''',
quiz='''[
 {q:'With an AI assistant, people’s scores on LSAT reasoning problems…',o:['Went up, but they thought they had done even better','Went down','Went up, and they judged them accurately'],a:0,f:'About 3 points up, and they overestimated by about 4 more.'},
 {q:'What happened to the Dunning–Kruger pattern with AI?',o:['It disappeared: everyone overestimated by about the same','It got stronger','Nothing changed'],a:0,f:'Normally the weakest overestimate most.'},
 {q:'People who knew more about how AI works were…',o:['More confident, but less accurate about themselves','Better calibrated','Less confident'],a:0,f:'The opposite of what you might expect.'}]''',
js=BASE+r'''
/* ---------- how sure are you? ----------
   8 puzzles, 3 options each, with a simulated assistant answer (3 of 8 wrong). Pick an answer, then a confidence.
   No feedback until the end: expected (sum of confidence) vs actual, and what happened where the assistant was wrong. */
const CQ=[
 ['All roses are flowers. Some flowers fade quickly. Does it follow that some roses fade quickly?','Yes. Roses are flowers, and some flowers fade quickly, so some roses must fade quickly.',['Yes, it follows','No, it doesn’t follow','It follows for most roses'],1,0,'No. The flowers that fade quickly might not include any roses.'],
 ['If it rains, the match is cancelled. The match was cancelled. Did it rain?','Not necessarily. The match could have been cancelled for another reason.',['Yes, it must have','Not necessarily','No, it can’t have'],1,1,'Not necessarily.'],
 ['Linda studied philosophy and campaigns for social justice. Which is more likely?','That she is a bank teller. Two things together can never be more likely than one of them alone.',['She is a bank teller','She is a bank teller and active in a feminist group','Both are equally likely'],0,0,'She is a bank teller. Adding a second condition can only make it less likely.'],
 ['A shirt costs $40 after a 20% discount. What was the price before the discount?','$48. Add the 20% back: 40 + 8 = 48.',['$48','$50','$60'],1,0,'$50. 20% off $50 is $10, leaving $40. The 20% is of the original price, not of $40.'],
 ['Every student in the class passed the test. Sam did not pass. What follows?','Sam is not in the class.',['Sam is not in the class','Sam missed the test','Nothing follows'],0,0,'Sam is not in the class.'],
 ['A train leaves at 10:50 and the trip takes 1 hour 25 minutes. When does it arrive?','12:15. 10:50 plus 1 hour is 11:50, and 25 minutes more is 12:15.',['12:05','12:15','12:25'],1,1,'12:15.'],
 ['No cats are dogs. Some pets are cats. Which must be true?','No pets are dogs. Cats can’t be dogs, and pets are cats, so pets can’t be dogs.',['Some pets are not dogs','No pets are dogs','Some dogs are not pets'],0,1,'Some pets are not dogs: the pets that are cats. Nothing says other pets can’t be dogs.'],
 ['Halve a number, then add 10, and you get 16. What was the number?','12. Half of 12 is 6, and 6 + 10 is 16.',['3','12','13'],1,1,'12.']];
/* each: [question, assistant text, options, correct index, assistant index, explanation]; CQ[i][4]!==CQ[i][3] means the assistant is wrong */
const CV=[1/3,0.7,1],CN=['Guessing','Fairly sure','Certain'];
let cr=null;
function cPick(opts){return new Promise(res=>{cr.res=res;const o=$('cO');o.innerHTML=opts.map(([t,j])=>`<button type="button" data-j="${j}" aria-pressed="false">${t}</button>`).join('');o.hidden=false;o.querySelector('button').focus()})}
$('cO').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!cr||!cr.res)return;const r=cr.res;cr.res=null;b.setAttribute('aria-pressed','true');$('cO').querySelectorAll('button').forEach(x=>x.disabled=true);r(+b.dataset.j)});
function cConf(){return new Promise(res=>{cr.cres=res;$('cL').hidden=false;const c=$('cC');c.hidden=false;c.querySelector('button').focus()})}
$('cC').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!cr||!cr.cres)return;const r=cr.cres;cr.cres=null;$('cC').hidden=true;$('cL').hidden=true;r(+b.dataset.c)});
const f1=x=>(Math.round(x*10)/10).toString();
$('cGo').addEventListener('click',async()=>{if(cr)return;cr={};const g=$('cGo');g.disabled=true;g.textContent='In progress';$('cRes').innerHTML='';
 const order=shuf([...CQ]);const log=[];
 $('cPhase').textContent='Answer and rate';$('cTitle').textContent='Your call';$('cText').textContent='No feedback until the end.';
 for(let i=0;i<8;i++){const [q,a,opts,ok,ai,ex]=order[i];$('cProg').textContent=`Puzzle ${i+1} of 8`;$('cQ').textContent=q;$('cA').innerHTML=`<b>Assistant</b>${a}`;$('cA').hidden=false;
  const pick=await cPick(shuf(opts.map((t,j)=>[t,j])));if(!cr)return;
  const conf=await cConf();if(!cr)return;$('cO').hidden=true;
  log.push({q,opts,ok,ai,ex,pick,conf,right:pick===ok,aiWrong:ai!==ok,withAI:pick===ai})}
 $('cQ').textContent='Done.';$('cA').hidden=true;$('cProg').textContent='';$('cPhase').textContent='Your results';
 const got=log.filter(x=>x.right).length,exp=log.reduce((s,x)=>s+CV[x.conf],0),diff=exp-got;
 const aw=log.filter(x=>x.aiWrong),fol=aw.filter(x=>x.withAI),folSure=fol.filter(x=>x.conf>0).length;
 $('cRes').innerHTML=`<div class="res wl2"><p class="gh">Out of 8</p>${barRow('You expected',exp,8,'about '+f1(exp),'#FCB316')}${barRow('You got right',got,8,got+' of 8','#7DD3A8')}</div><p class="gh">Your answers</p><ul class="rlist">${log.map(x=>`<li>${x.right?'<b class="ok">Right</b>':'<b class="no">Wrong</b>'} (${CN[x.conf].toLowerCase()}). ${x.q}${x.right?'':` <b>${x.ex}</b>`}${x.aiWrong?' <i>The assistant was wrong here.</i>':''}</li>`).join('')}</ul>`;
 const folTxt=fol.length?` The assistant was wrong on 3 puzzles, and you went with it on ${fol.length===1?'one':fol.length===2?'two':'all three'}${folSure?`, ${folSure===fol.length?(fol.length===1?'feeling':'each time feeling'):'sometimes feeling'} at least fairly sure`:''}. Its wrong answers sounded just as fluent as its right ones.`:' The assistant was wrong on 3 puzzles, and you didn’t follow it on any of them.';
 let title,text;
 if(diff>=1.5){title='More confident than correct';text=`You expected to get about ${f1(exp)} right, and got ${got}.`+folTxt+' Fluent answers feel like understanding. That is the gap the study found.'}
 else if(diff<=-1.5){title='More correct than confident';text=`You expected about ${f1(exp)}, and got ${got}: you did better than you thought.`+folTxt+' In the study, people with AI tended to overestimate, but underconfidence is still a gap between feeling and fact.'}
 else if(fol.length){title='Well calibrated overall';text=`You expected about ${f1(exp)} and got ${got}, which is close.`+folTxt+' Look at the confidence you gave those: calibration matters most question by question.'}
 else{title='Well calibrated, and not fooled';text=`You expected about ${f1(exp)} and got ${got}, and you didn’t go with any of the assistant’s 3 wrong answers. Most people in the study sent one prompt and accepted the answer. Checking the reasoning is what kept you accurate.`}
 $('cTitle').textContent=title;$('cText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();cr=null});
'''+grid('''[
 ['With an AI assistant, people’s scores on LSAT reasoning problems…',['Went up by about 3 points over a norm group','Went down','Didn’t change'],0,'Fernandes, Welsch and colleagues, 2026.'],
 ['How well did they think they had done?',['About 4 points better than they actually did','About right','Worse than they did'],0,'Better performance, worse self-judgement.'],
 ['Normally the weakest overestimate most. With AI…',['Everyone overestimated, by about the same amount','The weakest overestimated even more','No one overestimated'],0,'The Dunning–Kruger pattern disappeared.'],
 ['People who knew more about how AI works were…',['More confident, but less accurate about themselves','Better calibrated','Less confident'],0,'The opposite of what you might expect.'],
 ['How did most people use the AI?',['One prompt per question, then accepted the answer','Several prompts, testing the reasoning','They ignored it'],0,'So they got no feedback on where they were wrong.'],
 ['Did people working with the AI beat the AI working alone?',['No','Yes, by a lot','Yes, slightly'],0,'A second study, with 452 people, found the same pattern.']]''','The pattern: AI raised scores, but people’s sense of how well they had done rose even more. Fluency is not understanding.'))
open('a06/template.html','w').write(page(o))
