import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a04',n='4',label='The Learning Brain · Generative AI · Topic 4',epi='The Learning Brain, Generative AI, episode 4',
title='Crutch or Tutor: How AI Practice Can Help or Harm Learning',h1='Crutch or tutor',em='Producing the answer is what teaches',read='7',mins='2 minutes',vtitle='Crutch or tutor',
dek='With AI in hand, students did far better in practice. Take it away, and those who had used a standard chatbot did worse than students who never had it. A tutor that gave hints did not.',
jumps='<span><a href="#eT">Predict the exam</a></span><span><a href="#bT">Crutch or tutor?</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:42ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>Nearly a thousand high-school students in Turkey practised maths with one of two AI tutors, or with no AI at all. One tutor was a standard chat interface, like ChatGPT. The other was prompted to give hints, not answers. Hamsa Bastani and colleagues reported the results in 2025.</p>
    <p>During practice, both tutors helped a lot. Then the AI was taken away for the exam.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~1,000</strong><span>high-school maths students in a field experiment</span></div>
      <div role="listitem"><strong>+48%</strong><span>in practice with a standard chat, and +127% with the hint-giving tutor</span></div>
      <div role="listitem"><strong>−17%</strong><span>on the exam without AI, for students who had practised with the standard chat</span></div>
      <div role="listitem"><strong>About the same</strong><span>as students who never had AI, for those who had the hint-giving tutor</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="eT">
    <div class="col">
      <h2 class="sec" id="eT"><span class="n">Try it</span>Predict the exam</h2>
      <p>Three quick predictions about the study, then see the results. About 1 minute.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="eScreen">
          <p class="qq" id="eQ" aria-live="polite">Press Start.</p>
          <div class="jb" id="eB" hidden role="group" aria-label="Your prediction"></div>
          <p class="gfb" id="eFb" aria-live="polite"></p>
          <p class="prog" id="eProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="ePhase">Ready</p>
          <p class="mtitle" id="eTitle">Practice, then the exam</p>
          <p class="mtext" id="eText" aria-live="polite">Each group is compared with students who practised without AI.</p>
          <div id="eRes"></div>
          <div class="mrow"><button class="nbtn" id="eGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Why</span>A crutch skips the effort that builds skill</h2>
    <p>The logs suggested why. Without guardrails, many students used the AI as a crutch: they asked for the answer and copied it. The effort that builds skill never happened.</p>
    <p>This is the testing and generation effects from Series 2, run in reverse. Retrieving and generating answers build lasting memories because they take effort. Getting the answer is easy. Producing it is what teaches.</p>
  </div>

'''+cls_html('bT','Crutch or tutor?','Ten ways a student might use an AI while practising. For each, decide: is the AI doing the thinking (a crutch), or making the student do it (a tutor)? You’ll get feedback after each one.',[('C','Crutch','the AI does the thinking'),('T','Tutor','the student does the thinking')],'Crutch or tutor?','Crutch or tutor?','The question is always: who produced the answer?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>One school, one subject</h2>
    <p>This was one school and one subject, covering about 15% of the curriculum, with a model from 2023, and the students were in high school, not university. And the hint-giving tutor prevented the harm, but it did not raise exam scores.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Make students do the climbing</h3>
      <p>If students use AI in practice, give them a tutor that hints rather than solves. Grade the process, not just the answer. And always include some practice without AI, so you and they can see what they can do alone.</p>
    </aside>
  </div>
''',
tips_h='Only producing the answer builds the skill',
tips='''      <li><b>A tutor that hints</b><span>Not one that solves.</span></li>
      <li><b>Grade the process</b><span>Not just the answer.</span></li>
      <li><b>Some practice without AI</b><span>So everyone can see what students can do alone.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1073/pnas.2422633122">Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., &amp; Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. <i>Proceedings of the National Academy of Sciences, 122</i>(26), e2422633122.</a></li>''',
quiz='''[
 {q:'During practice, students with the standard chat…',o:['Did better than students without AI','Did worse','Did the same'],a:0,f:'Scores rose by 48%; with the hint-giving tutor, by 127%.'},
 {q:'On the exam without AI, students who had practised with the standard chat…',o:['Scored 17% lower than students who never had AI','Scored higher','Scored the same'],a:0,f:'Many had used the AI as a crutch, copying answers.'},
 {q:'What did the hint-giving tutor do for exam scores?',o:['Prevented the harm, but did not raise them','Raised them by 127%','Lowered them'],a:0,f:'Students scored about the same as those who never had AI.'}]''',
