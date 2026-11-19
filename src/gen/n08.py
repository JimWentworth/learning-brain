import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',8,'Brain Gym and “Brain-Based” Products','Brain Gym and “brain-based” products','If a product needs brain language to sell it, ask what the evidence says without it.','Brain Gym and “brain-based” products',
'Rub your brain buttons. Cross your arms and legs. Drink water to switch on your brain. These exercises have been used in schools in dozens of countries. Do they help learning?',
'<span><a href="#bT">Evidence or brain language?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['cer','pfc'],{'pfc':([40,-60],'left'),'cer':([900,760],'right')},'Drawing of the side of the brain with the cerebellum, at the back and bottom, involved in movement, and the prefrontal cortex, at the front, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>This is Brain Gym, a commercial program from the 1980s. Its short movements, like crawling, tracing shapes in the air, and yawning, are said to improve reading, focus, and coordination between the two halves of the brain.</p>
    <p>Its explanations draw on older ideas: that repeating early movements “repatterns” the brain, that one hemisphere should dominate, and that training perception improves academic skills. Each of those ideas was tested decades ago and not supported.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1980s</strong><span>a commercial program, used in schools in dozens of countries</span></div>
      <div role="listitem"><strong>Few</strong><span>peer-reviewed studies of Brain Gym itself</span></div>
      <div role="listitem"><strong>Serious</strong><span>design problems in most of them</span></div>
      <div role="listitem"><strong>Not supported</strong><span>by research, a 2007 review concluded</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The review</span>Not supported by research</h2>
    <p>In 2007, Keith Hyatt reviewed the research on Brain Gym itself. He found only a few peer-reviewed studies, most with serious design problems, and concluded the program was not supported by research.</p>
    <h2 class="sec"><span class="n">A larger pattern</span>“Brain-based” labels</h2>
    <p>Brain Gym is one example of a larger pattern: products labelled brain-based or brain-friendly, sold with neuroscience language but little evidence that they improve learning.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Moving is good</h2>
    <p>Short bouts of exercise can give a small, brief lift in attention and mood, as Habits of the Learner showed. But that comes from the movement, not from repatterning the brain.</p>
  </div>

'''+cls_html('bT','Evidence or brain language?','Eight claims a product might make. For each, decide: is it a claim backed by the kind of evidence you’d want, or brain language doing the selling? You’ll get feedback after each one.',[('E','Evidence you can check',''),('B','Brain language selling','')],'Evidence or brain language?','Evidence or brain language?','The question is always: take out the brain words. Is there still a tested claim about learning?')+GRID_HTML+box('Keep movement breaks if your students like them, and drop the brain claims. Before adopting any brain-based product, ask for controlled studies, published by people who do not sell it. Share this tip with students: take movement breaks, but skip the brain claims.'),
tips_h='If a product needs brain language to sell it, ask what the evidence says without it.',
tips='''      <li><b>Keep movement breaks</b><span>Drop the brain claims.</span></li>
      <li><b>Controlled studies</b><span>Published by people who don’t sell it.</span></li>
      <li><b>Take out the brain words</b><span>Is there still a tested claim?</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/07419325070280020201">Hyatt, K. J. (2007). Brain Gym®: Building stronger brains or wishful thinking? <i>Remedial and Special Education, 28</i>(2), 117–124.</a></li>''',
quiz='''[
 {q:'In 2007, a review concluded Brain Gym was…',o:['Not supported by research','Strongly supported','Never studied'],a:0,f:'Few studies, most with serious design problems.'},
 {q:'The ideas behind Brain Gym, like “repatterning”, were…',o:['Tested decades ago and not supported','Recently confirmed','Never tested'],a:0,f:'Old ideas, new packaging.'},
 {q:'The benefit of a short movement break comes from…',o:['The movement itself','Repatterning the brain','Pressing brain buttons'],a:0,f:'A small, brief lift in attention and mood.'}]''',
js=BASE+cls_js("{E:'Evidence you can check',B:'Brain language selling'}",'''[
 ['“Activates both hemispheres for whole-brain learning”','B','Brain language selling: both hemispheres are always active. What learning outcome was tested?'],
 ['“In a randomized trial run by independent researchers, students using it scored higher on a reading test”','E','Evidence you can check: a comparison group, an outcome you care about, and researchers who don’t sell it.'],
 ['“Rubbing these points switches on the brain”','B','Brain language selling: nothing to switch on, and no tested learning outcome.'],
 ['“Brain-friendly classroom design, based on neuroscience”','B','Brain language selling: take out the brain words, and what was tested?'],
 ['“Results replicated in two other schools, with a control group”','E','Evidence you can check: replication and a comparison group.'],
 ['“Repatterns neural pathways through crawling movements”','B','Brain language selling: repatterning was tested decades ago and not supported.'],
 ['“Students who took a 5-minute movement break were more alert afterwards, compared with students who stayed seated”','E','Evidence you can check: a comparison, and a modest, specific claim.'],
 ['“Thousands of teachers love it”','B','Popularity, not evidence: liking isn’t learning.']]''','Evidence or brain language?',r'''
 if(right>=7){title='You can see through the label';text=`${right} of 8 right. Take out the brain words: what’s left should be a tested claim about learning.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Look for a comparison group, a learning outcome, and independent researchers.`}
 else{title='Worth another look';text=`${right} of 8 right. Hemispheres, switching on and repatterning are brain language. Comparison groups, real outcomes and replication are evidence.`}''')+grid('''[
 ['Brain Gym is…',['A commercial program from the 1980s','A university research program','A government curriculum'],0,'Used in dozens of countries.'],
 ['Its explanations draw on ideas that were…',['Tested decades ago and not supported','Recently proven','Never tested'],0,'Like repatterning and hemisphere dominance.'],
 ['In 2007, Keith Hyatt found how many peer-reviewed studies of Brain Gym itself?',['Only a few','Hundreds','None at all'],0,'Most with serious design problems.'],
 ['Can a short movement break help?',['Yes, a small, brief lift in attention and mood','No, never','Yes, it repatterns the brain'],0,'From the movement, not the claims.'],
 ['“Brain-based” products are often sold with…',['Neuroscience language but little evidence','Strong independent trials','No claims at all'],0,'A larger pattern.'],
 ['Before adopting a product, ask for studies published by…',['People who don’t sell it','The company','Happy customers'],0,'Independent evidence.']]''','The pattern: brain language sells; tested evidence about learning is often missing.'))
open('n08/template.html','w').write(page(o))
