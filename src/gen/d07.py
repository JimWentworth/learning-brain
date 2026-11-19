import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(7,'Laptop or Longhand? What the Note-Taking Evidence Shows','Laptop or longhand?','It’s not the pen or the keyboard. It’s what you do with the words.','Laptop or longhand?',
'“The pen is mightier than the keyboard.” In 2014, a study with that title made headlines and changed laptop policies in classrooms everywhere. What happened next is a good lesson in how science works.',
'<span><a href="#bT">Transcribe or transform?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which helps select and rephrase ideas, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>Pam Mueller and Daniel Oppenheimer found that students who typed notes wrote more words and copied more of the lecture word for word. Students who wrote by hand did better on conceptual questions. The explanation: handwriting is slower, so you have to choose and rephrase.</p>
    <p>Then came direct replications.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2014</strong><span>the original study: handwriting ahead on conceptual questions</span></div>
      <div role="listitem"><strong>2019, 2021</strong><span>close replications: no clear difference</span></div>
      <div role="listitem"><strong>24</strong><span>studies of college students pooled in 2024</span></div>
      <div role="listitem"><strong>~0.25</strong><span>effect size favouring handwritten notes: small</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Replications</span>Smaller than the headlines</h2>
    <p>In 2019, Kayla Morehead, John Dunlosky and Katherine Rawson repeated the study closely. They found only small differences favouring handwriting, which were not statistically significant. A preregistered replication in 2021, led by Heather Urry, also found no clear difference on the quiz.</p>
    <h2 class="sec"><span class="n">Pooled</span>A small edge for handwriting</h2>
    <p>In 2024, Abraham Flanigan and colleagues pooled 24 studies of college students. Taking and reviewing handwritten notes was linked to higher achievement, with a small effect size of about a quarter of a standard deviation. Typing produced far more notes.</p>
    <h2 class="sec"><span class="n">So what?</span>Method over medium</h2>
    <p>Across studies, handwriting seems to have a small edge, as students currently take notes. But the medium matters less than the method. Notes that select, rephrase and connect ideas beat notes that transcribe, whatever the device. And for some students, a laptop is not a preference but an accommodation. Any policy needs to protect that.</p>
  </div>

'''+cls_html('bT','Transcribe or transform?','Eight note-taking habits. For each, decide: does it just transcribe the lecture, or transform it, by selecting, rephrasing and connecting? You’ll get feedback after each one.',[('T','Transcribes',''),('F','Transforms','')],'Transcribes or transforms?','Transcribe or transform?','The question is always: is the student choosing and rephrasing, or copying?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Still debated</h2>
    <p>The original effect was larger than the replications. The pooled edge is small, and it reflects how students currently take notes on each device, not a fixed property of pens or keyboards.</p>
  </div>

'''+GRID_HTML+box('Teach students how to take notes: main ideas, in their own words, with sketches of key diagrams. Leave pauses so they can catch up and revise. Let students choose their medium, while explaining the trade-offs. Protect accommodations. Share this tip with students: take fewer notes, in your own words.'),
tips_h='It’s not the pen or the keyboard. It’s what you do with the words.',
tips='''      <li><b>Main ideas, in your own words</b><span>Select, rephrase, connect.</span></li>
      <li><b>Pauses to catch up</b><span>And to revise notes.</span></li>
      <li><b>Choice, with the trade-offs</b><span>And accommodations protected.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/0956797614524581">Mueller, P. A., &amp; Oppenheimer, D. M. (2014). The pen is mightier than the keyboard: Advantages of longhand over laptop note taking. <i>Psychological Science, 25</i>(6), 1159–1168.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-019-09468-2">Morehead, K., Dunlosky, J., &amp; Rawson, K. A. (2019). How much mightier is the pen than the keyboard for note-taking? A replication and extension of Mueller and Oppenheimer (2014). <i>Educational Psychology Review, 31</i>, 753–780.</a></li>
        <li><a href="https://doi.org/10.1177/0956797620965541">Urry, H. L., et al. (2021). Don’t ditch the laptop just yet: A direct replication of Mueller and Oppenheimer’s (2014) Study 1 plus mini meta-analyses across similar studies. <i>Psychological Science, 32</i>(3), 326–339.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-024-09914-w">Flanigan, A. E., et al. (2024). Typed versus handwritten lecture notes and college student achievement: A meta-analysis. <i>Educational Psychology Review, 36</i>, 78.</a></li>''',
quiz='''[
 {q:'Close replications of the 2014 study found…',o:['Small, non-significant differences','A much bigger handwriting advantage','A laptop advantage'],a:0,f:'Morehead 2019; Urry 2021.'},
 {q:'The 2024 meta-analysis found handwriting’s edge was…',o:['Small: about 0.25','Large: about 1.0','Zero'],a:0,f:'Flanigan and colleagues, 24 studies.'},
 {q:'What matters most?',o:['Selecting and rephrasing, whatever the device','The device itself','How many words you write'],a:0,f:'Method over medium.'}]''',
js=BASE+cls_js("{T:'Transcribes',F:'Transforms'}",'''[
 ['Typing everything the lecturer says, word for word','T','Transcribes: lots of words, little thinking. This was the pattern in the 2014 study.'],
 ['Writing the main idea of each section in one sentence of your own','F','Transforms: you have to choose what matters and rephrase it.'],
 ['Sketching the diagram from the slide, with your own labels','F','Transforms: redrawing makes you work out how the parts connect.'],
 ['Copying each slide’s bullet points exactly','T','Transcribes: the slides already exist. Copying adds little.'],
 ['Adding an arrow linking today’s idea to last week’s','F','Transforms: connecting ideas builds understanding.'],
 ['Writing a question in the margin about something unclear','F','Transforms: it marks a gap to fix, which is real thinking.'],
 ['Recording the lecture and planning to take notes later, but never doing it','T','Neither, really, and that’s the problem: no selecting or rephrasing ever happens.'],
 ['During a pause, rereading your notes and filling in a step you missed','F','Transforms: revising notes in a pause makes you check and complete the ideas.']]''','Transcribes or transforms?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Good notes select, rephrase and connect. That matters more than pen or keyboard.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: is the student choosing and rephrasing, or copying?`}
 else{title='Worth another look';text=`${right} of 8 right. Copying words or slides transcribes. Summarizing, sketching, connecting and questioning transform.`}''')+grid('''[
 ['In the 2014 study, students who typed…',['Wrote more and copied more word for word','Wrote less','Drew more diagrams'],0,'Mueller and Oppenheimer.'],
 ['In 2014, handwriters did better on…',['Conceptual questions','Every kind of question','Nothing'],0,'The headline result.'],
 ['The 2019 close replication found…',['Small differences, not statistically significant','A bigger handwriting advantage','A laptop advantage'],0,'Morehead, Dunlosky and Rawson.'],
 ['The 2021 preregistered replication found…',['No clear difference on the quiz','A large handwriting advantage','A large laptop advantage'],0,'Led by Heather Urry.'],
 ['Pooling 24 studies in 2024, handwriting was linked to…',['Slightly higher achievement','Much higher achievement','Lower achievement'],0,'An effect size of about 0.25.'],
 ['In the same analysis, typing produced…',['Far more notes','Fewer notes','The same amount'],0,'More words, not more learning.']]''','The pattern: a small edge for handwriting as students take notes now; the method matters more than the device.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['d07']
open('d07/template.html','w').write(page(o))
