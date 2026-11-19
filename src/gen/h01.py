import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='h01',n='1',label='The Learning Brain · Habits of the Learner · Topic 1',epi='The Learning Brain, Habits of the Learner, episode 1',
title='Habits, Not Willpower: How Study Becomes Automatic',h1='Habits, not willpower',em='Willpower starts it; habits keep it going',read='7',mins='2 minutes',vtitle='Habits, not willpower',
dek='Students who get the most done lean less on willpower and more on habits: behaviours set off by a cue, like a time or a place, rather than a fresh decision each day.',
jumps='<span><a href="#cT">How long does a habit take?</a></span><span><a href="#bT">Habit or willpower?</a></span>',
hero_aria='Drawing of the side of the brain with the striatum, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.str.lab=[330,640];BR.R.str.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['str','pfc'],labels:['str','pfc'],labelT:{str:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.qq{font:600 clamp(18px,2.2vw,21px)/1.45 var(--body);color:#fff;max-width:42ch;margin:0;text-align:center}
.jb{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.jb[hidden]{display:none}
.hctl{display:grid;gap:12px;width:100%;max-width:560px}
.hctl[hidden]{display:none}
.hctl fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px;margin:0}
.hctl legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.hctl label{display:flex;gap:8px;align-items:flex-start;padding:4px 0;color:#E9EEF6;font-size:16px;line-height:1.35;cursor:pointer}
.hctl input{margin-top:3px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.hchart{width:100%;max-width:560px;height:auto;display:block}
.hchart[hidden]{display:none}
.gfb{font:600 17px/1.45 var(--body);color:#E9EEF6;min-height:1.5em;margin:0;text-align:center;max-width:44ch}
.gfb b.ok{color:#7DD3A8}.gfb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>You might think the students who get the most done simply have more willpower. The research points somewhere else. They lean less on willpower, and more on habits.</p>
    <p>A habit is a behaviour set off by a cue, like a time or a place, rather than by a fresh decision. In a study at University College London, reported by Phillippa Lally and colleagues in 2010, 96 volunteers repeated one daily behaviour after a fixed cue, such as after breakfast, for 12 weeks.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>66 days</strong><span>median time to near-full automaticity, for those whose data fit the model</span></div>
      <div role="listitem"><strong>18 to 254</strong><span>days: the range, from fastest to slowest estimate</span></div>
      <div role="listitem"><strong>1 missed day</strong><span>did not derail the process</span></div>
      <div role="listitem"><strong>23 labs</strong><span>and more than 2,000 people found almost no “willpower runs out” effect</span></div>
    </div>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>How long does a habit take?</h2>
      <p>First, a guess. Then try a simple model of habit growth: pick a behaviour and how often you do it, and see when it becomes close to automatic. The model is a sketch, set to match the study’s fastest, median and slowest estimates. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
          <p class="qq" id="cQ" aria-live="polite">Press Start.</p>
          <div class="jb" id="cB" hidden role="group" aria-label="Your guess"></div>
          <p class="gfb" id="cFb" aria-live="polite"></p>
          <form class="hctl" id="cCtl" hidden>
            <fieldset><legend>The behaviour</legend>
              <label><input type="radio" name="hk" value="18">Simple: a glass of water with lunch</label>
              <label><input type="radio" name="hk" value="66" checked>Typical: 20 minutes of study after lunch</label>
              <label><input type="radio" name="hk" value="254">Demanding: a run before breakfast</label>
            </fieldset>
            <fieldset><legend>How often</legend>
              <label><input type="radio" name="hf" value="1" checked>Every day</label>
              <label><input type="radio" name="hf" value="0.86">Miss about one day a week</label>
              <label><input type="radio" name="hf" value="0.5">About half the days</label>
            </fieldset>
          </form>
          <svg class="hchart" id="cSvg" viewBox="0 0 560 220" hidden role="img" aria-labelledby="cSvgT"><title id="cSvgT">Habit strength over days</title></svg>
          <p class="prog" id="cProg" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase" id="cPhase">Ready</p>
          <p class="mtitle" id="cTitle">Guess, then model</p>
          <p class="mtext" id="cText" aria-live="polite">How long does a new daily behaviour take to become close to automatic?</p>
          <div id="cRes"></div>
          <div class="mrow"><button class="nbtn" id="cGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Self-control</span>Resisting less, not more</h2>
    <p>So why does self-control predict good outcomes? Across six studies with more than 2,000 people, Brian Galla and Angela Duckworth at the University of Pennsylvania found that people with better self-control reported resisting temptation less often, not more. Their habits, including study habits, explained much of the link between self-control and good outcomes, such as being able to study even when it was hard.</p>
    <h2 class="sec"><span class="n">The fuel tank</span>A shaky idea</h2>
    <p>You may have heard that willpower is a tank that runs dry. Earlier studies suggested a sizeable effect. But a replication across 23 labs and more than 2,000 people found an effect close to zero. The debate goes on, so planning your day around a fuel tank is a shaky strategy.</p>
  </div>

'''+cls_html('bT','Habit or willpower?','Ten ways a student might try to study more. For each, decide: does it build a habit (a cue does the work), or lean on willpower (a fresh decision or a fight each time)? You’ll get feedback after each one.',[('H','Habit','a cue does the work'),('W','Willpower','a fresh fight each time')],'Habit or willpower?','Habit or willpower?','The question is always: what starts the behaviour, a cue or a decision?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Small study, correlations</h2>
    <p>The habit study was small, and about half the volunteers never showed a clear habit curve. The self-control findings are correlations. And more complex behaviours took longer to become automatic.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Try this</h3>
      <p>Pick one fixed time and place for study. Attach it to something you already do, like after lunch. Start small enough to manage on a bad day. And if you miss a day, simply start again tomorrow.</p>
    </aside>
  </div>
''',
tips_h='Willpower gets you started. Habits keep you going.',
tips='''      <li><b>One time, one place</b><span>The cue does the deciding.</span></li>
      <li><b>Start small</b><span>Small enough for a bad day.</span></li>
      <li><b>Missed a day?</b><span>Start again tomorrow; one miss doesn’t undo it.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1002/ejsp.674">Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., &amp; Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <i>European Journal of Social Psychology, 40</i>(6), 998–1009.</a></li>
        <li><a href="https://doi.org/10.1037/pspp0000026">Galla, B. M., &amp; Duckworth, A. L. (2015). More than resisting temptation: Beneficial habits mediate the relationship between self-control and positive life outcomes. <i>Journal of Personality and Social Psychology, 109</i>(3), 508–525.</a></li>
        <li><a href="https://doi.org/10.1177/1745691616652873">Hagger, M. S., Chatzisarantis, N. L. D., et al. (2016). A multilab preregistered replication of the ego-depletion effect. <i>Perspectives on Psychological Science, 11</i>(4), 546–573.</a></li>''',
quiz='''[
 {q:'In the UCL study, the median time to near-full automaticity was…',o:['66 days','21 days','A year'],a:0,f:'With a range from 18 to about 254 days.'},
 {q:'People with better self-control reported…',o:['Resisting temptation less often','Resisting temptation more often','No difference'],a:0,f:'Their habits explained much of the link to good outcomes.'},
 {q:'If you miss a day of a new habit…',o:['Start again tomorrow; one miss did not derail it','Start the count from zero','Give up'],a:0,f:'Very inconsistent practice is what stops a habit forming.'}]''',
js=BASE+r'''
/* ---------- how long does a habit take? ----------
   1) guess (21 days / about 2 months / it varies a lot); 2) model: A(n)=1-exp(-k n) per performed day,
   k set so 95% is reached on day D (18, 66, 254) when done every day. Missed days add nothing (no reset). */
let hr=null;
function hChoose(opts){return new Promise(res=>{hr.res=res;const b=$('cB');b.innerHTML=opts.map(([k,t],j)=>`<button class="nbtn${j?' ghost':''}" type="button" data-v="${k}">${t}</button>`).join('');b.hidden=false;b.querySelector('button').focus()})}
$('cB').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!hr||!hr.res)return;const r=hr.res;hr.res=null;$('cB').hidden=true;r(b.dataset.v)});
function sim(D,f){const k=Math.log(20)/D;let n=0,acc=0,pts=[],reach=null;for(let d=1;d<=300;d++){acc+=f;if(acc>=1-1e-9){acc-=1;n++}const A=1-Math.exp(-k*n);pts.push(A);if(reach===null&&A>=0.95)reach=d}return{pts,reach}}
function draw(){const D=+document.querySelector('input[name=hk]:checked').value,f=+document.querySelector('input[name=hf]:checked').value;const {pts,reach}=sim(D,f);
 const X=d=>40+d/300*500,Y=a=>190-a*160;let p='';pts.forEach((a,i)=>{p+=(i?'L':'M')+X(i+1).toFixed(1)+' '+Y(a).toFixed(1)});
 const w84=X(84);
 $('cSvg').innerHTML=`<title id="cSvgT">Habit strength over 300 days</title><rect x="40" y="30" width="${(w84-40).toFixed(1)}" height="160" fill="#22375C"/><text x="${(w84-4).toFixed(1)}" y="44" text-anchor="end" font-size="12" fill="#C9D3E3">the 12-week study</text>`+
  `<line x1="40" y1="190" x2="540" y2="190" stroke="#8FA3C2"/><line x1="40" y1="30" x2="40" y2="190" stroke="#8FA3C2"/><line x1="40" y1="${Y(.95)}" x2="540" y2="${Y(.95)}" stroke="#FCB316" stroke-dasharray="4 4"/><text x="536" y="${Y(.95)-5}" text-anchor="end" font-size="12" fill="#FCB316">near-automatic</text>`+
  [0,100,200,300].map(d=>`<text x="${X(d)}" y="206" text-anchor="middle" font-size="12" fill="#C9D3E3">${d}</text>`).join('')+`<text x="290" y="219" text-anchor="middle" font-size="12" fill="#C9D3E3">days</text>`+
  `<path d="${p}" fill="none" stroke="#7DD3A8" stroke-width="3"/>`+(reach?`<circle cx="${X(reach)}" cy="${Y(.95)}" r="5" fill="#FCB316"/>`:'');
 const txt=reach?`Near-automatic on about day ${reach}.`:'Not near-automatic within 300 days.';
 $('cProg').textContent=txt;
 let note;
 if(f===1)note=D===18?'A simple behaviour, done daily, got there in under three weeks: the fastest in the study.':D===66?'The median in the study: about two months, not three weeks.':'Demanding behaviours took far longer; the slowest estimate was about 254 days, well beyond the 12 weeks of the study.';
 else if(f>0.8)note=`Missing about one day a week delays it (day ${reach} here, against day ${D} when done every day), but it still gets there. In the study, one missed day did not derail the process.`;
 else note='Doing it only about half the days slows everything. In the study, people who were very inconsistent did not form habits at all, so the real picture is probably worse than this sketch.';
 $('cText').textContent=note;
 hr&&(hr.last={D,f,reach})}
$('cCtl').addEventListener('change',draw);
$('cGo').addEventListener('click',async()=>{if(hr&&hr.res)return;hr={};const g=$('cGo');g.disabled=true;g.textContent='In progress';$('cRes').innerHTML='';$('cCtl').hidden=true;$('cSvg').hidden=true;$('cProg').textContent='';
 $('cPhase').textContent='Your guess';$('cTitle').textContent='How long?';$('cText').textContent='Pick the answer closest to your guess.';$('cFb').textContent='';
 $('cQ').textContent='How long does a new daily behaviour take to become close to automatic?';
 const v=await hChoose([['21','About 3 weeks'],['66','About 2 months'],['var','It varies a lot']]);if(!hr)return;
 $('cFb').innerHTML=v==='21'?'<b class="no">That’s the popular claim,</b> but the study’s median was 66 days.':v==='66'?'<b class="ok">That’s the median,</b> 66 days. But it varied a lot: from 18 to about 254.':'<b class="ok">Right:</b> from 18 to about 254 days, with a median of 66.';
 $('cQ').textContent='Now try the model. Change the behaviour and how often you do it.';
 $('cPhase').textContent='The model';$('cTitle').textContent='Habit strength over time';
 $('cCtl').hidden=false;$('cSvg').hidden=false;draw();g.textContent='Start again';g.disabled=false;$('cCtl').querySelector('input:checked').focus()});
'''+cls_js("{H:'Habit',W:'Willpower'}",'''[
 ['Studying at the same desk, right after lunch, every weekday','H','Habit: a fixed time and place become the cue, so there’s nothing to decide.'],
 ['Leaving your phone in another room before you start','H','Habit: you change the setting once, so there’s no temptation to fight.'],
 ['After brushing your teeth each night, reviewing one page of notes','H','Habit: attached to something you already do, which acts as the cue.'],
 ['Joining a study group that always meets on Tuesdays at four','H','Habit: the fixed meeting is a cue, and other people make it easy to keep.'],
 ['Putting your flashcards on your pillow in the morning, so you see them at night','H','Habit: you set up the cue in advance.'],
 ['Keeping your phone on the desk and trying not to check it when it buzzes','W','Willpower: every buzz is a fresh fight. Move the phone instead.'],
 ['Deciding each evening whether to study tonight','W','Willpower: a fresh decision every day, which is what habits remove.'],
 ['Promising yourself you’ll try harder next week','W','Willpower: a resolution with no cue, time or place attached.'],
 ['Forcing yourself through four hours straight when you’re exhausted','W','Willpower: and hard to repeat. Start small enough to manage on a bad day.'],
 ['Waiting until you feel motivated, then studying for as long as it lasts','W','Willpower: it depends on how you feel. A cue works even when you don’t feel like it.']]''','Habit or willpower?',r'''
 if(right>=9){title='You know the difference';text=`${right} of 10 right. Habits put the work on a cue, set up in advance. Willpower puts it on a fresh decision, every time.`}
 else if(right>=6){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. Ask: what starts the behaviour, a fixed cue or a decision in the moment?`}
 else{title='Worth another look';text=`${right} of 10 right. A habit is set off by a cue, like a time, a place or something you already do. If it needs a fresh decision or a fight, it’s willpower.`}'''))
open('h01/template.html','w').write(page(o))
