from wkit import *
o=wbase(5,'Is Younger Always Better? Age and Second Languages','Is younger','always better?',
'Children seem to soak up languages. Adults seem to struggle. A study of two-thirds of a million people put numbers on when language-learning ability changes, and the answer is later than many expected.')
o['hero_aria'],o['hero_js']=hero(['tem','hip'],{'tem':([300,770],'left'),'hip':([600,-40],'left')},'Drawing of the side of the brain with the temporal lobe and hippocampus, involved in learning language, glowing orange and labelled.')
screen='''            <p id="agQ" style="font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;margin:0;min-height:4em" aria-live="polite">Press Start.</p>
            <div id="agSl" hidden style="width:100%;max-width:440px;color:#E9EEF6"><label for="agIn" id="agLab" style="font-weight:700;display:block;margin-bottom:6px">Your estimate</label><input id="agIn" type="range" style="width:100%;accent-color:#FF5F05"><p id="agVal" style="margin:4px 0 0;font:800 26px var(--body);color:#fff;text-align:center"></p></div>'''
student=lab(screen,'Ready','Make your estimates','Four questions about age and learning a second language. Drag the slider to your best guess, then see what a very large study found.')
o.update(body=tabs('Make your estimates','When does the ability to learn a new language’s grammar start to decline? Guess first.',student,
 'About 10 minutes',
 ['Have everyone write down their estimate for question 1 before you reveal it. Collect a few.',
  'Work through the remaining questions the same way.',
  'Discuss what the study did and didn’t measure: grammar, in English, through an online quiz.',
  'Ask: what does this mean for adult students learning in English in this course?'],
 ['Were you surprised by the age?',
  'Why might children who start early still end up more native-like?',
  'What does this mean for adult students who are still learning English?'],
 'Many of your students are still learning the language of instruction, and they are fully capable of learning more of it. Judge their understanding by their ideas, and treat grammar errors as part of the process, unless language accuracy is the point of the task.',
 'The estimates are about grammar learning and native-like attainment, not about whether adults can become fluent; many do.')+'''
  <div class="col lede">
    <p>Joshua Hartshorne, Joshua Tenenbaum and Steven Pinker put a 10-minute English grammar quiz online. It went viral, and they collected complete data from 669,498 native and non-native speakers, along with each person’s age and the age they started learning English.</p>
    <p>Their model separated current age, age at first exposure and years of experience. It estimated that the ability to learn grammar is preserved until about age 17.4 and then declines steadily.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>669,498</strong><span>native and non-native English speakers took the quiz</span></div>
      <div role="listitem"><strong>17.4</strong><span>the age until which grammar-learning ability was preserved</span></div>
      <div role="listitem"><strong>Before 10</strong><span>the start needed to reach native-like grammar, by the authors’ estimate</span></div>
      <div role="listitem"><strong>Easy too</strong><span>the decline held for easy as well as difficult grammar</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">A late window</span>Later than many thought</h2>
    <p>Previous debate centred on whether learning ability declines from birth, from around age five, or from puberty. This study placed the end of the critical period for grammar learning much later than previously speculated. The decline held not only for difficult grammar but also for easy constructions that children normally master early.</p>
    <h2 class="sec"><span class="n">Why start early?</span>Time to learn</h2>
    <p>If learning ability stays high until about 17, why does starting early matter? Because becoming native-like takes years of learning. The authors estimated that people need to start before about age 10 to reach native-like grammar, since starting later leaves too little time before the ability declines.</p>
    <h2 class="sec"><span class="n">The limits</span>What was measured</h2>
    <p>The quiz tested English grammar online. It doesn’t speak to vocabulary, pronunciation, fluency or the ability to use a language well for study and work, and “not native-like” is not the same as “not proficient”.</p>
    <h2 class="sec"><span class="n">For learning</span>Adults keep learning</h2>
    <p>Adult students learning in a second language are still building it. Their grammar may stay slightly non-native for life while their command of the subject is excellent. Topic 7 covers what helps adults learn a language most efficiently.</p>
  </div>

'''+pgrid_html(),
tips_h='Adults are still learning the language. Judge the ideas.',
tips='''      <li><b>Separate ideas from grammar</b><span>Unless language accuracy is the learning goal.</span></li>
      <li><b>Expect lifelong accents</b><span>Non-native grammar or pronunciation isn’t a sign of weaker understanding.</span></li>
      <li><b>Support continued growth</b><span>Model the language of your field and give feedback on it when it matters.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.cognition.2018.04.007">Hartshorne, J. K., Tenenbaum, J. B., &amp; Pinker, S. (2018). A critical period for second language acquisition: Evidence from 2/3 million English speakers. <i>Cognition, 177</i>, 263–277.</a></li>''',
foot='The estimation questions summarise one large study. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Grammar-learning ability was preserved until about age…',o:['17','5','30'],a:0,f:'17.4, then a steady decline.'},
 {q:'To reach native-like grammar, people needed to start by about…',o:['Age 10','Age 17','Age 3'],a:0,f:'Because it takes years to get there.'},
 {q:'What did the study measure?',o:['English grammar, through an online quiz','Overall fluency','Vocabulary size'],a:0,f:'So it doesn’t cover everything about proficiency.'}]''',
js=PANEL_JS+r'''
/* ---------- estimates ---------- */
const QS=[
 {q:'Up to about what age does the ability to learn a new language’s grammar stay strong?',min:2,max:40,step:1,v:10,u:' years',ans:17,show:'about 17.4 years',f:'The model estimated that grammar-learning ability is preserved until about 17.4, then declines steadily.'},
 {q:'To reach native-like grammar, by about what age do learners need to start?',min:0,max:30,step:1,v:15,u:' years',ans:10,show:'before about 10',f:'Reaching native-like grammar takes years, so a later start leaves too little time before the ability declines.'},
 {q:'How many people took the grammar quiz?',min:1,max:7,step:1,v:3,u:'',ans:6,labels:['1,000','10,000','50,000','100,000','300,000','670,000','2 million'],show:'669,498',f:'The quiz went viral, giving a dataset of unprecedented size.'},
 {q:'Did the same decline show up for easy grammar, the kind young children master early?',min:0,max:2,step:1,v:1,u:'',ans:2,labels:['No','Partly','Yes'],show:'yes',f:'The decline held for easy grammar as well as difficult grammar.'}];
