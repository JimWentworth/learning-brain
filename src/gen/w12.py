from wkit import *
o=wbase(12,'Designing for Language: Before, During and After','Designing for language:','before, during and after',
'Every course is taught in a language, and every discipline has its own. This topic gathers the series into practical moves that help all students, and especially those learning in a second language.')
o['hero_aria'],o['hero_js']=hero(['tem','pfc'],{'tem':([300,770],'left'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the temporal lobe and the prefrontal cortex, part of the language network, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','Helps, or gets in the way?','Ten teaching decisions. For each, decide whether it helps students learn through language, or gets in the way. Each case links to the topic it comes from.')
o.update(body=tabs('Helps, or gets in the way?','Ten decisions instructors make about language. Sort each one.',student,
 'About 15 minutes',
 ['Run the ten cases with the class voting, or in pairs.',
  'Ask students who learn in a second language (if they are willing) which moves help them most.',
  'Pick three moves to try in the next two weeks.',
  'Revisit after a few weeks: which stuck, and what changed?'],
 ['Which of these do you already do?',
  'Which would cost least and help most in your course?',
  'What does a student learning in a second language need most from your lectures?'],
 'Before class, share key terms and slides. During class, flag technical uses of everyday words, speak at a steady pace, point and gesture, and prompt explanation. After class, caption recordings, use short writing to check understanding, and bring key terms back in quizzes.',
 'Each case links to a topic in this series, so the class can follow up on any one.')+'''
  <div class="col lede">
    <p>The topics in this series point the same way. Language is a specialised system, distinct from reasoning. Words build up over many encounters and stick through recall. Reading and listening depend on knowing nearly all the words. Explaining, writing and gesturing turn ideas into language, and help learning.</p>
    <p>None of these moves is only for second-language learners. They make a course clearer for everyone, and essential for some.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Before</strong><span>share key terms, slides and readings ahead of class</span></div>
      <div role="listitem"><strong>During</strong><span>flag technical words, pace, point, and prompt explanation</span></div>
      <div role="listitem"><strong>After</strong><span>caption recordings, write to check understanding, quiz the terms</span></div>
      <div role="listitem"><strong>12</strong><span>topics in this series, each with an activity to use in class</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Before</span>Prepare the words</h2>
    <p>Students can follow speech when they know 95–98% of the words. Post key terms with definitions and example sentences before class, and share slides or notes so students can preview them. Flag everyday words that have technical meanings in your field.</p>
    <h2 class="sec"><span class="n">During</span>Make meaning visible</h2>
    <p>Speak at a steady pace, pause after key points, and face the room. Point to what you are describing and use your hands to show shapes and changes. Ask students to explain steps to themselves and to each other.</p>
    <h2 class="sec"><span class="n">After</span>Bring the language back</h2>
    <p>Caption recordings. Use a minute of writing to see what students understood. Quiz key terms over several weeks, asking students to recall them, not just recognise them. When grading, decide whether you are assessing the ideas, the language, or both.</p>
    <h2 class="sec"><span class="n">A caution</span>Principles, not a formula</h2>
    <p>Much of the evidence comes from language classrooms, school settings or lab studies with short materials. The effects vary with learners and contexts. Use these moves as defaults and ask your students what helps them.</p>
  </div>

'''+pgrid_html('Each question comes from a topic in this series. Predict, then check.'),
tips_h='Plan for the language, not just the content.',
tips='''      <li><b>Before: share the words</b><span>Key terms, slides and readings ahead of class.</span></li>
      <li><b>During: show and prompt</b><span>Point, gesture, flag technical words, ask “why?”</span></li>
      <li><b>After: recall and caption</b><span>Quiz key terms; caption recordings.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41583-024-00802-4">Fedorenko, E., Ivanova, A. A., &amp; Regev, T. I. (2024). The language network as a natural kind within the broader landscape of the human brain. <i>Nature Reviews Neuroscience, 25</i>(5), 289–312.</a></li>
        <li><a href="https://doi.org/10.1111/lang.12343">Uchihara, T., Webb, S., &amp; Yanagisawa, A. (2019). The effects of repetition on incidental vocabulary learning: A meta-analysis of correlational studies. <i>Language Learning, 69</i>(3), 559–599.</a></li>
        <li><a href="https://doi.org/10.1016/j.system.2013.07.013">Montero Perez, M., Van Den Noortgate, W., &amp; Desmet, P. (2013). Captioned video for L2 listening and vocabulary learning: A meta-analysis. <i>System, 41</i>(3), 720–739.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-018-9434-x">Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., &amp; Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. <i>Educational Psychology Review, 30</i>.</a></li>
        <li>The other topics in this series list their own sources.</li>''',
foot='The ten cases are illustrations drawn from the topics in this series. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Which helps second-language listeners most before a lecture?',o:['Key terms and slides shared in advance','A longer lecture','Faster speech'],a:0,f:'Topic 8.'},
 {q:'To make a technical term stick, students should…',o:['Meet it several times and recall it','See it once in a reading','Copy it out'],a:0,f:'Topics 2 and 7.'},
 {q:'When grading a lab report about experimental design, focus on…',o:['The design and reasoning','Grammar only','Length'],a:0,f:'Separate the ideas from the language, unless language is the goal.'}]''',
js=PANEL_JS+cases_js(r'''[
 ['You post a list of key terms, with definitions and example sentences, before each lecture.',0,'Helps. Students can meet the words before they have to follow them at speaking speed. (Topic 8)'],
 ['You lecture quickly and post the slides only after the exam.',1,'Gets in the way. Listeners can’t reread, and students learning in a second language lose words with no way to recover them. (Topic 8)'],
 ['When you say “significant” in a statistics class, you contrast it with its everyday meaning.',0,'Helps. Familiar words with technical meanings are easy to misread. (Topic 4)'],
 ['You grade lab reports mainly on grammar, though the learning goal is experimental design.',1,'Gets in the way. Language and reasoning are different systems; grade what you mean to assess. (Topics 1 and 5)'],
 ['You caption all your recorded lectures.',0,'Helps. Captions had a large effect on second-language listening comprehension. (Topic 8)'],
 ['You end class with a one-minute “muddiest point” writing prompt.',0,'Helps. Short reflective writing is the kind most linked to learning. (Topic 9)'],
 ['A key term appears once in the assigned reading and never comes up again.',1,'Gets in the way. Words build up over many encounters, and stick through recall. (Topics 2 and 7)'],
 ['Worked examples include a “why does this step work?” prompt, and pairs explain steps to each other.',0,'Helps. Self-explanation prompts had a medium average benefit. (Topic 10)'],
 ['You tell bilingual students that their two languages give them a brain-training advantage.',1,'Gets in the way of accuracy. After correcting for publication bias, no advantage in executive function remained. Value their languages for real reasons. (Topic 6)'],
 ['You trace a rising curve in the air when describing growth, and point at the diagram as you talk.',0,'Helps. Gestures that picture or point added to comprehension. (Topic 11)']]''','["Helps","Gets in the way"]','Helps, or gets in the way?',STD_SUM)+grid('''[
 ['Is the brain’s language network distinct from its systems for reasoning?',['Yes, though closely linked','No, they are the same','Language has no network'],0,'Topic 1.'],
 ['What share of words must be known for adequate comprehension?',['About 95–98%','About 70%','About 50%'],0,'Topic 8.'],
 ['Until about what age is grammar-learning ability preserved?',['About 17','About 5','About 40'],0,'Topic 5.'],
 ['After correcting for publication bias, the bilingual advantage in executive function was…',['Not supported','Large','Doubled'],0,'Topic 6.'],
 ['Which had larger effects on comprehension?',['Producing gestures','Observing gestures','Neither'],0,'Topic 11.']]''','The pattern: plan for the language, and every student gains.'))
write(o)
