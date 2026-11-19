import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',2,'Quizzing in Real Classes','Quizzing in real classes','Small quizzes, often. It adds up to a lot of learning.','Quizzing in real classes',
'Lab studies are one thing. Real courses have real grades, busy students, and messy schedules. Does quizzing still help there?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip'],{'hip':([640,770],'left')},'Drawing of the side of the brain with the hippocampus, deep inside, which helps store memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS,
body='''  <div class="col lede">
    <p>In 2021, Chunliang Yang, David Shanks and colleagues gathered 222 classroom studies, with more than 48,000 students, from primary school to university.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the 2021 classroom analysis, then see the results. About 1 minute.','Quizzing in real classes','222 classroom studies, more than 48,000 students.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>222</strong><span>classroom studies</span></div>
      <div role="listitem"><strong>48,000+</strong><span>students, from primary school to university</span></div>
      <div role="listitem"><strong>~0.5</strong><span>effect size: large by education standards</span></div>
      <div role="listitem"><strong>Beyond facts</strong><span>concepts and problem solving improved too</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The result</span>Half a standard deviation</h2>
    <p>Class quizzes raised achievement by about half a standard deviation, an effect size of 0.5. That is large by the standards of education research. And it held across school levels and subjects.</p>
    <p>The benefit was not limited to facts. Quizzing also helped with understanding concepts and solving problems, which counters the worry that testing is just drill.</p>
    <h2 class="sec"><span class="n">In practice</span>Details that help</h2>
    <p>Format mattered less than expected: multiple choice and short answer both worked. Graded and ungraded quizzes both helped. Repeated quizzing across days helped more than a single quiz. Whether students answered alone or in groups made little difference.</p>
    <h2 class="sec"><span class="n">Why</span>Three reasons</h2>
    <p>The authors point to extra exposure to the material, practice in the form the final test will take, and motivation to keep up. Quizzes also show instructors where the class is, in time to adjust.</p>
  </div>

'''+GRID_HTML+box('Give short, frequent quizzes, weekly or even every class. Keep them low stakes. Repeat key questions across weeks. And let quizzes look like the questions students will face on exams. Share this tip with students: treat quizzes as practice, not judgment.'),
tips_h='Small quizzes, often. It adds up to a lot of learning.',
tips='''      <li><b>Short and frequent</b><span>Weekly, or every class.</span></li>
      <li><b>Low stakes</b><span>Graded or not, both helped.</span></li>
      <li><b>Repeat key questions</b><span>Across weeks.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/bul0000309">Yang, C., Luo, L., Vadillo, M. A., Yu, R., &amp; Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. <i>Psychological Bulletin, 147</i>(4), 399–435.</a></li>''',
quiz='''[
 {q:'Class quizzes raised achievement by about…',o:['Half a standard deviation','Nothing','Two standard deviations'],a:0,f:'Large by education standards.'},
 {q:'Quizzing helped with…',o:['Facts, concepts and problem solving','Facts only','Nothing beyond grades'],a:0,f:'Not just drill.'},
 {q:'Which helped more?',o:['Repeated quizzing across days','A single quiz','Neither'],a:0,f:'Repeat key questions.'}]''',
js=BASE+pred_js('''[
 ['Across 222 classroom studies, quizzing raised achievement by about…',['A tenth of a standard deviation','Half a standard deviation','Two standard deviations'],1,'About half: an effect size of 0.5, large for education research.'],
 ['Did quizzing help only with memorizing facts?',['Yes, facts only','No: concepts and problem solving too','It hurt understanding'],1,'No: it helped with understanding concepts and solving problems too.'],
 ['Did quizzes need to be graded to help?',['Yes, only graded quizzes helped','No: graded and ungraded both helped','Only ungraded helped'],1,'No: both helped.']]''',
'''<p class="gh">What the 2021 analysis found</p><p class="mtext">Effect size about 0.5, across school levels and subjects. Facts, concepts and problem solving. Multiple choice and short answer. Graded and ungraded. Repeated beats single.</p>''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Classroom quizzing works, beyond facts, and without high stakes.'}
 else if(!got[0]){title='Bigger than you’d think';text=`You got ${n} of 3. An effect of about half a standard deviation is large by the standards of education research.`}
 else{title='More than drill';text=`You got ${n} of 3. Quizzing helped understanding and problem solving too, and low-stakes quizzes worked.`}''')+grid('''[
 ['The 2021 analysis gathered how many classroom studies?',['222','22','2,220'],0,'Yang, Shanks and colleagues.'],
 ['It included students from…',['Primary school to university','University only','Primary school only'],0,'More than 48,000 students.'],
 ['Did the format matter much?',['Less than expected: multiple choice and short answer both worked','Only short answer worked','Only multiple choice worked'],0,'Choose what fits.'],
 ['Answering alone or in groups made…',['Little difference','A big difference','Groups hurt learning'],0,'Either works.'],
 ['One reason quizzes help is…',['Practice in the form of the final test','They replace teaching','They lower standards'],0,'Plus exposure and motivation.'],
 ['Quizzes also help instructors by…',['Showing where the class is, in time to adjust','Reducing teaching time','Replacing exams'],0,'Assessment for teaching.']]''','The pattern: frequent, low-stakes classroom quizzes raise achievement substantially, beyond facts.'))
open('e02/template.html','w').write(page(o))
