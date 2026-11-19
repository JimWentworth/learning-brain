import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h04',n='4',label='The Learning Brain · Habits of the Learner · Topic 4',epi='The Learning Brain, Habits of the Learner, episode 4',
title='Exercise and the Brain: When to Move for Learning',h1='Exercise and the brain',em='Move your body; help your brain',read='7',mins='2 minutes',vtitle='Exercise and the brain',
dek='If you have ever felt clearer after a walk, you are not imagining it. Movement changes the brain, over months and within minutes. For memory, the timing matters.',
jumps='<span><a href="#eT">When should you move?</a></span><span><a href="#bT">Good move?</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:44ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>In a year-long trial with 120 older adults, reported by Kirk Erickson and colleagues in 2011, people who walked briskly three days a week grew their hippocampus, a key memory region, by about 2%. A stretching group lost about 1.4%.</p>
    <p>But those adults were in their late fifties to seventies, not students. And on the study’s memory test, both groups improved by similar amounts. So it shows the brain can change, not that a gym habit will raise your grades.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~2%</strong><span>growth of the hippocampus after a year of brisk walking, in older adults</span></div>
      <div role="listitem"><strong>79</strong><span>studies in an early meta-analysis of a single bout of exercise</span></div>
      <div role="listitem"><strong>30</strong><span>meta-analyses in a 2025 review: a small-to-medium boost to thinking</span></div>
      <div role="listitem"><strong>After</strong><span>learning, exercise helped memory more clearly than before it</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">One session</span>A small boost, within minutes</h2>
    <p>What about a single session? A 2012 meta-analysis of 79 studies, by Yu-Kai Chang and colleagues, found a small boost to thinking during and after one bout of exercise. In 2025, the same team pooled 30 meta-analyses, covering more than 18,000 people, and put the average effect at small to medium, with the largest benefits measured after exercise rather than during it.</p>
  </div>

  <section class="night" aria-labelledby="eT">
    <div class="col">
      <h2 class="sec" id="eT"><span class="n">Try it</span>When should you move?</h2>
      <p>For memory, timing matters. Predict when a single bout of exercise helped people remember most, then see what pooled studies found. About 1 minute.</p>
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
          <p class="mtitle" id="eTitle">Before, during or after?</p>
          <p class="mtext" id="eText" aria-live="polite">Two quick predictions, then the pooled results.</p>
          <div id="eRes"></div>
          <div class="mrow"><button class="nbtn" id="eGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

'''+cls_html('bT','Good move?','Eight ways a student might fit exercise around study. For each, decide: does it fit the evidence, or work against it? You’ll get feedback after each one.',[('G','Fits the evidence',''),('P','Works against it','')],'Fits the evidence or works against it?','Good move?','The question is always: when does the movement happen, relative to the learning?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Modest effects, small studies</h2>
    <p>Effects are modest and vary from study to study. Many experiments are small and run in labs. Exercise will not replace studying, but it is a cheap way to support it.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Take a brisk walk of 10 to 20 minutes before a study session. After a hard session, move again instead of scrolling. Don’t try to memorize while working out hard. And build movement into every week, not just exam week.</p>
    </aside>
  </div>
''',
tips_h='Exercise won’t replace studying. It’s a cheap way to support it.',
tips='''      <li><b>A brisk walk first</b><span>10 to 20 minutes before you study.</span></li>
      <li><b>Move again after</b><span>Instead of scrolling.</span></li>
      <li><b>Every week</b><span>Not just exam week.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1073/pnas.1015950108">Erickson, K. I., Voss, M. W., Prakash, R. S., et al. (2011). Exercise training increases size of hippocampus and improves memory. <i>Proceedings of the National Academy of Sciences, 108</i>(7), 3017–3022.</a></li>
        <li><a href="https://doi.org/10.1016/j.brainres.2012.02.068">Chang, Y.-K., Labban, J. D., Gapin, J. I., &amp; Etnier, J. L. (2012). The effects of acute exercise on cognitive performance: A meta-analysis. <i>Brain Research, 1453</i>, 87–101.</a></li>
        <li><a href="https://doi.org/10.1037/bul0000460">Chang, Y.-K., Ren, F.-F., Li, R.-H., Ai, J.-Y., Kao, S.-C., &amp; Etnier, J. L. (2025). Effects of acute exercise on cognitive function: A meta-review of 30 systematic reviews with meta-analyses. <i>Psychological Bulletin, 151</i>(2), 240–259.</a></li>
        <li><a href="https://doi.org/10.3390/brainsci9040087">Loprinzi, P. D., Blough, J., Crawford, L., Ryu, S., Zou, L., &amp; Li, H. (2019). The temporal effects of acute exercise on episodic memory function: Systematic review with meta-analysis. <i>Brain Sciences, 9</i>(4), 87.</a></li>''',
quiz='''[
 {q:'After a year of brisk walking, older adults’ hippocampus…',o:['Grew by about 2%','Shrank by about 2%','Did not change'],a:0,f:'A stretching group lost about 1.4%. But memory improved similarly in both groups.'},
 {q:'For memory, exercise in the hours after learning…',o:['Gave a clearer benefit than exercise before','Hurt memory','Made no difference'],a:0,f:'Exercise before gave a small, uncertain benefit.'},
 {q:'Exercising hard while trying to memorize…',o:['Tended to hurt','Helped most','Made no difference'],a:0,f:'Move before or after, not during.'}]''',
