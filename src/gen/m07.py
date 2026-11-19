import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m07',n='7',label='The Learning Brain · Memory · Topic 7',epi='The Learning Brain, Memory, episode 7',
title='What Sleep Does: How the Brain Files the Day',h1='What sleep does',em='The brain files the day',read='7',mins='2½ minutes',vtitle='What sleep does',
dek='Sleep after learning helps memories stick, and sleep loss before learning makes them harder to get in. In deep sleep, the brain seems to replay what it learned.',
jumps='<span><a href="#bT">Which night matters?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus and the thalamus, both deep inside, glowing orange and labelled. In deep sleep, ripples in the hippocampus line up with spindles that the thalamus helps generate.',
hero_js="BR.R.hip.lab=[640,770];BR.R.hip.al='left';BR.R.tha.lab=[560,-70];BR.R.tha.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','tha'],labels:['hip','tha'],labelT:{tha:0.8,hip:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>Record from cells in a rat’s hippocampus while it explores. Cells that fired together in the same places fire together again later, while the rat is in deep sleep. In Matthew Wilson and Bruce McNaughton’s 1994 study, the pattern was weaker in the sleep before the exploring.</p>
    <p>The brain seems to replay the day.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>97% vs 86%</strong><span>of card locations remembered, with and without a scent cue during deep sleep</span></div>
      <div role="listitem"><strong>91</strong><span>experiments on cueing memories during sleep, with about 2,000 people</span></div>
      <div role="listitem"><strong>Under ⅓</strong><span>of a standard deviation: the size of that cueing effect, and only outside dream sleep</span></div>
      <div role="listitem"><strong>19%</strong><span>fewer pictures recognized by people who had missed a night’s sleep before learning them</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Inside deep sleep</span>Waves, spindles and ripples</h2>
    <p>Deep, slow-wave sleep is where replay happens most. Large slow waves sweep across the cortex. Short bursts called spindles ride on them, and the thalamus helps generate those. In the <a href="@@LB:hippocampus@@">hippocampus</a>, brief ripples carry the replay. Their timing lines up, which is thought to help move new memories from the hippocampus toward the cortex.</p>
    <h2 class="sec"><span class="n">Steering the replay</span>A scent in the night</h2>
    <p>In 2007, Björn Rasch, Jan Born and colleagues had people learn the locations of card pairs while smelling roses. During deep sleep that night, the scent was released again. The next day they remembered 97% of the locations, against 86% without the cue. The same scent during dream (REM) sleep, or while awake, didn’t help. This is called targeted memory reactivation.</p>
    <p>A 2020 review by Xiaoqing Hu, Ken Paller and colleagues combined 91 experiments with about 2,000 people. The effect was real but small, under a third of a standard deviation, and showed up only in non-REM sleep.</p>
    <h2 class="sec"><span class="n">Before learning</span>Sleep loss closes the gate</h2>
    <p>Sleep matters before learning too. In 2007, Seung-Schik Yoo, Matthew Walker and colleagues kept volunteers awake for a night. While learning new pictures the next day, they showed less hippocampal activity, and two days later, after catching up on sleep, they recognized 19% fewer pictures than people who had slept.</p>
  </div>

'''+cls_html('bT','Which night matters?','Eight short cases. For each, decide when the missing sleep did the damage: the night before learning, the night after, or both. You’ll get feedback after each one.',[('B','The night before','harder to get in'),('A','The night after','less filed away'),('X','Both','')],'When did missing sleep do the damage?','When did sleep matter?','Sleep before learning helps take things in; sleep after helps them stick.')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Labs, not classrooms</h2>
    <p>Most of this comes from labs, with simple materials, and cueing memories during sleep isn’t a classroom tool. The reliable message is simpler: sleep after learning helps it stick, and sleep loss before learning makes it harder to get in.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Sleep is part of studying</h3>
      <p>Avoid deadlines that reward all-nighters, like midnight submissions before a morning exam. Teach students that sleep is part of studying, not time taken from it. And review hard material the day after it’s introduced, once sleep has had its first pass. The <a href="@@LB:lb11@@">spacing and sleep page</a> has more.</p>
    </aside>
  </div>
''',
tips_h='Learning doesn’t stop at night',
tips='''      <li><b>No deadlines that reward all-nighters</b><span>No midnight submissions before a morning exam.</span></li>
      <li><b>Sleep is part of studying</b><span>Not time taken from it.</span></li>
      <li><b>Review the next day</b><span>After sleep has had its first pass.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/8036517/">Wilson, M. A., &amp; McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. <i>Science</i>.</a></li>
        <li><a href="https://doi.org/10.1126/science.1138581">Rasch, B., Büchel, C., Gais, S., &amp; Born, J. (2007). Odor cues during slow-wave sleep prompt declarative memory consolidation. <i>Science</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7144680">Hu, X., Cheng, L. Y., Chiu, M. H., &amp; Paller, K. A. (2020). Promoting memory consolidation during sleep: A meta-analysis of targeted memory reactivation. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/17293859/">Yoo, S.-S., Hu, P. T., Gujar, N., Jolesz, F. A., &amp; Walker, M. P. (2007). A deficit in the ability to form new human memories without sleep. <i>Nature Neuroscience</i>.</a></li>''',
