from wkit import *
o=wbase(11,'Gesture and Learning','Gesture','and learning',
'We talk with our hands, and listeners use what they see. Gestures that show shape, movement or location add information that words alone carry less well, and making gestures yourself may help even more than watching them.')
o['hero_aria'],o['hero_js']=hero(['par','tem'],{'par':([560,-70],'left'),'tem':([300,770],'left')},'Drawing of the side of the brain with the parietal lobe, involved in space and movement, and the temporal lobe, involved in language, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','Which gesture helps?','Six teaching moments. For each, choose the gesture most likely to help students understand.')
o.update(body=tabs('Which gesture helps?','Six moments from a class. Which gesture would add the most to the words?',student,
 'About 10 minutes, plus a quick try',
 ['Run the six cases with the class voting.',
  'Quick try: in pairs, one student explains how to get from the classroom to the library while sitting on their hands; then again with hands free. Swap.',
  'Ask what changed for the speaker and for the listener.',
  'Plan one gesture for a key idea in your next class: a shape, a motion, a direction.'],
 ['What did gestures add that the words didn’t?',
  'How did sitting on your hands change your explanation?',
  'Which idea in this course has a shape or motion you could show with your hands?'],
 'Use your hands to show shapes, directions and changes over time, and point to what you are talking about. Encourage students to gesture when they explain, especially for spatial ideas.',
 'Gestures are not universal; some have different meanings in different cultures. Shape-and-motion gestures and pointing travel better than emblem gestures such as thumbs-up.')+'''
  <div class="col lede">
    <p>In 2019, Nicole Dargue, Naomi Sweller and Michael Jones pooled 83 independent samples that compared comprehension of speech with and without gestures. Across all of them, gesture had a moderate, beneficial effect on comprehension, whether the learner produced the gestures or observed them.</p>
    <p>Which gestures were used, what information they carried, how comprehension was measured and the learner’s age all affected how much gesture helped.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>83</strong><span>independent samples in the 2019 meta-analysis of gesture and comprehension</span></div>
      <div role="listitem"><strong>Moderate</strong><span>benefit of gesture alongside speech</span></div>
      <div role="listitem"><strong>Making</strong><span>gestures had larger effects than watching them</span></div>
      <div role="listitem"><strong>Depends</strong><span>on the type of gesture, the information it carries and how learning is measured</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Kinds of gesture</span>Pointing, picturing and beating time</h2>
    <p>Gestures that point direct attention to a place or object. Representational gestures picture a shape, size or movement, such as a curve rising steeply. Beat gestures keep rhythm with speech and add emphasis but no content. The first two carry information the words may not.</p>
    <h2 class="sec"><span class="n">Doing beats watching</span>Gesturing yourself</h2>
    <p>Studies in which learners produced gestures found significantly larger effects on comprehension, on average, than studies in which learners only observed gestures. Asking students to use their hands while explaining is a free addition to any discussion.</p>
    <h2 class="sec"><span class="n">For learning</span>Hands as a second channel</h2>
    <p>For students learning in a second language, a gesture that pictures “increase”, “rotate” or “between” gives meaning a second route in. Gestures also tie to the face-to-face class: a reason to keep your hands, and yourself, visible on screen and in the room.</p>
  </div>

'''+pgrid_html(),
tips_h='Show it with your hands; let students show it with theirs.',
tips='''      <li><b>Picture shapes and changes</b><span>Trace a curve, show a rotation, mark a size.</span></li>
      <li><b>Point while you talk</b><span>Show where to look on a diagram.</span></li>
      <li><b>Let students gesture</b><span>Making gestures had the larger benefit.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/bul0000202">Dargue, N., Sweller, N., &amp; Jones, M. P. (2019). When our hands help us understand: A meta-analysis into the effects of gesture on comprehension. <i>Psychological Bulletin, 145</i>(8), 765–784.</a></li>''',
foot='The six teaching moments are examples written for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Across 83 samples, gesture alongside speech had…',o:['A moderate benefit for comprehension','No effect','A harmful effect'],a:0,f:'Dargue, Sweller and Jones, 2019.'},
 {q:'Which had larger effects on average?',o:['Producing gestures','Observing gestures','No difference'],a:0,f:'Doing beats watching.'},
 {q:'A gesture that traces a rising curve is…',o:['Representational','A beat','Pointing'],a:0,f:'It pictures the shape.'}]''',
js=PANEL_JS+cases_js(r'''[
 ['You explain that a population grew slowly at first, then very fast.',0,'Tracing a curve that bends sharply upward pictures the change over time. That is a representational gesture, carrying shape information the words convey less vividly.',['Trace a curve that bends sharply upward','Tap the desk on each word','Point at the door']],
 ['You want students to look at the third label on a busy diagram.',0,'Pointing directs attention to the exact place; words alone (“the third label”) make students search.',['Point to the label as you name it','Wave both hands','Cross your arms and describe it']],
 ['You describe two meshing gears turning in opposite directions.',0,'Rotating your hands in opposite directions shows the motion directly.',['Turn your two fists in opposite directions','Count on your fingers','Nod']],
 ['You explain the difference between “increase” and “decrease” to a class with many students learning in English.',0,'Raising and lowering your hand gives the meaning a second, non-verbal route, useful for anyone still learning the words.',['Raise your hand for increase and lower it for decrease','Say the words more slowly only','Write them in italics']],
 ['Pairs are explaining to each other how a molecule rotates.',0,'Producing gestures had larger benefits than watching them. Inviting students to use their own hands costs nothing.',['Encourage them to show the rotation with their own hands','Ask them to keep their hands still','Have them write it out silently']],
 ['You emphasise a point by moving your hand in rhythm with each word.',1,'That is a beat gesture: it adds emphasis but no content. Fine for emphasis, but it doesn’t show the idea itself.',['It adds information about the idea','It adds emphasis, not content','It distracts and should be avoided']]]''','[]','Which gesture helps most?',STD_SUM).replace("const [t,k,ex,o]=order[i];","const [t,k0,ex,o0]=order[i];const sh=shuf(o0.map((x,j)=>[x,j]));const o=sh.map(x=>x[0]);const k=sh.findIndex(x=>x[1]===k0);")+grid('''[
 ['How many independent samples did Dargue, Sweller and Jones analyse?',['83','8','830'],0,'Comparing speech with and without gesture.'],
 ['Did gesture help comprehension overall?',['Yes, a moderate benefit','No','Only for children'],0,'Whether produced or observed.'],
 ['Which had significantly larger effects on average?',['Producing gestures','Observing gestures','Neither'],0,'Students’ own gestures matter.'],
 ['Did the function of the gesture affect the size of the benefit?',['Yes','No','Only for pointing'],0,'Producing versus observing made a significant difference.'],
 ['Did the type of gesture affect how much it helped?',['Yes','No','There was only one type'],0,'Along with the information it carried and how comprehension was measured.']]''','The pattern: gestures add a second channel for meaning, especially when learners make them.'))
write(o)
