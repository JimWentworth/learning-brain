import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b07',n='7',label='The Learning Brain · Belonging · Topic 7',epi='The Learning Brain, Belonging, episode 7',
title='The Teacher’s Mindset: How Beliefs About Ability Reach Students',h1='The teacher’s mindset',em='What you believe about ability, your students can hear',read='7',mins='2 minutes',vtitle='The teacher’s mindset',
dek='Some instructors believe students either have what it takes, or they don’t. Others believe ability grows with effort and good teaching. That belief seems to show up in students’ grades.',
jumps='<span><a href="#bT">Fixed or growth signal?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>At one large university, Elizabeth Canning, Katherine Muenks, Dorainne Green and Mary Murphy surveyed 150 STEM faculty about their beliefs on ability. Then they examined the records of more than 15,000 students in those faculty members’ courses, over two years. They reported the results in 2019.</p>
    <p>In courses taught by faculty with more fixed mindsets, the racial achievement gap was about twice as large as in courses taught by faculty with growth mindsets.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>150</strong><span>STEM faculty surveyed about whether ability is fixed</span></div>
      <div role="listitem"><strong>15,000+</strong><span>students’ records in their courses</span></div>
      <div role="listitem"><strong>2×</strong><span>the racial achievement gap in courses taught by more fixed-mindset faculty</span></div>
      <div role="listitem"><strong>Better</strong><span>predictor than the instructor’s gender, race, age, experience or tenure</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Who was hit</span>All students, some more</h2>
    <p>All students tended to do worse in the fixed-mindset courses, but students from underrepresented groups were hit hardest. The instructor’s mindset predicted these gaps better than their gender, race, age, teaching experience or tenure. And students in fixed-mindset courses reported feeling less motivated, even though they did not rate those courses as harder.</p>
    <h2 class="sec"><span class="n">How it leaks</span>Comments, advice, praise, grading</h2>
    <p>How might a belief leak into a course? Through comments like “not everyone is cut out for this”. Through advising students to drop after one bad exam. Through praising only speed and brilliance. And through grading that offers no second chance.</p>
  </div>

'''+cls_html('bT','Fixed or growth signal?','Nine things an instructor might say or do. For each, decide: does it signal that ability is fixed, or that it grows? You’ll get feedback after each one.',[('F','Fixed','ability is set'),('G','Growth','ability develops')],'Fixed or growth signal?','Fixed or growth signal?','The question is always: what does it tell students about whether they can get better?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Correlational, one university</h2>
    <p>This is a correlational study at one university, and faculty with fixed mindsets may differ in other ways. But the signals you send are under your control.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Talk about ability as something students develop. Praise strategies and improvement, not just talent. Don’t suggest dropping after a single setback. And give chances to show growth, like revisions or retakes.</p>
    </aside>
  </div>
''',
tips_h='What you believe about ability, your students can hear.',
tips='''      <li><b>Ability develops</b><span>Say so, and mean it.</span></li>
      <li><b>Praise strategy and improvement</b><span>Not just talent or speed.</span></li>
      <li><b>Second chances</b><span>Revisions or retakes.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/sciadv.aau4734">Canning, E. A., Muenks, K., Green, D. J., &amp; Murphy, M. C. (2019). STEM faculty who believe ability is fixed have larger racial achievement gaps and inspire less student motivation in their classes. <i>Science Advances, 5</i>(2), eaau4734.</a></li>''',
quiz='''[
 {q:'In courses taught by more fixed-mindset STEM faculty, the racial achievement gap was…',o:['About twice as large','About the same','Smaller'],a:0,f:'Canning and colleagues, 2019.'},
 {q:'Students in fixed-mindset courses reported…',o:['Less motivation, though they didn’t rate the courses as harder','Finding the courses much harder','More motivation'],a:0,f:'The belief, not the difficulty.'},
 {q:'The instructor’s mindset predicted gaps better than…',o:['Their gender, race, age, experience or tenure','Nothing else was measured','Only their age'],a:0,f:'The signals you send are under your control.'}]''',
js=BASE+cls_js("{F:'Fixed',G:'Growth'}",'''[
 ['“Not everyone is cut out for this major.”','F','Fixed: it suggests some students simply can’t.'],
 ['Advising a student to drop after one bad exam','F','Fixed: it treats a single result as a verdict on ability.'],
 ['“Your second draft shows you tried a new approach, and it worked.”','G','Growth: praise for strategy and improvement.'],
 ['Praising the student who finished first as “a natural”','F','Fixed: it rewards speed and innate brilliance.'],
 ['Offering a retake or revision for a key assignment','G','Growth: it gives a chance to show what students learned.'],
 ['“Everyone in this room can master this with practice and help.”','G','Growth: ability as something students develop.'],
 ['Grading with no second chances, “to see who really gets it”','F','Fixed: it sorts students rather than developing them.'],
 ['Showing your own early mistakes in the field, and how you got better','G','Growth: struggle as part of the path, even for experts.'],
 ['“Some people have a maths brain, and some don’t.”','F','Fixed: a direct statement that ability is set.']]''','Fixed or growth signal?',r'''
 if(right>=8){title='You can hear the signals';text=`${right} of 9 right. Comments, advice, praise and grading all tell students whether their ability can grow.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Ask: does this tell students they can get better, or that they either have it or don’t?`}
 else{title='Worth another look';text=`${right} of 9 right. Fixed signals treat ability as set: “cut out for it”, “a natural”, no second chances. Growth signals praise strategy and offer chances to improve.`}''')+grid('''[
 ['The 2019 study surveyed how many STEM faculty?',['150','15','1,500'],0,'Canning and colleagues, 2019.'],
 ['Their students’ records numbered…',['More than 15,000','About 500','About 1 million'],0,'Over two years.'],
 ['In courses taught by more fixed-mindset faculty, the racial achievement gap was…',['About twice as large','About half as large','The same'],0,'All students tended to do worse; underrepresented students most.'],
 ['Did students rate the fixed-mindset courses as harder?',['No','Yes, much harder','Yes, slightly'],0,'But they reported feeling less motivated.'],
 ['The instructor’s mindset predicted gaps better than their…',['Gender, race, age, experience or tenure','Course content only','Nothing; it was the weakest predictor'],0,'The belief mattered most.'],
 ['This study shows…',['A correlation, at one university','A randomized experiment','A national trend'],0,'Fixed-mindset faculty may differ in other ways.']]''','The pattern: instructors’ beliefs about ability travel through their comments, advice, praise and grading, and track larger gaps.'))
open('b07/template.html','w').write(page(o))
