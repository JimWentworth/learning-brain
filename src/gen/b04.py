import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b04',n='4',label='The Learning Brain · Belonging · Topic 4',epi='The Learning Brain, Belonging, episode 4',
title='Stereotype Threat, Carefully: What the Evidence Supports',h1='Stereotype threat, carefully',em='Lower the stakes of identity, not the standards',read='7',mins='2 minutes',vtitle='Stereotype threat, carefully',
dek='A famous 1995 experiment made stereotype threat one of the best-known ideas in education. Later work tells a more careful story: the effect is probably smaller and narrower than the headlines suggested.',
jumps='<span><a href="#bT">Raise or lower the threat?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the amygdala, deep inside, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[330,740];BR.R.amy.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','amy'],labels:['pfc','amy'],labelT:{pfc:0.8,amy:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 1995, an experiment by Claude Steele and Joshua Aronson suggested that simply framing a test as a measure of ability could lower the scores of students whose group is stereotyped as weaker. It was called stereotype threat. The idea was intuitive: worry about confirming a stereotype takes up attention and working memory, the same resources the test needs.</p>
    <p>But later work tells a more careful story.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~0.2</strong><span>average effect for schoolgirls on maths and science tests, with clear signs of publication bias</span></div>
      <div role="listitem"><strong>931</strong><span>students in three studies: no evidence of the effect</span></div>
      <div role="listitem"><strong>212</strong><span>adult studies: signs of bias here too</span></div>
      <div role="listitem"><strong>0 to ~0.14</strong><span>the effect in settings most like real high-stakes tests</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>Smaller and narrower</h2>
    <p>A 2015 meta-analysis by Paulette Flore and Jelte Wicherts, of studies with schoolgirls on maths and science tests, found a small average effect, about 0.2, with clear signs of publication bias. A set of three studies by Colleen Ganley and colleagues, with 931 students, found no evidence of the effect at all.</p>
    <p>A 2019 meta-analysis by Oren Shewach and colleagues, of 212 adult studies, also found signs of bias. In settings most like real high-stakes tests, the effects ranged from zero to about 0.14.</p>
    <p>So stereotype threat may be real in some situations. But it is probably smaller and narrower than the headlines suggested, and it is unlikely to explain most achievement gaps on its own.</p>
    <h2 class="sec"><span class="n">Why still care?</span>The triggers are worth avoiding anyway</h2>
    <p>The conditions that might trigger it, like being the only one of your group in the room, or hearing that a test measures fixed ability, are worth avoiding anyway. And they cost nothing to change.</p>
  </div>

'''+cls_html('bT','Raise or lower the threat?','Eight test-day and classroom practices. For each, decide: does it make identity more salient and the stakes higher (raises the threat), or lower the stakes of identity while keeping standards (lowers it)? You’ll get feedback after each one.',[('R','Raises it',''),('L','Lowers it','')],'Raises or lowers the threat?','Raise or lower the threat?','The question is always: does it make students think about their group, or about the task?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Take the evidence seriously too</h2>
    <p>Stereotype threat is a reason to remove needless triggers, not a reason to lower expectations. And it is not a full explanation for gaps that have many causes.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Don’t describe tests as measures of natural ability. Avoid collecting demographic questions right before an exam. Try not to leave any student as the only member of their group on a team. And keep the bar high. Lower the stakes of identity, not the standards.</p>
    </aside>
  </div>
''',
tips_h='Take the threat seriously. Take the evidence seriously too.',
tips='''      <li><b>Not “natural ability”</b><span>Don’t frame tests that way.</span></li>
      <li><b>No demographics before exams</b><span>Ask afterwards, or not at all.</span></li>
      <li><b>Never the only one</b><span>On a team, where you can help it.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/0022-3514.69.5.797">Steele, C. M., &amp; Aronson, J. (1995). Stereotype threat and the intellectual test performance of African Americans. <i>Journal of Personality and Social Psychology, 69</i>(5), 797–811.</a></li>
        <li><a href="https://doi.org/10.1016/j.jsp.2014.10.002">Flore, P. C., &amp; Wicherts, J. M. (2015). Does stereotype threat influence performance of girls in stereotyped domains? A meta-analysis. <i>Journal of School Psychology, 53</i>(1), 25–44.</a></li>
        <li><a href="https://doi.org/10.1037/a0031412">Ganley, C. M., Mingle, L. A., Ryan, A. M., Ryan, K., Vasilyeva, M., &amp; Perry, M. (2013). An examination of stereotype threat effects on girls’ mathematics performance. <i>Developmental Psychology, 49</i>(10), 1886–1897.</a></li>
        <li><a href="https://doi.org/10.1037/apl0000420">Shewach, O. R., Sackett, P. R., &amp; Quint, S. (2019). Stereotype threat effects in settings with features likely versus unlikely in operational test settings: A meta-analysis. <i>Journal of Applied Psychology, 104</i>(12), 1514–1534.</a></li>''',
quiz='''[
 {q:'For schoolgirls on maths and science tests, the average stereotype threat effect was…',o:['Small, about 0.2, with signs of publication bias','Large','Exactly zero'],a:0,f:'Flore and Wicherts, 2015.'},
 {q:'In settings most like real high-stakes tests, the effect ranged from…',o:['Zero to about 0.14','0.5 to 1','1 to 2'],a:0,f:'Shewach and colleagues, 2019.'},
 {q:'The safest response is to…',o:['Remove needless triggers and keep standards high','Lower standards','Ignore it entirely'],a:0,f:'Lower the stakes of identity, not the standards.'}]''',
js=BASE+cls_js("{R:'Raises it',L:'Lowers it'}",'''[
 ['Describing an exam as “a test of your natural maths ability”','R','Raises it: framing a test as a measure of fixed ability is the classic trigger.'],
 ['Asking students to record their gender and race on the first page of an exam','R','Raises it: collect demographics afterwards, or not at all.'],
 ['Describing the test as a check on what you’ve practised this term','L','Lowers it: it points students at the task, not at fixed ability.'],
 ['Putting the one woman in a lab section on an otherwise all-male team','R','Raises it: being the only one of your group makes identity salient.'],
 ['Forming teams so no student is the only member of their group','L','Lowers it, where class composition allows.'],
 ['Lowering the standard for some students to protect them','R','Works against students either way: it signals low expectations. Lower the stakes of identity, not the standards.'],
 ['Keeping the standard high and saying everyone can reach it with practice','L','Lowers it: high standards, with belief in students.'],
 ['Joking before the test that “some groups are just better at this”','R','Raises it: a direct reminder of a stereotype.']]''','Raises or lowers the threat?',r'''
 if(right>=7){title='You can remove the triggers';text=`${right} of 8 right. Frame tests around practice, not fixed ability; skip demographics before exams; avoid “only one” teams; keep the bar high.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does this make students think about their group, or about the task?`}
 else{title='Worth another look';text=`${right} of 8 right. Triggers make identity salient or frame a test as fixed ability. Lowering standards doesn’t help; lowering the stakes of identity does.`}''')+grid('''[
 ['For schoolgirls on maths and science tests, the average effect found in 2015 was…',['Small, about 0.2','Large, about 1','Negative'],0,'Flore and Wicherts, 2015.'],
 ['That meta-analysis also found…',['Clear signs of publication bias','No problems','Bigger effects in better studies'],0,'So the true effect is likely smaller still.'],
 ['Three studies with 931 students found…',['No evidence of the effect','A large effect','A reversed effect'],0,'Ganley and colleagues, 2013.'],
 ['A 2019 meta-analysis covered how many adult studies?',['212','12','2,000'],0,'Shewach and colleagues, 2019.'],
 ['In settings most like real high-stakes tests, the effect was…',['Zero to about 0.14','About 0.5','About 1'],0,'Negligible to small.'],
 ['Can stereotype threat explain most achievement gaps on its own?',['Unlikely','Yes','Yes, completely'],0,'Gaps have many causes.']]''','The pattern: stereotype threat is smaller and narrower than once claimed, but its triggers are cheap to remove.'))
open('b04/template.html','w').write(page(o))
