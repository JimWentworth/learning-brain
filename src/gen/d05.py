import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(5,'Questions Inside the Video: Quizzes and Mind Wandering','Questions inside the video','A question is a small promise of attention. Ask often.','Questions inside the video',
'Twenty minutes into an online lecture, where is your students’ attention? The answer may surprise you.',
'<span><a href="#eT">Predict the results</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which helps sustain attention, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS,
body='''  <div class="col lede">
    <p>In 2013, Karl Szpunar, Novall Khan and Daniel Schacter at Harvard had students watch a 21-minute statistics lecture online, in segments. Some students answered short quiz questions after each segment. Others did not, or simply restudied.</p>
    <p>At random moments, students were asked whether their minds were wandering.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the study, then see the results. About 1 minute.','Quizzes between segments','Compare students who were quizzed after each segment with students who were not.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>21 minutes</strong><span>an online statistics lecture, in segments</span></div>
      <div role="listitem"><strong>~40% → ~20%</strong><span>of the time minds were wandering, without and with quizzes</span></div>
      <div role="listitem"><strong>~3×</strong><span>as many notes taken by quizzed students</span></div>
      <div role="listitem"><strong>Less anxious</strong><span>about the final test, and remembered more</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Restudy</span>Not the same</h2>
    <p>Restudying the material, without questions, did not produce the same benefits.</p>
    <h2 class="sec"><span class="n">Why</span>A reason to stay with it</h2>
    <p>Knowing a question is coming gives students a reason to stay with the material. And answering is itself retrieval practice, which strengthens memory. It also shows students, and you, what has not been understood yet.</p>
    <h2 class="sec"><span class="n">A caution</span>Promising, not final</h2>
    <p>This was one lecture on one topic, in a lab. The authors themselves noted it is not yet clear how well the benefit holds across a whole course, or in a live classroom. It is a promising finding, not a final answer.</p>
  </div>

'''+GRID_HTML+box('Break videos into short segments with one or two questions between them. Keep the questions low-stakes and quick. Use them in live lectures too, with polls or a minute of writing. And give quick feedback on the answers, so mistakes get corrected. Share this tip with students: pause and quiz yourself every few minutes.'),
tips_h='A question is a small promise of attention. Ask often.',
tips='''      <li><b>Questions between segments</b><span>One or two, low-stakes.</span></li>
      <li><b>In live lectures too</b><span>A poll or a minute of writing.</span></li>
      <li><b>Quick feedback</b><span>So mistakes get corrected.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1073/pnas.1221764110">Szpunar, K. K., Khan, N. Y., &amp; Schacter, D. L. (2013). Interpolated memory tests reduce mind wandering and improve learning of online lectures. <i>Proceedings of the National Academy of Sciences, 110</i>(16), 6313–6317.</a></li>''',
quiz='''[
 {q:'Without quizzes, students said their minds were wandering about…',o:['40% of the time','5% of the time','90% of the time'],a:0,f:'With quizzes, about 20%.'},
 {q:'Restudying instead of answering questions…',o:['Did not produce the same benefits','Worked just as well','Worked better'],a:0,f:'Answering is retrieval practice.'},
 {q:'This was…',o:['One lecture, in a lab: promising, not final','A whole-course field trial','A meta-analysis'],a:0,f:'The authors said so themselves.'}]''',
js=BASE+pred_js('''[
 ['Without quizzes, how often did students say their minds were wandering?',['About 10% of the time','About 40% of the time','About 75% of the time'],1,'About 40%: almost every other time they were asked.'],
 ['With a short quiz after each segment, mind wandering…',['Stayed about the same','Roughly halved, to about 20%','Went up, from the stress'],1,'Roughly halved, to about 20%.'],
 ['Quizzed students took…',['Fewer notes','About the same notes','About three times as many notes'],2,'About three times as many notes, and remembered more on the final test.']]''',
'''<p class="gh">Minds wandering (share of the times asked)</p>${barRow('No quizzes',40,100,'~40%','#FFB38A')}${barRow('Quiz after each segment',20,100,'~20%','#7DD3A8')}<p class="gh">Notes taken (no quizzes = 1)</p>${barRow('No quizzes',1,3,'1×','#C9D3E3')}${barRow('Quizzed',3,3,'~3×','#7DD3A8')}''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Without questions, minds wandered almost half the time. A short quiz after each segment halved that, and tripled note taking.'}
 else if(!got[0]){title='Minds wander a lot';text=`You got ${n} of 3. Even the researchers were surprised by how often minds wandered without questions: about 40% of the time.`}
 else{title='Quizzes changed behaviour';text=`You got ${n} of 3. A short quiz after each segment roughly halved mind wandering and tripled note taking. Knowing a question is coming gives students a reason to stay with the material.`}''')+grid('''[
 ['The lecture students watched was about…',['21 minutes, on statistics','2 hours, on history','5 minutes, on art'],0,'Shown online, in segments.'],
 ['Did restudying, without questions, give the same benefits?',['No','Yes','It was better'],0,'Answering questions was the key.'],
 ['On the final test, quizzed students…',['Remembered more','Remembered less','Did the same'],0,'And felt less anxious about it.'],
 ['Quizzed students felt…',['Less anxious about the final test','More anxious','No different'],0,'Practice made the test familiar.'],
 ['Answering a question is itself…',['Retrieval practice','A distraction','Rereading'],0,'Which strengthens memory.'],
 ['How strong is this evidence?',['One lecture, in a lab: promising','Many courses, settled','None'],0,'The authors said it is not yet clear how well it holds across a course.']]''','The pattern: short questions between segments keep minds on the lecture and build memory.'))
open('d05/template.html','w').write(page(o))
