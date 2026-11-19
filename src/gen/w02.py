from wkit import *
o=wbase(2,'How Words Are Learned: Encounters, Context and Retrieval','How words','are learned',
'Nobody learns a word in one go. Each encounter adds a little: its form, its meaning, how it is used. Context helps, repetition helps, and deliberately recalling a word helps most of all.')
o['hero_aria'],o['hero_js']=hero(['tem','hip'],{'tem':([300,770],'left'),'hip':([600,-40],'left')},'Drawing of the side of the brain with the temporal lobe, which stores word meanings, and the hippocampus, which helps learn new words, glowing orange and labelled.')
student=lab(TEXT_SCREEN,'Ready','Learn six new words','You will read a dozen sentences containing six made-up words. Some words appear once, some three times. Then you will be asked what each word means.')
o.update(body=tabs('Learn six new words','Made-up words in real sentences. Some you meet once, some three times. How much does each encounter add?',student,
 'About 10 minutes',
 ['Students read the sentences on their own devices without writing anything down.',
  'Run the meaning test. Ask: were the words you met three times easier?',
  'Now ask students to use two of the words in a sentence of their own, without looking. Which could they do?',
  'Connect to your subject: which key terms do students meet only once or twice?'],
 ['Which words could you guess from one sentence? Which could you use yourself?',
  'What did the second and third sentence add?',
  'How many times do students meet each key term in your course, and in how many different contexts?'],
 'Plan for repeated, varied encounters with key terms: in the reading, in your talk, in problems, and in low-stakes quizzes where students must recall the term themselves.',
 'Guessing a meaning from a rich sentence is easier than knowing a word well enough to use it. The test here only checks recognition.')+'''
  <div class="col lede">
    <p>Words are mostly learned gradually. Researchers who study second-language vocabulary distinguish incidental learning, picking words up while reading or listening for meaning, from intentional learning, setting out to learn them.</p>
    <p>Incidental learning works, but slowly. A 2023 meta-analysis by Stuart Webb, Takumi Uchihara and Akifumi Yanagisawa found average gains of roughly 15% of target words from reading or listening, on both immediate and delayed tests.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~15%</strong><span>of new words learned, on average, from reading or listening alone</span></div>
      <div role="listitem"><strong>r = .34</strong><span>the link between number of encounters and learning: a medium effect</span></div>
      <div role="listitem"><strong>26 studies</strong><span>and 1,918 learners in that meta-analysis of repetition</span></div>
      <div role="listitem"><strong>~80%</strong><span>of Swahili words recalled a week later by students who were repeatedly tested on them</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Repetition</span>Each encounter adds a little</h2>
    <p>Uchihara, Webb and Yanagisawa pooled 26 studies with 1,918 learners and found a medium relationship between the number of encounters with a word and how well it was learned (r = .34). How much each encounter helped depended on the learner, the spacing of the encounters, visual support and how learning was tested.</p>
    <h2 class="sec"><span class="n">Context</span>Quality, not just quantity</h2>
    <p>In an earlier study, Webb gave learners target words in contexts that varied in how much they revealed. The informativeness of the context mattered more for learning a word’s meaning, while the number of encounters mattered more for learning its form.</p>
    <h2 class="sec"><span class="n">Retrieval</span>Recall beats rereading</h2>
    <p>In a well-known study, Jeffrey Karpicke and Henry Roediger had students learn 40 Swahili–English word pairs. A week later, students who had been repeatedly tested on all the pairs recalled about 80% of them, while those who kept studying but were not repeatedly tested recalled about 35%. Topic 7 looks at this in more detail.</p>
    <h2 class="sec"><span class="n">For learning</span>Every subject has a vocabulary</h2>
    <p>This applies to the technical terms of any course, not only to foreign languages. A term met once in a reading is unlikely to stick; a term met several times, in different contexts, and recalled in a quiz, is far more likely to.</p>
  </div>

'''+pgrid_html(),
tips_h='Plan the encounters. Then make students recall.',
tips='''      <li><b>Several encounters</b><span>Key terms should come back in reading, talk and problems.</span></li>
      <li><b>Informative contexts</b><span>Use examples that make the meaning clear.</span></li>
      <li><b>Recall, not just recognise</b><span>Quiz students on producing the term from its meaning.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1111/lang.12343">Uchihara, T., Webb, S., &amp; Yanagisawa, A. (2019). The effects of repetition on incidental vocabulary learning: A meta-analysis of correlational studies. <i>Language Learning, 69</i>(3), 559–599.</a></li>
        <li>Webb, S., Uchihara, T., &amp; Yanagisawa, A. (2023). How effective is second language incidental vocabulary learning? A meta-analysis. <i>Language Teaching, 56</i>(2), 161–180.</li>
        <li><a href="http://hdl.handle.net/10125/66826">Webb, S. (2008). The effects of context on incidental vocabulary learning. <i>Reading in a Foreign Language, 20</i>(2).</a></li>
        <li><a href="https://doi.org/10.1126/science.1152408">Karpicke, J. D., &amp; Roediger, H. L., III. (2008). The critical importance of retrieval for learning. <i>Science, 319</i>(5865), 966–968.</a></li>''',
foot='The six words are made up for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Learning words just from reading or listening is…',o:['Real but slow','Instant','Impossible'],a:0,f:'About 15% of target words, on average.'},
 {q:'More encounters with a word generally lead to…',o:['More learning','Less learning','No change'],a:0,f:'A medium relationship, r = .34.'},
 {q:'Which helped students remember Swahili words a week later?',o:['Repeatedly recalling them','Repeatedly rereading them','Copying them'],a:0,f:'About 80% versus about 35%.'}]''',
js=PANEL_JS+r'''
/* ---------- six words ---------- */
const WORDS=[
 ['tarvish',['She shook the rain off her tarvish before stepping inside.','The wind turned his cheap tarvish inside out.','Bring a tarvish; the forecast says showers all afternoon.'],['an umbrella','a coat','a bicycle','a dog']],
 ['meskle',['He filled the meskle and switched it on.','The meskle whistled loudly on the stove.','Don’t touch the meskle; the water just boiled.'],['a kettle','a cup','an oven','a spoon']],
 ['drovel',['The painter leaned his drovel against the wall.','He climbed the drovel to clean the gutters.','Hold the drovel steady while I reach the top shelf.'],['a ladder','a rope','a brush','a table']],
 ['quisp',['He quisped her name, afraid of waking the baby.','In the library, students quisp instead of talking.','She quisped the answer so the others wouldn’t hear.'],['to whisper','to shout','to run','to laugh']],
 ['lorrent',['My lorrent little brother insists on wearing boots in summer.','The lorrent mule refused to move, no matter how hard we pulled.','Even with good evidence, he stayed lorrent and wouldn’t change his mind.'],['stubborn','tired','generous','clever']],
 ['fennick',['A dry summer meant a poor fennick.','Farmers worked from dawn to dusk during the autumn fennick.','After the fennick, the barns were full of grain.'],['a harvest','a storm','a market','a wedding']]];
