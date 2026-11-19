import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',9,'Multiple Intelligences in the Classroom','Multiple intelligences','Many ways to show an idea, yes. Eight kinds of student, no.','Multiple intelligences',
'Linguistic. Logical-mathematical. Spatial. Musical. Bodily-kinesthetic. Interpersonal. Intrapersonal. Naturalist. Eight kinds of smart. Many teachers plan lessons around them. Should they?',
'<span><a href="#bT">Content or type?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','par'],{'pfc':([60,730],'left'),'par':([560,-70],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the parietal lobe, at the top, glowing orange and labelled. These areas support many kinds of thinking, not one each.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 1983, psychologist Howard Gardner proposed multiple intelligences: separate abilities, each with its own brain basis. It was a generous idea that challenged a single number for intelligence, and teachers embraced it.</p>
    <p>But the theory makes testable claims.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1983</strong><span>Howard Gardner proposes multiple intelligences</span></div>
      <div role="listitem"><strong>Go together</strong><span>scores on the “separate” abilities tend to correlate</span></div>
      <div role="listitem"><strong>No distinct</strong><span>brain systems found for each intelligence</span></div>
      <div role="listitem"><strong>2006, 2023</strong><span>reviews: the theory lacks empirical support</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The test</span>Separate, or together?</h2>
    <p>If the intelligences are separate, scores on them should be largely independent. Studies found the opposite: they tend to go together. And researchers have not found distinct brain systems for each one.</p>
    <p>In reviews in 2006 and 2023, Lynn Waterhouse concluded that the theory lacks empirical support, and that studies of teaching to the intelligences were not done by standard scientific methods. Even so, the idea remains popular in teacher training.</p>
    <h2 class="sec"><span class="n">Gardner’s own line</span>Not learning styles</h2>
    <p>Gardner himself has drawn a line. He says multiple intelligences are not learning styles, and that matching lessons to a student’s intelligence is a misreading of his work.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Many representations</h2>
    <p>People do have different strengths and interests. And showing an idea in more than one way, a graph, an equation, a story, can deepen understanding for everyone.</p>
  </div>

'''+cls_html('bT','Content or type?','Eight lesson plans. For each, decide: is the representation chosen because the content needs it, or to match students to an intelligence type? You’ll get feedback after each one.',[('C','The content needs it',''),('T','Matching a type','')],'The content needs it, or matching a type?','Content or type?','The question is always: would every student understand this idea better with this representation?')+GRID_HTML+box('Choose representations because the content needs them, not to match student types. Value many kinds of talent without sorting students into boxes. And put planning time into methods with strong evidence. Share this tip with students: use many representations because the content needs them, not because you are a type.'),
tips_h='Many ways to show an idea, yes. Eight kinds of student, no.',
tips='''      <li><b>Representations for the content</b><span>Graph, equation, story.</span></li>
      <li><b>Value many talents</b><span>Without sorting into boxes.</span></li>
      <li><b>Plan with strong methods</b><span>Retrieval, spacing, feedback.</span></li>''',
sources='''        <li>Gardner, H. (1983). <i>Frames of mind: The theory of multiple intelligences</i>. Basic Books.</li>
        <li><a href="https://doi.org/10.1207/s15326985ep4104_1">Waterhouse, L. (2006). Multiple intelligences, the Mozart effect, and emotional intelligence: A critical review. <i>Educational Psychologist, 41</i>(4), 207–225.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2023.1217288">Waterhouse, L. (2023). Why multiple intelligences theory is a neuromyth. <i>Frontiers in Psychology, 14</i>, 1217288.</a></li>''',
quiz='''[
 {q:'If the intelligences were separate, scores on them should be…',o:['Largely independent','Highly correlated','Identical'],a:0,f:'Studies found they tend to go together.'},
 {q:'Gardner says multiple intelligences are…',o:['Not learning styles','The same as learning styles','A way to sort students'],a:0,f:'Matching lessons misreads his work.'},
 {q:'Showing an idea in several ways helps…',o:['Everyone, when the content needs it','Only one type of student','No one'],a:0,f:'The grain of truth.'}]''',
js=BASE+cls_js("{C:'The content needs it',T:'Matching a type'}",'''[
 ['Teaching exponential growth with a graph, an equation and a story about doubling','C','The content needs it: each view shows a different side of the same idea, for everyone.'],
 ['Letting “musical” students learn the periodic table only by song','T','Matching a type: and they miss what the table’s structure shows.'],
 ['Using a timeline to teach the order of historical events','C','The content needs it: order in time is shown clearly on a line.'],
 ['Sorting the class into eight intelligence groups with different worksheets','T','Matching a type: little evidence that this helps, and Gardner says it misreads his work.'],
 ['Having everyone build a physical model of a molecule’s shape','C','The content needs it: 3D shape is easier to grasp in 3D, for everyone.'],
 ['Giving “interpersonal” students only group work, and “intrapersonal” students only solo work','T','Matching a type: both kinds of work have value for everyone.'],
 ['Showing a worked example and a diagram for a physics problem','C','The content needs it: worked examples and diagrams help nearly everyone learn problem solving.'],
 ['Telling a student they’re not “logical-mathematical”, so algebra isn’t for them','T','Matching a type: a label that can discourage practice.']]''','The content needs it, or matching a type?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Choose representations for the content, and offer them to everyone.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: would every student understand this better this way?`}
 else{title='Worth another look';text=`${right} of 8 right. Graphs, timelines, models and worked examples fit their content. Sorting students into intelligence types lacks support.`}''')+grid('''[
 ['Howard Gardner proposed multiple intelligences in…',['1983','1903','2013'],0,'Frames of Mind.'],
 ['How many intelligences are commonly listed today?',['Eight','Two','Twenty'],0,'Including naturalist.'],
 ['Scores on the “separate” intelligences tend to…',['Go together','Be unrelated','Be opposites'],0,'The opposite of what the theory predicts.'],
 ['Have researchers found a distinct brain system for each intelligence?',['No','Yes','For half of them'],0,'Waterhouse’s reviews.'],
 ['Waterhouse reviewed the evidence in…',['2006 and 2023','1983 only','Never'],0,'Concluding it lacks empirical support.'],
 ['According to Gardner, matching lessons to a student’s intelligence is…',['A misreading of his work','What he recommends','Required'],0,'He has drawn that line himself.']]''','The pattern: a generous idea, but the testable claims haven’t held up; choose representations for the content.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['n09']
open('n09/template.html','w').write(page(o))
