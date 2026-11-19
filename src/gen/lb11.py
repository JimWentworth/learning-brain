import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb11',n='11',title='Spacing and Sleep: Time Apart Makes It Last',h1='Spacing and sleep',em='Time apart makes it last',read='8',mins='2 minutes',vtitle='Spacing and sleep',
dek='The same practice, spread out over time, lasts longer than practice crammed together. Spacing feels worse while you do it. And sleep, between and after sessions, is part of how learning settles in.',
jumps='<span><a href="#sT">In a row or spread out</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: the hippocampus, which replays the day’s experiences during sleep, and the temporal lobe of the cortex, where memories are thought to settle over time.',
hero_js="BR.R.tem.lab=[300,760];BR.R.tem.al='right';BR.R.hip.lab=[700,760];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.44,s:fitS(W,H,1.32),t,active:['hip','tem'],labels:['hip','tem'],labelT:{hip:0.8,tem:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.rpair{font:800 clamp(28px,4.6vw,44px)/1.25 var(--body);color:#fff;text-align:center;min-height:1.25em}
.rpair .en{color:#FCB316}
.rcap{font-size:18px;color:#E9EEF6;text-align:center;margin:0;min-height:1.4em;max-width:36ch}
.rin{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.rin[hidden]{display:none}
.rin input{min-height:52px;width:min(280px,100%);padding:0 12px;font:700 22px var(--body);border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.rin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.brk{width:110px;height:110px;border-radius:50%;background:#3A4E72;border:4px solid #8FA3C2;cursor:pointer}
.brk.on{background:#FF8A3D}
.brk[hidden]{display:none}
.rq{display:grid;gap:8px;margin:6px 0 14px;border:1px solid var(--night-line);border-radius:8px;padding:10px 12px;color:#fff}
.rq[hidden]{display:none}
.rq legend{font-size:17px;font-weight:700;padding:0 4px}
.rq label{display:flex;align-items:center;gap:8px;font-size:17px;min-height:36px}
.res.wl2 .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl2 .row{grid-template-columns:110px minmax(0,1fr) 70px}}''',
body='''  <div class="col lede">
    <p>Memory fades fast at first, then more slowly. Hermann Ebbinghaus mapped this forgetting curve in the 1880s, testing himself on lists of nonsense syllables. Each review lifts the curve back up, and afterwards it falls more slowly.</p>
    <p>That is the spacing effect: the same amount of practice, spread out, lasts longer than practice crammed together.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>839</strong><span>tests of spaced practice, from 317 experiments, in one 2006 review</span></div>
      <div role="listitem"><strong>1,350+</strong><span>people in a follow-up study of the best gap between sessions</span></div>
      <div role="listitem"><strong>90%</strong><span>of learners in a flashcard study did better with spacing than with massing</span></div>
      <div role="listitem"><strong>72%</strong><span>of them believed massing had worked better</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The gap</span>How far apart?</h2>
    <p>Spacing is one of the most replicated findings in psychology. In 2006, Nicholas Cepeda and colleagues reviewed 839 tests of it, from 317 experiments in 184 articles. In a 2008 follow-up, they taught more than 1,350 people a set of facts, reviewed them after a gap of up to 3.5 months, then tested them up to a year later. The best gap grew with how long the memory had to last. Measured as a share of the time until the test, it was about 20 to 40% for a test a week away, and about 5 to 10% for a test a year away. For a test in a week, that means reviewing after one to three days; for a year, after about three to five weeks.</p>
    <h2 class="sec"><span class="n">The feeling</span>Spacing feels worse</h2>
    <p>Massed practice feels smooth: the answer is still fresh each time it comes back. Spaced practice feels harder, because you have partly forgotten. In 2009, Nate Kornell had students learn word pairs with flashcards. Spacing beat massing for 90% of them, yet after the first session, 72% believed massing had worked better.</p>
  </div>

  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>In a row or spread out</h2>
      <p>You’ll see 16 Swahili words with their meanings, each three times. Some words come three times in a row. Others come back spread out across the session. After a 45-second break, you’ll be tested on all 16. About 4 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <div class="rpair" id="sPair" aria-live="polite"></div>
          <p class="rcap" id="sCap"></p>
          <div class="tbar" aria-hidden="true"><i id="sTb" style="width:0"></i></div>
          <form class="rin" id="sForm" hidden><label class="sr-only" for="sIn">English meaning</label><input id="sIn" autocomplete="off" autocapitalize="off" spellcheck="false" maxlength="30"><button class="nbtn" type="submit">Enter</button></form>
          <button class="brk" id="sBrk" hidden aria-label="Tap when the circle is orange"></button>
          <p class="prog" id="sProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="sPhase">Ready</p>
          <p class="mtitle" id="sTitle">Does spacing pay, even within minutes?</p>
          <p class="mtext" id="sText" aria-live="polite">Which words come in a row and which come spread out is chosen at random. Every word is shown for the same total time.</p>
          <fieldset class="rq" id="sQ" hidden><legend>Which words will you remember better?</legend><label><input type="radio" name="sq" value="M">The ones that came three times in a row</label><label><input type="radio" name="sq" value="S">The ones that came back spread out</label><label><input type="radio" name="sq" value="E">About the same</label></fieldset>
          <div id="sRes"></div>
          <div class="mrow"><button class="nbtn" id="sGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Sleep</span>Part of the schedule</h2>
    <p>In 1994, Matthew Wilson and Bruce McNaughton recorded place cells in rats. Cells that fired together while a rat explored fired together again during the sleep that followed, as if the hippocampus were replaying the day.</p>
    <p>In people, sleep between sessions seems to help. In 2016, Stéphanie Mazza and colleagues taught 40 adults 16 French–Swahili word pairs, then had them relearn the pairs 12 hours later, either after a night’s sleep or after a day awake. Those who had slept needed about 3 rounds to relearn all 16, against about 6 for those who hadn’t, and they remembered more a week and six months later. And in 2007, Seung-Schik Yoo, Matthew Walker and colleagues found that one night without sleep cut the hippocampus’s response during new learning. The sleep-deprived group remembered 19% fewer of the pictures they studied.</p>
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
    <h2 class="sec"><span class="n">Some caution</span>Strongest for facts</h2>
    <p>The evidence for spacing is strongest for facts and vocabulary. For complex skills, results are more mixed. And many sleep studies are small, so treat them as consistent signals rather than precise numbers.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Bring it back later</h3>
      <p>Return to old material in later weeks, not only in the unit where it was taught. Make exams cumulative, so spacing pays off. Start practice early and come back to it. Set deadlines that don’t reward all-nighters, and tell students plainly that sleep is part of studying.</p>
    </aside>
  </div>
''',
tips_h='Learning settles in between sessions',
tips='''      <li><b>Bring old material back</b><span>In later weeks, not only in its own unit.</span></li>
      <li><b>Cumulative exams</b><span>So spacing pays off for students.</span></li>
      <li><b>Sleep is studying</b><span>No deadlines that reward all-nighters.</span></li>''',
sources='''        <li><a href="https://pubmed.ncbi.nlm.nih.gov/16719566/">Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., &amp; Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. <i>Psychological Bulletin</i>.</a></li>
        <li><a href="https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2008.02209.x/">Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., &amp; Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. <i>Psychological Science</i>.</a></li>
        <li><a href="https://doi.org/10.1002/acp.1537">Kornell, N. (2009). Optimising learning using flashcards: Spacing is more effective than cramming. <i>Applied Cognitive Psychology</i>.</a></li>
        <li><a href="https://doi.org/10.1126/science.8036517">Wilson, M. A., &amp; McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. <i>Science</i>.</a></li>
        <li><a href="https://www.psychologicalscience.org/news/releases/sleep-makes-relearning-faster-and-longer-lasting.html">Association for Psychological Science on Mazza, S., et al. (2016). Relearn faster and retain longer: Along with practice, sleep makes perfect. <i>Psychological Science</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/17293859/">Yoo, S.-S., Hu, P. T., Gujar, N., Jolesz, F. A., &amp; Walker, M. P. (2007). A deficit in the ability to form new human memories without sleep. <i>Nature Neuroscience</i>.</a></li>''',
quiz='''[
 {q:'For a test a year away, roughly when should you review?',o:['After about three to five weeks','The next day','The night before the test only'],a:0,f:'The best gap grows with how long the memory must last: about 5 to 10% of a year.'},
 {q:'In the flashcard study, what did most learners believe?',o:['That massing had worked better','That spacing had worked better','That neither mattered'],a:0,f:'Spacing won for 90% of them, but 72% believed massing had worked better.'},
 {q:'What did sleep between two study sessions do?',o:['Halved the practice needed to relearn, and improved memory months later','Nothing measurable','Helped only on the next morning'],a:0,f:'About 3 relearning rounds instead of 6, and better recall a week and six months later.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- in a row or spread out ----------
   16 Swahili-English pairs, 8 massed, 8 spaced. Each pair is shown 3 times for 3 s (same total time).
   Sequence in 3 segments: each segment holds one showing of every spaced pair plus 2-3 massed blocks
   (a massed block = the same pair 3 times in a row). Spaced showings of the same pair never sit next to each other.
   Then a prediction, a 45 s easy task, and a cued test of all 16 (no feedback). */
const POOL=[['kiti',['chair','seat']],['mlango',['door']],['mto',['river']],['jiwe',['stone','rock']],['kisu',['knife']],['sukari',['sugar']],['maziwa',['milk']],['kikombe',['cup']],['meza',['table']],['mwezi',['moon','month']],['nyoka',['snake']],['paka',['cat']],['viatu',['shoes','shoe']],['moto',['fire']],['jua',['sun']],['mbuzi',['goat']]];
function ed1(a,b){if(a===b)return true;if(Math.abs(a.length-b.length)>1)return false;let i=0,j=0,d=0;while(i<a.length&&j<b.length){if(a[i]===b[j]){i++;j++;continue}if(++d>1)return false;if(a.length>b.length)i++;else if(b.length>a.length)j++;else{i++;j++}}return d+(a.length-i)+(b.length-j)<=1}
function ok(typed,ans){const t=typed.toLowerCase().trim().replace(/^(a|an|the|to)\s+/,'').replace(/[^a-z ]/g,'').trim();if(!t)return false;
 return ans.some(a=>t===a||t===a+'s'||(a.length>=4&&ed1(t,a)))}
function buildSeq(items){const M=items.filter(x=>x[2]==='M'),S=items.filter(x=>x[2]==='S');const blocks=shuf([...M]);const per=[3,3,2];let bi=0;let seq=[];
 for(let g=0;g<3;g++){let units=[...S.map(x=>[x]),...blocks.slice(bi,bi+per[g]).map(x=>[x,x,x])];bi+=per[g];
  let tries=0,flat;do{flat=shuf([...units]).flat();tries++}while(tries<200&&seq.length&&flat[0][0]===seq[seq.length-1][0]);seq=seq.concat(flat)}
 return seq}
let sr=null;
function sTimer(sec,me){const t0=performance.now();const tick=()=>{if(!sr||sr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('sTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
const pairHTML=(s,e)=>`${s} <span aria-hidden="true">=</span><span class="sr-only">means</span> <span class="en">${e}</span>`;
async function hold(sec){const me=Symbol();sr.tok=me;sTimer(sec,me);await sw(sec*1000);if(!sr)return false;sr.tok=null;$('sTb').style.width='0';return true}
function sAsk(){return new Promise(res=>{sr.res=res;$('sForm').hidden=false;$('sIn').value='';$('sIn').focus()})}
$('sForm').addEventListener('submit',e=>{e.preventDefault();if(!sr||!sr.res)return;const r=sr.res;sr.res=null;$('sForm').hidden=true;r($('sIn').value)});
async function sBreak(){$('sPair').textContent='Easy break';$('sCap').textContent='';$('sBrk').hidden=false;$('sBrk').focus();let on=false;const me=Symbol();sr.tok=me;
 $('sProg').textContent='For 45 seconds, tap the circle (or press Space) whenever it turns orange.';
 const brk=$('sBrk');brk.onclick=()=>{if(on){on=false;brk.classList.remove('on')}};const t0=performance.now();sTimer(45,me);
 while(performance.now()-t0<45000){await sw(1000+Math.random()*1800);if(!sr)return;on=true;brk.classList.add('on');await sw(900);on=false;brk.classList.remove('on')}
 brk.hidden=true;sr.tok=null;$('sTb').style.width='0'}
$('sBrk').addEventListener('keydown',e=>{if(e.key===' '){e.preventDefault();$('sBrk').click()}});
function sWait(label){return new Promise(res=>{const b=$('sGo');b.textContent=label;b.disabled=false;b.focus();b.onclick=()=>{b.onclick=null;b.disabled=true;b.textContent='In progress';res()}})}
$('sGo').addEventListener('click',async()=>{if(sr||$('sGo').onclick)return;sr={};const g=$('sGo');g.disabled=true;g.textContent='In progress';$('sRes').innerHTML='';
 const sets=shuf([...'MMMMMMMMSSSSSSSS']);const items=shuf([...POOL]).map((p,i)=>[p[0],p[1],sets[i]]);const seq=buildSeq(items);
 $('sPhase').textContent='Step 1 of 3 · Study';$('sTitle').textContent='Learn the words';$('sText').textContent='Each showing lasts 3 seconds. Just learn what each word means.';
 for(let i=0;i<seq.length;i++){const [s,a]=seq[i];$('sPair').innerHTML=pairHTML(s,a[0]);$('sCap').textContent='';$('sProg').textContent=`Showing ${i+1} of ${seq.length}`;if(!await hold(3))return}
 $('sPair').textContent='One question';$('sProg').textContent='';$('sPhase').textContent='Step 2 of 3 · Break';$('sTitle').textContent='Your prediction';$('sText').textContent='Some words came three times in a row. Others came back spread out. Make a guess, then take a short break.';
 $('sQ').hidden=false;document.querySelectorAll('#sQ input').forEach(n=>n.checked=false);$('sQ').querySelector('input').focus();
 await sWait('Start the break');if(!sr)return;const pr=(document.querySelector('input[name="sq"]:checked')||{}).value||'';$('sQ').hidden=true;
 $('sTitle').textContent='Step away';$('sText').textContent='An easy, 45-second task.';await sBreak();if(!sr)return;
 $('sPhase').textContent='Step 3 of 3 · Test';$('sTitle').textContent='Test';$('sText').textContent='Type the English for each word. Leave it blank if you don’t know. No feedback.';
 let M=0,S=0;const order=shuf([...items]);
 for(let i=0;i<16;i++){const [s,a,set]=order[i];$('sPair').textContent=s;$('sCap').textContent='What does it mean in English?';$('sProg').textContent=`Word ${i+1} of 16`;
  const v=await sAsk();if(!sr)return;if(ok(v,a)){if(set==='M')M++;else S++}}
 $('sPair').textContent='Done';$('sCap').textContent='';$('sProg').textContent='Done.';$('sPhase').textContent='Your results';
 const row=(l,n,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${n/8*100}%;background:${c}"></i></div><b>${n} of 8</b></div>`;
 $('sRes').innerHTML=`<div class="res wl2">${row('Three in a row',M,'#C9D3E3')}${row('Spread out',S,'#FCB316')}</div>`;
 const pTxt=pr==='M'?' You predicted the words in a row would do better, as most people in the flashcard study believed.':pr==='S'?' You predicted the spread-out words would do better.':pr==='E'?' You predicted no difference.':'';
 let title,text;
 if(M>=7&&S>=7){title='Near perfect on both';text=`You got ${M} of 8 words seen in a row and ${S} of 8 spread out.${pTxt} After only a short break, both sets can still be fresh. The spacing advantage grows as the test gets further away.`}
 else if(S-M>=2){title='Spacing won';text=`Same time on every word, but you got ${S} of 8 spread-out words and only ${M} of 8 words seen in a row.${pTxt} The second and third showings in a row added little, because the word was still fresh. Coming back after a gap, when it had partly faded, each showing did more work.`}
 else if(M-S>=2){title='In a row won this time';text=`You got ${M} of 8 words seen in a row and ${S} of 8 spread out.${pTxt} With eight words in each set and a short break, chance plays a big part. Across hundreds of studies, spacing comes out ahead, and the gap grows over days.`}
 else{title='Close this time';text=`You got ${M} of 8 words seen in a row and ${S} of 8 spread out.${pTxt} After a 45-second break, the difference can be small. Across hundreds of studies, spacing comes out ahead, and the gap grows over days.`}
 $('sTitle').textContent=title;$('sText').textContent=text;g.onclick=null;g.textContent='Try again';g.disabled=false;g.focus();sr=null});

/* ---------- predict the findings ---------- */
const PI=[
 ['For a test one week away, the best gap between two study sessions',['A few days','Zero: study twice in a row','About a month'],0,'About 20 to 40% of the week: one to three days.'],
 ['For a test one year away, the best gap',['About three to five weeks','A few days','Six months'],0,'About 5 to 10% of the year. The best gap grows with the test delay.'],
 ['Flashcards studied in one big stack (spaced) against small stacks (massed)',['Spacing better for 90% of learners','Massing better for most learners','No difference'],0,'Yet 72% believed massing had worked better.'],
 ['Rat place cells during the sleep after exploring',['Fired together again in the same pairings','Fell silent','Fired at random'],0,'As if the hippocampus were replaying the day.'],
 ['Relearning 16 word pairs after a night’s sleep against after a day awake',['Sleepers needed about half the practice','Same practice needed','Sleepers needed more practice'],0,'About 3 rounds against about 6, and better recall six months later.'],
 ['Learning new pictures after one night without sleep',['Fewer remembered, with less hippocampal response','No difference','More remembered, from extra effort'],0,'19% fewer pictures, and a weaker hippocampal response during learning.']];
const NP=PI.length;
$('pGrid').innerHTML=PI.map(([q,o],i)=>`<div class="prow"><p class="it" id="pq${i}">${i+1}. ${q}</p><fieldset aria-labelledby="pq${i}"><legend>${q}</legend>${shuf(o.map((t,j)=>[t,j])).map(([t,j])=>`<label><input type="radio" name="p${i}" value="${j}">${t}</label>`).join('')}</fieldset><p class="ex" id="px${i}" hidden></p></div>`).join('');
$('pCheck').addEventListener('click',()=>{let right=0,ans=0;PI.forEach(([q,o,a,ex],i)=>{const sel=document.querySelector(`input[name="p${i}"]:checked`);let lead;
  if(!sel)lead=`<b class="no">Not answered.</b> ${o[a]}. `;else{ans++;const ok=+sel.value===a;if(ok)right++;lead=ok?`<b>Right.</b> `:`<b class="no">Not quite.</b> ${o[a]}. `}
  const x=$('px'+i);x.innerHTML=lead+ex;x.hidden=false});
 document.querySelectorAll('#pGrid input').forEach(n=>n.disabled=true);
 $('pSum').textContent=(ans===0?'You didn’t make any predictions, so here are the answers. ':`You got ${right} of ${ans} prediction${ans>1?'s':''} right${ans<NP?` (${NP-ans} left blank)`:''}. `)+'The pattern: gaps and sleep make memories last, even though cramming feels better at the time.';
 $('pCheck').hidden=true;$('pReset').hidden=false;$('pReset').focus()});
$('pReset').addEventListener('click',()=>{document.querySelectorAll('#pGrid input').forEach(n=>{n.disabled=false;n.checked=false});document.querySelectorAll('#pGrid .ex').forEach(x=>{x.hidden=true;x.innerHTML=''});$('pSum').textContent='';$('pReset').hidden=true;$('pCheck').hidden=false;document.querySelector('#pGrid input').focus()});
''')
open('lb11/template.html','w').write(page(o))
