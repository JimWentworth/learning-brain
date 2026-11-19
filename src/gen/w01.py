from wkit import *
o=wbase(1,'Language in the Brain: A Network, Not Two Boxes','Language in the brain:','a network, not two boxes',
'Many of us learned that language lives in two spots: Broca’s area for speaking, Wernicke’s for understanding. Modern brain imaging tells a richer story, with consequences for how we think about students who learn in a second language.')
o['hero_aria'],o['hero_js']=hero(['pfc','tem'],{'pfc':([40,-60],'left'),'tem':([300,770],'left')},'Drawing of the side of the brain with the frontal area and the temporal lobe, which hold the core language network, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','Supported, or a myth?','Eight claims about language and the brain. For each, decide whether current evidence supports it, or whether it is a myth or an oversimplification.')
o.update(body=tabs('Supported, or a myth?','Eight claims about where language lives in the brain. Sort them before reading the evidence.',student,
 'About 10 minutes',
 ['Show each claim and have students vote with a show of hands before revealing.',
  'After all eight, ask which surprised them most.',
  'Discuss the separation between language and reasoning: a student can reason well and still struggle to express it in a second language.',
  'Ask how your assessments might mix up language skill with understanding of the content.'],
 ['Where did you first learn the “two boxes” picture?',
  'If language and reasoning rely on different networks, what does that mean for students writing in a second language?',
  'Which of your assessments measure language as much as content?'],
 'When a student’s writing is hard to follow, ask whether it is the reasoning or the language that is weak. Offer other ways to show understanding, such as diagrams, worked solutions or short oral explanations, where that fits the goal.',
 'The research is moving fast, and researchers still debate how widely language is spread across the brain. That debate is part of the lesson.')+'''
  <div class="col lede">
    <p>Modern neuroscience began, in part, with Paul Broca’s 1861 proposal linking speech to a region of the left frontal lobe, later called Broca’s area. For a century and a half, textbooks taught a tidy two-region model.</p>
    <p>Imaging studies now describe a core language network of left-hemisphere frontal and temporal areas. In a 2024 review, Evelina Fedorenko, Anna Ivanova and Tamar Regev describe it as strongly interconnected, the same whether language comes in through the ears or the eyes, causally important for language, and selective for language.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1861</strong><span>Broca links speech to a region of the left frontal lobe</span></div>
      <div role="listitem"><strong>2 parts</strong><span>of Broca’s area: one in the language network, one in a general problem-solving network</span></div>
      <div role="listitem"><strong>Any input</strong><span>the language network responds to heard and read language alike</span></div>
      <div role="listitem"><strong>772</strong><span>people’s brain scans in a 2026 study that found the network extends further than thought</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Broca’s area</span>Not one thing</h2>
    <p>Fedorenko and Idan Blank argued in 2020 that Broca’s area is not a single unit with a single job. One part belongs to the language network; a neighbouring part belongs to the domain-general “multiple-demand” network, which works on many kinds of hard tasks. Lesion studies have also found that damage to Broca’s area does not necessarily cause lasting language problems.</p>
    <h2 class="sec"><span class="n">Language and thought</span>Close partners, separate systems</h2>
    <p>The language network works closely with, but is distinct from, systems for perception and movement and the brain’s systems for knowledge and reasoning. Damage to the language network in adulthood can cause language-specific problems while leaving other thinking intact.</p>
    <h2 class="sec"><span class="n">An open debate</span>How far does it reach?</h2>
    <p>Not everyone agrees on the boundaries. Some researchers argue that language is widely distributed throughout the brain. And a 2026 MIT study, analysing scans of 772 people, found language-responsive regions outside the classic frontal and temporal areas.</p>
    <h2 class="sec"><span class="n">For learning</span>Language load is not thinking load</h2>
    <p>If language and reasoning draw on different systems, then difficulty expressing an idea in a second language is not the same as difficulty understanding it. The rest of this series looks at what that means for vocabulary, reading, listening, writing and explaining.</p>
  </div>

'''+pgrid_html(),
tips_h='Separate the language from the thinking when you can.',
tips='''      <li><b>Ask what you are grading</b><span>Content understanding, language, or both?</span></li>
      <li><b>Offer other routes</b><span>Diagrams, worked steps or brief oral explanations can show understanding.</span></li>
      <li><b>Retire the two-box picture</b><span>It’s a useful history lesson, not the current science.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41583-024-00802-4">Fedorenko, E., Ivanova, A. A., &amp; Regev, T. I. (2024). The language network as a natural kind within the broader landscape of the human brain. <i>Nature Reviews Neuroscience, 25</i>(5), 289–312.</a></li>
        <li><a href="https://doi.org/10.1016/j.tics.2020.01.001">Fedorenko, E., &amp; Blank, I. A. (2020). Broca’s area is not a natural kind. <i>Trends in Cognitive Sciences, 24</i>(4), 270–284.</a></li>
        <li><a href="https://doi.org/10.3389/flang.2025.1608928">Ivanova, M. V., Riès, S. K., &amp; Llorens, A. (2025). Editorial: Revisiting a 150-year-old conundrum on the role of Broca’s area in language processing. <i>Frontiers in Language Sciences, 4</i>, 1608928.</a></li>
        <li><a href="https://news.mit.edu/2026/brain-language-network-more-extensive-than-previously-thought-0701">Trafton, A. (2026, July 1). The brain’s language network is more extensive than previously thought. <i>MIT News</i>.</a></li>''',
quiz='''[
 {q:'The core language network sits mainly in…',o:['Left frontal and temporal areas','The back of the brain','One small spot'],a:0,f:'A network, not one region.'},
 {q:'Broca’s area is best described as…',o:['Two sub-regions belonging to different networks','A single speech centre','Not part of language at all'],a:0,f:'Fedorenko and Blank, 2020.'},
 {q:'Language and reasoning are supported by…',o:['Distinct but closely linked systems','Exactly the same areas','Unrelated hemispheres'],a:0,f:'Damage can affect one and spare the other.'}]''',
js=PANEL_JS+cases_js(r'''[
 ['Language lives in two spots: Broca’s area for speaking and Wernicke’s area for understanding.',1,'An oversimplification. Today’s picture is a core network of several left frontal and temporal areas.'],
 ['Broca’s area is one region with one job.',1,'A myth. One part belongs to the language network and a neighbouring part to a general problem-solving network.'],
 ['The language network responds to language whether you hear it or read it.',0,'Supported. The core network is the same regardless of input or output modality.'],
 ['The language network is distinct from the brain’s systems for knowledge and reasoning.',0,'Supported. It works closely with them, but it is a separate system.'],
 ['Damage to the language network in adulthood can impair language while leaving other thinking intact.',0,'Supported. Such damage can cause selectively linguistic problems.'],
 ['Damage to Broca’s area always causes lasting speech problems.',1,'A myth. Lesion studies have found damage there does not necessarily cause persistent language deficits.'],
 ['Researchers fully agree on where language stops and the rest of the brain begins.',1,'A myth. Some argue language is widely distributed, and a 2026 study found language-responsive regions beyond the classic ones.'],
 ['Without language, there is no reasoning.',1,'A myth. The language network is distinct from systems for reasoning; people with language damage can still reason.']]''','["Supported","Myth or oversimplified"]','Supported, or a myth?',STD_SUM)+grid('''[
 ['In what year did Broca link speech to a region of the left frontal lobe?',['1861','1961','1761'],0,'The start of the classic model.'],
 ['Is the core language network the same whether language is heard or read?',['Yes','No, they are separate networks','Only for children'],0,'It is independent of input and output modality.'],
 ['Is Broca’s area a single unit, according to Fedorenko and Blank?',['No: two sub-regions in different networks','Yes','It doesn’t exist'],0,'Language network and multiple-demand network.'],
 ['How many people’s scans did the 2026 MIT study analyse?',['772','72','7,720'],0,'Finding language-responsive regions beyond the classic areas.'],
 ['Does damage to Broca’s area always cause lasting language problems?',['No','Yes','Only in children'],0,'Lesion studies show it does not necessarily do so.']]''','The pattern: language is a specialised network, close to but distinct from thinking.'))
write(o)
