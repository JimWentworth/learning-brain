import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b08',n='8',label='The Learning Brain · Belonging · Topic 8',epi='The Learning Brain, Belonging, episode 8',
title='First in the Family: Teaching the Hidden Curriculum',h1='First in the family',em='Don’t hide the rules of college. Teach them.',read='7',mins='2 minutes',vtitle='First in the family',
dek='First-generation college students arrive just as capable as their peers. But many have never been told the unwritten rules: what office hours are for, that asking for help is normal, how to talk to a professor.',
jumps='<span><a href="#hT">Build a hidden-curriculum handout</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','hip'],labels:['pfc','hip'],labelT:{pfc:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.aud{display:grid;gap:6px;width:100%;max-width:600px}
.aud label{display:flex;gap:10px;align-items:flex-start;padding:8px 10px;border:1px solid #3A4E72;border-radius:10px;color:#E9EEF6;font-size:16px;line-height:1.4;cursor:pointer}
.aud input{margin-top:3px;width:20px;height:20px;accent-color:#FCB316;flex:none}
.pout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:16px;line-height:1.6;margin:10px 0;white-space:pre-wrap}
.pout[hidden]{display:none}''',
body='''  <div class="col lede">
    <p>At a selective private university, Nicole Stephens, MarYam Hamedani and Mesmin Destin ran a one-hour panel for incoming students. In both versions, senior students shared stories about adjusting to college. In the “difference-education” version, they also explained how their social-class backgrounds shaped those stories. One panelist said that because their parents had not gone to college, the family could not always give the advice they needed.</p>
    <p>In the standard version, first-generation students ended the year with grades about 0.3 points lower than their peers. The difference-education panel closed that gap by 63%.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1 hour</strong><span>a student panel at the start of the year</span></div>
      <div role="listitem"><strong>0.3</strong><span>grade points: the first-generation gap after the standard panel</span></div>
      <div role="listitem"><strong>63%</strong><span>of that gap closed by the difference-education panel</span></div>
      <div role="listitem"><strong>Help seeking</strong><span>accounted for the higher grades</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why it worked</span>Asking for help felt normal</h2>
    <p>First-generation students who heard it sought out more campus resources, and that help seeking accounted for their higher grades. Hearing how people like them had struggled, and coped, made asking for help feel normal.</p>
    <p>Continuing-generation students benefited too. Students in the difference-education panel reported better well-being, engagement and social fit, and a deeper appreciation of different backgrounds.</p>
  </div>

  <section class="night" aria-labelledby="hT">
    <div class="col">
      <h2 class="sec" id="hT"><span class="n">Try it</span>Build a hidden-curriculum handout</h2>
      <p>Tick the unwritten rules you want to make explicit for your students. The page drafts a plain-language handout you can copy and edit for your course.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="hScreen">
          <form class="aud" id="hF">
            <label><input type="checkbox" value="0" checked>What office hours are for</label>
            <label><input type="checkbox" value="1" checked>Asking for help is normal, not remedial</label>
            <label><input type="checkbox" value="2">How to email a professor</label>
            <label><input type="checkbox" value="3">What the syllabus is for</label>
            <label><input type="checkbox" value="4">How to ask for an extension</label>
            <label><input type="checkbox" value="5">Tutoring and writing centres</label>
            <label><input type="checkbox" value="6">How to read a grade and feedback</label>
            <label><input type="checkbox" value="7">Study groups</label>
          </form>
          <div class="mrow" style="justify-content:center"><button class="nbtn" id="hGo" type="button">Make my handout</button><button class="nbtn ghost" id="hCopy" type="button" hidden>Copy the handout</button></div>
        </div>
        <div>
          <p class="phase" id="hPhase">Hidden curriculum</p>
          <p class="mtitle" id="hTitle">Name it, explain it</p>
          <p class="mtext" id="hText" aria-live="polite">Make help seeking routine, not remedial.</p>
          <div class="pout" id="hOut" hidden aria-live="polite"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>One university, real resources</h2>
    <p>This was one university, one cohort, and a modest sample. And it worked best where real resources existed for students to use.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Name the hidden curriculum. Explain what office hours are for, and how to use them. Share stories, yours or former students’, including what was hard. And make help seeking routine, not remedial.</p>
    </aside>
  </div>
''',
tips_h='Don’t hide the rules of college. Teach them.',
tips='''      <li><b>Name the hidden curriculum</b><span>Office hours, emails, extensions.</span></li>
      <li><b>Share real stories</b><span>Including what was hard.</span></li>
      <li><b>Help seeking is routine</b><span>Not remedial.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/0956797613518349">Stephens, N. M., Hamedani, M. G., &amp; Destin, M. (2014). Closing the social-class achievement gap: A difference-education intervention improves first-generation students’ academic performance and all students’ college transition. <i>Psychological Science, 25</i>(4), 943–953.</a></li>''',
quiz='''[
 {q:'The difference-education panel closed the first-generation grade gap by…',o:['63%','6%','100%'],a:0,f:'Stephens, Hamedani and Destin, 2014.'},
 {q:'What accounted for the higher grades?',o:['More help seeking','More study hours','Easier courses'],a:0,f:'Asking for help felt normal.'},
 {q:'The panel worked best where…',o:['Real resources existed for students to use','There were no resources','Classes were small'],a:0,f:'Teach the rules, and have the help ready.'}]''',
js=BASE+r'''
/* ---------- hidden-curriculum handout ---------- */
const HC=[['Office hours','Office hours are time I set aside for you. Come with a question, a problem you’re stuck on, or just to say hello. You don’t need to be struggling to come.'],
 ['Asking for help','Asking for help is what successful students do. It isn’t a sign that you don’t belong; it’s how people get through hard courses.'],
 ['Emailing me','Start with a greeting and your name, say which course you’re in, ask your question in a sentence or two, and say thank you. I’ll reply within [your time frame].'],
 ['The syllabus','The syllabus is the rulebook for this course: deadlines, grading and policies. When in doubt, check it first, then ask.'],
 ['Extensions','If something comes up, ask before the deadline if you can. Say briefly what happened and suggest a new date. Asking is allowed.'],
 ['Tutoring and writing centres','The tutoring and writing centres are free, and students at every level use them. [Add your campus links and hours.]'],
 ['Grades and feedback','A grade tells you where you are now, not what you can do. Read the comments first: they tell you what to change next time.'],
 ['Study groups','Study groups help almost everyone. Find two or three classmates, meet weekly, and quiz each other.']];
let htxt='';
$('hGo').addEventListener('click',()=>{const on=[...document.querySelectorAll('#hF input')].filter(x=>x.checked).map(x=>+x.value);
 if(!on.length){$('hTitle').textContent='Tick at least one';$('hText').textContent='Choose the unwritten rules to explain.';$('hOut').hidden=true;$('hCopy').hidden=true;return}
 htxt='How this course works: the unwritten rules\n\n'+on.map(i=>`${HC[i][0]}\n${HC[i][1]}`).join('\n\n');
 $('hOut').textContent=htxt;$('hOut').hidden=false;$('hCopy').hidden=false;$('hCopy').textContent='Copy the handout';
 $('hTitle').textContent=`${on.length} unwritten ${on.length===1?'rule':'rules'}, written down`;$('hText').textContent='Edit the parts in brackets, and add a line or two from your own experience, including what was hard.'});
$('hCopy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(htxt);$('hCopy').textContent='Copied'}catch(err){$('hCopy').textContent='Copy not available: select the text instead'}});
'''+grid('''[
 ['After the standard panel, first-generation students’ grades were lower by about…',['0.3 grade points','1 grade point','Nothing'],0,'Stephens, Hamedani and Destin, 2014.'],
 ['The difference-education panel closed that gap by…',['63%','10%','100%'],0,'From a one-hour panel.'],
 ['What made the difference-education panel different?',['Panelists explained how their social-class backgrounds shaped their stories','It was longer','It was online'],0,'Both panels shared stories of adjusting to college.'],
 ['The higher grades were accounted for by…',['Seeking out more campus resources','Studying alone more','Taking easier courses'],0,'Help seeking felt normal.'],
 ['Did continuing-generation students benefit?',['Yes: better well-being, engagement and social fit','No','They did worse'],0,'And more appreciation of different backgrounds.'],
 ['The panel worked best where…',['Real resources existed for students to use','Students were told not to ask for help','There was no tutoring'],0,'Teach the rules, and have the help ready.']]''','The pattern: naming how background shapes college made help seeking normal, and help seeking closed much of the gap.'))
open('b08/template.html','w').write(page(o))
