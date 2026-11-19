import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(11,'Lecture Recordings: Review, Don’t Replace','Lecture recordings','A recording keeps the lecture. Only attending keeps the class.','Lecture recordings',
'Lecture recordings are now standard at many universities. Students love them. But do they change who shows up, and what students learn?',
'<span><a href="#bT">Review or replace?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip','pfc'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In a 2019 study, Martin Edwards and Michael Clinton compared two matched groups in the same course: 161 students before recordings were introduced, and 160 after.</p>
    <p>After recordings arrived, attendance dropped substantially. Attendance predicted grades. And watching recordings did not make up for the lectures students missed. The authors concluded that, for this group, the net effect was generally negative.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>161 / 160</strong><span>students, before and after recordings</span></div>
      <div role="listitem"><strong>Down</strong><span>attendance after recordings arrived, in that course</span></div>
      <div role="listitem"><strong>Not made up</strong><span>watching recordings didn’t replace missed lectures</span></div>
      <div role="listitem"><strong>On top</strong><span>weaker students gained only when recordings added to attending</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">A second study</span>A more nuanced picture</h2>
    <p>A 2019 study by Emily Nordmann and colleagues found a more nuanced picture. Higher-achieving students could use recordings to make up for missed lectures. Lower-achieving students benefited only when they used recordings on top of the lectures they attended. And in that study, recordings did not reduce attendance.</p>
    <h2 class="sec"><span class="n">Why recordings matter</span>Review, not replacement</h2>
    <p>Recordings still matter. They support students with disabilities, students who are ill or working, and anyone reviewing a hard section. The problem is not the recording. It is using it as a replacement for class, often in a late binge before an exam.</p>
    <p>A binge is massed practice, and spacing works better. One long cram is the least effective way to use a recording.</p>
  </div>

'''+cls_html('bT','Review or replace?','Eight ways students use lecture recordings. For each, decide: is it using the recording to review, or to replace class? You’ll get feedback after each one.',[('V','Review',''),('X','Replace','')],'Review or replace?','Review or replace?','The question is always: is the recording added to class, or standing in for it?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Two studies, different results</h2>
    <p>These are two studies in particular courses, with different results on attendance. Neither was a randomized trial. The safest reading is the one they share: recordings help most as a supplement, not a substitute.</p>
  </div>

'''+GRID_HTML+box('Keep recordings, and say plainly how to use them: to review and fill gaps, not to replace attending. Make class time worth attending, with activities a recording cannot capture. Suggest a weekly review rather than a binge. Share this tip with students: use recordings to review, not to replace class.'),
tips_h='A recording keeps the lecture. Only attending keeps the class.',
tips='''      <li><b>Keep recordings</b><span>And say how to use them.</span></li>
      <li><b>Make class worth attending</b><span>Things a recording can’t capture.</span></li>
      <li><b>Weekly review, not a binge</b><span>Spacing beats cramming.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1007/s10734-018-0275-9">Edwards, M. R., &amp; Clinton, M. E. (2019). A study exploring the impact of lecture capture availability and lecture capture usage on student attendance and attainment. <i>Higher Education, 77</i>(3), 403–421.</a></li>
        <li><a href="https://doi.org/10.1007/s10734-018-0320-8">Nordmann, E., Calder, C., Bishop, P., Irwin, A., &amp; Comber, D. (2019). Turn up, tune in, don’t drop out: The relationship between lecture attendance, use of lecture recordings, and achievement at different levels of study. <i>Higher Education, 77</i>(6), 1065–1084.</a></li>''',
quiz='''[
 {q:'After recordings arrived in the Edwards and Clinton course, attendance…',o:['Dropped substantially','Rose','Stayed the same'],a:0,f:'And recordings didn’t make up for it.'},
 {q:'In Nordmann’s study, lower-achieving students benefited when recordings were…',o:['Used on top of attending','Used instead of attending','Not used'],a:0,f:'A supplement, not a substitute.'},
 {q:'The least effective way to use recordings is…',o:['One long binge before the exam','A weekly review','Rewatching a hard section'],a:0,f:'Massed practice; spacing works better.'}]''',
js=BASE+cls_js("{V:'Review',X:'Replace'}",'''[
 ['Rewatching the five minutes of a lecture you found confusing','V','Review: filling a gap after attending.'],
 ['Skipping lectures all term and planning to watch them later','X','Replace: in Edwards and Clinton’s course, recordings didn’t make up for missed lectures.'],
 ['Watching the whole term’s recordings the weekend before the exam','X','Replace, and a binge: massed practice is the least effective way to use them.'],
 ['A short weekly review of that week’s recordings, with a self-quiz','V','Review: spaced, and with retrieval practice.'],
 ['Catching up on a lecture missed through illness','V','Review: exactly what recordings are for. Higher-achieving students used them well this way.'],
 ['A student with a disability rewatching at their own pace','V','Review and access: recordings support students who need them.'],
 ['Leaving the recording playing in the background while doing other work','X','Neither, really: a recording you don’t attend to replaces nothing.'],
 ['Checking a definition you weren’t sure you wrote down correctly','V','Review: a quick, targeted use.']]''','Review or replace?',r'''
 if(right>=7){title='You can tell review from replacement';text=`${right} of 8 right. Recordings help most added to class: to fill gaps, catch up, and review a little each week.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: is the recording added to class, or standing in for it?`}
 else{title='Worth another look';text=`${right} of 8 right. Reviewing, catching up after illness and access needs are what recordings do well. Skipping class and bingeing before the exam are where they fail.`}''')+grid('''[
 ['The 2019 Edwards and Clinton study compared about how many students before and after recordings?',['160 in each group','16 in each','1,600 in each'],0,'161 before, 160 after.'],
 ['After recordings arrived, attendance in that course…',['Dropped substantially','Rose','Stayed the same'],0,'In three matched lectures.'],
 ['Did watching recordings make up for missed lectures?',['No','Yes','Only for weaker students'],0,'Attendance predicted grades.'],
 ['In Nordmann’s study, higher-achieving students could…',['Use recordings to make up for missed lectures','Not benefit at all','Only benefit by bingeing'],0,'Weaker students needed to attend too.'],
 ['In Nordmann’s study, recordings…',['Did not reduce attendance','Halved attendance','Doubled attendance'],0,'A different result from Edwards and Clinton.'],
 ['Bingeing recordings before an exam is…',['Massed practice: less effective','Spaced practice','The best strategy'],0,'Spacing works better.']]''','The pattern: recordings help as a supplement to attending, not a substitute for it.'))
open('d11/template.html','w').write(page(o))
