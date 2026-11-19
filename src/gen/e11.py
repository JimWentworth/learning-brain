import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',11,'Integrity in the Age of AI: The Trouble with Detectors','Integrity in the age of AI','The best protection for integrity is an assignment where the thinking shows.','Integrity in the age of AI',
'Generative AI can write an essay in seconds. Many instructors have turned to AI detectors to catch it. But how fair are those detectors?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#bT">Does the thinking show?</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','pfc'],{'pfc':([40,-60],'left'),'tem':([600,770],'left')},'Drawing of the side of the brain with the temporal lobe, at the side, involved in language, and the prefrontal cortex, at the front, involved in planning and judgment, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 2023, Weixin Liang, James Zou and colleagues at Stanford tested seven widely used AI detectors on essays written by people. They used 91 essays by non-native English speakers, written for the TOEFL exam, and 88 essays by American eighth graders.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the 2023 detector study, then see the results. About 1 minute.','Human essays, flagged as AI?','Seven detectors, 179 essays, all written by people.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>7</strong><span>widely used AI detectors tested</span></div>
      <div role="listitem"><strong>Nearly perfect</strong><span>on American eighth graders’ essays</span></div>
      <div role="listitem"><strong>61%</strong><span>of non-native speakers’ essays flagged as AI, on average</span></div>
      <div role="listitem"><strong>~98%</strong><span>flagged by at least one detector</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why</span>Predictable words</h2>
    <p>Detectors look for predictable word choices. Writers with a smaller vocabulary in English write more predictably, so their human writing looks machine-like.</p>
    <h2 class="sec"><span class="n">Both ways wrong</span>Easy to fool, too</h2>
    <p>The same study showed that a simple prompt asking AI to vary its word choice could get AI-written text past the detectors. So detectors can both accuse the innocent and miss the guilty.</p>
    <h2 class="sec"><span class="n">From detection to design</span>Make the thinking visible</h2>
    <p>That shifts attention from detection to design. Assignments that include drafts, process notes, in-class writing, oral explanations, or reflections on personal experience make it easier to see students’ own thinking. This connects to the Generative AI series: decide where AI can help, say so clearly, and assess the thinking you care about.</p>
  </div>

'''+cls_html('bT','Does the thinking show?','Eight assignment designs or integrity practices. For each, decide: does it make students’ own thinking visible, or rely on the final product alone? You’ll get feedback after each one.',[('V','Thinking shows',''),('P','Product only','')],'Does the thinking show, or product only?','Does the thinking show?','The question is always: could you see how the student got there?')+GRID_HTML+box('Don’t rely on a detector score as evidence on its own. State your AI policy for each assignment. Build in visible process: outlines, drafts, conversations about the work. Share this tip with students: show your process, not just the product.'),
tips_h='The best protection for integrity is an assignment where the thinking shows.',
tips='''      <li><b>No detector score alone</b><span>It isn’t evidence on its own.</span></li>
      <li><b>An AI policy per assignment</b><span>Say where AI can help.</span></li>
      <li><b>Visible process</b><span>Outlines, drafts, conversations.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.patter.2023.100779">Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., &amp; Zou, J. (2023). GPT detectors are biased against non-native English writers. <i>Patterns, 4</i>(7), 100779.</a></li>''',
quiz='''[
 {q:'On essays by American eighth graders, detectors were…',o:['Nearly perfect','Mostly wrong','Never tested'],a:0,f:'Liang and colleagues, 2023.'},
 {q:'On average, what share of non-native speakers’ essays were flagged as AI?',o:['61%','6%','100%'],a:0,f:'All written by people.'},
 {q:'Detectors flag writing that uses…',o:['Predictable word choices','Long sentences','Spelling mistakes'],a:0,f:'Which penalizes smaller English vocabularies.'}]''',
js=BASE+pred_js('''[
 ['On the 88 essays by American eighth graders, the detectors were…',['Nearly perfect','Wrong about half the time','Wrong almost every time'],0,'Nearly perfect: they correctly saw the essays as human.'],
 ['On the 91 TOEFL essays by non-native speakers, what share did detectors flag as AI, on average?',['About 6%','About 61%','About 99%'],1,'About 61%, though every essay was written by a person.'],
 ['What share of the TOEFL essays were flagged by at least one of the seven detectors?',['About 20%','About 50%','About 98%'],2,'Almost 98%. Nearly every non-native writer would have been flagged somewhere.']]''',
'''<p class="gh">Human-written TOEFL essays flagged as AI</p>${barRow('Average across 7 detectors',61,100,'~61%','#FFB38A')}${barRow('By at least one detector',98,100,'~98%','#FFB38A')}<p class="gh">American eighth graders’ essays</p><p class="mtext">Classified nearly perfectly as human.</p>''',
r''' if(n===3){title='You saw it coming';text='All 3 right. The same detectors that worked well on native speakers flagged most non-native speakers’ human writing as AI.'}
 else if(!got[1]){title='Worse than most expect';text=`You got ${n} of 3. On average, 61% of human essays by non-native speakers were flagged as AI.`}
 else{title='Unfair in a specific way';text=`You got ${n} of 3. Detectors penalize predictable word choice, which is common in writing in a second language.`}''')+cls_js("{V:'Thinking shows',P:'Product only'}",'''[
 ['Running each submitted essay through a detector and failing anything over 50%','P','Product only: and the 2023 study shows the score can accuse the innocent.'],
 ['Submitting an outline, a rough draft and a final draft, with brief notes on changes','V','Thinking shows: you can see how the work developed.'],
 ['A five-minute conversation where the student explains a key choice in their paper','V','Thinking shows: an oral explanation reveals understanding.'],
 ['A take-home essay on a generic topic, with only the final file submitted','P','Product only: nothing shows how it was made.'],
 ['Short in-class writing that the final paper builds on','V','Thinking shows: you have a sample of the student’s own writing and ideas.'],
 ['A reflection connecting the course idea to the student’s own experience','V','Thinking shows: personal experience is harder to outsource and reveals thinking.'],
 ['Banning AI with no explanation of what counts as AI use','P','Product only: and students can’t tell what’s allowed. State a clear policy per assignment.'],
 ['A stated policy saying AI may help brainstorm, with students noting how they used it','V','Thinking shows: AI use becomes part of the visible process.']]''','Does the thinking show, or product only?',r'''
 if(right>=7){title='You can design for integrity';text=`${right} of 8 right. Drafts, conversations, in-class writing and clear policies make thinking visible.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: could you see how the student got there?`}
 else{title='Worth another look';text=`${right} of 8 right. Detector scores and bare final products show little. Visible process shows the thinking.`}''')+grid('''[
 ['The 2023 Stanford study tested how many AI detectors?',['7','70','1'],0,'Widely used ones.'],
 ['The TOEFL essays were written by…',['Non-native English speakers','AI','Teachers'],0,'91 essays, all by people.'],
 ['On average, detectors flagged what share of those essays as AI?',['61%','16%','6%'],0,'Liang, Zou and colleagues.'],
 ['Why did detectors misfire?',['They look for predictable word choices','The essays were too long','The essays had typos'],0,'Smaller vocabulary means more predictable text.'],
 ['Could AI text get past the detectors?',['Yes, with a prompt to vary word choice','No, never','Only with special software'],0,'They miss the guilty, too.'],
 ['A better approach than detection is…',['Designing assignments where thinking shows','Banning computers','Longer essays'],0,'Drafts, conversations, in-class writing.']]''','The pattern: detectors are unreliable and unfair to some writers; visible process is the better safeguard.'))
open('e11/template.html','w').write(page(o))