js=BASE+r'''
/* ---------- when should you move? ----------
   2 predictions, then bars of pooled effect sizes (Loprinzi et al., 2019):
   before learning d=0.11 (uncertain), during learning: negative, after learning (early consolidation) d=0.47. */
const EQ=[
 ['When did a single bout of exercise help memory most clearly?',['Just before learning','During learning','In the hours after learning'],2,'In the hours after learning. Exercise just before gave only a small, uncertain benefit.'],
 ['And exercising during learning, like memorizing while working out hard?',['Helped','Made no difference','Tended to hurt'],2,'It tended to hurt. Move before or after, not during.']];
let er=null;
function eChoose(opts){return new Promise(res=>{er.res=res;const b=$('eB');b.innerHTML=opts.map((t,j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${j}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('eB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!er||!er.res)return;const r=er.res;er.res=null;$('eB').hidden=true;r(+b.dataset.v)});
function eNext(label){return new Promise(res=>{const g=$('eGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('eGo').addEventListener('click',async()=>{if(er||$('eGo').onclick)return;er={};const g=$('eGo');g.disabled=true;g.textContent='In progress';$('eRes').innerHTML='';
 const got=[];$('ePhase').textContent='Predict';$('eTitle').textContent='Your prediction';$('eText').textContent='Pick one answer.';
 for(let i=0;i<2;i++){const [q,o,a,ex]=EQ[i];$('eProg').textContent=`Prediction ${i+1} of 2`;$('eQ').textContent=q;$('eFb').textContent='';
  const c=await eChoose(o);if(!er)return;got.push(c===a);
  $('eFb').innerHTML=(c===a?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex;
  if(i<1){await eNext('Next prediction');if(!er)return}}
 $('eQ').textContent='Done.';$('eProg').textContent='';$('ePhase').textContent='Pooled results';
 $('eRes').innerHTML=`<div class="res wl2"><p class="gh">Effect on memory (bigger bar = bigger benefit)</p>${barRow('Before learning',0.11,0.5,'small, uncertain','#C9D3E3')}${barRow('During learning',0.01,0.5,'tended to hurt','#FFB38A')}${barRow('After learning',0.47,0.5,'clearer benefit','#7DD3A8')}</div><p class="mtext">From a 2019 meta-analysis by Paul Loprinzi and colleagues. Vigorous exercise, and young adults, showed larger effects when the exercise came first.</p>`;
 const n=got.filter(Boolean).length;let title,text;
 if(n===2){title='You had the timing';text='Both right. After learning is the clearest window, and during learning is the one to avoid. Before learning can still help, especially vigorous exercise in young adults.'}
 else if(!got[0]){title='After, more than before';text=`You got ${n} of 2. It’s natural to guess “just before”. That helped a little, but the clearer benefit came from moving in the hours after learning, while memories were settling in.`}
 else{title='Not during';text='You got 1 of 2. Hard exercise while trying to memorize tended to hurt: the body and the memory task compete. Move before or after.'}
 $('eTitle').textContent=title;$('eText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();er=null});
'''+cls_js("{G:'Fits the evidence',P:'Works against it'}",'''[
 ['A brisk 15-minute walk, then sitting down to study','G','Fits: a short, moderate bout before learning can give a small boost.'],
 ['After a hard study session, going for a run instead of scrolling','G','Fits: moving in the hours after learning gave the clearest memory benefit.'],
 ['Reading flashcards while doing hard sprints on a treadmill','P','Works against it: exercising hard during learning tended to hurt memory.'],
 ['Cycling to class on the morning of an exam','G','Fits: moderate exercise shortly before thinking tends to help a little.'],
 ['Skipping all exercise during exam week to save time','P','Works against it: a short walk costs little and supports thinking.'],
 ['Exercising regularly across the semester, not just before exams','G','Fits: build movement into every week.'],
 ['Doing an exhausting workout and then trying to cram straight away','P','Works against it: right after very hard exercise, some kinds of thinking can suffer. Give yourself time to recover.'],
 ['Joining the gym instead of studying, expecting the gym to raise your grades','P','Works against it: exercise supports studying; it doesn’t replace it.']]''','Fits the evidence or works against it?',r'''
 if(right>=7){title='Good timing';text=`${right} of 8 right. Move before or after studying, not during, and make it a weekly habit, not a substitute for study.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. The clearest benefit came after learning; hard exercise during learning tended to hurt.`}
 else{title='Worth another look';text=`${right} of 8 right. A short walk before studying, more movement after, nothing hard during, and never instead of studying.`}''')+grid('''[
 ['After a year of brisk walking, older adults’ hippocampus…',['Grew by about 2%','Did not change','Shrank by about 1.4%'],0,'Erickson and colleagues, 2011. The stretching group lost about 1.4%.'],
 ['On the study’s memory test, the walking group…',['Improved about as much as the stretching group','Improved far more','Got worse'],0,'So it shows the brain can change, not that memory improved more.'],
 ['A single bout of exercise gave thinking…',['A small-to-medium boost on average','A large boost','No boost'],0,'Chang and colleagues, 2025: 30 meta-analyses.'],
 ['Benefits were largest when thinking was measured…',['After exercise','During exercise','A week later'],0,'From the 2025 meta-review.'],
 ['For memory, the clearest benefit came from exercise…',['In the hours after learning','Just before learning','During learning'],0,'Loprinzi and colleagues, 2019.'],
 ['Exercising during learning…',['Tended to hurt memory','Helped most','Made no difference'],0,'Don’t memorize while working out hard.']]''','The pattern: movement gives thinking a modest lift, and for memory, after learning beats before, and during is worst.'))
open('h04/template.html','w').write(page(o))
