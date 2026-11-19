import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m08',n='8',label='The Learning Brain · Memory · Topic 8',epi='The Learning Brain, Memory, episode 8',
title='Reconsolidation: Remembering Opens a Memory',h1='Reconsolidation',em='Remembering opens a memory for editing',read='8',mins='2½ minutes',vtitle='Reconsolidation',
dek='Recalling a memory may make it open to change for a few hours, before it is stored again. A surprise seems to be what opens it. In people, the evidence is mixed.',
jumps='<span><a href="#bT">Will the memory open?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the amygdala and the hippocampus, both deep inside, glowing orange and labelled. In rats, a reminder made a fear memory in the amygdala need new proteins to be stored again.',
hero_js="BR.R.amy.lab=[300,770];BR.R.amy.al='right';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['amy','hip'],labels:['amy','hip'],labelT:{amy:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>Rats learned that a tone meant a shock. A day later, the tone was played again, and a drug that blocks protein synthesis was put into the <a href="@@LB:amy@@">amygdala</a>. The next day, the fear was gone. Without the reminder, the same drug did nothing. Given six hours later, it did nothing either. Karim Nader, Glenn Schafe and Joseph LeDoux reported this in 2000.</p>
    <p>So retrieval doesn’t just read a memory. It can unlock it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>6 hours</strong><span>after the reminder, the drug no longer had any effect</span></div>
      <div role="listitem"><strong>10 minutes vs 6 hours</strong><span>between reminder and new learning: only the first stopped an old fear returning</span></div>
      <div role="listitem"><strong>A year</strong><span>later, that effect was still there in the people retested</span></div>
      <div role="listitem"><strong>4</strong><span>direct replications of a well-known human motor study that found no effect</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Reconsolidation</span>Open, then stored again</h2>
    <p>The <a href="#" id="m06link">engram</a> becomes unstable again for a few hours after it’s recalled, and then has to be stored again. This is reconsolidation.</p>
    <h2 class="sec"><span class="n">In people</span>Reminders let new things in</h2>
    <p>In 2007, Almut Hupbach, Lynn Nadel and colleagues had students learn a set of objects on day one. On day two, some were reminded of that session, in the same room, then learned a second set. On day three, asked for the first set, the reminded group mixed in objects from the second; without the reminder, students rarely did. The mixing showed up only after a delay.</p>
    <p>Reopening a memory may also allow updating. In 2010, Daniela Schiller, Elizabeth Phelps and colleagues taught people to fear a coloured square. A reminder 10 minutes before extinction training, where the square appeared without shocks, stopped the fear from returning; a reminder 6 hours before didn’t. In those retested, the effect lasted at least a year.</p>
    <p>One condition seems to matter. In 2013, Dieuwke Sevenster, Tom Beckers and Merel Kindt found that a memory opened only if something about the reminder was unexpected. Without that prediction error, it stayed locked.</p>
  </div>

'''+cls_html('bT','Will the memory open?','Ten cases, from the studies and from classrooms. For each, decide whether the memory opens and can change, stays locked because nothing was surprising, is reminded too late, or was never reminded. You’ll get feedback after each one.',[('O','Opens','and can change'),('L','Stays locked','no surprise'),('T','Too late','window closed'),('N','No reminder','never reopened')],'Will the memory open?','Will it open?','A memory seems to open when it’s recalled, something is unexpected, and the change comes within hours.')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Mixed results in people</h2>
    <p>Human results are mixed. In 2016, Tom Hardwicke, Mahdi Taqi and David Shanks made four direct attempts to replicate a well-known motor-skill study of reconsolidation and found no effect, and some fear studies haven’t replicated either. Whether old memories are rewritten, or simply outcompeted by new ones, is still debated.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Bring it out, then surprise it</h3>
      <p>Bring out students’ existing ideas before you correct them. Then show something that surprises them, which links this to <a href="@@LB:lb04@@">the power of prediction</a>. And when two topics are similar, mark the differences clearly, since reactivated memories can absorb new material.</p>
    </aside>
  </div>
''',
tips_h='Remembering opens a memory for editing',
tips='''      <li><b>Bring out existing ideas</b><span>Before you correct them.</span></li>
      <li><b>Then surprise them</b><span>A prediction that fails.</span></li>
      <li><b>Mark differences clearly</b><span>Between similar topics.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/10963596/">Nader, K., Schafe, G. E., &amp; LeDoux, J. E. (2000). Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval. <i>Nature</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC1838545">Hupbach, A., Gomez, R., Hardt, O., &amp; Nadel, L. (2007). Reconsolidation of episodic memories: A subtle reminder triggers integration of new information. <i>Learning &amp; Memory</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3640262">Schiller, D., Monfils, M.-H., Raio, C. M., et al. (2010). Preventing the return of fear in humans using reconsolidation update mechanisms. <i>Nature</i>.</a></li>
        <li><a href="https://dare.uva.nl/id/2f076b62-5eb2-4a37-abad-19977f6419de">Sevenster, D., Beckers, T., &amp; Kindt, M. (2013). Prediction error governs pharmacologically induced amnesia for learned fear. <i>Science</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4868433">Hardwicke, T. E., Taqi, M., &amp; Shanks, D. R. (2016). Postretrieval new learning does not reliably induce human memory updating via reconsolidation. <i>PNAS</i>.</a></li>''',
