import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',5,'Feedback That Works','Feedback that works','Feedback works when it can be used. Make every comment usable.','Feedback that works',
'Feedback is often called one of the most powerful tools in teaching. But is all feedback helpful? The answer is a clear no.',
'<span><a href="#bT">Sort the comments</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','str'],{'pfc':([40,-60],'left'),'str':([330,640],'right')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which plans the next attempt, and the striatum, deep inside, involved in learning from outcomes, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 1996, Avraham Kluger and Angelo DeNisi reviewed more than 130 studies of feedback. On average, feedback helped. But about a third of the effects were negative: performance got worse after feedback. Feedback was most likely to backfire when it drew attention to the person rather than the task.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~1 in 3</strong><span>feedback effects were negative, in 1996</span></div>
      <div role="listitem"><strong>435</strong><span>studies, 61,000+ participants, pooled in 2020</span></div>
      <div role="listitem"><strong>~0.5</strong><span>average effect, but it varied enormously</span></div>
      <div role="listitem"><strong>Information</strong><span>about how to improve made the difference</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The big picture</span>It varies enormously</h2>
    <p>A 2020 meta-analysis by Benedikt Wisniewski, Klaus Zierer and John Hattie pooled 435 studies with more than 61,000 participants. The average effect was medium, about 0.5, but it varied enormously. Feedback that told students how to improve, and on what, worked best. Praise alone, rewards and punishments did little.</p>
    <h2 class="sec"><span class="n">Levels</span>Task, process, person</h2>
    <p>Feedback on the task says what is right or wrong. Feedback on the process says how to approach it better. And feedback about the person, like “you’re so smart”, tends to do the least. This fits wise feedback from the Belonging series: high standards, belief that the student can meet them, and specific next steps.</p>
  </div>

'''+cls_html('bT','Sort the comments','Eight comments on a student’s lab report. For each, decide: is it about the task, the process, or the person? You’ll get feedback after each one.',[('T','The task',''),('P','The process',''),('S','The person','')],'Task, process, or person?','Sort the comments','The question is always: does the comment point at the work, at how to do it better, or at the student?')+GRID_HTML+box('Give fewer comments, but make them specific and actionable: one thing to keep, one thing to change. Focus on the work and the strategy, not the person. And build in a chance to use the feedback, like a revision or the next assignment. Share this tip with students: look for the next step in feedback, not the score.'),
tips_h='Feedback works when it can be used. Make every comment usable.',
tips='''      <li><b>Fewer, specific comments</b><span>One to keep, one to change.</span></li>
      <li><b>Work and strategy</b><span>Not the person.</span></li>
      <li><b>A chance to use it</b><span>Revision or the next task.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0033-2909.119.2.254">Kluger, A. N., &amp; DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. <i>Psychological Bulletin, 119</i>(2), 254–284.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2019.03087">Wisniewski, B., Zierer, K., &amp; Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. <i>Frontiers in Psychology, 10</i>, 3087.</a></li>''',
quiz='''[
 {q:'In 1996, about what share of feedback effects were negative?',o:['About a third','None','Almost all'],a:0,f:'Kluger and DeNisi.'},
 {q:'Feedback was most likely to backfire when it focused on…',o:['The person','The task','The next step'],a:0,f:'“You’re so smart” does the least.'},
 {q:'What made feedback work best?',o:['Information about how to improve','Praise','Rewards'],a:0,f:'Wisniewski, Zierer and Hattie, 2020.'}]''',
js=BASE+cls_js("{T:'The task',P:'The process',S:'The person'}",'''[
 ['“Your graph is missing units on the y-axis.”','T','The task: what’s right or wrong in the work. Clear, and fixable.'],
 ['“You’re a natural scientist!”','S','The person: pleasant, but it says nothing about what to do next.'],
 ['“Before you write the conclusion, check whether your data actually support it.”','P','The process: how to approach the work better next time.'],
 ['“The hypothesis is clearly stated.”','T','The task: names what to keep doing.'],
 ['“Try sketching the setup before you describe it; it’ll help you spot missing steps.”','P','The process: a strategy the student can reuse.'],
 ['“Disappointing. I expected more from you.”','S','The person: this is where feedback most often backfires.'],
 ['“Your error analysis lists only one source of error; there are at least two more.”','T','The task: specific and actionable.'],
 ['“When you’re stuck, compare your method with the worked example step by step.”','P','The process: a way to get unstuck next time.']]''','Task, process, or person?',r'''
 if(right>=7){title='You can read feedback';text=`${right} of 8 right. Task and process comments give students something to use. Person comments rarely do.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does it point at the work, the strategy, or the student?`}
 else{title='Worth another look';text=`${right} of 8 right. Task: what’s right or wrong. Process: how to do it better. Person: praise or blame about the student, which does the least.`}''')+grid('''[
 ['In 1996, Kluger and DeNisi reviewed about how many studies?',['More than 130','13','1,300'],0,'On average, feedback helped.'],
 ['About what share of feedback effects were negative?',['About a third','None','Most'],0,'Performance got worse after feedback.'],
 ['The 2020 meta-analysis pooled how many studies?',['435','43','4,350'],0,'More than 61,000 participants.'],
 ['The average effect of feedback was…',['Medium, about 0.5, but varied enormously','Tiny and consistent','Huge and consistent'],0,'Wisniewski, Zierer and Hattie.'],
 ['Praise alone, rewards and punishments did…',['Little','A lot','Harm, always'],0,'Information did the work.'],
 ['Which level of feedback tends to do the least?',['About the person','About the process','About the task'],0,'“You’re so smart.”']]''','The pattern: feedback helps when it carries usable information about the work, not the person.'))
open('e05/template.html','w').write(page(o))
