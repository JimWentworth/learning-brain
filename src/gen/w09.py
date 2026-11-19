from wkit import *
o=wbase(9,'Writing to Learn','Writing','to learn',
'Writing about a subject can deepen understanding of it, but not all writing does. Short tasks that make students explain, predict or monitor their own understanding do more than long reports or copying.')
o['hero_aria'],o['hero_js']=hero(['pfc','tem'],{'pfc':([40,-60],'left'),'tem':([300,770],'left')},'Drawing of the side of the brain with the prefrontal cortex and the temporal lobe, both active when we put ideas into words, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','Which prompt helps learning?','Eight writing tasks an instructor might set. For each, decide: is it likely to help students learn the content, or less likely?')
o.update(body=tabs('Which prompt helps learning?','Writing tasks from muddiest-point notes to term papers. Which ones are most likely to help students learn the content?',student,
 'About 10 minutes, plus a one-minute paper',
 ['Run the activity, voting on each task.',
  'Then try one: give students two minutes to write the muddiest point of today’s class and why it is unclear.',
  'Read a handful aloud (anonymously) and address the most common one.',
  'Ask students which kinds of writing have helped them learn in other courses.'],
 ['What do the helpful prompts have in common?',
  'Why might a long paper teach less of the content than several short prompts?',
  'Which short writing prompt could you add to your next class?'],
 'Add short, frequent writing that asks students to explain, predict, or monitor their understanding: a muddiest point, a one-sentence summary of the key idea, a prediction before a demonstration. Read a sample and respond.',
 'Most of the evidence comes from school classrooms; studies in college courses are fewer and more mixed. Long papers can serve other goals, such as learning to write in the discipline.')+'''
  <div class="col lede">
    <p>In 2004, Robert Bangert-Drowns, Marlene Hurley and Barbara Wilkinson pooled 48 school-based writing-to-learn programmes. Writing had a small, positive effect on conventional measures of achievement. Two features predicted larger effects: prompts that asked students to reflect on their own understanding, and longer programmes. Two predicted smaller ones: middle-school grades, and longer writing assignments.</p>
    <p>A 2020 meta-analysis by Steve Graham, Sharlene Kiuhara and Meade MacKay, covering 56 experiments in science, social studies and mathematics, found that writing about content reliably enhanced learning, with an average effect size of 0.30.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>48</strong><span>writing-to-learn programmes in the 2004 meta-analysis</span></div>
      <div role="listitem"><strong>Reflection</strong><span>prompts, asking students to monitor their understanding, predicted larger benefits</span></div>
      <div role="listitem"><strong>0.30</strong><span>average effect of writing about content, across 56 experiments</span></div>
      <div role="listitem"><strong>Same</strong><span>benefit in science, social studies and mathematics</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">What kind of writing</span>Thinking, not transcribing</h2>
    <p>Writing to learn is writing that makes students do something with the content: explain it, connect it, apply it or notice what they don’t understand. Prompts asking students to reflect on their own understanding were the strongest predictor of benefit in the 2004 analysis. Longer assignments, perhaps because they shift effort toward producing the text itself, were linked to smaller effects.</p>
    <h2 class="sec"><span class="n">Every subject</span>Not just for essay courses</h2>
    <p>Graham and colleagues found the benefit was about equal in science, social studies and mathematics, and across elementary, middle and high school. The individual studies varied widely, though: some found large gains and some found little, which suggests that the design of the task matters a great deal.</p>
    <h2 class="sec"><span class="n">A caution</span>Thin evidence in college</h2>
    <p>Both meta-analyses studied schools. Research in college courses is sparser, and some studies have found no measurable effect on achievement even when students valued the writing. Short, focused prompts are a low-cost bet; they are not a guarantee.</p>
    <h2 class="sec"><span class="n">For language learners</span>Writing builds both</h2>
    <p>For students learning in a second language, short low-stakes writing gives practice using the discipline’s vocabulary without the pressure of a graded paper. Respond to the ideas first.</p>
  </div>

'''+pgrid_html(),
tips_h='Short writing that makes students think.',
tips='''      <li><b>Muddiest point</b><span>What is least clear, and why?</span></li>
      <li><b>Predict before you show</b><span>Write what will happen, then check.</span></li>
      <li><b>Explain it simply</b><span>Three sentences for a friend in another major.</span></li>''',
sources='''        <li><a href="https://doi.org/10.3102/00346543074001029">Bangert-Drowns, R. L., Hurley, M. M., &amp; Wilkinson, B. (2004). The effects of school-based writing-to-learn interventions on academic achievement: A meta-analysis. <i>Review of Educational Research, 74</i>(1), 29–58.</a></li>
        <li><a href="https://doi.org/10.3102/0034654320914744">Graham, S., Kiuhara, S. A., &amp; MacKay, M. (2020). The effects of writing on learning in science, social studies, and mathematics: A meta-analysis. <i>Review of Educational Research, 90</i>(2), 179–226.</a></li>''',
foot='The eight tasks are examples written for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Which feature predicted larger benefits from writing to learn?',o:['Prompts to reflect on one’s own understanding','Longer assignments','Typing instead of handwriting'],a:0,f:'Metacognitive prompts.'},
 {q:'Writing about content in science, social studies and maths had an average effect of about…',o:['0.30','0.03','1.30'],a:0,f:'Graham and colleagues, 2020.'},
 {q:'Is the evidence as strong for college courses?',o:['No, it is thinner and more mixed','Yes, stronger','There is none at all'],a:0,f:'Most studies are in schools.'}]''',
js=PANEL_JS+cases_js(r'''[
 ['“Muddiest point: what was least clear in today’s class, and why?”',0,'Likely to help. It asks students to monitor their own understanding, the feature most linked to benefit.'],
 ['“Copy the definitions from the slides into your notebook.”',1,'Less likely. Copying doesn’t require students to do anything with the ideas.'],
 ['“In three sentences, explain to a friend in another major why the moon has phases.”',0,'Likely to help. Short, and it requires explaining the idea in their own words.'],
 ['“A 10-page report due at the end of term, with no feedback before then.”',1,'Less likely to teach the content. Longer assignments were linked to smaller effects, and there is no reflection or feedback along the way. It may serve other goals.'],
 ['“Before the demonstration, write what you predict will happen and why.”',0,'Likely to help. A prediction makes students commit to an explanation they can then check.'],
 ['“Which strategy did you use for problem 3, and would you use it again?”',0,'Likely to help. It prompts reflection on how they learn and solve problems.'],
 ['“Write a summary by rearranging sentences from the textbook.”',1,'Less likely. Rearranging others’ sentences can be done without understanding them.'],
 ['“A weekly five-minute learning journal: what I understood, what I didn’t, what I’ll do about it.”',0,'Likely to help. Short, regular and reflective, combining monitoring with a plan.']]''','["Likely to help","Less likely"]','Likely to help learning the content?',STD_SUM)+grid('''[
 ['How many writing-to-learn programmes did the 2004 meta-analysis include?',['48','8','480'],0,'Bangert-Drowns, Hurley and Wilkinson.'],
 ['Overall, the effect of writing to learn was…',['Small but positive','Large','Negative'],0,'With big differences between programmes.'],
 ['Which feature predicted smaller effects?',['Longer writing assignments','Metacognitive prompts','Longer programmes'],0,'Along with implementation in grades 6–8.'],
 ['How many experiments were in the 2020 meta-analysis?',['56','6','560'],0,'In science, social studies and mathematics.'],
 ['Was the benefit different across those three subjects?',['No, about the same','Only in science','Only in mathematics'],0,'And across grade levels.']]''','The pattern: short writing that makes students explain and reflect helps them learn.'))
write(o)
