from wkit import *
o=wbase(8,'Lectures in a Second Language: Coverage, Load and Captions','Lectures in','a second language',
'Following a lecture in a second language is a different task from following it in your first. A few unknown words per hundred can make the difference between understanding and losing the thread.')
o['hero_aria'],o['hero_js']=hero(['tem','pfc'],{'tem':([300,770],'left'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the temporal lobe, which processes speech, and the prefrontal cortex, which holds the thread of an argument, glowing orange and labelled.')
screen='''            <div id="cvT" style="background:#fff;color:#13294B;border-radius:6px;padding:18px 20px;font:17px/1.6 var(--body);max-width:540px;width:100%" aria-live="polite">The passage appears when you press Start.</div>
            <p class="prog" id="cvP">&nbsp;</p>'''
student=lab(screen,'Ready','Read with gaps','Two short passages. In one, 2 words in every 100 are unknown to you. In the other, 10 in every 100. Read each once, then answer two questions without looking back.')
o.update(body=tabs('Read with gaps','What it feels like to know 98% of the words, and then 90%. Read, then answer from memory.',student,
 'About 10 minutes',
 ['Students read each passage once, at their normal pace, then answer the questions without scrolling back.',
  'Ask how the second passage felt. What did students do when they hit an unknown word?',
  'Explain that a lecture moves at the speaker’s pace: listeners can’t reread.',
  'Look at one of your own slides or a passage of your notes. Which words might be unknown to some students?'],
 ['What did the unknown words cost you, beyond the words themselves?',
  'How would this feel at lecture speed, with no chance to reread?',
  'Which words in your course are likely unknown to students learning in a second language?'],
 'Give students the key terms before class, post slides or notes in advance, caption your recordings, and speak at a steady pace with pauses after key points. Each of these lets students prepare or recover the words they missed.',
 'Reading lets you pause and reread; listening doesn’t. If anything, this activity understates how hard a lecture with unknown words can be.')+'''
  <div class="col lede">
    <p>Researchers call the share of words in a text that a reader or listener knows <i>lexical coverage</i>. Most research suggests that coverage of 95–98% is needed for adequate comprehension, in other words, that only 2–5% of words can be unknown.</p>
    <p>That sounds generous until you translate it. At 95% coverage, one word in every 20 is unknown; at 98%, one in every 50.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>98%</strong><span>coverage needed for adequate unassisted reading, in a widely cited study</span></div>
      <div role="listitem"><strong>95%</strong><span>may be enough for informal listening</span></div>
      <div role="listitem"><strong>1 in 20</strong><span>words unknown at 95% coverage; 1 in 50 at 98%</span></div>
      <div role="listitem"><strong>Large</strong><span>effect of captions on second-language listening comprehension</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Reading</span>The 98% figure</h2>
    <p>In a widely cited study, Marcella Hu and Paul Nation found that about 98% coverage was needed for adequate, unassisted reading comprehension of a relatively easy fiction text. Later work suggested two thresholds: 95% for minimal comprehension and 98% for good comprehension.</p>
    <h2 class="sec"><span class="n">Listening</span>Informal talk versus lectures</h2>
    <p>Hilde van Zeeland and Norbert Schmitt found that 95% coverage may be enough to follow informal spoken narratives, which can be reached with 2,000–3,000 word families. Academic listening is a different matter: one study found that 98% coverage was needed for academic listening.</p>
    <h2 class="sec"><span class="n">Captions</span>Seeing the words helps</h2>
    <p>A 2013 meta-analysis by Maribel Montero Perez, Wim Van den Noortgate and Piet Desmet pooled studies of second-language learners watching video with captions in the same language. Captions had a large effect on listening comprehension (15 studies) and on vocabulary learning (10 studies).</p>
    <h2 class="sec"><span class="n">For learning</span>Give students a way to catch up</h2>
    <p>A lecture runs at the speaker’s pace. A reader can stop on an unknown word; a listener loses it, and often the next sentence too. Key terms in advance, slides and notes to review, and captioned recordings give students learning in a second language the chance to recover what they missed.</p>
  </div>

'''+pgrid_html(),
tips_h='Let students meet the words before they meet the lecture.',
tips='''      <li><b>Key terms first</b><span>Post a short list of terms and definitions before class.</span></li>
      <li><b>Slides and notes ahead</b><span>So students can preview and review.</span></li>
      <li><b>Caption everything</b><span>A large benefit for second-language listeners.</span></li>''',
sources='''        <li>Hu, M., &amp; Nation, I. S. P. (2000). Unknown vocabulary density and reading comprehension. <i>Reading in a Foreign Language, 13</i>(1), 403–430.</li>
        <li>van Zeeland, H., &amp; Schmitt, N. (2013). Lexical coverage in L1 and L2 listening comprehension: The same or different from reading comprehension? <i>Applied Linguistics, 34</i>(4), 457–479.</li>
        <li>Schmitt, N., Cobb, T., Horst, M., &amp; Schmitt, D. (2015). How much vocabulary is needed to use English? Replication of van Zeeland &amp; Schmitt (2012), Nation (2006) and Cobb (2007). <i>Language Teaching</i>.</li>
        <li><a href="https://doi.org/10.1016/j.system.2013.07.013">Montero Perez, M., Van Den Noortgate, W., &amp; Desmet, P. (2013). Captioned video for L2 listening and vocabulary learning: A meta-analysis. <i>System, 41</i>(3), 720–739.</a></li>''',
foot='The two passages and their unknown words are made up for this activity. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Adequate comprehension usually needs about what share of words to be known?',o:['95–98%','70%','50%'],a:0,f:'Lexical coverage.'},
 {q:'At 95% coverage, how often is a word unknown?',o:['About 1 in 20','About 1 in 200','About 1 in 5'],a:0,f:'At 98%, about 1 in 50.'},
 {q:'For second-language learners, same-language captions had…',o:['A large effect on listening comprehension','No effect','A negative effect'],a:0,f:'Montero Perez and colleagues, 2013.'}]''',
js=PANEL_JS+r'''
/* ---------- coverage ---------- */
const PASS=[
 {cov:'98%',t:'Most cities clean their drinking water in several steps. First, water from a river or lake passes through screens that remove leaves and fish. Then chemicals are added that make tiny particles stick together into larger <u>vorbels</u>, which sink to the bottom of large tanks. The clearer water on top flows through beds of sand and <u>plinter</u> that trap smaller particles. Finally, a small amount of chlorine is added to kill bacteria, and the water is pumped through pipes to homes. Engineers test samples throughout the day to make sure the water stays safe.',
  q:[['What makes the tiny particles sink?',['Chemicals that make them stick together','Screens that catch them','Chlorine that dissolves them'],0],['Why is chlorine added?',['To kill bacteria','To remove leaves','To make particles clump']]].map(x=>x.length===2?[...x,0]:x)},
 {cov:'90%',t:'Honeybees tell each other where to find food by dancing. A <u>trelp</u> that has found a <u>brannish</u> <u>skeld</u> of flowers returns to the hive and performs a waggle dance on the <u>opple</u> surface of the <u>dorrow</u>. The <u>flinch</u> of the dance, relative to straight up, shows the <u>meskwith</u> of the food relative to the sun. The <u>durrow</u> of the waggle run shows how far away the food is. Other bees <u>vasken</u> the dancer, smell the flowers on her body, and then fly out to search. Bees can even <u>pondle</u> for the movement of the sun during the day.',
  q:[['What does the dance’s angle relative to straight up tell other bees?',['Which way to fly, relative to the sun','How far away the food is','How much food there is'],0],['What else does the waggle run tell them?',['How far away the food is','What colour the flowers are','When the flowers open'],0]]}];
startRun(async()=>{const res=[];
 for(let p=0;p<2;p++){const P_=PASS[p];$('cvT').innerHTML=P_.t;$('cvP').textContent=`Passage ${p+1} of 2 · ${P_.cov} of words known`;
  say(`Passage ${p+1} of 2`,'Read it once','Read at your normal pace. Underlined words are unknown to you. Press the button when you’re done; you won’t be able to look back.');
  await nextBtn('Done reading');if(!RUN)return;$('cvT').innerHTML='<i>Passage hidden.</i>';let r=0;
  for(let k=0;k<2;k++){const [qq,os,ai]=P_.q[k];say('Questions',qq,'');const sh=shuf(os.map((x,j)=>[x,j]));const a=await ask(sh.map(x=>x[0]),qq);if(!RUN)return;const ok=sh[a][1]===ai;if(ok)r++;mark(sh.findIndex(x=>x[1]===ai),a);
   say(null,null,ok?'<b class="ok">Right.</b>':`<b class="no">Not quite.</b> ${os[ai]}.`);await nextBtn(k?'Continue':'Next question');if(!RUN)return;hideCh()}
  const h=await ask(['Easy','A bit hard','Hard','Very hard'],'How hard was that passage to follow?');if(!RUN)return;hideCh();res.push([P_.cov,r,h])}
 $('cvT').innerHTML='<i>Done.</i>';$('cvP').textContent=' ';const lab=['easy','a bit hard','hard','very hard'];
 $('sRes').innerHTML='<div class="res">'+res.map(([c,r])=>barRow(c+' known',r,2,`${r} of 2`,c==='98%'?'#7DD3A8':'#FCB316')).join('')+'</div>';
 say('What happened','Ten in a hundred is a lot',`You rated the 98% passage ${lab[res[0][2]]} and the 90% passage ${lab[res[1][2]]}. At 90% coverage, unknown words land in almost every sentence, and they often hit the words that carry the meaning. In a lecture, there is no going back to reread. That is why research suggests 95–98% coverage is needed, and why key terms in advance and captions help so much.`)});
'''+grid('''[
 ['Most research suggests adequate comprehension needs what lexical coverage?',['95–98%','80–85%','100%'],0,'Only 2–5% of words unknown.'],
 ['In Hu and Nation’s widely cited study, what coverage was needed for adequate unassisted reading?',['About 98%','About 90%','About 80%'],0,'Of a relatively easy fiction text.'],
 ['For informal spoken narratives, van Zeeland and Schmitt found what coverage may be enough?',['95%','80%','99%'],0,'Reached with 2,000–3,000 word families.'],
 ['Did captions help second-language learners’ listening comprehension?',['Yes, a large effect','No effect','They hurt it'],0,'Across 15 studies.'],
 ['And vocabulary learning from video?',['Yes, a large effect','No effect','Only for beginners'],0,'Across 10 studies.']]''','The pattern: a few unknown words per hundred decide whether a lecture can be followed.'))
write(o)
