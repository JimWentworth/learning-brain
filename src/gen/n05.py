import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',5,'Brain-Training Games: Better at the Game, Not at Everything','Brain-training games','You get better at what you practise. So practise what matters.','Brain-training games',
'Ten minutes a day of brain games, and you will think faster, remember more and focus better. That was the promise. What did the evidence show?',
'<span><a href="#bT">Does the evidence back it?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','hip'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which supports working memory, and the hippocampus, deep inside, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>By 2014, scientists were split. One open letter, from about seventy researchers, objected to brain-training claims. Another, from more than a hundred, defended them.</p>
    <p>So in 2016, Daniel Simons of the University of Illinois and six colleagues reviewed the studies cited in support of brain training, more than 130 of them. They asked: how big was the study, was there a proper control group, and did the results match the claims?</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>130+</strong><span>studies cited in support, reviewed in 2016</span></div>
      <div role="listitem"><strong>Better</strong><span>at the trained games</span></div>
      <div role="listitem"><strong>Little</strong><span>evidence of transfer to everyday thinking</span></div>
      <div role="listitem"><strong>$2 million</strong><span>paid by Lumosity’s maker to settle FTC deceptive-advertising charges</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The review</span>Near gains, far claims</h2>
    <p>Many studies were small or lacked good controls. The better studies showed that people got better at the trained games. But there was little evidence that the gains transferred to everyday thinking, at work or at school. The authors did not say training can never work, only that the evidence did not yet support the claims.</p>
    <h2 class="sec"><span class="n">Regulators</span>The FTC settlement</h2>
    <p>In 2016, the company behind Lumosity agreed to pay $2 million to settle Federal Trade Commission charges of deceptive advertising. The company has since scaled back its claims.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Practice works on what you practise</h2>
    <p>Practice really does improve what you practise. That is exactly why the games get easier. The trouble is the leap from a game to everything else.</p>
  </div>

'''+cls_html('bT','Does the evidence back it?','Eight claims about practice and training. For each, decide: does the evidence support it, or not? You’ll get feedback after each one.',[('Y','Supported',''),('N','Not supported','')],'Supported or not?','Does the evidence back it?','The question is always: is the gain in the thing practised, or is it a leap to something else?')+GRID_HTML+box('Have students practise the actual skills your course needs, with feedback, in varied contexts. Build transfer on purpose, by showing the same idea in different settings. Share this tip with students: practise the actual skill you want to improve.'),
tips_h='You get better at what you practise. So practise what matters.',
tips='''      <li><b>Practise the real skill</b><span>With feedback.</span></li>
      <li><b>Varied contexts</b><span>The same idea in different settings.</span></li>
      <li><b>Teach transfer on purpose</b><span>It rarely happens by itself.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1177/1529100616661983">Simons, D. J., Boot, W. R., Charness, N., Gathercole, S. E., Chabris, C. F., Hambrick, D. Z., &amp; Stine-Morrow, E. A. L. (2016). Do “brain-training” programs work? <i>Psychological Science in the Public Interest, 17</i>(3), 103–186.</a></li>
        <li>Federal Trade Commission. (2016, January 5). Lumosity to pay $2 million to settle FTC deceptive advertising charges for its “brain training” program [Press release].</li>''',
quiz='''[
 {q:'The better brain-training studies showed people got better at…',o:['The trained games','Everything','Nothing'],a:0,f:'Near gains.'},
 {q:'Evidence that gains transferred to everyday thinking was…',o:['Little','Strong','Overwhelming'],a:0,f:'Simons and colleagues, 2016.'},
 {q:'To improve a skill, students should…',o:['Practise the actual skill','Play a general brain game','Rest'],a:0,f:'You get better at what you practise.'}]''',
js=BASE+cls_js("{Y:'Supported',N:'Not supported'}",'''[
 ['Players get better at the brain-training games they practise','Y','Supported: the better studies showed improvement on the trained games.'],
 ['Ten minutes of brain games a day will improve your grades','N','Not supported: little evidence that gains transfer to school performance.'],
 ['Practising fraction problems improves fraction problems','Y','Supported: practice improves what you practise.'],
 ['A memory game will help you remember names at work','N','Not supported: the leap from a game to everyday memory lacked good evidence.'],
 ['Practising a skill in varied settings helps you use it in new ones','Y','Supported by learning research more broadly: varied practice is one way to build transfer on purpose.'],
 ['Brain games can delay everyday cognitive decline','N','Not supported by the 2016 review: claims went beyond the evidence.'],
 ['Small studies without proper control groups prove brain training works','N','Not supported: many cited studies were small or lacked good controls.'],
 ['Some kinds of training might help in future, with better studies','Y','Consistent with the review: the authors said the evidence did not yet support the claims, not that training can never work.']]''','Supported or not?',r'''
 if(right>=7){title='You can spot the leap';text=`${right} of 8 right. Practice improves what you practise. The claims fail at the leap from a game to everything else.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: is the gain in the thing practised, or a leap to something else?`}
 else{title='Worth another look';text=`${right} of 8 right. Trained games improve; everyday thinking, grades and memory at work showed little benefit in the evidence reviewed.`}''')+grid('''[
 ['In 2014, scientists’ open letters on brain training…',['Disagreed','All agreed','Didn’t exist'],0,'About seventy objected; more than a hundred defended.'],
 ['The 2016 review was led by Daniel Simons of…',['The University of Illinois','Lumosity','The FTC'],0,'With six colleagues.'],
 ['Many of the cited studies were…',['Small or lacked good controls','Large and well-controlled','Not about brain training'],0,'A common problem.'],
 ['The better studies showed improvement on…',['The trained games','School grades','Work performance'],0,'Near, not far, transfer.'],
 ['In 2016, the company behind Lumosity agreed to pay…',['$2 million','$2,000','$200 million'],0,'To settle FTC deceptive-advertising charges.'],
 ['Did the reviewers say training can never work?',['No: the evidence didn’t yet support the claims','Yes','They didn’t say'],0,'A careful conclusion.']]''','The pattern: practice improves what you practise; the leap to everything else lacks evidence.'))
open('n05/template.html','w').write(page(o))
