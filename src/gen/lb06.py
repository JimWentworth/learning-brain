import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb06',n='6',title='Working Memory Limits: Why Less Is More',h1='Working memory limits',em='Why less is more',read='8',mins='2½ minutes',vtitle='Working memory limits',
dek='You can hold only a few things in mind at once, and they fade within seconds. Experts get around the limit by packing more into each chunk. Teaching that respects the limit leaves room for the ideas that matter.',
jumps='<span><a href="#cT">Hold the letters</a></span><span><a href="#dT">Find the part</a></span>',
hero_aria='Drawing of the side of the brain with two areas glowing orange and labelled: the prefrontal cortex at the front, and the intraparietal sulcus, a groove in the parietal lobe. Both are active when people hold information in mind.',
hero_js="BR.R.pfc.lab=[60,730];BR.R.pfc.al='left';BR.R.ips.lab=[560,-70];BR.R.ips.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.44,s:fitS(W,H,1.32),t,active:['pfc','ips'],labels:['pfc','ips'],labelT:{pfc:0.8,ips:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.cl{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 8px;min-height:1.4em;max-width:100%}
.cl span{font:800 clamp(22px,4.6vw,38px)/1.3 var(--body);color:#fff;min-width:.8em;text-align:center}
.cl .msg{font-size:clamp(20px,3vw,26px);font-weight:700;color:#C9D3E3}
.cin{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.cin[hidden]{display:none}
.cin input{min-height:52px;width:min(300px,100%);padding:0 12px;font:700 22px var(--body);letter-spacing:.12em;text-transform:uppercase;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.cin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.tbar{width:100%;max-width:420px;height:8px;background:#1B2E50;border-radius:4px;overflow:hidden}.tbar i{display:block;height:100%;background:#FCB316}
.res.wl .row{grid-template-columns:150px minmax(0,1fr) 90px}
@media (max-width:520px){.res.wl .row{grid-template-columns:110px minmax(0,1fr) 80px}}
.dq{font:800 clamp(22px,3vw,28px)/1.3 var(--body);color:var(--ink);text-align:center;margin:0 0 12px;min-height:1.3em}
.dwrap{display:grid;grid-template-columns:minmax(0,1fr) 190px;gap:56px;align-items:center}
@media (max-width:700px){.dwrap{grid-template-columns:minmax(0,1fr);gap:18px}}
.dg{position:relative;height:340px;background:#F3F6FA;border-radius:10px}
@media (max-width:700px){.dg{height:300px}}
.dg svg{position:absolute;inset:0;width:100%;height:100%}
.dg button{position:absolute;transform:translate(-50%,-50%);min-width:86px;min-height:46px;padding:0 8px;border-radius:10px;border:3px solid #13294B;background:#fff;color:#13294B;font:800 17px var(--body);cursor:pointer}
@media (max-width:700px){.dg button{min-width:70px;min-height:44px;font-size:15px;padding:0 4px}}
.dg button.num{min-width:48px;border-radius:50%;font-size:19px}
.dg button:focus-visible{outline:3px solid #B84300;outline-offset:2px}
.dg button.bad{border-color:#B84300;background:#FCE9DE}
.dleg{background:#fff;border:2px solid #13294B;border-radius:10px;padding:12px 16px;min-height:120px}
.dleg h3{font:800 15px var(--body);letter-spacing:.08em;text-transform:uppercase;margin:0 0 8px;color:var(--ink-2)}
.dleg ol{list-style:none;margin:0;padding:0;display:grid;gap:4px;font-size:17px}
@media (max-width:700px){.dleg ol{grid-template-columns:1fr 1fr}}
.dleg ol b{display:inline-block;min-width:1.6em}
.dleg p{margin:0;font-size:17px;color:var(--ink-2)}
.dmsg{text-align:center;font-size:17px;margin:12px 0 0;min-height:1.5em}''',
body='''  <div class="col lede">
    <p>Read these ten letters once, then look away and say them back: F B I C I A N A S A. Hard? Now read them as FBI, CIA, NASA. Three things instead of ten, and suddenly easy.</p>
    <p>That is working memory: the small mental space where you hold and work with ideas right now. It is tiny, it fades fast, and it decides how much new material a learner can take in at once.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>7 ± 2</strong><span>items, George Miller’s famous 1956 estimate of how much people can hold</span></div>
      <div role="listitem"><strong>About 4</strong><span>chunks, Nelson Cowan’s 2001 estimate once rehearsal and grouping are ruled out</span></div>
      <div role="listitem"><strong>18 s</strong><span>after which fewer than 1 in 10 unrehearsed three-letter strings were recalled</span></div>
      <div role="listitem"><strong>20+</strong><span>chess pieces a master could put back after a 5-second look at a real game</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The limit</span>How much fits</h2>
    <p>In 1956, the psychologist George Miller noted that people can repeat back about seven items, give or take two. He also saw that the unit that counts is not a letter or a digit but a chunk: a group that means something to you. In 2001, Nelson Cowan reviewed the evidence again and argued that once people can’t rehearse or group items, the true limit is nearer four chunks. Prefrontal and parietal regions, including the intraparietal sulcus, are among the areas that stay active while people hold information in mind.</p>
    <h2 class="sec"><span class="n">The fade</span>Gone in seconds</h2>
    <p>Working memory also fades. In 1959, Lloyd and Margaret Peterson asked students to remember three consonants, then count backwards by threes so they couldn’t rehearse. After 3 seconds, about 80% of the letter strings were recalled. After 18 seconds, fewer than 10% were.</p>
  </div>

  <section class="night" aria-labelledby="cT">
    <div class="col">
      <h2 class="sec" id="cT"><span class="n">Try it</span>Hold the letters</h2>
      <p>You’ll see a row of 12 letters for 6 seconds. When they disappear, type as many as you can, in order. Six rows in all. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="cScreen">
          <div class="cl" id="cL"></div>
          <div class="tbar" aria-hidden="true"><i id="cTb" style="width:0"></i></div>
          <form class="cin" id="cForm" hidden><label class="sr-only" for="cIn">Type the letters in order</label><input id="cIn" autocomplete="off" autocapitalize="characters" spellcheck="false" maxlength="20"><button class="nbtn" type="submit">Check</button></form>
          <p class="prog" id="cProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="cPhase">Ready</p>
          <p class="mtitle" id="cTitle">How many letters can you hold?</p>
          <p class="mtext" id="cText" aria-live="polite">Read the letters any way you like. You’ll get a score for each row: the number of letters you typed in the right order.</p>
          <div id="cRes"></div>
          <div class="mrow"><button class="nbtn" id="cGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Expertise</span>Chunks are where expertise lives</h2>
    <p>In the 1940s, the Dutch psychologist Adriaan de Groot showed chess players a real game position for a few seconds, then asked them to rebuild it. Masters put back almost every piece. In 1973, William Chase and Herbert Simon repeated the test with a 5-second look: a master could place 20 or more pieces, a beginner about four. Then came the control. On boards with the pieces placed at random, everyone, master or beginner, placed only about three or four.</p>
    <p>The master’s working memory was no bigger. Years of play had stored thousands of familiar patterns in long-term memory, so a cluster of pieces became one chunk. Knowledge makes working memory go further, but only for material in your own field.</p>
    <h2 class="sec"><span class="n">Teaching</span>Load you can’t avoid, and load you can</h2>
    <p>John Sweller’s cognitive load theory, first set out in 1988, builds on this limit. Some load comes from the material itself: a hard idea with many parts that interact. That load can only be broken into smaller steps. Other load comes from how the material is presented, and that part is under the teacher’s control.</p>
    <p>One example is split attention. When a diagram’s labels sit in a separate key, learners have to hold a name in mind while they search for it, so effort goes into the layout, not the content. Paul Chandler and John Sweller found that putting the text into the diagram itself helped learning. Decorative pictures and on-screen text that is read aloud word for word add load too.</p>
  </div>

  <section aria-labelledby="dT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Find the part</h2>
      <p>A machine with eight parts. Each round, tap the part named above it as fast as you can. Sometimes the names are on the drawing. Sometimes the parts have numbers and the names are in a key. 12 rounds, about 1 minute.</p>
    </div>
    <div class="wide">
      <div class="lbox">
        <p class="dq" id="dQ" aria-live="polite">Press Start.</p>
        <div class="dwrap">
          <div class="dg" id="dG" role="group" aria-label="Machine diagram"></div>
          <div class="dleg" id="dLeg"><h3>Key</h3><p>The key appears here when it’s needed.</p></div>
        </div>
        <p class="dmsg" id="dMsg" aria-live="polite"></p>
        <div class="qrow" style="justify-content:center"><button class="pbtn" id="dGo">Start</button></div>
        <div id="dRes" aria-live="polite"></div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Some caution</span>Two limits of the theory</h2>
    <p>First, load is hard to measure. Studies use self-ratings of effort, speed on a second task, or body signals, and these don’t always agree. Ton de Jong, among others, has argued that this makes the theory hard to test. Second, what helps a beginner can hinder an expert. Slava Kalyuga and colleagues called this the expertise reversal effect: worked examples and full guidance help novices, but for learners who already know the material, the extra guidance becomes redundant and can make learning worse.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Spend the space on what matters</h3>
      <p>Give new material in small steps, put labels on the diagram, and cut what doesn’t teach. Start beginners with worked examples, then fade the help as their chunks grow, and give more freedom to the learners who are ready for it.</p>
    </aside>
  </div>
''',
tips_h='Working memory is a narrow doorway',
tips='''      <li><b>Small steps</b><span>Break complex ideas into parts a learner can hold at once.</span></li>
      <li><b>Labels on the diagram</b><span>Don’t make learners hunt between a picture and a key.</span></li>
      <li><b>Worked examples first</b><span>Then fade the help as knowledge builds up.</span></li>''',
sources='''        <li><a href="https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf">Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. <i>Behavioral and Brain Sciences</i>. (Discusses Miller, 1956.)</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034">Cowan, N. (2010). The magical mystery four: How is working memory capacity limited, and why? <i>Current Directions in Psychological Science</i>.</a></li>
        <li><a href="https://www.simplypsychology.org/peterson-peterson.html">Simply Psychology: Peterson, L. R., &amp; Peterson, M. J. (1959). Short-term retention of individual verbal items.</a></li>
        <li><a href="https://andymatuschak.org/prompts/Chase1973.pdf">Chase, W. G., &amp; Simon, H. A. (1973). Perception in chess. <i>Cognitive Psychology</i>.</a></li>
        <li><a href="https://www.Gwern.net/doc/psychology/chess/1973-simon.pdf">Simon, H. A., &amp; Chase, W. G. (1973). Skill in chess. <i>American Scientist</i>. (Random positions: about three or four pieces for all players.)</a></li>
        <li><a href="https://doi.org/10.1207/s15516709cog1202_4">Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. <i>Cognitive Science</i>.</a></li>
        <li><a href="https://doi.org/10.1207/s1532690xci0804_2">Chandler, P., &amp; Sweller, J. (1991). Cognitive load theory and the format of instruction. <i>Cognition and Instruction</i>.</a></li>
        <li><a href="https://doi.org/10.1007/s11251-009-9110-0">de Jong, T. (2010). Cognitive load theory, educational research, and instructional design: Some food for thought. <i>Instructional Science</i>.</a></li>
        <li><a href="https://doi.org/10.1207/S15326985EP3801_4">Kalyuga, S., Ayres, P., Chandler, P., &amp; Sweller, J. (2003). The expertise reversal effect. <i>Educational Psychologist</i>.</a></li>''',
quiz='''[
 {q:'Why could a chess master rebuild a real game position from a 5-second look?',o:['Familiar patterns let a group of pieces count as one chunk','Masters have a bigger working memory','Masters see faster'],a:0,f:'On random boards, masters did no better than beginners.'},
 {q:'Which kind of load can a teacher reduce by changing how material is presented?',o:['Extraneous load, such as labels kept apart from a diagram','Intrinsic load, the difficulty of the idea itself','Neither'],a:0,f:'The difficulty of the idea can only be broken into smaller steps.'},
 {q:'What is the expertise reversal effect?',o:['Help that suits beginners can hinder learners who already know the material','Experts forget faster than beginners','Beginners learn best without guidance'],a:0,f:'Worked examples help novices; for experts they become redundant.'}]''',
js=r'''
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
/* ---------- hold the letters ----------
   6 rows of 12 letters, shown 6 s. Three rows are four familiar abbreviations run together; three rows use the letters
   of four other abbreviations shuffled, so no abbreviation (and no doubled letter) remains. Same letters, different chunks.
   Score: longest common subsequence of typed and shown letters (letters in the right order, 0-12). */
const ACR=['USA','DVD','ATM','CEO','PDF','VIP','DIY','FAQ','GPS','SUV','UFO','CPR','BBQ','IOU'];
function lcs(a,b){const d=Array.from({length:a.length+1},()=>new Array(b.length+1).fill(0));for(let i=1;i<=a.length;i++)for(let j=1;j<=b.length;j++)d[i][j]=a[i-1]===b[j-1]?d[i-1][j-1]+1:Math.max(d[i-1][j],d[i][j-1]);return d[a.length][b.length]}
function scrambled(){const src=shuf([...ACR]).slice(0,4).join('').split('');let s,n=0;
 do{s=shuf(src).join('');n++}while(n<500&&(/(.)\1/.test(s)||ACR.some(a=>s.includes(a))));return s}
let cr=null;
function cTimer(sec,me){const t0=performance.now();const tick=()=>{if(!cr||cr.tok!==me)return;const f=Math.min(1,(performance.now()-t0)/(sec*1000));$('cTb').style.width=(100-f*100)+'%';if(f<1)requestAnimationFrame(tick)};tick()}
function cShow(s){$('cL').innerHTML=s.split('').map(c=>`<span>${c}</span>`).join('');$('cL').setAttribute('aria-label',s.split('').join(' '))}
function cMsg(t){$('cL').innerHTML=`<span class="msg">${t}</span>`;$('cL').removeAttribute('aria-label')}
function cAnswer(){return new Promise(res=>{cr.res=res;$('cForm').hidden=false;$('cIn').value='';$('cIn').focus()})}
$('cForm').addEventListener('submit',e=>{e.preventDefault();if(!cr||!cr.res)return;const v=$('cIn').value.toUpperCase().replace(/[^A-Z]/g,'');const r=cr.res;cr.res=null;$('cForm').hidden=true;r(v)});
function cNext(){return new Promise(res=>{const b=$('cGo');b.textContent='Next row';b.disabled=false;b.focus();b.onclick=()=>{b.onclick=null;b.disabled=true;b.textContent='In progress';res()}})}
$('cGo').addEventListener('click',async()=>{if(cr||$('cGo').onclick)return;cr={};const go=$('cGo');go.disabled=true;go.textContent='In progress';$('cRes').innerHTML='';
 const pool=shuf([...ACR]);const kinds=shuf(['C','C','C','R','R','R']);let ci=0;const sc={C:[],R:[]};
 for(let i=0;i<6;i++){
  const k=kinds[i];let s,grp;if(k==='C'){grp=pool.slice(ci*4,ci*4+4);ci++;s=grp.join('')}else{s=scrambled()}
  $('cPhase').textContent=`Row ${i+1} of 6`;$('cTitle').textContent='Watch the letters';$('cText').textContent='They disappear after 6 seconds.';
  cMsg('Get ready…');$('cProg').textContent=`Row ${i+1} of 6`;await sw(1000);if(!cr)return;
  cShow(s);const me=Symbol();cr.tok=me;cTimer(6,me);await sw(6000);if(!cr)return;cr.tok=null;$('cTb').style.width='0';
  cMsg('Type them in order');$('cTitle').textContent='Now type them';$('cText').textContent='Type the letters you remember, in order. Leave out any you’ve lost.';
  const v=await cAnswer();if(!cr)return;const n=lcs(v,s);sc[k].push(n);
  $('cL').innerHTML=(k==='C'?grp:[s]).map(g=>`<span>${g}</span>`).join('<span aria-hidden="true">·</span>');$('cL').setAttribute('aria-label','The letters were '+(k==='C'?grp.join(', '):s.split('').join(' ')));
  $('cProg').textContent=`${n} of 12 in order.`;
  $('cTitle').textContent=n>=11?'Nearly all of them':n>=7?'More than half':'A tough row';
  $('cText').textContent=k==='C'?`This row was made of four abbreviations: ${grp.join(', ')}. You got ${n} of 12 letters in order.`:`This row had no familiar groups. You got ${n} of 12 letters in order.`;
  if(i<5){await cNext();if(!cr)return}}
 cMsg('Done');$('cProg').textContent='Done.';$('cPhase').textContent='Your results';
 const av=a=>a.reduce((x,y)=>x+y,0)/a.length,mC=av(sc.C),mR=av(sc.R),f=x=>x.toFixed(1).replace(/\.0$/,'');
 const row=(l,m,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${m/12*100}%;background:${c}"></i></div><b>${f(m)} of 12</b></div>`;
 $('cRes').innerHTML=`<div class="res wl">${row('No familiar groups',mR,'#C9D3E3')}${row('Abbreviations',mC,'#FCB316')}</div>`;
 let title,text;const d=mC-mR;
 if(mC>=11&&mR>=11){title='Near perfect on both';text=`You averaged ${f(mR)} of 12 without familiar groups and ${f(mC)} with them. Twelve letters in 6 seconds is beyond most people’s limit, so you probably found a strategy of your own, such as grouping or saying the letters in a rhythm. That is chunking too.`}
 else if(d>=1.5){title='Chunks did the work';text=`Same letters, very different results: an average of ${f(mR)} of 12 without familiar groups, and ${f(mC)} when the letters formed abbreviations you know. Twelve loose letters are far more than four things to hold. Four abbreviations are four things. What you already know set how much you could hold.`}
 else if(d>-1.5){title='About the same this time';text=`You averaged ${f(mR)} of 12 without familiar groups and ${f(mC)} with them. Did you spot the abbreviations while the letters were showing? Chunking helps only when you recognise the chunks in time, which is why it depends on what you already know.`}
 else{title='The rows without groups went better this time';text=`You averaged ${f(mR)} of 12 without familiar groups and ${f(mC)} with them. With only three rows of each, chance plays a big part. In studies, letters that form familiar groups are reliably easier to hold.`}
 $('cTitle').textContent=title;$('cText').textContent=text;go.onclick=null;go.textContent='Try again';go.disabled=false;go.focus();cr=null});

/* ---------- find the part (split attention) ----------
   8 parts placed at random in 8 slots each round. 12 rounds, 6 with names on the parts and 6 with numbers plus a key,
   in random order. Time from showing the round to the correct tap; wrong taps are counted. Compare medians. */
const PARTS=['valve','filter','pump','tank','gauge','heater','fan','switch'];
const SLOTS=[[12,26],[37,22],[63,26],[88,22],[12,74],[37,78],[63,74],[88,78]];
let dr=null;
const med=a=>{const s=[...a].sort((x,y)=>x-y),m=s.length>>1;return s.length%2?s[m]:(s[m-1]+s[m])/2};
function dRound(mode,target){return new Promise(res=>{
 const jit=SLOTS.map(([x,y])=>[x+(Math.random()*6-3),y+(Math.random()*8-4)]);const pos=shuf([...jit]);const nums=shuf([1,2,3,4,5,6,7,8]);
 const path=[0,1,2,3,7,6,5,4,0].map(k=>jit[k]);
 let h=`<svg aria-hidden="true" viewBox="0 0 100 100" preserveAspectRatio="none"><polyline points="${path.map(p=>p.join(',')).join(' ')}" fill="none" stroke="#8FA3C2" stroke-width="1.2" vector-effect="non-scaling-stroke" style="stroke-width:6px"/></svg>`;
 h+=PARTS.map((p,i)=>`<button type="button" data-i="${i}" class="${mode==='S'?'num':''}" style="left:${pos[i][0]}%;top:${pos[i][1]}%" ${mode==='S'?`aria-label="Part ${nums[i]}"`:''}>${mode==='S'?nums[i]:p}</button>`).join('');
 $('dG').innerHTML=h;
 $('dLeg').innerHTML=mode==='S'?`<h3>Key</h3><ol>${PARTS.map((p,i)=>[nums[i],p]).sort((a,b)=>a[0]-b[0]).map(([n,p])=>`<li><b>${n}</b>${p}</li>`).join('')}</ol>`:`<h3>Key</h3><p>No key this round: the names are on the drawing.</p>`;
 $('dQ').textContent=`Tap the ${PARTS[target]}`;$('dMsg').textContent=mode==='S'?'Numbers and a key':'Names on the drawing';
 const t0=performance.now();let err=0;
 $('dG').querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{if(!dr)return;if(+b.dataset.i===target){res({t:(performance.now()-t0)/1000,err})}else{err++;b.classList.add('bad');$('dMsg').textContent='Not that one.'}}));
 const first=$('dG').querySelector('button');if(dr.kb)first.focus()})}
$('dGo').addEventListener('click',async e=>{dr={kb:e.detail===0};$('dGo').hidden=true;$('dRes').innerHTML='';
 const modes=shuf(['I','I','I','I','I','I','S','S','S','S','S','S']);const R={I:[],S:[]},E={I:0,S:0};let last=-1;
 for(let i=0;i<12;i++){let tg;do{tg=Math.floor(Math.random()*8)}while(tg===last);last=tg;
  const r=await dRound(modes[i],tg);if(!dr)return;R[modes[i]].push(r.t);E[modes[i]]+=r.err;
  $('dG').innerHTML='';$('dQ').textContent=i<11?`Round ${i+2} of 12…`:'Done.';$('dMsg').textContent='';await sw(i<11?700:200);if(!dr)return}
 $('dLeg').innerHTML='<h3>Key</h3><p>The key appears here when it’s needed.</p>';$('dQ').textContent='Your results';
 const mI=med(R.I),mS=med(R.S),mx=Math.max(mI,mS),f=x=>x.toFixed(1);
 const row=(l,m,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${m/mx*100}%;background:${c}"></i></div><b>${f(m)} s</b></div>`;
 const r=mS/mI;let head,body;
 const errs=E.I+E.S?` Wrong taps: ${E.I} with names on the drawing, ${E.S} with the key.`:'';
 if(r>=1.2){head='The key cost you time';body=`Typical time to find a part: ${f(mI)} s with names on the drawing, ${f(mS)} s with numbers and a key.${errs} With the key, you had to hold a name and a number in mind while your eyes moved back and forth. That effort went into the layout, not the content: split attention.`}
 else if(r>=0.85){head='Little difference this time';body=`Typical time to find a part: ${f(mI)} s with names on the drawing, ${f(mS)} s with the key.${errs} With only eight parts and short names, the look-up is easy, and you may have started to remember numbers. In studies, the cost of a separate key is clearest when the material is complex and the words and picture only make sense together.`}
 else{head='The key was faster this time';body=`Typical time to find a part: ${f(mI)} s with names on the drawing, ${f(mS)} s with the key.${errs} With only six rounds of each, chance plays a big part. A short sorted list can also be quick to scan. In learning studies, labels placed in the diagram usually help more than a separate key.`}
 $('dRes').innerHTML=`<div class="lres">${row('Names on the drawing',mI,'#13294B')}${row('Numbers and a key',mS,'#B84300')}</div><p class="pmsg"><b class="h">${head}</b>${body}</p>`;
 $('dGo').hidden=false;$('dGo').textContent='Try again';$('dGo').focus();dr=null});
''')
open('lb06/template.html','w').write(page(o))
