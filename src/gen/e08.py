import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',8,'The Case for Cumulative Exams','The case for cumulative exams','What gets tested again gets remembered longer.','The case for cumulative exams',
'Students love unit exams. Study the chapter, take the test, move on. Cumulative exams, which cover everything so far, are much less popular. But which one helps students remember?',
'<span><a href="#xT">Plan the exams</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip'],{'hip':([640,770],'left')},'Drawing of the side of the brain with the hippocampus, deep inside, which helps store and consolidate memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.xp{display:grid;gap:10px;width:100%;max-width:560px}
.xp .row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.xp label{display:block;font:600 14px var(--body);color:#C9D3E3}
.xp select{display:block;width:100%;margin-top:4px;min-height:42px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 6px}
.xp select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
#xRes{width:100%;max-width:560px}''',
body='''  <div class="col lede">
    <p>In 2013, Maya Khanna, Amy Badura Brack and Laura Finken compared psychology courses with cumulative and noncumulative finals. Students who had taken cumulative finals scored higher on later tests of course content, even up to 18 months after the course.</p>
    <p>That same year, Natalie Kudrna Lawrence taught two sections of introductory psychology. One had cumulative exams all term. Students in that section did better on the final, on chapter quizzes, and in their overall course grade.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>18 months</strong><span>later, cumulative-final students still retained more</span></div>
      <div role="listitem"><strong>2 sections</strong><span>of introductory psychology, compared in 2013</span></div>
      <div role="listitem"><strong>Lower scorers</strong><span>gained most from cumulative exams</span></div>
      <div role="listitem"><strong>Few studies</strong><span>mostly psychology, not randomized</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Who benefits</span>Lower-scoring students</h2>
    <p>In Lawrence’s study, the benefit showed up mainly for lower-scoring students. Cumulative exams seemed to push them into habits that high scorers already had.</p>
    <h2 class="sec"><span class="n">Why</span>Spacing and retrieval</h2>
    <p>Cumulative exams require students to return to earlier material, which is spacing and retrieval practice, both from earlier series. Material is reviewed, not dropped after the unit test.</p>
    <h2 class="sec"><span class="n">A caution</span>A small evidence base</h2>
    <p>These were a small number of studies, mostly in psychology courses, and students were not randomly assigned to sections. Results in other subjects may differ. Cumulative exams can also feel overwhelming: students need help with how to review a whole course, not just a chapter.</p>
  </div>

  <section class="night" aria-labelledby="xT">
    <div class="col">
      <h2 class="sec" id="xT"><span class="n">Try it</span>Plan the exams</h2>
      <p>Pick how many exams your course has, and what share of each later exam covers earlier units. See how often early material comes back before the course ends.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="xScreen">
          <form class="xp" id="xF"><div class="row2">
            <label for="xN">Exams in the course<select id="xN"></select></label>
            <label for="xS">Earlier material on each later exam<select id="xS"></select></label></div>
          </form>
          <div id="xRes"></div>
        </div>
        <div>
          <p class="phase">Your exams</p>
          <p class="mtitle" id="xTitle"></p>
          <p class="mtext" id="xText" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>

'''+GRID_HTML+box('Make the final cumulative, and include some earlier material on every exam. Tell students in advance, and teach them to review weekly. Provide practice questions from earlier units. Share this tip with students: review old units every week.'),
tips_h='What gets tested again gets remembered longer.',
tips='''      <li><b>Cumulative final</b><span>And earlier material on every exam.</span></li>
      <li><b>Tell students early</b><span>Teach weekly review.</span></li>
      <li><b>Practice questions</b><span>From earlier units.</span></li>''',
sources='''        <li>Khanna, M. M., Badura Brack, A. S., &amp; Finken, L. L. (2013). Short- and long-term effects of cumulative finals on student learning. <i>Teaching of Psychology, 40</i>(3), 175–182.</li>
        <li>Lawrence, N. K. (2013). Cumulative exams in the introductory psychology course. <i>Teaching of Psychology, 40</i>(1), 15–19.</li>''',
quiz='''[
 {q:'Students with cumulative finals retained more up to…',o:['18 months later','18 days later','Nowhere'],a:0,f:'Khanna and colleagues, 2013.'},
 {q:'In Lawrence’s study, who benefited most?',o:['Lower-scoring students','Top students','Nobody'],a:0,f:'It pushed them into better habits.'},
 {q:'Cumulative exams work through…',o:['Spacing and retrieval practice','Harder questions','Longer exams'],a:0,f:'Earlier material comes back.'}]''',
js=BASE+r'''
/* ---------- plan the exams ---------- */
$('xN').innerHTML=[2,3,4,5,6].map(n=>`<option value="${n}"${n===4?' selected':''}>${n} exams</option>`).join('');
$('xS').innerHTML=[[0,'None: unit exams only'],[10,'About 10%'],[20,'About 20%'],[30,'About 30%']].map(([v,t])=>`<option value="${v}"${v===20?' selected':''}>${t}</option>`).join('');
const nth=['','first','second','third','fourth','fifth','sixth'];
function xUpd(){const N=+$('xN').value,S=+$('xS').value;const back=S?N-1:0;
 $('xRes').innerHTML=`<div class="res wl2">${barRow('Times unit 1 is tested',1+back,N,(1+back)+'×','#7DD3A8')}${barRow('Exams that revisit earlier units',back,N-1,back+' of '+(N-1),'#FCB316')}</div>`;
 let title,text;
 if(!S){title='Unit exams only';text=`Each unit is tested once, then dropped. With ${N} exams, unit 1 never comes back. A cumulative final alone would bring it back once; in Khanna’s study, that helped retention up to 18 months later.`}
 else if(S>=30){title='Strongly cumulative';text=`Unit 1 comes back on all ${back} later exams. That’s plenty of spacing and retrieval. Watch the load: give practice questions and teach students to review weekly so it doesn’t feel overwhelming.`}
 else{title='Cumulative across the term';text=`Unit 1 is tested ${1+back} times, and every later exam revisits earlier units, with about ${S}% of each. Lawrence’s cumulative section worked a similar way: later exams included questions from earlier ones.`}
 $('xTitle').textContent=title;$('xText').textContent=text}
$('xF').addEventListener('change',xUpd);xUpd();
'''+grid('''[
 ['In 2013, Khanna and colleagues compared…',['Cumulative and noncumulative finals','Online and in-person exams','Essays and quizzes'],0,'In psychology courses.'],
 ['Students with cumulative finals retained more up to…',['18 months later','A week later','Never'],0,'On later content tests.'],
 ['Lawrence compared how many sections of introductory psychology?',['Two','Twenty','One'],0,'One with cumulative exams all term.'],
 ['The cumulative section did better on…',['The final, quizzes and the course grade','Nothing','Only attendance'],0,'Lawrence, 2013.'],
 ['In Lawrence’s study, the benefit was mainly for…',['Lower-scoring students','Higher-scoring students','Everyone equally'],0,'They adopted better habits.'],
 ['Were students randomly assigned to sections?',['No','Yes','Only in one study'],0,'One reason for caution.']]''','The pattern: cumulative exams bring earlier material back, and students remember it longer.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['e08']
open('e08/template.html','w').write(page(o))
