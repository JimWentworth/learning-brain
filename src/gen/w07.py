from wkit import *
o=wbase(7,'Learning a Language as an Adult: What Works','Learning a language','as an adult',
'Adults have one big advantage over children: they can choose how to study. The catch is that the methods that feel most effective, rereading lists and highlighting, are not the ones that work best.')
o['hero_aria'],o['hero_js']=hero(['hip','pfc'],{'hip':([600,-40],'left'),'pfc':([60,730],'left')},'Drawing of the side of the brain with the hippocampus, which helps store new words, and the prefrontal cortex, which helps retrieve them, glowing orange and labelled.')
screen='''            <p id="swS" style="font:700 clamp(24px,3vw,32px)/1.3 var(--body);color:#fff;margin:0;text-align:center;min-height:2.6em" aria-live="polite">Press Start.</p>
            <form id="swF" hidden style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center"><label for="swIn" class="sr-only">English meaning</label><input id="swIn" autocomplete="off" autocapitalize="off" spellcheck="false" style="font:600 20px var(--body);padding:10px 12px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;width:220px"><button class="nbtn" type="submit">Enter</button></form>
            <p class="prog" id="swP" aria-live="polite">&nbsp;</p>'''
student=lab(screen,'Ready','Eight Swahili words','Study eight Swahili words. Then you’ll practise half of them by studying again and half by recalling them. A final test shows which practice worked better.')
o.update(body=tabs('Eight Swahili words','Study, then practise: half by rereading, half by recalling. Which half do you remember?',student,
 'About 10 minutes, or split across two classes',
 ['Students do the activity on their own devices.',
  'For a stronger effect, stop after the practice phase and run the final test at the start of the next class.',
  'Ask which words felt better learned during practice, and which were remembered in the test.',
  'Discuss how students actually study vocabulary and terminology: rereading lists, flashcards that they flip too soon, or genuine recall?'],
 ['Which practice felt more effective at the time?',
  'Which words did you remember in the final test?',
  'How could you turn your own study of terms into recall rather than rereading?'],
 'Give students recall practice with key terms: low-stakes quizzes, flashcards used properly (answer before flipping), and returning to earlier terms in later weeks. The Learning Brain series covers retrieval and spacing in depth.',
 'With only a few minutes between practice and test, the difference can be small. In the original study the gap was large a week later.')+'''
  <div class="col lede">
    <p>In a study published in <i>Science</i>, Jeffrey Karpicke and Henry Roediger had university students learn 40 Swahili–English word pairs, such as mashua–boat, over several alternating study and test periods. Some students kept being tested on all the words; others kept studying them but were tested less.</p>
    <p>A week later, students who had been repeatedly tested on every pair recalled about 80%. Those who weren’t recalled about 35%. And the students seemed unaware of this advantage.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>40</strong><span>Swahili–English word pairs in the study</span></div>
      <div role="listitem"><strong>~80%</strong><span>recalled a week later after repeated testing</span></div>
      <div role="listitem"><strong>~35%</strong><span>recalled without repeated testing</span></div>
      <div role="listitem"><strong>Unaware</strong><span>students seemed unaware of the benefit of recall</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why recall works</span>Practising the skill you’ll need</h2>
    <p>Using a word means retrieving it: finding “boat” when you see mashua, or finding mashua when you want to say boat. Rereading practises recognising; recalling practises retrieving. Karpicke described remembering as a skill that gets better with practice.</p>
    <h2 class="sec"><span class="n">Feeling versus learning</span>Why students choose the wrong method</h2>
    <p>Rereading a list makes it feel familiar, and familiarity feels like learning. Recall is harder and produces mistakes, so it feels worse in the moment, even though it leads to more learning. Students need to know that, or they will drift back to rereading.</p>
    <h2 class="sec"><span class="n">Beyond words</span>Use, input and time</h2>
    <p>Vocabulary is only part of a language. Topic 2 covers how words build up from many encounters in context, and topic 8 how much of the vocabulary listeners need to know to follow speech. Spacing practice over days, rather than cramming, adds further benefit; the Learning Brain series covers spacing and retrieval in detail.</p>
    <h2 class="sec"><span class="n">For learning</span>It isn’t only for language courses</h2>
    <p>Every discipline asks students to learn a vocabulary. The same principle applies to anatomy, legal terms or chemical names: practise retrieving them, not just reading them.</p>
  </div>

'''+pgrid_html(),
tips_h='Recall, don’t reread.',
tips='''      <li><b>Test, don’t just show</b><span>Ask for the term before revealing it.</span></li>
      <li><b>Use flashcards properly</b><span>Answer out loud before you flip.</span></li>
      <li><b>Come back later</b><span>Revisit terms after days, not just minutes.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1126/science.1152408">Karpicke, J. D., &amp; Roediger, H. L., III. (2008). The critical importance of retrieval for learning. <i>Science, 319</i>(5865), 966–968.</a></li>''',
foot='The Swahili words come from everyday vocabulary; four of them (mashua, elimu, mbwa, mkono) appear in published accounts of the original study. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'A week later, students repeatedly tested on Swahili words recalled about…',o:['80%','35%','100%'],a:0,f:'Versus about 35% without repeated testing.'},
 {q:'Why do students often prefer rereading?',o:['It feels more familiar, so it feels like learning','It works better','It is required'],a:0,f:'Familiarity misleads.'},
 {q:'Recall practice means…',o:['Producing the answer before seeing it','Reading the list again','Copying it out'],a:0,f:'Answer first, then check.'}]''',
js=PANEL_JS+r'''
/* ---------- Swahili retrieval ---------- */
const P=[['mashua','boat'],['elimu','science'],['mbwa','dog'],['mkono','hand'],['maji','water'],['kitabu','book'],['nyumba','house'],['rafiki','friend']];
$('swF').addEventListener('submit',e=>e.preventDefault());
function typed(){return new Promise(res=>{const f=$('swF'),i=$('swIn');f.hidden=false;i.value='';i.focus();f.onsubmit=e=>{e.preventDefault();f.onsubmit=null;f.hidden=true;res(i.value.trim().toLowerCase())}})}
const okAns=(a,w)=>a===w||a===w+'s'||(w==='science'&&a==='education');
startRun(async()=>{const ps=shuf(P.map(x=>x.slice()));const rec=new Set(ps.slice(0,4).map(p=>p[0]));
 say('Study','Learn these eight words','Each pair appears for a few seconds. Try to remember them.');await nextBtn('Begin');if(!RUN)return;
 for(let i=0;i<8;i++){$('swS').innerHTML=`${ps[i][0]} – ${ps[i][1]}`;$('swP').textContent=`${i+1} of 8`;await sw(3200);if(!RUN)return}
 $('swS').textContent='';$('swP').textContent=' ';
 say('Practice','Half reread, half recall','For four words you’ll see the pair again. For the other four, type the English meaning, then see the answer.');await nextBtn('Start practice');if(!RUN)return;
 const pr=shuf(ps.slice());
 for(let i=0;i<8;i++){const [s,e]=pr[i];$('swP').textContent=`Practice ${i+1} of 8`;
  if(rec.has(s)){$('swS').textContent=s;say('Practice','Recall it','Type the English meaning.');const a=await typed();if(!RUN)return;
   $('swS').innerHTML=`${s} – ${e}`;say(null,okAns(a,e)?'Right':'Here it is',okAns(a,e)?'<b class="ok">Right.</b>':`<b class="no">Not quite.</b> It’s “${e}”.`);await sw(1800);if(!RUN)return}
  else{$('swS').innerHTML=`${s} – ${e}`;say('Practice','Study it again','Read the pair.');await sw(3600);if(!RUN)return}}
 $('swS').textContent='';say('Short break','Before the final test','If you can, come back to the final test later today or tomorrow. Otherwise, count backward from 100 by sevens in your head for about 30 seconds.');
 await nextBtn('Take the final test');if(!RUN)return;
 const got={r:0,s:0};const ft=shuf(ps.slice());
 for(let i=0;i<8;i++){const [s,e]=ft[i];$('swS').textContent=s;$('swP').textContent=`Final test ${i+1} of 8`;say('Final test','What does it mean?','Type the English meaning.');
  const a=await typed();if(!RUN)return;const ok=okAns(a,e);if(ok)got[rec.has(s)?'r':'s']++;
  say(null,null,(ok?'<b class="ok">Right.</b> ':`<b class="no">Not quite.</b> It was “${e}”. `)+(rec.has(s)?'(You recalled this one in practice.)':'(You restudied this one.)'));await sw(1300);if(!RUN)return}
 $('swS').textContent='Done.';$('swP').textContent=' ';
 $('sRes').innerHTML='<div class="res">'+barRow('Restudied',got.s,4,`${got.s} of 4`,'#FCB316')+barRow('Recalled',got.r,4,`${got.r} of 4`,'#7DD3A8')+'</div>';
 say('What happened',got.r>got.s?'Recall won':got.r===got.s?'A tie, this time':'Restudy won, this time',
  'After only a few minutes, the two kinds of practice can look similar. The benefit of recall grows with time: in Karpicke and Roediger’s study, the gap a week later was about 80% versus 35%. Try the final test again tomorrow, and see which words survive.')});
'''+grid('''[
 ['How many Swahili–English pairs did students learn in Karpicke and Roediger’s study?',['40','8','400'],0,'Across alternating study and test periods.'],
 ['A week later, students repeatedly tested on all pairs recalled about…',['80%','50%','35%'],0,'Compared with about 35% without repeated testing.'],
 ['Did students predict this difference in their own performance?',['No','Yes, accurately','They predicted the opposite strongly'],0,'Students seem unaware of the benefit of retrieval.'],
 ['In which journal was the study published?',['Science','Nature','The Lancet'],0,'Science, 2008.'],
 ['Which practice feels more effective while you’re doing it?',['Rereading','Recall','Both the same'],0,'Familiarity feels like learning.']]''','The pattern: recalling a word teaches more than seeing it again.'))
write(o)