startRun(async()=>{const ws=shuf(WORDS.map(w=>w.slice()));const n3=new Set(ws.slice(0,3).map(w=>w[0]));
 let sents=[];ws.forEach(([w,ss])=>{(n3.has(w)?ss:[ss[0]]).forEach(s=>sents.push(s.replace(w,`<b>${w}</b>`)))});sents=shuf(sents);
 say('Reading','Read each sentence','Read for meaning, as you would any text. Don’t try to memorise.');
 for(let i=0;i<sents.length;i++){$('csS').innerHTML=sents[i];$('csP').textContent=`Sentence ${i+1} of ${sents.length}`;await nextBtn('Next sentence');if(!RUN)return}
 $('csS').textContent='Now the test.';$('csP').textContent='';
 const got={1:0,3:0};const order=shuf(ws.slice());
 for(let i=0;i<order.length;i++){const [w,ss,opts]=order[i];const k=n3.has(w)?3:1;
  $('csS').innerHTML=`What does <b>${w}</b> mean?`;$('csP').textContent=`Word ${i+1} of 6`;say('Test',null,'');
  const sh=shuf(opts.map((t,j)=>[t,j]));const a=await ask(sh.map(x=>x[0]),`What does ${w} mean?`);if(!RUN)return;const ok=sh[a][1]===0;if(ok)got[k]++;mark(sh.findIndex(x=>x[1]===0),a);
  say(null,null,(ok?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+`It means ${opts[0]}. You met it ${k===3?'three times':'once'}.`);
  if(i<5){await nextBtn('Next word');if(!RUN)return;hideCh()}}
 $('csS').textContent='Done.';$('csP').textContent='';
 $('sRes').innerHTML='<div class="res">'+barRow('Met once',got[1],3,`${got[1]} of 3`,'#FCB316')+barRow('Met 3 times',got[3],3,`${got[3]} of 3`,'#7DD3A8')+'</div>';
 say('What happened',got[3]>got[1]?'More encounters, more words':'Recognition is the easy part','Recognising a meaning in a test, right after reading, is the easiest kind of word knowledge. Using the word yourself, spelling it and remembering it next week take more: several encounters in varied contexts, and practice recalling it.')});
'''+grid('''[
 ['On average, what share of new words do learners pick up from reading or listening alone?',['About 15%','About 60%','About 2%'],0,'Webb, Uchihara and Yanagisawa, 2023.'],
 ['How strong is the link between number of encounters and vocabulary learning?',['Medium (r = .34)','None','Very strong (r = .90)'],0,'Uchihara, Webb and Yanagisawa, 2019.'],
 ['In Webb’s 2008 study, what mattered more for learning a word’s meaning?',['How informative the context was','How many times it appeared','How long the word was'],0,'Number of encounters mattered more for learning its form.'],
 ['A week later, students repeatedly tested on Swahili words recalled about…',['80%','35%','10%'],0,'Karpicke and Roediger, 2008.'],
 ['And students who kept studying but weren’t repeatedly tested recalled about…',['35%','80%','60%'],0,'Recall made the difference.']]''','The pattern: words build up over encounters, and recall makes them stick.'))
write(o)
