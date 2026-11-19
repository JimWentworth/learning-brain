import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',4,'Left Brain, Right Brain: No Such Types','Left brain, right brain','You are not half a brain. Neither are your students.','Left brain, right brain',
'Logical, careful, good with numbers: left-brained. Creative, intuitive, artistic: right-brained. Many people know which one they are. But is anyone either?',
'<span><a href="#bT">Left, right, or both?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','par'],{'pfc':([60,730],'left'),'par':([560,-70],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the parietal lobe, at the top, glowing orange and labelled. Both hemispheres have these areas, and they work together.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>The idea grew from real science. In the 1960s, Roger Sperry and colleagues studied split-brain patients, whose two hemispheres had been surgically separated. Each side showed different strengths. Sperry later shared a Nobel Prize. Popular books stretched this into personality types.</p>
    <p>In 2013, Jared Nielsen and colleagues at the University of Utah tested the idea directly.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1,011</strong><span>people’s resting brain scans</span></div>
      <div role="listitem"><strong>7 to 29</strong><span>years old</span></div>
      <div role="listitem"><strong>7,000+</strong><span>brain regions analyzed</span></div>
      <div role="listitem"><strong>No types</strong><span>no left-brained or right-brained people</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The test</span>Local, not whole-brain</h2>
    <p>Nielsen’s team analyzed resting brain scans from 1,011 people, aged 7 to 29, across more than 7,000 brain regions. They found lateralized connections, but no left-brained or right-brained people. Lateralization looked like a local property of particular networks, not a whole-brain type.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Some functions lean</h2>
    <p>Some functions do lean to one side. For most people, language leans left, and attention to space leans right. But real tasks, from maths to painting, draw on both hemispheres working together.</p>
    <h2 class="sec"><span class="n">Why it matters</span>Labels aren’t harmless</h2>
    <p>A student who decides they are right-brained may give up on maths. One who decides they are left-brained may never try to draw. And the label distracts from what actually builds both kinds of skill: practice, with feedback.</p>
  </div>

'''+cls_html('bT','Left, right, or both?','Eight things the brain does. For each, decide: does it lean left for most people, lean right, or draw on both sides working together? You’ll get feedback after each one.',[('L','Leans left',''),('R','Leans right',''),('B','Both sides','')],'Leans left, right, or both?','Left, right, or both?','The question is always: is this a single function, or a whole real-world task?')+GRID_HTML+box('Avoid hemisphere labels in your teaching, including quizzes that sort students into types. Talk about skills, which can be practised, rather than brain sides, which sound fixed. Share this tip with students: don’t label yourself; both halves of your brain work on every task.'),
tips_h='You are not half a brain. Neither are your students.',
tips='''      <li><b>No hemisphere labels</b><span>Including “which side are you?” quizzes.</span></li>
      <li><b>Skills, not sides</b><span>Skills can be practised.</span></li>
      <li><b>Practice with feedback</b><span>Builds both kinds of skill.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1371/journal.pone.0071275">Nielsen, J. A., Zielinski, B. A., Ferguson, M. A., Lainhart, J. E., &amp; Anderson, J. S. (2013). An evaluation of the left-brain vs. right-brain hypothesis with resting state functional connectivity magnetic resonance imaging. <i>PLoS ONE, 8</i>(8), e71275.</a></li>''',
quiz='''[
 {q:'In the 2013 study of 1,011 people, researchers found…',o:['No left-brained or right-brained types','Mostly left-brained people','Mostly right-brained people'],a:0,f:'Lateralization was local, not a whole-brain type.'},
 {q:'For most people, language leans…',o:['Left','Right','Neither'],a:0,f:'And attention to space leans right.'},
 {q:'Real tasks like maths or painting use…',o:['Both hemispheres together','Only one side','Neither'],a:0,f:'So labels mislead.'}]''',
js=BASE+cls_js("{L:'Leans left',R:'Leans right',B:'Both sides'}",'''[
 ['Producing grammatical sentences when speaking','L','Leans left for most people: language is the classic example.'],
 ['Keeping track of where things are in the space around you','R','Leans right for most people: attention to space is the classic right-side example.'],
 ['Solving an algebra problem','B','Both sides: real tasks combine language, number, space and memory.'],
 ['Painting a landscape','B','Both sides: planning, seeing, movement and memory all take part.'],
 ['Understanding the meaning of spoken words','L','Leans left for most people: part of language.'],
 ['Writing a persuasive essay','B','Both sides: language, planning and judgment work together.'],
 ['Recognizing a familiar face','R','Leans right for many people, though both sides contribute.'],
 ['Playing a piano piece from memory','B','Both sides: hearing, timing, movement of both hands, and memory.']]''','Leans left, right, or both?',r'''
 if(right>=7){title='You see the difference';text=`${right} of 8 right. Some single functions lean to one side. Whole real-world tasks use both.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Single functions can lean; whole tasks draw on both sides.`}
 else{title='Worth another look';text=`${right} of 8 right. Language tends to lean left and attention to space right, but tasks like maths, painting and writing use both hemispheres.`}''')+grid('''[
 ['Split-brain research in the 1960s was led by…',['Roger Sperry','William James','Howard Gardner'],0,'He later shared a Nobel Prize.'],
 ['The 2013 Utah study analyzed scans from about how many people?',['1,000','100','10,000'],0,'1,011 people, aged 7 to 29.'],
 ['Across more than 7,000 brain regions, they found…',['Lateralized connections, but no brain types','Clear left- and right-brained people','No lateralization at all'],0,'Lateralization was local.'],
 ['For most people, attention to space leans…',['Right','Left','Neither'],0,'And language leans left.'],
 ['A student who labels themselves right-brained may…',['Give up on maths','Get better at maths','Be unaffected'],0,'Labels can discourage practice.'],
 ['What builds both kinds of skill?',['Practice, with feedback','Finding your dominant side','Brain exercises for one side'],0,'Skills, not sides.']]''','The pattern: some functions lean, but people don’t come in left- and right-brained types.'))
open('n04/template.html','w').write(page(o))
