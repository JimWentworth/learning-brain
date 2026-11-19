from wkit import *
o=wbase(4,'The Hidden Vocabulary of Your Discipline','The hidden vocabulary','of your discipline',
'Some of the hardest words in a course look easy. “Significant”, “theory”, “work”, “culture”: students know these words, just not the meaning your field gives them.')
o['hero_aria'],o['hero_js']=hero(['tem','pfc'],{'tem':([300,770],'left'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the temporal lobe, which stores word meanings, and the prefrontal cortex, which helps choose between them, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','What does it mean here?','Eight everyday words used the way a particular discipline uses them. For each, pick the meaning it has in that sentence.')
o.update(body=tabs('What does it mean here?','Familiar words, specialist meanings. Choose what each word means in its sentence.',student,
 'About 10 minutes',
 ['Run the activity with the class voting on each word.',
  'Ask students to list three words in this course that also have an everyday meaning.',
  'Build a short class glossary: the word, its everyday meaning, its meaning here, and an example sentence.',
  'Return to the glossary words in quizzes over the following weeks.'],
 ['Which everyday meaning got in the way?',
  'Which words in this course mean something different from everyday use?',
  'How would a student know that a familiar word has a special meaning here?'],
 'When you use an everyday word in its technical sense, flag it: “In statistics, significant has a precise meaning…” Contrast the two meanings explicitly, and come back to them.',
 'Students who learned the subject in another language may know the technical meaning well but not the English term, or the reverse.')+'''
  <div class="col lede">
    <p>Academic writing uses a layer of vocabulary that is rare in everyday English but common across disciplines. Averil Coxhead’s Academic Word List gathers 570 word families that, together, made up about 10% of the words in a 3.5-million-word corpus of academic texts, but only 1.4% of the words in fiction.</p>
    <p>On top of that sits each discipline’s own vocabulary, and the trickiest part of it: ordinary words with specialised meanings.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>570</strong><span>word families on the Academic Word List</span></div>
      <div role="listitem"><strong>~10%</strong><span>of the words in academic texts come from that list</span></div>
      <div role="listitem"><strong>1.4%</strong><span>of the words in fiction do</span></div>
      <div role="listitem"><strong>2,000</strong><span>most common English words are excluded from the list</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Academic words</span>Common in courses, rare at home</h2>
    <p>The Academic Word List was built from texts across 28 subject areas in arts, commerce, law and science, and leaves out the 2,000 most frequent English words. Words such as “analyse”, “assume” and “derive” appear across disciplines but seldom in conversation, so students meet them mostly in coursework.</p>
    <h2 class="sec"><span class="n">False friends</span>Words students think they know</h2>
    <p>A word students have never seen tells them it is new. A familiar word with a technical meaning doesn’t. “Significant” sounds like “important”; “theory” sounds like “guess”; “work” sounds like “effort”. Students may read past these words, confident that they understood, while building the wrong idea.</p>
    <h2 class="sec"><span class="n">For learning</span>Name the shift</h2>
    <p>Making the contrast explicit, and returning to it over time, turns a hidden trap into a word students know they need to learn. Topic 2 describes how repeated, varied encounters and recall build word knowledge.</p>
  </div>

'''+pgrid_html(),
tips_h='Flag the familiar words that mean something new.',
tips='''      <li><b>Flag the shift</b><span>“In this field, X means…”</span></li>
      <li><b>Contrast both meanings</b><span>Put the everyday and technical meanings side by side.</span></li>
      <li><b>Bring them back</b><span>Quiz the tricky words over several weeks.</span></li>''',
sources='''        <li>Coxhead, A. (2000). A new academic word list. <i>TESOL Quarterly, 34</i>(2), 213–238.</li>''',
foot='The example sentences are written for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'About what share of words in academic texts come from the Academic Word List?',o:['10%','1%','50%'],a:0,f:'And only 1.4% of words in fiction.'},
 {q:'Why are words like “significant” or “theory” tricky?',o:['Students think they already know them','They are long','They are rare'],a:0,f:'The everyday meaning gets in the way.'},
 {q:'A good way to teach them is to…',o:['Contrast the everyday and technical meanings','Avoid using them','Assume students will infer them'],a:0,f:'Then return to them over time.'}]''',
js=PANEL_JS+cases_js(r'''[
 ['<b>Statistics.</b> “The difference between the two groups was <b>significant</b> (p &lt; .05).”',0,'In statistics, significant means unlikely to arise by chance alone if there were no real effect. It doesn’t mean large or important.',['Unlikely to be due to chance alone','Large and important','Noticeable']],
 ['<b>Biology.</b> “Evolution is a <b>theory</b>.”',0,'In science, a theory is a well-tested explanation supported by a large body of evidence, not a guess.',['A well-tested explanation backed by much evidence','A hunch','An idea not yet tested']],
 ['<b>Physics.</b> “The table pushes up on the book with a <b>normal</b> force.”',0,'Normal here means perpendicular to the surface, not usual.',['Perpendicular to the surface','The usual amount','An average']],
 ['<b>Physics.</b> “No <b>work</b> is done on a book you hold still, however tired your arm gets.”',0,'In physics, work is force times the distance moved in the direction of the force. No movement, no work.',['Force times distance moved','Effort','A job']],
 ['<b>Microbiology.</b> “The bacteria were grown in a <b>culture</b>.”',0,'A culture is a population of cells grown in a nutrient medium.',['Cells grown in a nutrient medium','Shared customs and beliefs','The arts']],
 ['<b>Economics.</b> “The economy entered a <b>depression</b>.”',0,'A depression is a severe and long downturn in economic activity.',['A severe, long economic downturn','Sadness','A dip in the ground']],
 ['<b>Statistics.</b> “Incomes were <b>skewed</b> to the right.”',0,'Skewed right means the distribution has a long tail toward high values. It doesn’t mean biased.',['Having a long tail toward high values','Biased or unfair','Moved to the right']],
 ['<b>Medicine.</b> “The test came back <b>positive</b>.”',0,'Positive means the condition or substance was detected, which is often not good news.',['The condition was detected','Good news','Certain']]]''','[]','What does it mean here?',STD_SUM).replace("const [t,k,ex,o]=order[i];","const [t,k0,ex,o0]=order[i];const sh=shuf(o0.map((x,j)=>[x,j]));const o=sh.map(x=>x[0]);const k=sh.findIndex(x=>x[1]===k0);")+grid('''[
 ['How many word families are on the Academic Word List?',['570','5,700','57'],0,'Coxhead, 2000.'],
 ['What share of words in the academic corpus did they cover?',['About 10%','About 1%','About 50%'],0,'Across 28 subject areas.'],
 ['And what share of words in fiction?',['About 1.4%','About 10%','About 25%'],0,'Evidence that the list is academic.'],
 ['How large was the academic corpus the list was built from?',['3.5 million words','35,000 words','350 million words'],0,'From over 400 texts.'],
 ['Which words were excluded from the list?',['The 2,000 most frequent English words','All technical terms','Words over 10 letters'],0,'So the list targets words beyond everyday vocabulary.']]''','The pattern: academic and disciplinary vocabulary has to be taught, especially when it looks familiar.'))
write(o)
