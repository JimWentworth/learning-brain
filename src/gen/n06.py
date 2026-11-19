import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',6,'The Mozart Effect: How a Small Finding Grew','The Mozart effect','Enjoy Mozart for Mozart. That is reason enough.','The Mozart effect',
'Play Mozart, get smarter. It became a news story, a parenting trend and a shelf of baby products. It started with one short paper.',
'<span><a href="#eT">Predict what happened</a></span><span><a href="#bT">Study or headline?</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','par'],{'tem':([600,770],'left'),'par':([560,-70],'left')},'Drawing of the side of the brain with the temporal lobe, at the side, where music is heard, and the parietal lobe, at the top, involved in spatial reasoning, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 1993, Frances Rauscher and colleagues reported in <i>Nature</i> that college students did better on a spatial reasoning task after ten minutes of a Mozart sonata. The boost was small, and it faded within about fifteen minutes. Rauscher stressed that the test measured only one kind of spatial ability.</p>
  </div>

'''+pred_html('eT','Predict what happened','Three quick predictions about what happened next, then see the results. About 1 minute.','From paper to legend','How a small, short-lived result travelled.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>10 minutes</strong><span>of Mozart before a spatial task, in 1993</span></div>
      <div role="listitem"><strong>~15 minutes</strong><span>before the small boost faded</span></div>
      <div role="listitem"><strong>~40 studies</strong><span>with more than 3,000 people, pooled in 2010</span></div>
      <div role="listitem"><strong>Small</strong><span>versus silence; smaller still versus other music</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The stretch</span>From students to babies</h2>
    <p>Headlines turned a brief effect on one kind of task into: Mozart makes you smarter. And then: Mozart makes babies smarter, which the study never tested. By the late 1990s, more news stories about the effect mentioned babies than college students.</p>
    <h2 class="sec"><span class="n">The evidence</span>Hard to replicate</h2>
    <p>Other labs found the result hard to replicate. In 2010, Jakob Pietschnig and colleagues pooled nearly 40 studies with more than 3,000 people. Compared with silence or no stimulus, the effect was small. Compared with other music, it was smaller still. And studies by the original research group found noticeably larger effects than studies by others.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Mood and alertness</h2>
    <p>A short burst of music you enjoy can lift mood and alertness for a while, which may help briefly. But that is not Mozart, and it is not intelligence. The bigger lesson is how a small, short-lived finding became a lasting belief, simply by being repeated.</p>
  </div>

'''+cls_html('bT','Study or headline?','Eight statements about the Mozart effect. For each, decide: is it what the research found, or what headlines turned it into? You’ll get feedback after each one.',[('S','What the study found',''),('H','The headline stretch','')],'Study or headline?','Study or headline?','The question is always: who was tested, on what task, and for how long?')+GRID_HTML+box('Treat music in class or study as a mood choice, not a cognitive enhancer. For students who study with lyrics, suggest trying silence or instrumental music for hard reading. Share this tip with students: play music you enjoy for mood, not for IQ.'),
tips_h='Enjoy Mozart for Mozart. That is reason enough.',
tips='''      <li><b>Music is a mood choice</b><span>Not a cognitive enhancer.</span></li>
      <li><b>Hard reading</b><span>Try silence or instrumental music.</span></li>
      <li><b>Watch the stretch</b><span>Who was tested, on what, for how long?</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/365611a0">Rauscher, F. H., Shaw, G. L., &amp; Ky, K. N. (1993). Music and spatial task performance. <i>Nature, 365</i>, 611.</a></li>
        <li><a href="https://doi.org/10.1016/j.intell.2010.03.001">Pietschnig, J., Voracek, M., &amp; Formann, A. K. (2010). Mozart effect–Shmozart effect: A meta-analysis. <i>Intelligence, 38</i>(3), 314–323.</a></li>
        <li>Bangerter, A., &amp; Heath, C. (2004). The Mozart effect: Tracking the evolution of a scientific legend. <i>British Journal of Social Psychology, 43</i>(4), 605–623.</li>''',
