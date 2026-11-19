import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b02',n='2',label='The Learning Brain · Belonging · Topic 2',epi='The Learning Brain, Belonging, episode 2',
title='Belonging at Scale: When the Message Has to Be True',h1='Belonging at scale',em='Tell students they belong; then build the course that proves it',read='7',mins='2 minutes',vtitle='Belonging at scale',
dek='A one-hour exercise that halves an achievement gap sounds almost too good to be true. So researchers tested it again, much bigger. It helped, but only where students actually had opportunities to belong.',
jumps='<span><a href="#aT">Is the message true here?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the temporal lobe, at the side, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.tem.lab=[600,770];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','tem'],labels:['pfc','tem'],labelT:{pfc:0.8,tem:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.aud{display:grid;gap:6px;width:100%;max-width:600px}
.aud label{display:flex;gap:10px;align-items:flex-start;padding:8px 10px;border:1px solid #3A4E72;border-radius:10px;color:#E9EEF6;font-size:16px;line-height:1.4;cursor:pointer}
.aud input{margin-top:3px;width:20px;height:20px;accent-color:#FCB316;flex:none}
.rlist{margin:8px 0 14px;padding-left:20px;font-size:16px;line-height:1.5}''',
body='''  <div class="col lede">
    <p>First, a follow-up of the original students, years later, by Shannon Brady and colleagues, reported better adult outcomes for the Black participants. But that was still one small group, on one campus.</p>
    <p>So in 2023, a large team led by Gregory Walton ran the exercise with 26,911 students at 22 colleges and universities. Students did it online, in one short session, before college began.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>26,911</strong><span>students at 22 colleges and universities</span></div>
      <div role="listitem"><strong>1 session</strong><span>short and online, before college began</span></div>
      <div role="listitem"><strong>749</strong><span>four-year institutions the results were estimated to generalize to</span></div>
      <div role="listitem"><strong>Only where</strong><span>students’ groups actually had opportunities to belong</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The result</span>More students completed the first year</h2>
    <p>The exercise raised the share of students who completed their first year as full-time students, especially in groups that had historically progressed at lower rates. The researchers estimated the results could generalize to 749 four-year institutions in the United States. And the online materials are freely available to colleges.</p>
    <h2 class="sec"><span class="n">The key finding</span>The message has to be true</h2>
    <p>It only worked where students’ groups actually had opportunities to belong. A message about belonging cannot create belonging that isn’t there.</p>
  </div>

  <section class="night" aria-labelledby="aT">
    <div class="col">
      <h2 class="sec" id="aT"><span class="n">Try it</span>Is the message true here?</h2>
      <p>Before you tell students they belong, check what your course offers. Tick what is already true for one of your courses. Nothing you tick leaves this page.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="aScreen">
          <form class="aud" id="aF">
            <label><input type="checkbox" value="0">Students can join a study group in the first few weeks.</label>
            <label><input type="checkbox" value="1">I learn and use students’ names.</label>
            <label><input type="checkbox" value="2">Office hours are at times students can make, and I invite students personally.</label>
            <label><input type="checkbox" value="3">Students get low-stakes feedback before the first big exam.</label>
            <label><input type="checkbox" value="4">I know who withdraws from or fails my course, and I’ve asked why.</label>
            <label><input type="checkbox" value="5">Students hear from former students, including students like them.</label>
            <label><input type="checkbox" value="6">My examples and images show the range of people who do this field.</label>
            <label><input type="checkbox" value="7">Students can tell me, anonymously, what isn’t working.</label>
          </form>
        </div>
        <div>
          <p class="phase" id="aPhase">Your course</p>
          <p class="mtitle" id="aTitle">Tick what’s true</p>
          <p class="mtext" id="aText" aria-live="polite">The belonging message works best where it is already true.</p>
          <div id="aRes"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Smaller effects are normal</h2>
    <p>The effects were smaller than in the original study. That is normal: large, careful studies usually shrink early results. And small effects, across many students, can still matter.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Share the belonging message early, before the first setbacks. Then back it up. Build study groups, learn students’ names, and hold office hours students actually use. Look at who leaves your course, and ask why.</p>
    </aside>
  </div>
''',
tips_h='Tell students they belong. Then build the course that proves it.',
tips='''      <li><b>Early, before setbacks</b><span>Share the message in week one.</span></li>
      <li><b>Back it up</b><span>Study groups, names, office hours students use.</span></li>
      <li><b>Who leaves?</b><span>Look, and ask why.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.ade4420">Walton, G. M., Murphy, M. C., Logel, C., Yeager, D. S., et al. (2023). Where and with whom does a brief social-belonging intervention promote progress in college? <i>Science, 380</i>(6644), 499–505.</a></li>
        <li><a href="https://doi.org/10.1126/sciadv.aay3689">Brady, S. T., Cohen, G. L., Jarvis, S. N., &amp; Walton, G. M. (2020). A brief social-belonging intervention in college improves adult outcomes for black Americans. <i>Science Advances, 6</i>(18), eaay3689.</a></li>
        <li><a href="https://doi.org/10.1126/science.1198364">Walton, G. M., &amp; Cohen, G. L. (2011). A brief social-belonging intervention improves academic and health outcomes of minority students. <i>Science, 331</i>(6023), 1447–1451.</a></li>''',
quiz='''[
 {q:'The 2023 study involved…',o:['26,911 students at 22 institutions','92 students on one campus','About 1,000 students'],a:0,f:'Online, in one short session, before college began.'},
 {q:'The exercise raised…',o:['The share of students completing their first year full-time','Everyone’s grades equally','Nothing'],a:0,f:'Especially in groups that had historically progressed at lower rates.'},
 {q:'Where did it work?',o:['Only where students’ groups had opportunities to belong','Everywhere equally','Only at small colleges'],a:0,f:'The message has to be true.'}]''',
js=BASE+r'''
/* ---------- is the message true here? ---------- */
const NEXT=['Set up study groups in week one, and put students who don’t sign up into one.','Learn names: a seating chart or name tents for the first weeks.','Personally invite every student to office hours once, early in the term.','Add a low-stakes quiz or draft with feedback before the first big exam.','Look at last year’s withdrawals and fails by group, and ask a few students why.','Collect a few short quotes from former students for next term.','Check your examples and images: who appears, and who doesn’t?','Add a short anonymous check-in around week three.'];
function audit(){const on=[...document.querySelectorAll('#aF input')].map(x=>x.checked);const n=on.filter(Boolean).length;const miss=on.map((v,i)=>v?null:i).filter(x=>x!==null);
 $('aRes').innerHTML=`<div class="res wl2">${barRow('Already true',n,8,n+' of 8','#7DD3A8')}</div>`+(miss.length?`<p class="gh">Next steps to make the message true</p><ul class="rlist" style="color:#E9EEF6">${miss.slice(0,3).map(i=>`<li>${NEXT[i]}</li>`).join('')}</ul>`:'');
 let title,text;
 if(n===8){title='The message is true here';text='All eight. Students who hear that they belong will find a course that backs it up.'}
 else if(n>=5){title='Mostly backed up';text=`${n} of 8 already true. The belonging message has something to stand on. A few more steps would make it more believable.`}
 else if(n>=1){title='Build first, then tell';text=`${n} of 8 already true. In the large study, the message only helped where students actually had opportunities to belong. Start with one or two of the steps below.`}
 else{title='Start with one step';text='Nothing ticked yet. Tick what is already true, or start with one of the steps below. A belonging message works best where it is already true.'}
 $('aTitle').textContent=title;$('aText').textContent=text}
$('aF').addEventListener('change',audit);audit();
'''+grid('''[
 ['Years later, a follow-up of the original 92 students found…',['Better adult outcomes for the Black participants','No lasting effects','Worse outcomes'],0,'Brady and colleagues, 2020.'],
 ['The 2023 study ran the exercise with…',['26,911 students at 22 institutions','About 900 students','One campus'],0,'Walton and colleagues, 2023.'],
 ['When did students do the online exercise?',['Before college began','In their final year','After graduating'],0,'One short session.'],
 ['It raised the share of students who…',['Completed their first year as full-time students','Chose a science major','Joined clubs'],0,'Especially in groups that had historically progressed at lower rates.'],
 ['Compared with the original study, the effects were…',['Smaller','Larger','Identical'],0,'Large, careful studies usually shrink early results.'],
 ['The exercise only worked where…',['Students’ groups actually had opportunities to belong','Classes were small','Students were told the results'],0,'The message has to be true.']]''','The pattern: the belonging exercise works at scale, modestly, and only where the course and campus make it true.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['b02']
open('b02/template.html','w').write(page(o))