js=BASE+r'''
/* ---------- predict the exam ----------
   3 predictions, each with 3 options. Then the results as bars relative to the no-AI group (100). */
const EQ=[
 ['During practice, which tutor raised scores more?',['The standard chat','The hint-giving tutor','About the same'],1,'The hint-giving tutor: +127%, against +48% for the standard chat.'],
 ['On the exam without AI, students who had practised with the standard chat scored…',['Higher than the no-AI group','About the same','Lower'],2,'Lower: 17% below students who never had AI.'],
 ['And students who had practised with the hint-giving tutor scored…',['Higher than the no-AI group','About the same','Lower'],1,'About the same as students who never had AI.']];
let er=null;
function eChoose(opts){return new Promise(res=>{er.res=res;const b=$('eB');b.innerHTML=opts.map((t,j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${j}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('eB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!er||!er.res)return;const r=er.res;er.res=null;$('eB').hidden=true;r(+b.dataset.v)});
function eNext(label){return new Promise(res=>{const g=$('eGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('eGo').addEventListener('click',async()=>{if(er||$('eGo').onclick)return;er={};const g=$('eGo');g.disabled=true;g.textContent='In progress';$('eRes').innerHTML='';
 const got=[];$('ePhase').textContent='Predict';$('eTitle').textContent='Your prediction';$('eText').textContent='Pick one answer.';
 for(let i=0;i<3;i++){const [q,o,a,ex]=EQ[i];$('eProg').textContent=`Prediction ${i+1} of 3`;$('eQ').textContent=q;$('eFb').textContent='';
  const c=await eChoose(o);if(!er)return;got.push(c===a);
  $('eFb').innerHTML=(c===a?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex;
  if(i<2){await eNext('Next prediction');if(!er)return}}
 $('eQ').textContent='Done.';$('eProg').textContent='';$('ePhase').textContent='The results';
 $('eRes').innerHTML=`<div class="res wl2"><p class="gh">Practice, with AI (no-AI group = 100)</p>${barRow('No AI',100,230,'100','#C9D3E3')}${barRow('Standard chat',148,230,'+48%','#FCB316')}${barRow('Hint-giving tutor',227,230,'+127%','#7DD3A8')}<p class="gh">Exam, without AI</p>${barRow('No AI',100,230,'100','#C9D3E3')}${barRow('Standard chat',83,230,'−17%','#FCB316')}${barRow('Hint-giving tutor',100,230,'about the same','#7DD3A8')}</div>`;
 const n=got.filter(Boolean).length;let title,text;
 if(!got[1]){title='The harm is the surprise';text=`You got ${n} of 3. It is easy to expect AI practice to help, or at worst do nothing. But the students who had used the standard chat did worse on their own than students who never had AI. Doing well in practice is not the same as learning.`}
 else if(n===3){title='You saw it coming';text='All 3 right. Practice scores rose with both tutors, but only the students who had to produce their own answers kept up once the AI was gone. Doing well in practice is not the same as learning.'}
 else if(!got[0]){title='Hints helped more in practice, too';text=`You got ${n} of 3. Holding back the answer did not hurt practice scores: the hint-giving tutor raised scores more than the standard chat. And on the exam, it did no harm.`}
 else{title='Hints prevented harm, but no more';text=`You got ${n} of 3. Students from the hint-giving tutor scored about the same as students who never had AI. It protected learning, but this time it did not add to it.`}
 $('eTitle').textContent=title;$('eText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();er=null});
'''+cls_js("{C:'Crutch',T:'Tutor'}",'''[
 ['“Solve question 4 for me.”','C','Crutch: the AI produces the answer, so the student skips the effort that builds the skill.'],
 ['“I got 12 but the key says 15. Point to the step where my working went wrong, but don’t fix it.”','T','Tutor: the student did the work, and now has to find and fix the error themselves.'],
 ['“Give me a hint for the first step only.”','T','Tutor: a hint leaves the student to do the rest of the thinking.'],
 ['Pasting in the whole worksheet and copying the answers back out','C','Crutch: this is what many students did with the standard chat, and they scored lower on the exam.'],
 ['“Quiz me on these formulas, and don’t show the answer until I’ve tried.”','T','Tutor: this is retrieval practice, with the AI holding the answers back.'],
 ['Asking for the full solution as soon as a problem looks hard','C','Crutch: the struggle is where the learning happens. Try first, then ask for a hint.'],
 ['Asking the AI to explain an answer, reading it, nodding, and moving on','C','Crutch: reading an explanation feels like understanding, but the student produced nothing. Try a similar problem alone next.'],
 ['“I think x = 3. Tell me only whether it’s right.”','T','Tutor: the student produced the answer, and gets quick feedback on it.'],
 ['Reading a worked example, then trying a similar problem alone','T','Tutor: the example shows the method, and the student then has to produce it.'],
 ['Asking the AI to write the steps of a proof the student will be examined on','C','Crutch: the student is meant to learn to produce those steps.']]''','Crutch or tutor?',r'''
 if(right>=9){title='You can tell them apart';text=`${right} of 10 right. The test is simple: who produced the answer? If the student did, the AI is a tutor. If the AI did, it’s a crutch.`}
 else if(right>=6){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. Ask: who produced the answer? Reading an AI’s explanation can feel like learning, but only producing it teaches.`}
 else{title='Worth another look';text=`${right} of 10 right. Ask, each time: who produced the answer? Hints, quizzes and checks of the student’s own work are tutoring. Answers to copy are a crutch.`}'''))
open('a04/template.html','w').write(page(o))
