import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(12,'Designing for Perception: Before, During and After','Designing for perception:','before, during and after',
'Everything a student learns from a slide, a diagram or a demonstration passes through perception first. This topic gathers the series into practical moves for planning, teaching and reviewing.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','pfc'],{'occ':([960,770],'right'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision begins, and the prefrontal cortex, at the front, glowing orange and labelled.')

screen='''            <p class="bscen" id="dpS" style="font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;margin:0;min-height:5.8em" aria-live="polite">Press Start.</p>
            <p class="prog" id="dpP"></p>'''
student=lab(screen,'Ready','With perception, or against it?','Ten teaching moves. For each, decide: does it work with how perception works, or against it? You’ll get feedback, with a link back to the topic it comes from.','Start')

o.update(body=tabs('With perception, or against it?','Ten things instructors do with slides, diagrams and demonstrations. Sort each one.',student,
 'About 15 minutes',
 ['Run the ten cases with the class voting, or have pairs work through them on their devices.',
  'Hand out one of your own slides or a page of your notes. In pairs, students audit it with the checklist below: what to look at, grouping, contrast, chart type, what changes.',
  'Collect the top three fixes and make them.',
  'Repeat the audit after your next unit; the checklist gets faster with practice.'],
 ['Which case surprised you?',
  'Which of these do you do now? Which will you change first?',
  'What would a student say is hardest to see in this course?'],
 'Before class, audit one slide deck with the checklist on this page. During class, say what to look at and point to it. After class, ask students what they noticed, and compare it with what you meant them to notice.',
 'Each case links to a topic in this series, so the class can follow up on any one.')+'''
  <div class="col lede">
    <p>The topics in this series point the same way. Perception is the brain’s best guess, built from context and expectation. It is sharp only in a small area and only for what we attend to. It groups, fills in and judges relative to surroundings. And experts and beginners literally see differently.</p>
    <p>None of that is a flaw to fix in students. It’s how vision and hearing work for everyone. Teaching works better when it works with it.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Before</strong><span>check grouping, contrast and chart type in your materials</span></div>
      <div role="listitem"><strong>During</strong><span>say what to look at, point to it, announce changes</span></div>
      <div role="listitem"><strong>After</strong><span>ask what students noticed, and train their eye with examples</span></div>
      <div role="listitem"><strong>12</strong><span>topics in this series, each with an activity to use in class</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Before</span>Plan what students will see</h2>
    <p>Put labels next to what they label and keep unrelated things apart, since layout tells the eye what goes together. Check text contrast with a tool, at least 4.5 to 1 for normal text, and don’t rely on colour alone. For comparisons that matter, use positions or lengths on a shared axis, and start bar charts at zero. Cut words from slides: every word costs an eye movement.</p>
    <h2 class="sec"><span class="n">During</span>Guide attention</h2>
    <p>Before you show an image, say what it is meant to show. Point to the part you are talking about, and build complex diagrams up in steps. When something changes, say so; unannounced changes are easily missed. Face the room when you speak, and use the microphone and captions.</p>
    <h2 class="sec"><span class="n">After</span>Check and train</h2>
    <p>Ask students to describe what they saw before you interpret it; their reading may differ from yours. For the distinctions that experts see at a glance, give many short, mixed examples with feedback.</p>
    <h2 class="sec"><span class="n">A caution</span>Principles, not a formula</h2>
    <p>Most of the evidence in this series comes from perception labs and multimedia learning studies, often with short lessons. The effects are real but vary by learner and setting. Use these as defaults and check them against what your students actually see.</p>
  </div>

'''+pgrid_html('Each question comes from a topic in this series. Predict, then check.'),
tips_h='Teach with perception, not against it.',
tips='''      <li><b>Before: audit one deck</b><span>Grouping, contrast, chart type, words per slide.</span></li>
      <li><b>During: name it and point</b><span>Say what to look at; show where; announce changes.</span></li>
      <li><b>After: ask what they saw</b><span>Then train the eye with mixed examples.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1007/s10648-011-9174-7">Gegenfurtner, A., Lehtinen, E., &amp; Säljö, R. (2011). Expertise differences in the comprehension of visualizations. <i>Educational Psychology Review, 23</i>(4), 523–552.</a></li>
        <li>Schneider, S., Beege, M., Nebel, S., &amp; Rey, G. D. (2018). A meta-analysis of how signaling affects learning with media. <i>Educational Research Review, 23</i>, 1–24.</li>
        <li><a href="https://doi.org/10.1007/s10648-018-9435-9">Schroeder, N. L., &amp; Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. <i>Educational Psychology Review, 30</i>(3), 679–701.</a></li>
        <li><a href="https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html">W3C. Understanding Success Criterion 1.4.3: Contrast (Minimum). WCAG 2.2.</a></li>
        <li>The other topics in this series list their own sources.</li>''',
foot='The ten cases are illustrations drawn from the topics in this series. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Before showing a complex diagram, you should…',o:['Say what it is meant to show','Let students discover it unaided','Add more labels in a key'],a:0,f:'Name what to look at.'},
 {q:'Which helps most when a slide changes?',o:['Saying what changed and pointing to it','Changing it quickly','Changing several things at once'],a:0,f:'Unannounced changes are easily missed.'},
 {q:'To train students to see like experts, give…',o:['Many short, mixed examples with feedback','One long explanation','A list of rules only'],a:0,f:'Perceptual learning.'}]''',
js=PANEL_JS+r'''
/* ---------- with or against ---------- */
const CASES=[
 ['Before showing a micrograph, you say which structure to look for and what to ignore.',0,'Works with it: perception is a best guess, and naming the target gives the right context. (Topic 1)'],
 ['A diagram’s labels sit in a numbered key at the bottom of the slide.',1,'Works against it: the eye has to jump between number and key. Put labels on the parts. (Topic 6)'],
 ['You build a circuit diagram up one part at a time, saying what each new part does.',0,'Works with it: announced, step-by-step change is easy to follow; silent changes are easily missed. (Topic 3)'],
 ['Your slide has 90 words of text, and you keep talking while students read it.',1,'Works against it: every word costs eye movements, and students can’t read and listen at once. (Topic 4)'],
 ['You use light orange text on white because it matches the course colours.',1,'Works against it: bright colours on white often fall well below 4.5 to 1 contrast, and fade further on a projector. (Topic 5)'],
 ['A results chart uses red and green as the only way to tell two groups apart.',1,'Works against it: about 1 in 12 men of Northern European ancestry have red–green colour vision deficiency. Add labels or patterns. (Topic 5)'],
 ['You turn on captions for every video and face the room when you speak.',0,'Works with it: seeing the face and the words helps understanding, most of all when sound is poor. (Topic 7)'],
 ['You introduce a new technical term by writing it on the board before using it in speech.',0,'Works with it: expectation shapes what we hear, so give the brain the word to expect. (Topic 8)'],
 ['To teach students to tell three rock types apart, you give 30 quick mixed photos with instant feedback.',0,'Works with it: many short, mixed examples with feedback train expert seeing. (Topic 9)'],
 ['You compare two pass rates in a bar chart whose axis starts at 80%.',1,'Works against it: a cut-off axis makes a small difference look large, even when the cut is visible. (Topic 11)']];
startRun(async()=>{const order=shuf([...CASES]);let right=0;
 for(let i=0;i<order.length;i++){const [t,k,ex]=order[i];$('dpS').textContent=t;$('dpP').textContent=`Case ${i+1} of ${order.length}`;
  say(`Case ${i+1} of ${order.length}`,'With perception, or against it?','');
  const a=await ask(['Works with it','Works against it'],'With perception or against it?');if(!RUN)return;mark(k,a);if(a===k)right++;
  say(null,null,(a===k?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex);
  if(i<order.length-1){await nextBtn('Next case');if(!RUN)return;hideCh()}}
 $('dpS').textContent='Done.';$('dpP').textContent='';
 say('Your results',`${right} of ${order.length} right`,right>=9?'You can spot what helps students see. Try the checklist on one of your own slide decks.':right>=6?'Mostly there. Revisit the topics linked in the cases you missed.':'Worth another look: the topic numbers in the feedback point to the pages that explain each one.')});
'''+grid('''[
 ['Squares A and B in the checker-shadow picture are…',['The same grey','Different greys','Different colours'],0,'Topic 1: perception is a best guess.'],
 ['What share of observers missed the gorilla while counting passes?',['About half','About 5%','About 95%'],0,'Topic 3: inattentional blindness.'],
 ['The sharp centre of vision covers about…',['2 degrees','20 degrees','Everything in view'],0,'Topic 4: the fovea.'],
 ['WCAG’s minimum contrast for normal text is…',['4.5 to 1','2 to 1','10 to 1'],0,'Topic 5: contrast.'],
 ['Which judgement is read most accurately from a chart?',['Position along a common scale','Area','Angle'],0,'Topic 11: graphical perception.']]''','The pattern: what students learn from what they see depends on how we show it.'))
write(o)