quiz='''[
 {q:'The 1993 study tested…',o:['College students on one spatial task','Babies’ intelligence','Adults’ IQ over a year'],a:0,f:'And the boost faded in about 15 minutes.'},
 {q:'Compared with other music, the effect was…',o:['Smaller still','Much larger','Exactly the same as versus silence'],a:0,f:'Pietschnig and colleagues, 2010.'},
 {q:'The grain of truth is that music you enjoy can…',o:['Briefly lift mood and alertness','Raise IQ','Make babies smarter'],a:0,f:'That’s not Mozart, and not intelligence.'}]''',
js=BASE+pred_js('''[
 ['In the 1993 study, how long did the small boost last?',['About 15 minutes','About a week','Permanently'],0,'About 15 minutes, on one kind of spatial task.'],
 ['By the late 1990s, news stories about the effect more often mentioned…',['College students','Babies','Neither'],1,'Babies, who were never tested.'],
 ['When about 40 studies were pooled in 2010, the effect compared with other music was…',['Large','Smaller still than the small effect versus silence','Exactly zero, everywhere'],1,'Smaller still. Music in general mattered more than Mozart.']]''',
'''<p class="gh">Tested in 1993</p><p class="mtext">College students, one spatial task, a small boost lasting about 15 minutes.</p><p class="gh">What spread</p><p class="mtext">“Mozart makes you smarter”, then “Mozart makes babies smarter”, which was never tested.</p>''',
r''' if(n===3){title='You saw it coming';text='All 3 right. A small, brief effect on one task in college students became a belief about babies, through repetition alone.'}
 else if(!got[1]){title='The stretch';text=`You got ${n} of 3. Babies were never tested, but by the late 1990s they dominated the news coverage.`}
 else{title='A small finding, a big legend';text=`You got ${n} of 3. The effect was brief and small, and smaller still compared with other music.`}''')+cls_js("{S:'What the study found',H:'The headline stretch'}",'''[
 ['College students did slightly better on a spatial task after ten minutes of Mozart','S','What the study found: one task, one group, a small effect.'],
 ['Mozart makes you smarter','H','The headline stretch: one kind of spatial task is not intelligence.'],
 ['The boost faded within about fifteen minutes','S','What the study found: brief.'],
 ['Playing Mozart to babies raises their IQ','H','The headline stretch: babies were never tested.'],
 ['Other labs found the result hard to replicate','S','What the research found, in the years after.'],
 ['Classical music in the classroom improves learning','H','The headline stretch: the study tested neither classrooms nor learning.'],
 ['Compared with other music, the effect was smaller still','S','What the research found: Pietschnig and colleagues, 2010.'],
 ['A Mozart CD for every newborn will build better brains','H','The headline stretch: a policy built on a result about college students and one task.']]''','Study or headline?',r'''
 if(right>=7){title='You can see the stretch';text=`${right} of 8 right. Who was tested, on what task, for how long: that’s where headlines drift.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. The study was college students, one spatial task, about fifteen minutes.`}
 else{title='Worth another look';text=`${right} of 8 right. The research found a small, brief effect on one task. Claims about intelligence, babies or classrooms were headlines.`}''')+grid('''[
 ['The 1993 study was published in…',['Nature','A parenting magazine','A music journal'],0,'Rauscher and colleagues.'],
 ['Students listened to Mozart for about…',['10 minutes','10 hours','10 days'],0,'Then did a spatial task.'],
 ['The study measured…',['One kind of spatial ability','General intelligence','Babies’ development'],0,'Rauscher stressed this.'],
 ['In 2010, Pietschnig and colleagues pooled about how many studies?',['40','4','400'],0,'More than 3,000 people.'],
 ['Studies by the original research group found…',['Noticeably larger effects than others','Smaller effects','No effect'],0,'A warning sign.'],
 ['The myth spread mainly by…',['Being repeated','New evidence','Large trials'],0,'A lesson about legends.']]''','The pattern: a small, brief effect on one task became a lasting belief through repetition.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['n06']
open('n06/template.html','w').write(page(o))
