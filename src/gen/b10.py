import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b10',n='10',label='The Learning Brain · Belonging · Topic 10',epi='The Learning Brain, Belonging, episode 10',
title='Structure Is Inclusive: Active Learning Narrows Gaps',h1='Structure is inclusive',em='Structure is how care reaches every student',read='7',mins='2 minutes',vtitle='Structure is inclusive',
dek='Who gains most when a lecture course becomes active? A large analysis of college science and maths courses suggests an answer: the students most often left behind.',
jumps='<span><a href="#cT">How active is your class?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','hip'],labels:['pfc','hip'],labelT:{pfc:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.cplan{display:grid;gap:8px;width:100%;max-width:560px}
.cplan .r{display:grid;grid-template-columns:1fr 92px;gap:10px;align-items:center;border:1px solid #3A4E72;border-radius:10px;padding:6px 10px}
.cplan label{color:#E9EEF6;font-size:16px;line-height:1.35}
.cplan label small{display:block;color:#C9D3E3;font-size:13px}
.cplan input{min-height:42px;width:100%;box-sizing:border-box;font:600 17px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 8px;text-align:right}
.cplan input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}''',
body='''  <div class="col lede">
    <p>In 2020, Elli Theobald and colleagues pooled studies of undergraduate STEM courses. They compared traditional lecturing with active learning, for underrepresented and low-income students, and for everyone else. Exam data came from 15 studies and over 9,000 students. Pass rates came from 26 studies and over 44,000 students.</p>
    <p>Active learning helped everyone, and it helped underrepresented students more. On average, it narrowed the gap in exam scores by 33%, and the gap in passing rates by 45%.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>9,238</strong><span>students’ exam scores, from 15 studies</span></div>
      <div role="listitem"><strong>44,606</strong><span>students’ pass rates, from 26 studies</span></div>
      <div role="listitem"><strong>33% / 45%</strong><span>narrower gaps in exam scores and passing rates, on average</span></div>
      <div role="listitem"><strong>42% / 76%</strong><span>narrower, when students were active for at least two-thirds of class time</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Intensity</span>How much class time is active</h2>
    <p>Intensity mattered. In classes where students were actively engaged for at least two-thirds of class time, the exam gap shrank by 42%, and the passing gap by 76%.</p>
    <h2 class="sec"><span class="n">Heads and hearts</span>Practice, and a signal</h2>
    <p>The authors call their explanation “heads and hearts”. Heads: deliberate practice, with frequent problem solving and feedback. Hearts: a classroom that tells every student they belong and can succeed. Good structure delivers both.</p>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>How active is your class?</h2>
      <p>Enter the minutes of a typical class session spent on each kind of activity. The page works out the share of time students are active, and compares it with the two-thirds mark from the study. Nothing you enter leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
          <form class="cplan" id="cF">
            <div class="r"><label for="c0">Lecture<small>students listen</small></label><input id="c0" type="number" min="0" max="240" value="35" inputmode="numeric"></div>
            <div class="r"><label for="c1">Demonstration or video<small>students watch</small></label><input id="c1" type="number" min="0" max="240" value="5" inputmode="numeric"></div>
            <div class="r"><label for="c2">Problems worked individually<small>active</small></label><input id="c2" type="number" min="0" max="240" value="5" inputmode="numeric"></div>
            <div class="r"><label for="c3">Pair or group work with clear roles<small>active</small></label><input id="c3" type="number" min="0" max="240" value="5" inputmode="numeric"></div>
            <div class="r"><label for="c4">Questions with think time, then discussion<small>active</small></label><input id="c4" type="number" min="0" max="240" value="0" inputmode="numeric"></div>
          </form>
        </div>
        <div>
          <p class="phase" id="cPhase">Your class</p>
          <p class="mtitle" id="cTitle"></p>
          <p class="mtext" id="cText" aria-live="polite"></p>
          <div id="cRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Existing courses, not random classrooms</h2>
    <p>These studies compared existing courses rather than randomly assigned classrooms, and there were not many of them.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Give students frequent, low-stakes problems to work on in class. Use structured group work with clear roles. Call on students in fair, predictable ways, with time to think first. And aim for more class time active, not less.</p>
    </aside>
  </div>
''',
tips_h='Structure is not the opposite of care. Done well, structure is how care reaches every student.',
tips='''      <li><b>Frequent low-stakes problems</b><span>In class, with feedback.</span></li>
      <li><b>Structured groups</b><span>Clear roles; fair, predictable calling.</span></li>
      <li><b>More time active</b><span>Aim for two-thirds.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1073/pnas.1916903117">Theobald, E. J., Hill, M. J., Tran, E., et al. (2020). Active learning narrows achievement gaps for underrepresented students in undergraduate science, technology, engineering, and math. <i>Proceedings of the National Academy of Sciences, 117</i>(12), 6476–6483.</a></li>''',
quiz='''[
 {q:'On average, active learning narrowed the gap in passing rates by…',o:['45%','5%','100%'],a:0,f:'And the exam-score gap by 33%.'},
 {q:'When students were active for at least two-thirds of class time, the passing gap shrank by…',o:['76%','10%','33%'],a:0,f:'Intensity mattered.'},
 {q:'“Heads and hearts” means…',o:['Deliberate practice, and a signal that everyone belongs','Lecture, then exam','Grades and attendance'],a:0,f:'Good structure delivers both.'}]''',
js=BASE+r'''
/* ---------- how active is your class? ---------- */
function calc(){const v=[0,1,2,3,4].map(i=>Math.max(0,+$('c'+i).value||0));const tot=v.reduce((a,b)=>a+b,0),act=v[2]+v[3]+v[4],sh=tot?act/tot:0,pc=Math.round(sh*100);
 const need=Math.max(0,Math.ceil(tot*2/3)-act);
 $('cRes').innerHTML=`<div class="res wl2">${barRow('Time students are active',sh,1,pc+'%','#7DD3A8')}${barRow('The two-thirds mark',2/3,1,'67%','#C9D3E3')}</div>`;
 let title,text;
 if(!tot){title='Enter some minutes';text='Add the minutes for a typical session.'}
 else if(sh>=2/3){title='High-intensity active learning';text=`${pc}% of your ${tot}-minute session is active. In the study, classes at or above two-thirds narrowed the exam gap by 42% and the passing gap by 76%.`}
 else if(sh>=1/3){title='Partly active';text=`${pc}% of your ${tot}-minute session is active. On average, active learning narrowed gaps by 33% (exams) and 45% (passing). Making about ${need} more minutes active would reach two-thirds.`}
 else if(act>0){title='Mostly lecture';text=`${pc}% of your ${tot}-minute session is active. Start small: swap ${Math.min(need,10)} minutes of lecture for a problem students work in pairs, with time to think first. Making about ${need} more minutes active would reach two-thirds.`}
 else{title='All lecture';text=`None of your ${tot}-minute session is active. One short problem with think time, then a few pairs sharing, is an easy first step.`}
 $('cTitle').textContent=title;$('cText').textContent=text}
$('cF').addEventListener('input',calc);calc();
'''+grid('''[
 ['Exam data in the 2020 analysis came from about how many students?',['9,000','900','90,000'],0,'Theobald and colleagues, 2020: 15 studies.'],
 ['Did active learning help everyone, or only underrepresented students?',['Everyone, and underrepresented students more','Only underrepresented students','Only overrepresented students'],0,'It narrowed gaps by lifting everyone, some more.'],
 ['On average, the exam-score gap narrowed by…',['33%','3%','90%'],0,'And the passing gap by 45%.'],
 ['With at least two-thirds of class time active, the passing gap narrowed by…',['76%','25%','No change'],0,'And the exam gap by 42%.'],
 ['The authors’ explanation is called…',['Heads and hearts','Carrots and sticks','Nature and nurture'],0,'Deliberate practice, and a signal of belonging.'],
 ['The studies compared…',['Existing courses, not randomly assigned classrooms','Randomly assigned students','Online courses only'],0,'And there were not many of them.']]''','The pattern: active learning lifts everyone and narrows gaps, more so the more class time is active.'))
open('b10/template.html','w').write(page(o))
