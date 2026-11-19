import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb03',n='3',title='Priming: Warming Up the Network',h1='Priming',em='Warming up the network',read='8',mins='2 minutes',vtitle='Priming',
dek='What you have just seen or thought about quietly shapes what comes next. Related ideas get a head start, and new information sticks better when something is already switched on for it to attach to.',
jumps='<span><a href="#ldT">Word or not?</a></span><span><a href="#paT">Topic first</a></span>',
hero_aria='Drawing of the brain with the temporal lobe glowing orange and labelled. The temporal lobe is central to stored knowledge about words and meanings.',
hero_js="BR.R.tem.lab=[300,700];BR.R.tem.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.42,s:fitS(W,H,1.32),t,active:['tem'],labels:['tem'],labelT:{tem:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''.ldw{font:800 clamp(34px,6vw,52px)/1.2 var(--body);color:#fff;min-height:1.3em;letter-spacing:.04em;text-align:center}
.ldp{font:600 clamp(22px,3.5vw,30px)/1.2 var(--body);color:#C9D3E3;min-height:1.3em;text-align:center}
.pass{font-size:19px;line-height:1.7;max-width:640px;margin:14px 0 0}
.ptopic{font-weight:800;font-size:18px;color:#B84300;margin:10px 0 0;min-height:1.4em}
.rec textarea{width:100%;max-width:640px;min-height:140px;padding:12px;font:400 18px/1.5 var(--body);border:2px solid #5A6B82;border-radius:8px;color:var(--ink)}
.rec textarea:focus-visible{outline:3px solid #13294B;outline-offset:2px}
.rec label{display:block;font-weight:700;font-size:17px;margin:14px 0 6px}
.ideas{margin:8px 0 0;padding-left:0;list-style:none;font-size:16px;line-height:1.5}
.ideas .y{color:#1F5C3F;font-weight:700}.ideas .n{color:#5A6B82}
.small{font-size:16px;color:var(--ink-2);margin:10px 0 0}''',
body='''  <div class="col lede">
    <p>Read this word: doctor. Now this one: nurse. In 1971, David Meyer and Roger Schvaneveldt asked 12 high-school students to decide, as fast as they could, whether two strings of letters were both real words. When the words were related, like doctor and nurse, answers came about 85 milliseconds faster than for unrelated pairs like bread and door.</p>
    <p>That head start is called semantic priming. It suggests that knowledge isn’t stored as a list. It’s a web of related ideas, and touching one part of the web warms up its neighbours.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>85 ms</strong><span>faster for related word pairs in the classic 1971 study</span></div>
      <div role="listitem"><strong>About 2×</strong><span>as much recalled when people were told the topic of a vague passage first</span></div>
      <div role="listitem"><strong>8 + 5 vs 13</strong><span>seconds: guessing first, then studying, beat studying for the whole time</span></div>
      <div role="listitem"><strong>2012</strong><span>a careful replication of a famous behaviour-priming study found no effect</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The web</span>Closer to the threshold</h2>
    <p>One leading explanation, described by Allan Collins and Elizabeth Loftus in 1975, is spreading activation. When one idea is activated, some of that activity spreads along the links to related ideas. They are not fully switched on, but they are closer to the threshold, so when one of them actually arrives, it takes less to tip it over.</p>
    <p>Something similar happens when you meet the same thing twice. The second time, the brain does less work for the same result: in brain scans, the response to a repeated item is smaller. This can happen even when you don’t remember the first encounter.</p>
  </div>

  <section class="night" aria-labelledby="ldT">
    <div class="col">
      <h2 class="sec" id="ldT"><span class="n">Try it</span>Word or not?</h2>
      <p>A small word flashes, then a word in capitals appears. Decide as fast as you can whether the capitals spell a real English word. Ignore the small word. 32 rounds.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="lScreen" tabindex="0" role="group" aria-label="Word decision. Press J for a real word, F for not a word, or tap the buttons." aria-describedby="lProg">
          <div class="ldp" id="lP" aria-hidden="true"></div>
          <div class="ldw" id="lW" aria-hidden="true"></div>
          <div class="keys" id="lKeys" hidden><button id="lNo">Not a word<small>F</small></button><button id="lYes">Real word<small>J</small></button></div>
          <p class="prog" id="lProg" aria-live="polite">Press Start. Keep your fingers on F and J.</p>
        </div>
        <div>
          <p class="phase" id="lPhase">Ready</p>
          <p class="mtitle" id="lTitle">Does the small word help?</p>
          <p class="mtext" id="lText" aria-live="polite">Sometimes the small word is related to the word in capitals, sometimes not. Your speed for each kind is compared at the end.</p>
          <div id="lRes"></div>
          <div class="mrow"><button class="nbtn" id="lGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <p>If you are using a screen reader, the timing in this activity won’t be meaningful. The text around it describes the result.</p>
    <h2 class="sec"><span class="n">Prime the lesson</span>Something to attach to</h2>
    <p>Priming matters for learning because new information needs something already active to attach to. In 1972, John Bransford and Marcia Johnson had people listen to a vague paragraph describing a procedure: sort things into groups, go somewhere else if you have to, and so on. One group was told the topic first: washing clothes. They recalled about twice as much as people who heard no topic. People told the topic only afterwards did no better than those never told at all. The words were identical. What changed was what was already active when they arrived.</p>
  </div>

  <section aria-labelledby="paT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="paT"><span class="n">Try it</span>Topic first, or topic after?</h2>
      <p>You’ll read two short, vague passages. For one, you’ll be told the topic before reading. For the other, only afterwards. Then write down what you remember from each.</p>
    </div>
    <div class="wide">
      <div class="lbox" id="pBox">
        <p class="small" id="pStep" aria-live="polite">Press Start when you have about three minutes.</p>
        <p class="ptopic" id="pTopic" aria-live="polite"></p>
        <p class="pass" id="pText" hidden></p>
        <div class="rec" id="pRec" hidden><label for="pIn">Write down everything you remember from the passage, in your own words.</label><textarea id="pIn"></textarea></div>
        <div class="qrow"><button class="pbtn" id="pGo">Start</button><button class="pbtn" id="pDone" hidden>I’ve read it</button><button class="pbtn" id="pSub" hidden>Done</button></div>
        <div id="pRes" aria-live="polite"></div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Some caution</span>What priming can’t do</h2>
    <p>Some of the most famous priming claims have not held up. In 1996, John Bargh and colleagues reported that students who unscrambled sentences containing words about old age walked more slowly as they left the lab. In 2012, Stéphane Doyen and colleagues repeated the study with twice as many people and infrared timing, and found no effect, except when the experimenters timing the walk had been led to expect slower walking. The effects that hold up are smaller and more specific, like the head start for related words.</p>
    <h2 class="sec"><span class="n">Questions first</span>Even a wrong guess helps</h2>
    <p>Priming a topic can be as simple as asking questions about it first. In 2009, Nate Kornell, Matthew Hays and Robert Bjork had people try to guess an answer for 8 seconds before studying it for 5. They remembered more than people who simply studied the same material for all 13 seconds, even though their guesses were almost always wrong.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Warm the network first</h3>
      <p>Before teaching something new, show where the session is headed, ask learners what they already know about it, or pose a question they can’t answer yet. Priming won’t do the learning for you, but the new idea lands on a network that’s already warm.</p>
    </aside>
  </div>
''',
tips_h='New ideas need something to attach to',
tips='''      <li><b>Show where it’s headed</b><span>Give the topic, an overview or a picture before the details.</span></li>
      <li><b>Activate what’s there</b><span>Ask learners to recall what they already know about the topic.</span></li>
      <li><b>Ask before you tell</b><span>Pose questions they can’t answer yet. Even wrong guesses help.</span></li>''',
sources='''        <li><a href="https://www.taylorfrancis.com/books/9780203338001/chapters/10.4324/9780203338001-7">Taylor &amp; Francis: on Meyer, D. E., &amp; Schvaneveldt, R. W. (1971). Facilitation in recognizing pairs of words. <i>Journal of Experimental Psychology</i>.</a></li>
        <li><a href="https://www.hedtags.org/hed-task/tasks/hedtsk_semantic_priming.html">HED task description: semantic priming and spreading activation.</a></li>
        <li><a href="https://psychologicalresources.blogspot.com/2011/01/effects-of-previous-knowledge.html">On Bransford, J. D., &amp; Johnson, M. K. (1972). Contextual prerequisites for understanding. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://doaj.org/article/70047cdc408c4ad690d1aaec0578c9f0">Doyen, S., Klein, O., Pichon, C.-L., &amp; Cleeremans, A. (2012). Behavioral priming: it’s all in the mind, but whose mind? <i>PLOS ONE</i>.</a></li>
        <li><a href="https://www.nationalgeographic.com/science/article/primed-by-expectations-why-a-classic-psychology-experiment-isnt-what-it-seemed">Ed Yong (2012). Primed by expectations: why a classic psychology experiment isn’t what it seemed.</a></li>
        <li><a href="https://www.scientificamerican.com/article/the-pluses-of-getting-it-wrong/">Scientific American: the pluses of getting it wrong, on Kornell, Hays &amp; Bjork (2009).</a></li>''',
quiz='''[
 {q:'In the 1971 doctor–nurse experiment, how much faster were related word pairs judged?',o:['About 85 milliseconds','About 2 seconds','No faster'],a:0,f:'A small but reliable head start: related ideas are already partly active.'},
 {q:'When did being told the topic of the vague passage help people remember it?',o:['Only when told before hearing it','Only when told afterwards','Both, equally'],a:0,f:'The topic has to be active when the information arrives.'},
 {q:'Which kind of priming effect has held up best?',o:['Small, specific effects like faster word recognition','Stray words changing how fast people walk','Both equally'],a:0,f:'The dramatic behaviour-priming claims have not replicated well.'}]''',
js=r'''
/* ---------- word or not? (lexical decision with primes) ----------
   24 related pairs, split at random: 12 shown with their own prime (related), 12 with another pair's prime (unrelated).
   Plus 8 rounds with a nonword target. 32 rounds, shuffled. Fixation 400 ms, prime 250 ms, blank 100 ms, target until answer (max 3 s).
   Result = median time on correct related vs correct unrelated word rounds. */
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const sw=ms=>new Promise(r=>setTimeout(r,ms));
const med=a=>{if(!a.length)return null;const s=[...a].sort((x,y)=>x-y),m=s.length>>1;return s.length%2?s[m]:(s[m-1]+s[m])/2};
const PAIRS=[['bread','butter'],['doctor','nurse'],['salt','pepper'],['king','queen'],['cat','dog'],['table','chair'],['night','day'],['hot','cold'],['boy','girl'],['black','white'],['knife','fork'],['shoe','sock'],['bee','honey'],['lock','key'],['rain','umbrella'],['cup','saucer'],['lion','tiger'],['bride','groom'],['needle','thread'],['pen','ink'],['moon','star'],['nut','bolt'],['soap','water'],['bat','ball']];
const NONW=[['river','BLINT'],['clock','FRANE'],['green','TROSH'],['horse','PLOME'],['paper','NURP'],['smile','GLAVE'],['garden','SPORL'],['apple','DRIN']];
let lr=null;
async function lTrial(){if(lr.i>=lr.trials.length)return lEnd();const tr=lr.trials[lr.i],me=lr.i;$('lKeys').hidden=true;$('lP').textContent='+';$('lW').textContent='';$('lProg').textContent=`Round ${lr.i+1} of ${lr.trials.length}`;
 await sw(400);if(!lr||lr.i!==me)return;$('lP').textContent=tr.prime;await sw(250);if(!lr||lr.i!==me)return;$('lP').textContent='';await sw(100);if(!lr||lr.i!==me)return;
 $('lW').textContent=tr.target;lr.t0=performance.now();lr.live=true;$('lKeys').hidden=false;await sw(3000);if(lr&&lr.live&&lr.i===me)lAns(null)}
function lAns(word){if(!lr||!lr.live)return;lr.live=false;const tr=lr.trials[lr.i];tr.rt=performance.now()-lr.t0;tr.ok=word===(tr.kind!=='non');tr.timeout=word===null;
 $('lW').textContent='';$('lKeys').hidden=true;$('lProg').textContent=tr.timeout?'Too slow.':tr.ok?'Right.':'Wrong.';lr.i++;setTimeout(()=>{if(lr)lTrial()},tr.ok?300:800)}
function lEnd(){const T=lr.trials;const acc=T.filter(t=>t.ok).length/T.length;const r=med(T.filter(t=>t.kind==='rel'&&t.ok).map(t=>t.rt)),u=med(T.filter(t=>t.kind==='unrel'&&t.ok).map(t=>t.rt));
 $('lP').textContent='';$('lW').textContent='';$('lProg').textContent='Done.';$('lPhase').textContent='Your results';const mx=Math.max(r||0,u||0,1);
 const row=(l,v,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${v?v/mx*100:0}%;background:${c}"></i></div><b>${v?Math.round(v)+' ms':'—'}</b></div>`;
 $('lRes').innerHTML=`<div class="res">${row('Related',r,'#5FD3A8')}${row('Unrelated',u,'#FCB316')}</div>`;let title,text;
 if(acc<0.75||r==null||u==null){title='Not enough clean rounds';text=`You answered ${Math.round(acc*100)}% of rounds correctly, which isn’t enough to compare. Try again, aiming to be accurate first and fast second.`}
 else{const d=u-r;if(d>=20){title='Related words got a head start';text=`You recognised words ${Math.round(d)} ms faster when the small word before was related, even though you were told to ignore it. In the 1971 study the head start was about 85 ms.`}
  else if(d>-20){title='Little difference this time';text=`Related and unrelated words differed by only ${Math.abs(Math.round(d))} ms. With 12 of each, timing is noisy, and priming effects are small. In larger studies, related words are reliably faster.`}
  else{title='Unrelated words were faster this time';text=`You were ${Math.round(-d)} ms faster after unrelated words, the opposite of the usual result. With only 12 of each, chance plays a big part. Try again.`}}
 $('lTitle').textContent=title;$('lText').textContent=text;$('lGo').textContent='Try again';$('lGo').disabled=false;$('lGo').focus();lr=null}
$('lGo').addEventListener('click',()=>{const P=shuf(PAIRS.map(p=>[...p]));const rel=P.slice(0,12),un=P.slice(12);const trials=[];
 rel.forEach(([a,b])=>trials.push({prime:a,target:b.toUpperCase(),kind:'rel'}));
 un.forEach(([a,b],i)=>trials.push({prime:un[(i+1)%12][0],target:b.toUpperCase(),kind:'unrel'}));
 NONW.forEach(([a,b])=>trials.push({prime:a,target:b,kind:'non'}));
 lr={trials:shuf(trials),i:0,live:false};$('lRes').innerHTML='';$('lGo').disabled=true;$('lPhase').textContent='Running';$('lTitle').textContent='Real word?';$('lText').textContent='J (or the right button) for a real word, F for not a word.';$('lScreen').focus();lTrial()});
$('lYes').addEventListener('click',()=>lAns(true));$('lNo').addEventListener('click',()=>lAns(false));
$('lScreen').addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(k==='j'){e.preventDefault();lAns(true)}else if(k==='f'){e.preventDefault();lAns(false)}});

/* ---------- topic first, or topic after? ----------
   Two original vague passages, each with 9 idea units. One passage (chosen at random) gets its topic before reading,
   the other only after reading. Passage order is also random. Reading: until "I've read it", or 75 s.
   Recall is scored roughly by keywords: an idea unit counts if any of its keywords appears in what was written. */
const PS=[{topic:'assembling flat-pack furniture',text:'First, lay everything out and check that nothing is missing. It helps to sort the small pieces into groups by size. The thin sheet of paper is more useful than it looks, even though it has hardly any words on it. Start with the largest part lying flat, and attach the sides before anything else. Don’t tighten anything fully until the end, or the last piece may not fit. The odd little tool that came with it will do, but a better one saves time. If something seems to be left over at the end, it is worth going back a few steps. When it is finished, the box makes a good home for whatever comes next.',
 ideas:[['Lay everything out and check nothing is missing',['missing','check','lay']],['Sort the small pieces by size',['sort','small','size','group','screw']],['Use the sheet with pictures (the instructions)',['paper','sheet','instruction','picture','diagram','manual']],['Start with the largest part lying flat',['largest','biggest','flat','base','bottom']],['Attach the sides first',['side']],['Don’t tighten fully until the end',['tight','loose']],['The little tool works, a better one is faster',['tool','allen','hex','screwdriver','key','drill']],['Pieces left over: go back a few steps',['left over','leftover','extra','go back','back a few','spare']],['Reuse the box',['box','recycl','cardboard']]]},
 {topic:'planting a vegetable garden',text:'Choose a spot that gets plenty of the main ingredient for most of the day. Before anything goes in, turn everything over and break up the large lumps. Some people add what is left over from the kitchen, and it does help. Follow the numbers on the small packets for depth and spacing, even though it is tempting to crowd them together. Afterwards, a gentle shower is better than a flood. For the first few weeks, check every day, and remove anything that arrives uninvited. Some visitors are welcome, but others will need a barrier. Patience matters: the reward comes weeks later, not tomorrow.',
 ideas:[['A spot with plenty of sun most of the day',['sun','light','spot','shade']],['Dig over the ground and break up lumps',['turn','dig','lump','soil','ground','earth']],['Add kitchen scraps (compost)',['kitchen','compost','scrap','left over','leftover','food']],['Follow the packet for depth and spacing',['packet','depth','deep','spacing','space','apart','number','seed']],['Don’t crowd them together',['crowd','close','too many']],['Water gently, don’t flood',['water','shower','flood','gentle','hose']],['Check daily and pull out weeds',['weed','uninvited','remove','pull','check','daily','every day']],['Some visitors need a barrier (pests)',['visitor','pest','barrier','fence','net','slug','snail','rabbit','bird','insect','bug']],['Be patient: it takes weeks',['patien','week','wait','later','grow','harvest']]]}];
let pa=null;
function pShowPassage(){const k=pa.order[pa.step],P=PS[k],before=pa.before===k;
 $('pStep').textContent=`Passage ${pa.step+1} of 2: read it once, carefully.`;$('pTopic').textContent=before?`This passage is about ${P.topic}.`:'The topic will be revealed after you read it.';
 $('pText').textContent=P.text;$('pText').hidden=false;$('pRec').hidden=true;$('pDone').hidden=false;$('pSub').hidden=true;$('pDone').focus();
 const me=pa.step;clearTimeout(pa.tm);pa.tm=setTimeout(()=>{if(pa&&pa.step===me&&!$('pDone').hidden)pRead()},75000)}
function pRead(){clearTimeout(pa.tm);const k=pa.order[pa.step],P=PS[k],before=pa.before===k;$('pText').hidden=true;$('pDone').hidden=true;
 $('pTopic').textContent=before?`This passage was about ${P.topic}.`:`The passage was about ${P.topic}.`;$('pStep').textContent=`Passage ${pa.step+1} of 2: what do you remember?`;
 $('pIn').value='';$('pRec').hidden=false;$('pSub').hidden=false;$('pIn').focus()}
const pnorm=s=>' '+s.toLowerCase().replace(/[^a-z ]/g,' ').replace(/\s+/g,' ')+' ';
function pScore(k,txt){const t=pnorm(txt);return PS[k].ideas.map(([d,kw])=>kw.some(w=>t.includes(w)))}
function pSubmit(){const k=pa.order[pa.step];pa.res[k]=pScore(k,$('pIn').value);pa.step++;if(pa.step<2){pShowPassage();return}pEnd()}
function pEnd(){$('pRec').hidden=true;$('pSub').hidden=true;$('pTopic').textContent='';$('pStep').textContent='Done.';
 const b=pa.before,a=1-b;const nb=pa.res[b].filter(Boolean).length,na=pa.res[a].filter(Boolean).length;
 const row=(l,v,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${v/9*100}%;background:${c}"></i></div><b>${v} of 9</b></div>`;
 const list=k=>`<ul class="ideas">${PS[k].ideas.map(([d],i)=>`<li class="${pa.res[k][i]?'y':'n'}">${pa.res[k][i]?'✓':'·'} ${d}</li>`).join('')}</ul>`;
 let head,body;const d=nb-na;
 if(nb+na===0){head='Nothing recalled';body='No ideas were picked up from what you wrote. Try again, and write down whatever you can remember, however vague.'}
 else if(d>=2){head='Knowing the topic first helped';body=`You recalled ${nb} ideas from the passage you were told about first, and ${na} from the one explained afterwards. The topic gave each sentence something to attach to as you read it.`}
 else if(d>=-1){head='About the same this time';body=`You recalled ${nb} ideas with the topic first and ${na} with it after. The two passages differ in difficulty, and the scoring is rough, so small differences mean little. In the original study, the topic-first group recalled about twice as much.`}
 else{head='The other way round this time';body=`You recalled ${na} ideas with the topic told afterwards and ${nb} with it first. The passages differ in difficulty and the scoring is rough. Try again: you’ll get the other passage with its topic first.`}
 $('pRes').innerHTML=`<div class="lres">${row('Topic told first',nb,'#13294B')}${row('Topic told after',na,'#B84300')}</div><p class="pmsg"><b class="h">${head}</b>${body}</p><p class="small" style="margin-top:14px"><b>Topic first: ${PS[b].topic}</b></p>${list(b)}<p class="small"><b>Topic after: ${PS[a].topic}</b></p>${list(a)}<p class="small">Scoring is automatic and rough: it looks for key words from each idea.</p>`;
 $('pGo').hidden=false;$('pGo').textContent='Try again';$('pGo').focus();pa.prev=b;pa=Object.assign({},{prevB:b,done:true})}
let lastB=null;
$('pGo').addEventListener('click',()=>{const before=lastB===null?(Math.random()<0.5?0:1):1-lastB;lastB=before;pa={before,order:shuf([0,1]),step:0,res:{}};$('pRes').innerHTML='';$('pGo').hidden=true;pShowPassage()});
$('pDone').addEventListener('click',()=>{if(pa&&pa.order)pRead()});$('pSub').addEventListener('click',()=>{if(pa&&pa.order)pSubmit()});
''')
open('lb03/template.html','w').write(page(o))