quiz='''[
 {q:'Rats got a protein-synthesis blocker six hours after a fear reminder. What happened?',o:['Nothing; the window had closed','The fear was erased','The fear grew'],a:0,f:'Only a drug given soon after the reminder worked.'},
 {q:'What seems needed for a recalled memory to open?',o:['Something unexpected','Exact repetition','A long delay'],a:0,f:'Without a prediction error, it stayed locked.'},
 {q:'How solid is the human evidence?',o:['Mixed; some studies haven’t replicated','Settled and strong','Non-existent'],a:0,f:'Four replications of a well-known motor study found no effect.'}]''',
js=BASE+cls_js("{O:'Opens',L:'Stays locked',T:'Too late',N:'No reminder'}",'''[
 ['Rats hear the tone that once meant a shock; right after, a protein-synthesis blocker goes into the amygdala.','O','Opens: the reminder unlocked the memory, and blocking the restore erased the fear.'],
 ['Rats get the same drug in the amygdala, but the tone is never played.','N','No reminder: the memory was never reopened, so the drug did nothing.'],
 ['Rats hear the tone; the drug is given six hours later.','T','Too late: by then the memory had been stored again.'],
 ['People who fear a coloured square see it once, then 10 minutes later start seeing it many times with no shocks.','O','Opens: the extinction training fell inside the window, and the fear didn’t return.'],
 ['The same, but the reminder comes 6 hours before the shock-free training.','T','Too late: the window had closed, and the fear came back.'],
 ['On day two, students are reminded of the first session in the same room, then learn a second set of objects.','O','Opens: on day three, objects from the second set crept into their memory of the first.'],
 ['On day two, students learn a second set of objects in a different room, with no reminder of day one.','N','No reminder: they rarely mixed the two sets.'],
 ['In a fear study, the reminder plays out exactly as during learning, with nothing new.','L','Stays locked: with no prediction error, the memory didn’t open.'],
 ['In class, a teacher restates the common wrong idea and moves on, with no evidence against it. (On this theory.)','L','Stays locked: recalling an idea without anything surprising may not open it for change.'],
 ['In class, students predict what a falling ball will do, then see the opposite. (On this theory.)','O','Opens: recall plus surprise is the combination that seems to open a memory.']]''','Will the memory open?',r'''
 if(right>=9){title='You know the conditions';text=`${right} of 10 right. A memory seems to open when it’s recalled, something is unexpected, and the change comes within a few hours.`}
 else if(right>=5){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. Check three things in order: was it recalled? Was anything unexpected? Did the change come within hours?`}
 else{title='Worth another look';text=`${right} of 10 right. Check three things in order. Was the memory recalled at all? If not, no reminder. Was anything unexpected? If not, it stays locked. Did the change come within a few hours? If not, too late.`}''')+grid('''[
 ['Rats reminded of a fear, then given a protein-synthesis blocker in the amygdala',['The fear was gone the next day','The fear was stronger','No change'],0,'The reminder made the memory need storing again.'],
 ['The same drug with no reminder',['No effect','The fear was gone','The rats forgot everything'],0,'An unopened memory was safe.'],
 ['Students reminded of day one before learning a second set of objects, tested on day three',['Mixed in objects from the second set','Remembered the first set perfectly','Forgot both sets'],0,'The reopened memory absorbed new material.'],
 ['People reminded of a fear 10 minutes before shock-free training',['The fear didn’t return','The fear returned','The fear grew'],0,'The new learning fell inside the window.'],
 ['When retested a year later',['The effect was still there','The fear had returned','Nobody could be retested'],0,'In those who came back.'],
 ['Four direct replications of a well-known human motor-skill study',['Found no effect','Found a bigger effect','Found the same effect'],0,'Human results are mixed.']]''','The pattern: recalling a memory may open it for change, but in people the evidence is still debated.'))
s=page(o).replace('<a href="#" id="m06link">engram</a>','<a href="@@LB:m06@@">engram from topic 6</a>')
open('m08/template.html','w').write(s)