quiz='''[
 {q:'When did a rose scent during sleep help people remember card locations?',o:['During deep, slow-wave sleep','During dream (REM) sleep','While awake'],a:0,f:'97% against 86% without the cue.'},
 {q:'How big was the effect of cueing memories during sleep, across 91 experiments?',o:['Real but small','Very large','Zero'],a:0,f:'Under a third of a standard deviation, and only in non-REM sleep.'},
 {q:'What did a night without sleep do to learning the next day?',o:['Less hippocampal activity, and 19% fewer pictures recognized later','Nothing, after catching up','It improved focus'],a:0,f:'Sleep loss before learning makes it harder to get in.'}]''',
js=BASE+cls_js("{B:'The night before',A:'The night after',X:'Both'}",'''[
 ['A student pulls an all-nighter finishing an essay, then sits through a morning lecture on brand-new material.','B','The night before: the lecture was learned on no sleep, so less got in.'],
 ['A nurse comes off a night shift and goes straight into training on a new procedure.','B','The night before: a brain that hasn’t slept takes in new material less well.'],
 ['Volunteers kept awake for a night studied pictures the next day. Even after catching up on sleep, they recognized 19% fewer.','B','The night before: their hippocampus was less active while learning.'],
 ['A student learns a new set of vocabulary in the evening, then stays up all night gaming.','A','The night after: the new words missed their first night of filing.'],
 ['People learned card locations with a rose scent. When the scent returned during deep sleep that night, they remembered more.','A','The night after: sleep after learning is when replay happens; the scent seemed to steer it.'],
 ['A dancer learns a routine on Friday afternoon, then sleeps only three hours that night. On Saturday, the routine feels shaky.','A','The night after: the routine was learned rested, but missed its night of consolidation.'],
 ['A student studies the first half of a unit, stays up all night on an essay, then has the second half taught the next morning.','X','Both: the first half missed its night of filing, and the second half was learned on no sleep.'],
 ['The night before an exam, a student stays up until 4 a.m. reading chapters for the first time.','X','Both: the chapters were read by a tired brain, then got almost no sleep to settle.']]''','Which night mattered?',r'''
 if(right>=7){title='You know which night matters';text=`${right} of 8 right. Sleep before learning helps it get in; sleep after helps it stick. An all-nighter can cost both.`}
 else if(right>=4){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask two questions: was the learner rested when they learned it? And did they sleep after?`}
 else{title='Worth another look';text=`${right} of 8 right. Ask two questions: was the learner rested when they learned it? If not, the night before mattered. Did they sleep after? If not, the night after did.`}''')+grid('''[
 ['Rat hippocampal cells that fired together while exploring, during deep sleep afterwards',['Fired together again','Stayed silent','Fired at random'],0,'The brain seems to replay the day.'],
 ['A rose scent released during deep sleep, after learning card locations with it',['Recall rose: 97% against 86%','No difference','Recall fell'],0,'Rasch and colleagues, 2007.'],
 ['The same scent during dream (REM) sleep',['Didn’t help','Helped even more','Made recall worse'],0,'The effect showed up only in deep, slow-wave sleep.'],
 ['Across 91 experiments on cueing memories during sleep, the effect was',['Real but small','Large','Zero'],0,'Under a third of a standard deviation.'],
 ['People kept awake for a night, learning pictures the next day',['Recognized 19% fewer later','Recognized the same','Recognized more, from the stress'],0,'Their hippocampus was less active while learning.'],
 ['Is cueing memories during sleep a classroom tool?',['No, it’s a lab method','Yes, it’s widely used','Only for languages'],0,'The reliable message is simpler: protect sleep.']]''','The pattern: sleep after learning helps it stick, and sleep loss before learning makes it harder to get in.'))
open('m07/template.html','w').write(page(o))
