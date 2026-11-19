import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb14',n='14',title='Stress and Emotion: Challenge, Not Threat',h1='Stress and emotion',em='Challenge, not threat',read='8',mins='2½ minutes',vtitle='Stress and emotion',
dek='Emotional arousal tags a moment as worth keeping. But the same stress chemistry takes the thinking part of the brain offline, which is why test anxiety hurts. The aim is challenge without threat.',
jumps='<span><a href="#eT">Which words stick?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with three areas glowing orange and labelled: the amygdala, which responds to emotional arousal; the hippocampus, which it signals to store the moment more strongly; and the prefrontal cortex, which stress quickly impairs.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.amy.lab=[300,770];BR.R.amy.al='right';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['amy','hip','pfc'],labels:['amy','hip','pfc'],labelT:{amy:0.8,hip:1.0,pfc:1.2},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.ew{font:800 clamp(30px,5vw,48px)/1.2 var(--body);color:#fff;text-align:center;min-height:1.2em}
.ecap{font-size:18px;color:#E9EEF6;text-align:center;margin:0;min-height:1.4em;max-width:36ch}
.ein{display:flex;flex-direction:column;gap:10px;align-items:center;width:100%}
.ein[hidden]{display:none}
.ein textarea{width:100%;max-width:440px;min-height:120px;padding:10px 12px;font:600 19px/1.4 var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;resize:vertical}
.ein textarea:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:110px;height:110px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>Two versions of a slide show tell nearly the same story. In one, a boy visits a hospital with his mother. In the other, he is badly hurt on the way and rushed into surgery. A week later, people remember the emotional version better, especially its middle, where the accident happens.</p>
    <p>In 1994, Larry Cahill, James McGaugh and colleagues found that a drug that blocks adrenaline’s effects, propranolol, removed that advantage.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1 week</strong><span>after the slide show, the emotional version was remembered better</span></div>
      <div role="listitem"><strong>Mild stress</strong><span>if uncontrollable, is enough to impair the prefrontal cortex quickly</span></div>
      <div role="listitem"><strong>10 min</strong><span>of writing about worries before an exam helped the most anxious students</span></div>
      <div role="listitem"><strong>GRE math</strong><span>scores were higher for students told their nerves could help them</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Arousal</span>Tagged as worth keeping</h2>
    <p>Emotional arousal releases stress hormones. The amygdala responds and signals the hippocampus to store the moment more strongly, as <a href="@@LB:amy@@">the amygdala page</a> describes. Arousal tags an experience as worth keeping.</p>
    <h2 class="sec"><span class="n">The cost</span>Thinking goes offline</h2>
    <p>The same chemistry has a cost. Amy Arnsten’s research shows that even quite mild stress, if it feels uncontrollable, rapidly impairs the prefrontal cortex, the home of working memory and flexible thought, while strengthening fast emotional responses. Timing matters too. A 2017 meta-analysis by Grant Shields and colleagues found that stress shortly after learning can help memory, while stress just before or during recall impairs it.</p>
  </div>

  <section class="night" aria-labelledby="eT">
    <div class="col">
      <h2 class="sec" id="eT"><span class="n">Try it</span>Which words stick?</h2>
      <p>24 words, one every 2 seconds. Half are emotionally charged; half are everyday objects. After a 30-second break, type all the words you remember. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="eScreen">
          <div class="ew" id="eW" aria-live="polite"></div>
          <p class="ecap" id="eCap"></p>
          <div class="tbar" aria-hidden="true"><i id="eTb" style="width:0"></i></div>
          <form class="ein" id="eForm" hidden><label class="sr-only" for="eIn">Type the words you remember</label><textarea id="eIn" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Type the words, in any order"></textarea><button class="nbtn" type="submit">Done</button></form>
          <button class="brk" id="eBrk" hidden aria-label="Tap when the circle is orange"></button>
          <p class="prog" id="eProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="ePhase">Ready</p>
          <p class="mtitle" id="eTitle">Does emotion help memory?</p>
          <p class="mtext" id="eText" aria-live="polite">Just read each word as it appears. The two kinds come in random order.</p>
          <div id="eRes"></div>
          <div class="mrow"><button class="nbtn" id="eGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Test anxiety</span>Worry takes up working memory</h2>
    <p>That is why test anxiety hurts: worries take up the working memory the test needs. In 2011, Gerardo Ramirez and Sian Beilock asked ninth graders to write for 10 minutes about their worries just before their first high-school final exam. Among those who wrote, the most anxious students did about as well as their calmer classmates. In 2010, Jeremy Jamieson and colleagues told students preparing for the GRE graduate admissions test that feeling nervous could help them perform. They scored higher on the maths section, both in a practice test and on the real exam one to three months later.</p>
  </div>

  <section aria-labelledby="brT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="brT"><span class="n">Try it</span>Predict the findings</h2>
      <p>For each comparison from the research, predict what was found. Then check.</p>
    </div>
    <div class="wide">
      <form class="pgrid" id="pGrid"></form>
      <div class="qrow"><button class="pbtn" id="pCheck" type="button">Check my predictions</button><button class="pbtn" id="pReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="pSum" aria-live="polite"></p>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Some caution</span>A sketch, not a law</h2>
    <p>The familiar inverted U, where a little arousal helps and too much hurts, is a useful sketch, not a precise law. Some emotional memory findings have not always replicated: a 1999 study using the same slide show found no effect of propranolol on memory. And chronic stress, lasting weeks or months, is a different problem from a tense exam.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Challenge without threat</h3>
      <p>Keep stakes clear and predictable. Spread grades across many small assessments rather than a few huge ones. Before big exams, give students a few minutes to write about their worries, and tell them that nerves are energy they can use.</p>
    </aside>
  </div>
''',
tips_h='Arousal helps memory keep a moment; threat takes thinking offline',
tips='''      <li><b>Clear, predictable stakes</b><span>Many small assessments, not a few huge ones.</span></li>
      <li><b>Write out the worry</b><span>A few minutes before a big exam.</span></li>
      <li><b>Nerves as energy</b><span>Tell students arousal can help them perform.</span></li>''',
sources='''        <li><a href="https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/41277805">Cahill, L., Prins, B., Weber, M., &amp; McGaugh, J. L. (1994). β-Adrenergic activation and memory for emotional events. <i>Nature</i>.</a></li>
        <li><a href="https://www.psych.ox.ac.uk/publications/139158">O’Carroll, R. E., et al. (1999). Memory for emotional material: A comparison of central versus peripheral beta blockade. <i>Journal of Psychopharmacology</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/2907136/">Arnsten, A. F. T. (2009). Stress signalling pathways that impair prefrontal cortex structure and function. <i>Nature Reviews Neuroscience</i>.</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5436944">Shields, G. S., Sazma, M. A., McCullough, A. M., &amp; Yonelinas, A. P. (2017). The effects of acute stress on episodic memory: A meta-analysis and integrative review. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://news.uchicago.edu/story/writing-about-worries-eases-anxiety-and-improves-test-performance">University of Chicago on Ramirez, G., &amp; Beilock, S. L. (2011). Writing about testing worries boosts exam performance in the classroom. <i>Science</i>.</a></li>
        <li><a href="https://dash.harvard.edu/handle/1/4214916">Jamieson, J. P., Mendes, W. B., Blackstock, E., &amp; Schmader, T. (2010). Turning the knots in your stomach into bows: Reappraising arousal improves performance on the GRE. <i>Journal of Experimental Social Psychology</i>.</a></li>''',
quiz='''[
 {q:'When does acute stress tend to help memory?',o:['Shortly after learning','Just before a test','During recall'],a:0,f:'Stress just before or during recall tends to impair it.'},
 {q:'Why does test anxiety hurt performance?',o:['Worries take up the working memory the test needs','It makes people study less','It weakens long-term memories'],a:0,f:'Writing out the worries first helped anxious students.'},
 {q:'What happened when students were told their nerves could help them?',o:['They scored higher on the GRE maths section','They felt calmer but scored the same','They scored lower'],a:0,f:'The benefit showed in a practice test and on the real exam.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- which words stick? ----------
   12 emotionally charged + 12 neutral words, random order, 2 s each. 30 s easy task. Free recall. Count each kind. */
const EMO=['danger','scream','kiss','fire','panic','thief','crash','victory','alarm','terror','rescue','storm'];
const NEU=['table','pencil','carpet','button','basket','folder','shelf','bottle','curtain','hallway','napkin','stapler'];
function ed1(a,b){if(a===b)return true;if(Math.abs(a.length-b.length)>1)return false;let i=0,j=0,d=0;while(i<a.length&&j<b.length){if(a[i]===b[j]){i++;j++;continue}if(++d>1)return false;if(a.length>b.length)i++;else if(b.length>a.length)j++;else{i++;j++}}return d+(a.length-i)+(b.length-j)<=1}
const match=(t,w)=>t===w||t===w+'s'||t===w+'es'||(w.length>=5&&ed1(t,w));
function count(txt,list){const toks=[...new Set(txt.toLowerCase().split(/[^a-z]+/).filter(Boolean))];return new Set(toks.map(t=>list.find(w=>match(t,w))).filter(Boolean)).size}
let er=null;
function eTimer(sec,me){const t0=performance.now();const tick=()=>{if(!er||er.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('eTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
async function hold(sec){const me=Symbol();er.tok=me;eTimer(sec,me);await sw(sec*1000);if(!er)return false;er.tok=null;$('eTb').style.width='0';return true}
async function eBreak(){$('eW').textContent='Easy break';$('eCap').textContent='';$('eBrk').hidden=false;$('eBrk').focus();let on=false;const me=Symbol();er.tok=me;
 $('eProg').textContent='For 30 seconds, tap the circle (or press Space) whenever it turns orange.';
 const brk=$('eBrk');brk.onclick=()=>{if(on){on=false;brk.classList.remove('on')}};const t0=performance.now();eTimer(30,me);
 while(performance.now()-t0<30000){await sw(1000+Math.random()*1800);if(!er)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;er.tok=null;$('eTb').style.width='0'}
$('eBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('eBrk').click()}});
function eRecall(){return new Promise(res=>{er.res=res;$('eForm').hidden=false;$('eIn').value='';$('eIn').focus()})}
$('eForm').addEventListener('submit',e=>{e.preventDefault();if(!er||!er.res)return;const r=er.res;er.res=null;$('eForm').hidden=true;r($('eIn').value)});
$('eGo').addEventListener('click',async()=>{if(er)return;er={};const g=$('eGo');g.disabled=true;g.textContent='In progress';$('eRes').innerHTML='';
 const seq=shuf([...EMO,...NEU]);
 $('ePhase').textContent='Step 1 of 3 · Read';$('eTitle').textContent='Just read';$('eText').textContent='One word every 2 seconds.';
 for(let i=0;i<seq.length;i++){$('eW').textContent=seq[i];$('eCap').textContent='';$('eProg').textContent=`Word ${i+1} of 24`;if(!await hold(2))return}
 $('eW').textContent='';$('ePhase').textContent='Step 2 of 3 · Break';$('eTitle').textContent='Step away';$('eText').textContent='An easy, 30-second task.';await eBreak();if(!er)return;
 $('ePhase').textContent='Step 3 of 3 · Recall';$('eTitle').textContent='Recall';$('eText').textContent='Type every word you remember, in any order.';$('eW').textContent='Which words?';$('eProg').textContent='';
 const v=await eRecall();if(!er)return;const e=count(v,EMO),n=count(v,NEU);
 $('eW').textContent='Done';$('eProg').textContent='Done.';$('ePhase').textContent='Your results';
 const row=(l,k,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${k/12*100}%;background:${c}"></i></div><b>${k} of 12</b></div>`;
 $('eRes').innerHTML=`<div class="res wl2">${row('Everyday',n,'#C9D3E3')}${row('Emotional',e,'#FCB316')}</div><p class="mtext">The emotional words: ${EMO.join(', ')}.</p>`;
 let title,text;
 if(e+n<4){title='Too few words to compare';text=`You recalled ${e} emotional and ${n} everyday words. That’s too few to compare. Try again, and read each word as it appears.`}
 else if(e>=10&&n>=10){title='Near perfect on both';text=`You recalled ${e} emotional and ${n} everyday words. A short list after a short break is easy. In the slide-show study, the emotional advantage showed up a week later.`}
 else if(e-n>=2){title='Emotion helped';text=`You recalled ${e} of 12 emotional words and ${n} of 12 everyday ones. Charged words grab attention and arousal. One caution: emotional words are also more related to each other than everyday objects are, and that alone helps memory. Studies try to rule this out; a quick demo can’t.`}
 else if(n-e>=2){title='Everyday words won this time';text=`You recalled ${n} of 12 everyday words and ${e} of 12 emotional ones. With 12 words of each, chance plays a part. Mildly charged words on a screen are a weak version of real emotional arousal.`}
 else{title='About the same this time';text=`You recalled ${e} of 12 emotional words and ${n} of 12 everyday ones. Words on a screen carry only a little arousal; the effect is clearest for events that really move people, and after a longer delay.`}
 $('eTitle').textContent=title;$('eText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();er=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['A slide show with an emotional middle, compared with a neutral version, a week later',['Emotional version remembered better','Neutral version remembered better','No difference'],0,'Especially the emotional middle of the story.'],
 ['The same emotional slide show, after a drug that blocks adrenaline’s effects',['The emotional advantage disappeared','The advantage grew','Memory for everything dropped'],0,'Propranolol removed the advantage in the 1994 study.'],
 ['A 1999 study repeating the drug test with the same slide show',['Found no effect of the drug on memory','Found the same effect','Found a bigger effect'],0,'Some emotional memory findings have not always replicated.'],
 ['Acute stress shortly after learning',['Tends to help memory','Tends to hurt memory','No effect'],0,'Stress after learning can help consolidation.'],
 ['Acute stress just before or during recall',['Tends to impair recall','Tends to help recall','No effect'],0,'Which is part of why test anxiety hurts.'],
 ['Highly anxious ninth graders who wrote about their worries for 10 minutes before a final',['Did about as well as calmer classmates','Did worse','No change'],0,'Writing out worries seemed to free working memory.'],
 ['Students told their nervous arousal could help them on the GRE',['Higher maths scores','Lower maths scores','No difference'],0,'Both in a practice test and on the real exam.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: arousal helps memory keep a moment, but stress at the wrong time, or felt as threat, gets in the way.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb14/template.html','w').write(page(o))
