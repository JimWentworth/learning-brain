import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',7,'Sugar Highs: What We Expect to See','Sugar highs','Sometimes the strongest effect in the room is what we expect to see.','Sugar highs',
'A birthday party, a pile of cake, and a room full of children bouncing off the walls. Everyone has seen a sugar high. Or have they?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#bT">Situation or single cause?</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','amy'],{'pfc':([40,-60],'left'),'amy':([330,740],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which shapes how we interpret what we see, and the amygdala, deep inside, involved in excitement and emotion, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>The claim: sugar makes children hyperactive and unable to focus. It is one of the most widely believed brain myths, among parents and teachers alike.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about two studies, then see the results. About 1 minute.','Sugar, or expectations?','A meta-analysis of double-blind studies, and an experiment on expectations.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>23</strong><span>double-blind studies, from 16 reports, pooled in 1995</span></div>
      <div role="listitem"><strong>No effect</strong><span>of sugar on behaviour or cognitive performance</span></div>
      <div role="listitem"><strong>35</strong><span>boys, all given a sugar-free drink, in 1994</span></div>
      <div role="listitem"><strong>More hyperactive</strong><span>in the eyes of mothers told their son had sugar</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>Double-blind</h2>
    <p>In 1995, Mark Wolraich and colleagues pooled 23 double-blind studies in the <i>Journal of the American Medical Association</i>. Children got either sugar or a sugar-free placebo, and no one watching knew which. The conclusion: sugar did not affect children’s behaviour or cognitive performance.</p>
    <h2 class="sec"><span class="n">Why we see it</span>Expectations</h2>
    <p>A 1994 study by Daniel Hoover and Richard Milich offers a clue. Thirty-five boys, described by their mothers as sugar-sensitive, all received a sugar-free drink. Mothers who were told their son had sugar rated him as more hyperactive, and behaved differently toward him. Expectations shape what we see. And settings matter too: parties and holidays are exciting, with or without the cake.</p>
    <h2 class="sec"><span class="n">A caution</span>Small effects not ruled out</h2>
    <p>The authors noted that a small effect, or effects in a few sensitive children, could not be ruled out. And too much sugar still harms health. It just does not explain the party.</p>
    <h2 class="sec"><span class="n">For instructors</span>The lesson travels</h2>
    <p>When we expect a student to struggle or misbehave, we tend to see it, and we may treat them differently.</p>
  </div>

'''+cls_html('bT','Situation or single cause?','Eight explanations for student behaviour. For each, decide: does it look at the situation and evidence, or jump to a single cause that matches an expectation? You’ll get feedback after each one.',[('S','Looks at the situation',''),('J','Jumps to one cause','')],'Looks at the situation or jumps to one cause?','Situation or single cause?','The question is always: what else about the setting could explain this, and what evidence can I check?')+GRID_HTML+box('Before you explain a student’s behaviour, look at the situation, not a single cause. Notice when your expectations are doing the observing. And base judgments on evidence you can check. Share this tip with students: notice the setting, not just the snack.'),
tips_h='Sometimes the strongest effect in the room is what we expect to see.',
tips='''      <li><b>Look at the situation</b><span>Not a single cause.</span></li>
      <li><b>Notice your expectations</b><span>They do some of the observing.</span></li>
      <li><b>Evidence you can check</b><span>Before you judge.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1001/jama.1995.03530200053037">Wolraich, M. L., Wilson, D. B., &amp; White, J. W. (1995). The effect of sugar on behavior or cognition in children: A meta-analysis. <i>JAMA, 274</i>(20), 1617–1621.</a></li>
        <li><a href="https://doi.org/10.1007/BF02168088">Hoover, D. W., &amp; Milich, R. (1994). Effects of sugar ingestion expectancies on mother-child interactions. <i>Journal of Abnormal Child Psychology, 22</i>(4), 501–515.</a></li>''',
quiz='''[
 {q:'In double-blind studies, sugar…',o:['Did not affect behaviour or cognitive performance','Made children hyperactive','Improved focus'],a:0,f:'Wolraich and colleagues, 1995.'},
 {q:'Mothers told their son had sugar (he hadn’t) rated him…',o:['More hyperactive','Less hyperactive','The same'],a:0,f:'Expectations shape what we see.'},
 {q:'Could a small effect in a few children be ruled out?',o:['No','Yes','The study didn’t say'],a:0,f:'The authors were careful.'}]''',
js=BASE+pred_js('''[
 ['When children got sugar or a placebo, and no one watching knew which, sugar…',['Made behaviour clearly worse','Made no difference to behaviour or performance','Made behaviour better'],1,'No difference: 23 double-blind studies, pooled in 1995.'],
 ['In 1994, every boy got a sugar-free drink. Mothers told their son had sugar rated him…',['More hyperactive','Less hyperactive','The same as other mothers did'],0,'More hyperactive, though no boy had sugar.'],
 ['Those mothers also…',['Behaved differently toward their sons','Left the room','Stopped watching'],0,'Behaved differently. Expectations changed both what they saw and what they did.']]''',
'''<p class="gh">What changed the ratings</p><p class="mtext">Not the sugar: no boy had any. What mothers were told changed what they saw.</p>''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Sugar didn’t change behaviour in blind studies, but expecting sugar changed what mothers saw and how they acted.'}
 else if(!got[0]){title='Blind tests change the picture';text=`You got ${n} of 3. When no one watching knew who had sugar, the effect disappeared.`}
 else{title='Expectations do the observing';text=`You got ${n} of 3. Mothers who expected a sugar high saw one, even with no sugar.`}''')+cls_js("{S:'Looks at the situation',J:'Jumps to one cause'}",'''[
 ['“He’s been bouncing off the walls since lunch. Must be all that sugar.”','J','Jumps to one cause: blind studies found no sugar effect. What else changed after lunch?'],
 ['Noticing the class is restless the day before a holiday, and planning a more active lesson','S','Looks at the situation: settings change behaviour.'],
 ['Deciding a student is lazy after one missed deadline','J','Jumps to one cause: one data point, and an expectation filling the gap.'],
 ['Asking a quiet student whether the group work is going well before assuming they’re disengaged','S','Looks at the evidence: you check before you judge.'],
 ['Expecting a student from a “difficult” class to cause trouble, and watching them closely','J','Jumps to one cause: like the mothers in 1994, expectation shapes what you see.'],
 ['Checking whether a whole section struggled on a question before blaming individuals','S','Looks at the situation: maybe the question was unclear.'],
 ['Attributing a drop in focus to “screen time” without asking what happened','J','Jumps to one cause: maybe, but check first.'],
 ['Keeping notes on behaviour over several weeks before talking to a student about it','S','Looks at the evidence: patterns, not single moments.']]''','Looks at the situation or jumps to one cause?',r'''
 if(right>=7){title='You check before you judge';text=`${right} of 8 right. Look at the setting, notice your expectations, and gather evidence.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: what else could explain this, and what can I check?`}
 else{title='Worth another look';text=`${right} of 8 right. Quick single-cause explanations often reflect expectations. Situations, patterns and checked evidence are more reliable.`}''')+grid('''[
 ['The 1995 meta-analysis pooled how many double-blind studies?',['23','3','230'],0,'From 16 reports.'],
 ['In those studies, who knew which children had sugar?',['No one watching','The parents','The teachers'],0,'That’s what double-blind means.'],
 ['How many boys were in the 1994 expectations study?',['35','350','5'],0,'All described by mothers as sugar-sensitive.'],
 ['How many of those boys actually got sugar?',['None','Half','All'],0,'All got a sugar-free drink.'],
 ['Parties and holidays are exciting…',['With or without the cake','Only because of the cake','Never'],0,'Settings matter.'],
 ['Too much sugar…',['Still harms health','Is harmless','Improves focus'],0,'It just doesn’t explain the party.']]''','The pattern: in blind tests sugar doesn’t change behaviour; expectations change what we see.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['n07']
open('n07/template.html','w').write(page(o))
