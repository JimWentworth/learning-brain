import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(9,'Paper or Screen? Reading Comprehension Across Media','Paper or screen?','Skim on screens if you like. Study at the speed of understanding.','Paper or screen?',
'More and more course reading happens on screens: textbooks, articles, slides, all online. Does it matter where students read?',
'<span><a href="#bT">Print, or screen is fine?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','pfc'],{'occ':([900,-60],'right'),'pfc':([60,730],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision starts, and the prefrontal cortex, at the front, which helps monitor understanding, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 2018, Pablo Delgado, Cristina Vargas, Rakefet Ackerman and Ladislao Salmerón pooled 54 studies with 171,055 participants, comparing the same texts on paper and on screens.</p>
    <p>Readers understood more on paper. The effect was small, an effect size of about 0.2, but it was consistent. A separate meta-analysis by Virginia Clinton in 2019 found a similar paper advantage.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>54</strong><span>studies, with 171,055 participants</span></div>
      <div role="listitem"><strong>~0.2</strong><span>effect size favouring paper: small, but consistent</span></div>
      <div role="listitem"><strong>Informational</strong><span>texts showed the gap; stories did not</span></div>
      <div role="listitem"><strong>Time pressure</strong><span>made the gap bigger</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The details</span>Which reading, and when</h2>
    <p>The paper advantage showed up for informational texts, the kind assigned in most courses, but not for narrative texts like stories. It grew under time pressure. And across the years studied, it did not shrink.</p>
    <h2 class="sec"><span class="n">Why</span>Shallow habits, and overconfidence</h2>
    <p>One idea is “shallowing”: we use screens mostly for quick, skimming reading, and carry that habit into study. Another is that screen readers can feel they understood more than they did, so they stop too soon.</p>
  </div>

'''+cls_html('bT','Print, or screen is fine?','Eight reading situations. For each, decide: is it worth printing or slowing down, or is a screen fine? You’ll get feedback after each one.',[('P','Print or slow down',''),('S','Screen is fine','')],'Print or slow down, or screen is fine?','Print, or screen is fine?','The question is always: is this informational text that students need to understand, maybe under time pressure?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Small, and an average</h2>
    <p>The effect is small, and it is an average. Good screen habits can narrow it, and digital text has real advantages: cost, search, and accessibility tools for many students.</p>
  </div>

'''+GRID_HTML+box('For key readings, offer a printable version, or encourage students to print. Avoid tight time limits on screen reading. Ask students to slow down and check their understanding with a question or summary. Keep accessible digital versions for students who need them. Share this tip with students: print or slow down for hard reading.'),
tips_h='Skim on screens if you like. Study at the speed of understanding.',
tips='''      <li><b>Printable key readings</b><span>And accessible digital versions.</span></li>
      <li><b>No tight time limits on screen</b><span>That’s where the gap grows.</span></li>
      <li><b>A question or summary</b><span>To check understanding.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.edurev.2018.09.003">Delgado, P., Vargas, C., Ackerman, R., &amp; Salmerón, L. (2018). Don’t throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. <i>Educational Research Review, 25</i>, 23–38.</a></li>
        <li><a href="https://doi.org/10.1111/1467-9817.12269">Clinton, V. (2019). Reading from paper compared to screens: A systematic review and meta-analysis. <i>Journal of Research in Reading, 42</i>(2), 288–325.</a></li>''',
quiz='''[
 {q:'Across 54 studies, readers understood more…',o:['On paper, by a small margin','On screens','Equally'],a:0,f:'An effect size of about 0.2.'},
 {q:'The paper advantage showed up for…',o:['Informational texts, not stories','Stories, not informational texts','Neither'],a:0,f:'The kind of text assigned in most courses.'},
 {q:'Under time pressure, the gap…',o:['Grew','Shrank','Disappeared'],a:0,f:'Avoid tight time limits on screen reading.'}]''',
js=BASE+cls_js("{P:'Print or slow down',S:'Screen is fine'}",'''[
 ['A dense textbook chapter students will be examined on','P','Print or slow down: informational text, studied for understanding, is where paper had the edge.'],
 ['A short story for a creative writing class, read at leisure','S','Screen is fine: narrative texts showed no paper advantage.'],
 ['A timed online reading quiz on a research article','P','Print or slow down: time pressure made the gap bigger. Loosen the time limit if you can.'],
 ['Checking the due date in the course schedule','S','Screen is fine: that’s looking something up, not studying.'],
 ['A key journal article for a seminar discussion','P','Print or slow down: informational text that students need to understand well.'],
 ['Searching an online reader for every mention of a term','S','Screen is fine: search is one of digital text’s real advantages.'],
 ['A student who uses text-to-speech or screen magnification','S','Screen is fine, and essential: accessibility tools are a real advantage of digital text.'],
 ['Skimming a long technical PDF the night before, with no time to stop and check','P','Slow down: dense informational text under time pressure is where the screen gap was largest.']]''','Print or slow down, or screen is fine?',r'''
 if(right>=7){title='You know when it matters';text=`${right} of 8 right. Paper or slow reading matters most for informational texts, studied for understanding, especially under time pressure.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Stories, look-ups and accessibility needs are fine on screen. Dense study reading, especially timed, is where paper helps.`}
 else{title='Worth another look';text=`${right} of 8 right. The paper advantage was for informational texts and grew under time pressure. For stories, searching and accessibility, screens are fine or better.`}''')+grid('''[
 ['The 2018 meta-analysis pooled about how many participants?',['171,000','1,700','17 million'],0,'From 54 studies.'],
 ['Readers understood more…',['On paper','On screens','Equally'],0,'A small but consistent effect.'],
 ['The effect size was about…',['0.2: small','1.0: large','Zero'],0,'Clinton, 2019, found a similar advantage.'],
 ['The paper advantage showed up for…',['Informational texts','Stories','Both equally'],0,'Not for narrative texts.'],
 ['Under time pressure, the paper advantage…',['Grew','Shrank','Reversed'],0,'Tight limits on screen reading hurt.'],
 ['Across the years studied, the gap…',['Did not shrink','Disappeared','Reversed'],0,'Familiarity with screens did not close it.']]''','The pattern: a small but steady paper advantage for informational reading, bigger under time pressure.'))
open('d09/template.html','w').write(page(o))