const fmt=q=>v=>q.labels?q.labels[v-(q.min===1?1:0)]:v+q.u;
startRun(async()=>{let close=0;
 for(let i=0;i<QS.length;i++){const q=QS[i],f=fmt(q);const s=$('agIn');s.min=q.min;s.max=q.max;s.step=q.step;s.value=q.v;s.disabled=false;$('agSl').hidden=false;
  const upd=()=>{$('agVal').textContent=f(+s.value)};s.oninput=upd;upd();$('agQ').textContent=q.q;
  say(`Question ${i+1} of 4`,'Your estimate','Drag the slider, then press Done.');s.focus();await nextBtn('Done');if(!RUN)return;
  s.disabled=true;const v=+s.value;const ok=Math.abs(v-q.ans)<=(q.labels?0:2);if(ok)close++;
  say(null,`Answer: ${q.show}`,(ok?'<b class="ok">Close.</b> ':`<b class="no">You said ${f(v)}.</b> `)+q.f);
  if(i<3){await nextBtn('Next question');if(!RUN)return}}
 $('agSl').hidden=true;$('agQ').textContent='Done.';
 say('What happened',`${close} of 4 close`,'Language-learning ability lasts longer than many people think, but reaching native-like grammar still takes an early start because it takes so long. Adults remain capable learners; native-like grammar is a different target from fluent, effective use.')});
'''+grid('''[
 ['How many people’s data did the study use?',['669,498','6,694','66,949'],0,'Native and non-native English speakers.'],
 ['Grammar-learning ability was preserved until about…',['17.4 years','5 years','25 years'],0,'Then it declined steadily.'],
 ['Was this offset earlier or later than previously speculated?',['Much later','Much earlier','About the same'],0,'Earlier debate focused on birth, age five or puberty.'],
 ['Did the decline affect easy grammar too?',['Yes','No, only hard grammar','No decline was found'],0,'Even constructions children master early.'],
 ['What did the model separate?',['Current age, age at first exposure and years of experience','Gender and income','Native language and country'],0,'Which allowed a direct estimate of learning ability by age.']]''','The pattern: the window lasts into the late teens, and native-like grammar needs an early start.'))
write(o)
