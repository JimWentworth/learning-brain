import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',11,'Digital Natives and Multitaskers','Digital natives and multitaskers','No one is born digital. Skills with information are learned, and they can be taught.','Digital natives and multitaskers',
'Today’s students grew up with screens. So they must be fluent with information, and able to handle several streams at once. That is the digital native idea.',
'<span><a href="#bT">Comfort or skill?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','par'],{'pfc':([60,730],'left'),'par':([560,-70],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which switches between tasks, and the parietal lobe, at the top, involved in attention, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>The term came from a 2001 article by Marc Prensky. He argued that students born into digital technology think and learn differently, and that teaching must change to match.</p>
    <p>In 2017, Paul Kirschner and Pedro De Bruyckere reviewed the evidence.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2001</strong><span>Marc Prensky coins “digital natives”</span></div>
      <div role="listitem"><strong>No sign</strong><span>of an information-savvy generation, a 2017 review found</span></div>
      <div role="listitem"><strong>Switching</strong><span>not true multitasking, for thinking tasks</span></div>
      <div role="listitem"><strong>A cost</strong><span>in time and errors with each switch</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Claim 1</span>Information-savvy?</h2>
    <p>Kirschner and De Bruyckere found no sign of an information-savvy generation. Using technology often is not the same as using it well, for searching, judging sources or learning.</p>
    <h2 class="sec"><span class="n">Claim 2</span>Multitaskers?</h2>
    <p>The second claim fares no better. People do not really do two thinking tasks at once. They switch between them. Each switch has a cost in time and errors, and designing learning around multitasking hinders rather than helps.</p>
    <h2 class="sec"><span class="n">Why it matters</span>Skills we don’t teach</h2>
    <p>If we assume students already have digital skills, we may not teach them. And older instructors may wrongly assume they cannot keep up.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Comfort is not skill</h2>
    <p>Young people are often comfortable with devices and quick to try new apps. But comfort is not the same as skill. The Digital Learning series looks at screens, slides, video and online courses, and what the evidence says about each.</p>
  </div>

'''+cls_html('bT','Comfort or skill?','Eight things a student might do online. For each, decide: does it show comfort with devices, or a learned information skill? You’ll get feedback after each one.',[('C','Comfort with devices',''),('S','A learned skill','')],'Comfort or skill?','Comfort or skill?','The question is always: does this take judgment that has to be taught, or just familiarity?')+GRID_HTML+box('Teach information skills explicitly, like evaluating sources and searching well. Design study and class time for one task at a time. And don’t assume age predicts skill, in either direction. Share this tip with students: one task, one screen, during study.'),
tips_h='No one is born digital. Skills with information are learned, and they can be taught.',
tips='''      <li><b>Teach information skills</b><span>Evaluating sources, searching well.</span></li>
      <li><b>One task at a time</b><span>In study and in class.</span></li>
      <li><b>Age doesn’t predict skill</b><span>In either direction.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1108/10748120110424816">Prensky, M. (2001). Digital natives, digital immigrants. <i>On the Horizon, 9</i>(5), 1–6.</a></li>
        <li><a href="https://doi.org/10.1016/j.tate.2017.06.001">Kirschner, P. A., &amp; De Bruyckere, P. (2017). The myths of the digital native and the multitasker. <i>Teaching and Teacher Education, 67</i>, 135–142.</a></li>''',
quiz='''[
 {q:'The 2017 review found…',o:['No sign of an information-savvy generation','Today’s students are expert searchers','Older people can’t use technology'],a:0,f:'Kirschner and De Bruyckere.'},
 {q:'For thinking tasks, what people call multitasking is really…',o:['Switching, with a cost each time','Doing two things at once','A special talent'],a:0,f:'Time and errors add up.'},
 {q:'Comfort with devices is…',o:['Not the same as skill','The same as skill','Bad'],a:0,f:'Skills can be taught.'}]''',
js=BASE+cls_js("{C:'Comfort with devices',S:'A learned skill'}",'''[
 ['Installing and trying a new app in minutes','C','Comfort: quick and familiar, but no judgment about information involved.'],
 ['Checking who runs a website before trusting its claims','S','A learned skill: evaluating sources has to be taught.'],
 ['Typing fast on a phone','C','Comfort: a motor habit, not information skill.'],
 ['Opening other tabs to see what others say about a source','S','A learned skill: reading laterally, as fact-checkers do.'],
 ['Keeping chat, video and homework open all at once','C','Comfort, not skill: switching between them costs time and errors.'],
 ['Choosing search terms that narrow results to good evidence','S','A learned skill: searching well takes practice.'],
 ['Finding the share button in any app','C','Comfort: familiarity with interfaces.'],
 ['Noticing that a viral chart has no source and no axis labels','S','A learned skill: judging evidence is taught, not absorbed.']]''','Comfort or skill?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Comfort comes from use. Information skills come from teaching.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does this take judgment that has to be taught?`}
 else{title='Worth another look';text=`${right} of 8 right. Using apps fast is comfort. Judging sources, searching well and spotting weak evidence are skills.`}''')+grid('''[
 ['“Digital natives” came from a 2001 article by…',['Marc Prensky','Howard Gardner','John Bruer'],0,'He argued teaching must change.'],
 ['In 2017, Kirschner and De Bruyckere found…',['No sign of an information-savvy generation','Proof of digital natives','Older people are better at everything'],0,'Using tech often isn’t using it well.'],
 ['For two thinking tasks, people…',['Switch between them','Do both at once','Do neither'],0,'Each switch has a cost.'],
 ['Designing learning around multitasking…',['Hinders rather than helps','Helps a lot','Has no effect'],0,'One task at a time.'],
 ['If we assume students already have digital skills, we may…',['Not teach them','Teach them twice','Ban devices'],0,'A hidden cost of the myth.'],
 ['Does age predict digital skill?',['Not reliably, in either direction','Yes, younger is always better','Yes, older is always better'],0,'Skills are learned.']]''','The pattern: comfort with devices isn’t skill with information, and multitasking is switching.'))
open('n11/template.html','w').write(page(o))
