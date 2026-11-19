import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',9,'Mastery and Retakes','Mastery and retakes','Expect mastery. Then give students the time and the second chance to reach it.','Mastery and retakes',
'Most courses move on whether students have mastered a topic or not. What if students had to reach a standard first, with another try if they missed it?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#bT">Build a retake policy</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>That is the idea behind mastery learning. Students work toward a clear standard on each unit, get feedback and extra help, and retake an assessment until they meet it.</p>
    <p>In 1990, Chen-Lin Kulik, James Kulik and Robert Bangert-Drowns reviewed 108 controlled studies, in colleges, high schools and the upper elementary grades.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the 1990 review, then see the results. About 1 minute.','Mastery learning','108 controlled studies.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>108</strong><span>controlled studies reviewed in 1990</span></div>
      <div role="listitem"><strong>~0.5</strong><span>standard deviations higher exam scores, on average</span></div>
      <div role="listitem"><strong>Weaker students</strong><span>gained more: the gap narrowed</span></div>
      <div role="listitem"><strong>A cost</strong><span>self-paced versions sometimes lowered completion</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The results</span>Higher, and fairer</h2>
    <p>Mastery programs raised exam scores by about half a standard deviation on average. The benefit was larger for weaker students, so mastery learning narrowed the gap, rather than widening it. Mastery programs also had moderate, positive effects on how students felt about the subject and the teaching.</p>
    <h2 class="sec"><span class="n">The cost</span>Time, and pace</h2>
    <p>Self-paced mastery programs sometimes lowered course completion, as students fell behind. Mastery programs can increase the time students spend on instruction. And retakes take time for instructors too. So design matters: retakes work best when they require new learning between attempts, use new versions of questions, and fit a clear schedule.</p>
  </div>

'''+cls_html('bT','Build a retake policy','Eight possible features of a retake policy. For each, decide: does it make the retake a real chance to learn, or a weak spot? You’ll get feedback after each one.',[('L','Builds learning',''),('W','A weak spot','')],'Builds learning or a weak spot?','Build a retake policy','The question is always: does the student have to learn something new before trying again, and keep pace?')+GRID_HTML+box('Choose the few outcomes that truly matter, and allow a retake on those. Require a short correction or study step before a retake. Use fresh questions, and set deadlines so students keep pace. Share this tip with students: use a retake to fix what you missed.'),
tips_h='Expect mastery. Then give students the time and the second chance to reach it.',
tips='''      <li><b>Retakes on key outcomes</b><span>Not everything.</span></li>
      <li><b>A study step first</b><span>New learning between attempts.</span></li>
      <li><b>Fresh questions, firm deadlines</b><span>So students keep pace.</span></li>''',
sources='''        <li><a href="https://doi.org/10.3102/00346543060002265">Kulik, C.-L. C., Kulik, J. A., &amp; Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. <i>Review of Educational Research, 60</i>(2), 265–299.</a></li>''',
quiz='''[
 {q:'Mastery programs raised exam scores by about…',o:['Half a standard deviation','Nothing','Two standard deviations'],a:0,f:'Across 108 studies.'},
 {q:'The benefit was larger for…',o:['Weaker students','Stronger students','Neither'],a:0,f:'The gap narrowed.'},
 {q:'Self-paced mastery programs sometimes…',o:['Lowered course completion','Raised completion','Had no costs'],a:0,f:'Deadlines help students keep pace.'}]''',
js=BASE+pred_js('''[
 ['Across 108 controlled studies, mastery programs changed exam scores by about…',['Nothing','Half a standard deviation','Three standard deviations'],1,'About half a standard deviation, on average.'],
 ['Which students gained more?',['Stronger students','Weaker students','Both equally'],1,'Weaker students: mastery learning narrowed the gap.'],
 ['What was a cost of self-paced mastery programs?',['Lower course completion, as students fell behind','Lower exam scores','Students disliked the subject more'],0,'Lower completion, sometimes. Clear schedules matter.']]''',
'''<p class="gh">What the 1990 review found</p><p class="mtext">Exam scores up about half a standard deviation. Weaker students gained more. Attitudes improved moderately. Self-paced versions sometimes lowered completion.</p>''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Mastery learning raises scores and narrows gaps, but needs a schedule so students keep pace.'}
 else if(!got[1]){title='It narrows the gap';text=`You got ${n} of 3. Weaker students gained more, so mastery learning narrowed the gap rather than widening it.`}
 else{title='Benefits, and a cost';text=`You got ${n} of 3. The gains were real, but self-paced versions could leave students behind. Design matters.`}''')+cls_js("{L:'Builds learning',W:'A weak spot'}",'''[
 ['Students must correct their errors and explain why before a retake','L','Builds learning: new learning happens between attempts.'],
 ['Retakes use exactly the same questions as the first attempt','W','A weak spot: students may memorize answers instead of learning.'],
 ['Retakes are offered on the three outcomes that matter most','L','Builds learning: focused, and manageable for you.'],
 ['Unlimited retakes on everything, any time before the end of term','W','A weak spot: students fall behind, the cost the 1990 review found for self-paced programs.'],
 ['Each retake has a deadline within two weeks','L','Builds learning: a clear schedule keeps students moving.'],
 ['A retake can only raise the grade to a C','W','Arguably a weak spot: a cap weakens the reason to reach mastery the second time.'],
 ['Fresh versions of each question for the retake','L','Builds learning: they test understanding, not memory of the answers.'],
 ['Students can retake without any study or feedback step','W','A weak spot: trying again without new learning rarely helps.']]''','Builds learning or a weak spot?',r'''
 if(right>=7){title='A policy that teaches';text=`${right} of 8 right. Key outcomes, a study step, fresh questions and deadlines.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: is there new learning before the retake, and a schedule?`}
 else{title='Worth another look';text=`${right} of 8 right. Retakes work best with a study step, fresh questions and clear deadlines, on the outcomes that matter most.`}''')+grid('''[
 ['The 1990 review covered how many controlled studies?',['108','18','1,080'],0,'Kulik, Kulik and Bangert-Drowns.'],
 ['The studies were in…',['Colleges, high schools and upper elementary grades','Colleges only','Primary schools only'],0,'A wide range.'],
 ['Mastery learning tended to…',['Narrow the gap','Widen the gap','Not affect the gap'],0,'Weaker students gained more.'],
 ['Effects on attitudes to the subject were…',['Moderate and positive','Negative','Zero'],0,'Students felt better about it.'],
 ['Mastery programs can increase…',['Time spent on instruction','Class sizes','Exam length'],0,'A real cost.'],
 ['Retakes work best when they…',['Require new learning between attempts','Repeat the same questions','Have no deadline'],0,'Design matters.']]''','The pattern: mastery with retakes raises scores and narrows gaps, if the schedule keeps students moving.'))
open('e09/template.html','w').write(page(o))
