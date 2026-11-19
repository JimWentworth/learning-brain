import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b11',n='11',label='The Learning Brain · Belonging · Topic 11',epi='The Learning Brain, Belonging, episode 11',
title='Impostor Feelings: Common, Real, and Not Evidence',h1='Impostor feelings',em='Feeling like an impostor is not evidence that you are one',read='7',mins='2 minutes',vtitle='Impostor feelings',
dek='Ever feel that everyone else belongs here, and you somehow slipped through? That one day you will be found out? That feeling is often called the impostor phenomenon.',
jumps='<span><a href="#bT">Ease the doubt, or deepen it?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the amygdala, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['amy','pfc'],labels:['amy','pfc'],labelT:{amy:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>The idea goes back to psychologists Pauline Clance and Suzanne Imes in 1978. People with impostor feelings credit their success to luck or extra effort, not ability, and fear being exposed as a fraud.</p>
    <p>In 2020, Dena Bravata and colleagues systematically reviewed 62 studies, with over 14,000 participants. Reported rates ranged from 9% to 82%. That huge range depended mostly on which questionnaire was used, and where the cutoff was set.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>62</strong><span>studies, with more than 14,000 participants</span></div>
      <div role="listitem"><strong>9% to 82%</strong><span>reported rates, depending mostly on the questionnaire and cutoff</span></div>
      <div role="listitem"><strong>Men and women</strong><span>both commonly reported impostor feelings</span></div>
      <div role="listitem"><strong>No studies</strong><span>in the review tested a treatment</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">What came with it</span>Depression, anxiety, burnout</h2>
    <p>Impostor feelings were common in both men and women. They often came with depression and anxiety, and were linked to burnout and poorer job performance.</p>
    <h2 class="sec"><span class="n">Belonging</span>The doubt grows in isolation</h2>
    <p>Impostor feelings and belonging doubts overlap. When students think they are the only one who feels this way, the doubt grows. Learning that others share it can help, as the belonging studies in topic 1 suggest.</p>
  </div>

'''+cls_html('bT','Ease the doubt, or deepen it?','Eight things an instructor might say or do. For each, decide: does it help ease impostor feelings, or deepen them? You’ll get feedback after each one.',[('E','Eases it',''),('D','Deepens it','')],'Eases or deepens the doubt?','Ease the doubt, or deepen it?','The question is always: does it tell students that doubt is common, and that success comes from work they can see?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Not a diagnosis; no tested treatments</h2>
    <p>It is not a clinical diagnosis, and the measures vary widely. No study in the review tested a treatment. So be wary of quick fixes.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Normalize doubt: say that struggle and uncertainty are common, even among experts. Share your own early struggles. Praise strategy and progress, and make the standards clear.</p>
    </aside>
  </div>
''',
tips_h='Feeling like an impostor is not evidence that you are one.',
tips='''      <li><b>Normalize doubt</b><span>Even experts feel it.</span></li>
      <li><b>Share your own early struggles</b><span>Specifically.</span></li>
      <li><b>Clear standards</b><span>And praise for strategy and progress.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/h0086006">Clance, P. R., &amp; Imes, S. A. (1978). The imposter phenomenon in high achieving women: Dynamics and therapeutic intervention. <i>Psychotherapy: Theory, Research &amp; Practice, 15</i>(3), 241–247.</a></li>
        <li><a href="https://doi.org/10.1007/s11606-019-05364-1">Bravata, D. M., Watts, S. A., Keefer, A. L., et al. (2020). Prevalence, predictors, and treatment of impostor syndrome: A systematic review. <i>Journal of General Internal Medicine, 35</i>(4), 1252–1275.</a></li>''',
quiz='''[
 {q:'Reported rates of impostor feelings ranged from…',o:['9% to 82%, depending mostly on the questionnaire','About 50% everywhere','Under 1%'],a:0,f:'Bravata and colleagues, 2020.'},
 {q:'Impostor feelings were common in…',o:['Both men and women','Only women','Only students'],a:0,f:'And they often came with depression and anxiety.'},
 {q:'How many studies in the review tested a treatment?',o:['None','Most','About half'],a:0,f:'Be wary of quick fixes.'}]''',
js=BASE+cls_js("{E:'Eases it',D:'Deepens it'}",'''[
 ['“Most people in this room will feel out of their depth at some point. I did too.”','E','Eases it: doubt is named as common, even for the instructor.'],
 ['Telling a struggling student that “top students never find this hard”','D','Deepens it: it suggests struggle means you don’t belong.'],
 ['Describing a specific time you struggled early in your career, and what you did','E','Eases it: a concrete story makes the message believable.'],
 ['Praising only students who seem to get it instantly','D','Deepens it: success looks like luck or talent, not work.'],
 ['Making grading criteria clear, so students can see what success is built from','E','Eases it: success becomes something students can trace to their work.'],
 ['“If you’re here, you obviously belong. Stop worrying.”','D','Deepens it, often: it dismisses the feeling instead of normalizing it.'],
 ['Praising a student’s strategy and progress on a hard problem','E','Eases it: success is linked to work they can repeat.'],
 ['Promoting a one-off workshop as a cure for impostor syndrome','D','Deepens it, or at best untested: calling it a cure overpromises, and no study in the review tested a treatment.']]''','Eases or deepens the doubt?',r'''
 if(right>=7){title='You can ease it';text=`${right} of 8 right. Name doubt as common, share real struggles, and make success traceable to strategy and progress.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Dismissing the feeling, or praising only effortless talent, tends to deepen it.`}
 else{title='Worth another look';text=`${right} of 8 right. Easing impostor feelings means normalizing doubt and linking success to work students can see, not talent or luck.`}''')+grid('''[
 ['The impostor phenomenon was first described in…',['1978','2008','1878'],0,'Clance and Imes.'],
 ['The 2020 review covered how many studies?',['62','6','620'],0,'With more than 14,000 participants.'],
 ['Reported rates ranged from 9% to 82%, mostly because of…',['Different questionnaires and cutoffs','Different countries only','Different years'],0,'The measures vary widely.'],
 ['Impostor feelings were…',['Common in both men and women','Found only in women','Found only in men'],0,'Bravata and colleagues, 2020.'],
 ['They were linked to…',['Depression, anxiety, burnout and poorer job performance','Better performance','Nothing measurable'],0,'Often alongside other difficulties.'],
 ['Is impostor syndrome a clinical diagnosis?',['No','Yes','Only in some countries'],0,'And no study in the review tested a treatment.']]''','The pattern: impostor feelings are common, hard to measure, and linked to real costs. Normalizing doubt helps; quick fixes are untested.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['b11']
open('b11/template.html','w').write(page(o))
