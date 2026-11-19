import sys;sys.path.insert(0,'gen')
from common import page
o=dict(id='lb02',n='2',title='Attention: A Competition in the Brain',h1='Attention',em='A competition in the brain',read='8',mins='2.5 minutes',vtitle='Attention',
dek='Your eyes take in far more than your brain can fully process. Objects compete for the brain’s limited processing, and attention is a bias on that competition. Some things win because they stand out; others win because you chose them.',
jumps='<span><a href="#srchT">Find the target</a></span><span><a href="#cueT">Where to look</a></span>',
hero_aria='Drawing of the brain with three areas glowing orange and labelled: the visual cortex at the back, where objects compete, and the frontal lobe and intraparietal sulcus, which send signals back to bias the competition.',
hero_js="BR.R.v1.lab=[860,650];BR.R.v1.al='right';BR.R.ips.lab=[500,-70];BR.R.ips.al='left';BR.R.fro.lab=[200,-70];BR.R.fro.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.5,s:fitS(W,H,1.32),t,active:['v1','ips','fro'],labels:['v1','ips','fro'],labelT:{v1:0.8,ips:1.0,fro:1.2},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css='''#sC{width:100%;max-width:560px;height:auto;aspect-ratio:600/420;display:block;border-radius:6px}
.pz{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;align-items:center;justify-items:center;padding:30px 10px;border-radius:10px;background:#F3F6FA;min-height:200px}
.pz:focus-visible{outline:3px solid #13294B;outline-offset:3px}
.pz .bx{width:min(120px,24vw);aspect-ratio:1;border:4px solid #13294B;border-radius:10px;display:flex;align-items:center;justify-content:center;background:#fff}
.pz .bx i{width:44%;aspect-ratio:1;border-radius:50%;background:#B84300;display:none}
.pz .bx.on i{display:block}
.pz .cue{font:800 clamp(34px,6vw,52px)/1 var(--body);color:#13294B;min-width:1.2em;text-align:center}
.cmsg{text-align:center;font-size:17px;margin:12px 0 0;min-height:1.5em}''',
body='''  <div class="col lede">
    <p>Imagine a desk with four objects on it. Light from all four reaches your eyes at the same moment, but your brain can’t fully process all of them at once. Something has to decide which gets through.</p>
    <p>In 1995, Robert Desimone and John Duncan proposed an answer called biased competition. Objects in view compete for processing in the visual cortex. Attention doesn’t work like a spotlight that switches things on. It tips the balance of a competition that is already happening.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>&lt;2° vs 4–6°</strong><span>estimated field each cell covers in V1 and V4 of the human visual cortex</span></div>
      <div role="listitem"><strong>4</strong><span>images shown one at a time or all together in the classic brain-scan test</span></div>
      <div role="listitem"><strong>30–40%</strong><span>more firing in monkey visual cells where attention was directed, with nothing yet on screen</span></div>
      <div role="listitem"><strong>80%</strong><span>of cues pointed the right way in Posner’s classic “where to look” task</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The competition</span>Bigger windows, more crowding</h2>
    <p>Each cell in the visual cortex responds to one patch of the scene, its receptive field. In the first visual area, V1, those patches are tiny. Further along, they grow: in people, they have been estimated at under 2 degrees across in V1 and 4 to 6 degrees in V4, at a point a little way out from the centre of gaze. A bigger patch can hold several objects at once, and when it does, their signals don’t add up. They suppress each other.</p>
    <p>In 1998, Sabine Kastner, Peter De Weerd, Robert Desimone and Leslie Ungerleider measured this in people with brain scans. They showed four colourful images either one after another or all at once. In V4 and beyond, the response to all four together was smaller than to the same images shown in turn. In V1, where each cell’s patch was too small to hold more than one image, there was little difference.</p>
    <h2 class="sec"><span class="n">Bottom-up</span>Some things win on their own</h2>
    <p>One way to win the competition is to stand out. Something brighter than its surroundings, or different from everything around it, captures attention automatically. Anne Treisman and Garry Gelade showed in 1980 that a target differing by one simple feature, such as colour, seems to pop out: it is found just as fast however many other items there are. A target defined by a combination of features takes longer with every item added.</p>
  </div>

  <section class="night" aria-labelledby="srchT">
    <div class="col">
      <h2 class="sec" id="srchT"><span class="n">Try it</span>Find the target</h2>
      <p>Is there an orange upright bar? Answer as fast as you can. In one block it is the only orange item. In the other, there are also orange bars lying flat. 36 rounds.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen" tabindex="0" role="group" aria-label="Search display. Press J if an orange upright bar is there, F if not, or tap the buttons." aria-describedby="sProg">
          <canvas id="sC" width="600" height="420" aria-hidden="true"></canvas>
          <div class="keys" id="sKeys" hidden><button id="sNo">Not there<small>F</small></button><button id="sYes">It’s there<small>J</small></button></div>
          <p class="prog" id="sProg" aria-live="polite">Press Start. Keep your fingers on F and J.</p>
        </div>
        <div>
          <p class="phase" id="sPhase">Ready</p>
          <p class="mtitle" id="sTitle">Does the number of items matter?</p>
          <p class="mtext" id="sText" aria-live="polite">Each display has 4, 12 or 24 items. You’ll see how your speed changes with the number of items in each block.</p>
          <div id="sRes"></div>
          <div class="mrow"><button class="nbtn" id="sGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <p>If you are using a screen reader, this activity is not meaningful, because it depends on seeing the display. The text around it describes the result.</p>
    <h2 class="sec"><span class="n">Top-down</span>Choosing the winner</h2>
    <p>The other way to win is to be chosen. Areas in the frontal and parietal lobes send signals back to the visual cortex, toward the cells covering the place or feature you are looking for. In Kastner’s experiment, when people attended to the location of the images, the response there grew, and much of the suppression between the images was cancelled out.</p>
    <p>The bias can be set up before anything appears. In 1997, Steven Luck, Leonardo Chelazzi, Steven Hillyard and Robert Desimone recorded from monkeys waiting for a stimulus. When attention was directed to a cell’s patch, its spontaneous firing in areas V2 and V4 was 30 to 40% higher, even though the screen there was still blank.</p>
  </div>

  <section aria-labelledby="cueT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="cueT"><span class="n">Try it</span>Where to look</h2>
      <p>Keep your eyes on the centre. An arrow points left or right, and then a dot appears in one of the boxes. Press the space bar, or tap the area, as soon as you see the dot, wherever it is. The arrow is usually right, but not always. 40 rounds.</p>
    </div>
    <div class="wide">
      <div class="lbox">
        <div class="pz" id="cBox" tabindex="0" role="group" aria-label="Cue task. Press space or tap as soon as a dot appears." aria-describedby="cMsg"><div class="bx" id="cL"><i></i></div><div class="cue" id="cCue" aria-hidden="true">+</div><div class="bx" id="cR"><i></i></div></div>
        <p class="cmsg" id="cMsg" aria-live="polite">Press Start.</p>
        <div class="qrow" style="justify-content:center"><button class="pbtn" id="cGo">Start</button></div>
        <div id="cRes" aria-live="polite"></div>
      </div>
    </div>
  </section>

  <div class="col">
    <p>This is Michael Posner’s cueing task from 1980. The arrow sets up a bias before the dot appears, and responses are faster at the expected place and slower at the other one, even though your eyes never move. It is the behavioural version of the bias Luck and colleagues saw in monkey cells.</p>
    <h2 class="sec"><span class="n">Some caution</span>From the lab to the lecture</h2>
    <p>Most of this evidence comes from simple displays, brain scans and recordings in monkeys. How cleanly it carries over to a crowded lecture slide is an open question. Still, the logic is consistent: attention is a bias on a competition, and whatever wins is what gets passed on to memory and action.</p>
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Set the bias before the slide</h3>
      <p>Tell students what to look for before a slide or demonstration appears, so the bias is in place early. And cut what competes with the one thing that matters: decoration, extra text and animations all join the competition.</p>
    </aside>
  </div>
''',
tips_h='Attention is a bias, not a switch',
tips='''      <li><b>Say where to look, first</b><span>Point to what matters before it appears, so attention is already biased toward it.</span></li>
      <li><b>Cut the competition</b><span>Remove decoration and extra text that compete with the key point.</span></li>
      <li><b>Make the key thing stand out</b><span>A single feature that differs, such as colour, pops out without effort.</span></li>''',
sources='''        <li><a href="https://collaborate.princeton.edu/en/publications/mechanisms-of-directed-attention-in-the-human-extrastriate-cortex/">Kastner, S., De Weerd, P., Desimone, R., &amp; Ungerleider, L. G. (1998). Mechanisms of directed attention in the human extrastriate cortex as revealed by functional MRI. <i>Science</i>.</a></li>
        <li><a href="https://www.sciencedaily.com/releases/1998/10/981005073941.htm">ScienceDaily (1998). Focusing attention cancels brain-dampening effects of visual clutter.</a></li>
        <li><a href="https://napl.scholar.princeton.edu/bibcite/export/bibtex/bibcite_reference/67771">Kastner, S., et al. (2001). Modulation of sensory suppression: implications for receptive field sizes in the human visual cortex. <i>Journal of Neurophysiology</i>.</a></li>
        <li><a href="https://data.zhenzhi.com/details/1/869127426/1/5">Luck, S. J., Chelazzi, L., Hillyard, S. A., &amp; Desimone, R. (1997). Neural mechanisms of spatial selective attention in areas V1, V2, and V4 of macaque visual cortex. <i>Journal of Neurophysiology</i>.</a></li>
        <li><a href="https://www.jneurosci.org/content/jneuro/31/2/587.full.pdf">McMains, S., &amp; Kastner, S. (2011). Interactions of top-down and bottom-up mechanisms in human visual cortex. <i>Journal of Neuroscience</i> (on Desimone &amp; Duncan, 1995).</a></li>
        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8965574">Wolfe, J. M. (2021). Guided Search 6.0, reviewing Treisman &amp; Gelade (1980). <i>Psychonomic Bulletin &amp; Review</i>.</a></li>
        <li><a href="https://en.wikipedia.org/wiki/Posner_cueing_task">Posner cueing task (Posner, 1980).</a></li>''',
quiz='''[
 {q:'Why do objects compete in later visual areas like V4?',o:['Each cell’s patch is big enough to hold several objects, and their signals suppress each other','The cells there are tired','Those areas only see colour'],a:0,f:'In V1 the patches are too small to hold more than one object, so there is little competition there.'},
 {q:'What does top-down attention do to the competition?',o:['Boosts the chosen object and cancels much of the suppression','Makes the object brighter on the screen','Switches off all other objects completely'],a:0,f:'It biases the competition toward what you chose.'},
 {q:'In monkeys, what happened in cells covering a location that attention was directed to, before anything appeared?',o:['Their firing went up by 30 to 40%','They stopped firing','Nothing until the stimulus appeared'],a:0,f:'The bias is in place early, which is why saying where to look first helps.'}]''',
js=r'''
/* ---------- find the target (visual search) ----------
   Two blocks, in random order: pop-out (target = orange upright bar among blue upright bars) and conjunction
   (among blue upright and orange flat bars). Each block: 18 rounds = 3 set sizes (4, 12, 24) x 6 (3 target present, 3 absent), shuffled.
   Display stays up to 5 s. Speed = median time on correct target-present rounds for each set size.
   Slope = (time at 24 - time at 4) / 20, in ms per item. */
const SC=$('sC'),SX=SC.getContext('2d');const OR='#FF8A3D',BL='#7DB8FF';let sr=null;
const sw=ms=>new Promise(r=>setTimeout(r,ms));
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
function sClear(){SX.fillStyle='#0F2240';SX.fillRect(0,0,600,420)}
function sCross(){sClear();SX.strokeStyle='#C9D3E3';SX.lineWidth=4;SX.beginPath();SX.moveTo(285,210);SX.lineTo(315,210);SX.moveTo(300,195);SX.lineTo(300,225);SX.stroke()}
function bar(x,y,col,up){SX.fillStyle=col;if(up)SX.fillRect(x-5,y-19,10,38);else SX.fillRect(x-19,y-5,38,10)}
function sShow(tr){sClear();const cells=shuf([...Array(24).keys()]).slice(0,tr.n);const items=[];
 cells.forEach((c,i)=>{const gx=c%6,gy=Math.floor(c/6);const x=60+gx*96+(Math.random()-0.5)*36,y=58+gy*100+(Math.random()-0.5)*30;items.push([x,y])});
 items.forEach(([x,y],i)=>{if(i===0&&tr.present){bar(x,y,OR,true);return}
  if(tr.cond==='pop')bar(x,y,BL,true);else{(i%2)?bar(x,y,OR,false):bar(x,y,BL,true)}})}
async function sTrial(){if(sr.i>=sr.trials.length)return sEnd();const tr=sr.trials[sr.i];
 if(sr.i===0||sr.trials[sr.i-1].cond!==tr.cond){$('sKeys').hidden=true;sClear();$('sProg').textContent=tr.cond==='pop'?'Next block: the target is the only orange item.':'Next block: some orange bars lie flat. Only an upright orange bar counts.';await sw(2200);if(!sr)return}
 $('sKeys').hidden=true;sCross();$('sProg').textContent=`Round ${sr.i+1} of ${sr.trials.length}`;await sw(500);if(!sr)return;
 sShow(tr);sr.t0=performance.now();sr.live=true;$('sKeys').hidden=false;const me=sr.i;
 await sw(5000);if(sr&&sr.live&&sr.i===me)sAns(null)}
function sAns(yes){if(!sr||!sr.live)return;sr.live=false;const tr=sr.trials[sr.i];tr.rt=performance.now()-sr.t0;tr.ok=yes===tr.present;tr.timeout=yes===null;
 sClear();$('sKeys').hidden=true;$('sProg').textContent=tr.timeout?'Too slow.':tr.ok?'Right.':'Wrong.';sr.i++;setTimeout(()=>{if(sr)sTrial()},tr.ok?300:800)}
const med=a=>{if(!a.length)return null;const s=[...a].sort((x,y)=>x-y),m=s.length>>1;return s.length%2?s[m]:(s[m-1]+s[m])/2};
function sEnd(){const T=sr.trials;const acc=T.filter(t=>t.ok).length/T.length;const R={};
 ['pop','conj'].forEach(c=>{R[c]={};[4,12,24].forEach(n=>R[c][n]=med(T.filter(t=>t.cond===c&&t.n===n&&t.present&&t.ok).map(t=>t.rt)))});
 const slope=c=>(R[c][24]!=null&&R[c][4]!=null)?(R[c][24]-R[c][4])/20:null;const sp=slope('pop'),sc=slope('conj');
 sClear();$('sProg').textContent='Done.';$('sPhase').textContent='Your results';
 const mx=Math.max(1,...['pop','conj'].flatMap(c=>[4,12,24].map(n=>R[c][n]||0)));
 const row=(c,n)=>{const v=R[c][n];return `<div class="row"><span>${n} items</span><div class="bar"><i style="width:${v?v/mx*100:0}%;background:${c==='pop'?'#7DB8FF':'#FCB316'}"></i></div><b>${v?Math.round(v)+' ms':'—'}</b></div>`};
 $('sRes').innerHTML=`<div class="res"><div class="grp">Only orange item (pop-out)</div>${[4,12,24].map(n=>row('pop',n)).join('')}<div class="grp">Among flat orange bars</div>${[4,12,24].map(n=>row('conj',n)).join('')}</div>`;
 let title,text;
 if(acc<0.7||sp===null||sc===null){title='Not enough clean rounds';text=`You answered ${Math.round(acc*100)}% of rounds correctly, which isn’t enough to compare the blocks. Try again, aiming to be accurate first and fast second.`}
 else if(sc-sp>=8){title='Pop-out was flat; the mixed search was not';text=`When the target was the only orange item, each extra item added about ${Math.max(0,Math.round(sp))} ms. Among flat orange bars, each extra item added about ${Math.round(sc)} ms. A single different feature wins the competition automatically. A combination of features has to be checked item by item.`}
 else{title='No clear difference this time';text=`Extra items added about ${Math.round(sp)} ms each in the pop-out block and ${Math.round(sc)} ms in the mixed block. With only 3 rounds per size, timing is noisy. In larger experiments, the mixed search slows down much more as items are added.`}
 if(acc>=0.7&&acc<0.9)text+=` You got ${Math.round(acc*100)}% of rounds right.`;
 $('sTitle').textContent=title;$('sText').textContent=text;$('sGo').textContent='Try again';$('sGo').disabled=false;$('sGo').focus();sr=null}
$('sGo').addEventListener('click',()=>{const blocks=shuf(['pop','conj']);const trials=[];blocks.forEach(c=>{const b=[];[4,12,24].forEach(n=>{for(let k=0;k<6;k++)b.push({cond:c,n,present:k<3})});trials.push(...shuf(b))});
 sr={trials,i:0,live:false};$('sRes').innerHTML='';$('sGo').disabled=true;$('sPhase').textContent='Running';$('sTitle').textContent='Is it there?';$('sText').textContent='J (or the right button) if there is an orange upright bar, F if not.';$('sScreen').focus();sTrial()});
$('sYes').addEventListener('click',()=>sAns(true));$('sNo').addEventListener('click',()=>sAns(false));
$('sScreen').addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(k==='j'){e.preventDefault();sAns(true)}else if(k==='f'){e.preventDefault();sAns(false)}});
sClear();

/* ---------- where to look (Posner cueing) ----------
   40 rounds: 32 valid (dot appears where the arrow points), 8 invalid, shuffled. Fixation 600-1000 ms, arrow, dot 500 ms later.
   Pressing before the dot = "too early" and the round is repeated later. No press within 1.5 s = missed.
   Result = median valid vs median invalid response time. */
let cr=null;
function cSet(cue,side){$('cCue').textContent=cue;$('cL').classList.toggle('on',side==='L');$('cR').classList.toggle('on',side==='R')}
async function cTrial(){if(cr.i>=cr.trials.length)return cEnd();const tr=cr.trials[cr.i],me=cr.i;cr.phase='wait';
 cSet('+',null);$('cMsg').textContent=`Round ${cr.i+1} of ${cr.trials.length}`;await sw(600+Math.random()*400);if(!cr||cr.i!==me)return;
 cSet(tr.arrow==='L'?'←':'→',null);await sw(500);if(!cr||cr.i!==me||cr.phase!=='wait')return;
 cSet(tr.arrow==='L'?'←':'→',tr.side);cr.t0=performance.now();cr.phase='live';await sw(1500);if(cr&&cr.i===me&&cr.phase==='live'){tr.miss=true;cNext('Missed.')}}
function cPress(){if(!cr)return;if(cr.phase==='wait'){const tr=cr.trials[cr.i];cr.trials.push({...tr});cr.phase='done';cNext('Too early: wait for the dot.');return}
 if(cr.phase!=='live')return;const tr=cr.trials[cr.i];tr.rt=performance.now()-cr.t0;cNext(`${Math.round(tr.rt)} ms`)}
function cNext(msg){cr.phase='done';cSet('+',null);$('cMsg').textContent=msg;cr.i++;setTimeout(()=>{if(cr)cTrial()},700)}
function cEnd(){const T=cr.trials.filter(t=>t.rt!=null&&!t.miss);const v=med(T.filter(t=>t.valid).map(t=>t.rt)),iv=med(T.filter(t=>!t.valid).map(t=>t.rt));
 cSet('+',null);$('cMsg').textContent='Done.';const mx=Math.max(v||0,iv||0,1);
 const row=(l,x,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${x?x/mx*100:0}%;background:${c}"></i></div><b>${x?Math.round(x)+' ms':'—'}</b></div>`;
 let head,body;if(v==null||iv==null){head='Not enough rounds';body='Too many rounds were missed or too early to compare. Try again, keeping your eyes on the centre.'}
 else{const d=iv-v;if(d>=15){head='The arrow moved your attention';body=`You were ${Math.round(d)} ms slower when the dot appeared on the side the arrow didn’t point to. Your eyes stayed still, but your attention had already gone to the expected side, and had to move back.`}
  else if(d>-15){head='Little difference this time';body=`Your times differed by only ${Math.abs(Math.round(d))} ms. With only 8 rounds where the arrow was wrong, small effects are hard to see. In larger studies, responses on the unexpected side are reliably slower.`}
  else{head='Faster on the unexpected side';body=`You were ${Math.round(-d)} ms faster when the arrow was wrong, the opposite of the usual result. With only 8 such rounds, chance plays a big part. Try again, keeping your eyes on the centre.`}}
 $('cRes').innerHTML=`<div class="lres">${row('Arrow was right',v,'#13294B')}${row('Arrow was wrong',iv,'#B84300')}</div><p class="pmsg"><b class="h">${head}</b>${body}</p>`;$('cGo').hidden=false;$('cGo').textContent='Try again';$('cGo').focus();cr=null}
$('cGo').addEventListener('click',()=>{const t=[];for(let k=0;k<40;k++){const arrow=Math.random()<0.5?'L':'R',valid=k<32;t.push({arrow,valid,side:valid?arrow:(arrow==='L'?'R':'L')})}
 cr={trials:shuf(t),i:0,phase:'done'};$('cRes').innerHTML='';$('cGo').hidden=true;$('cBox').focus();cTrial()});
$('cBox').addEventListener('keydown',e=>{if(e.key===' '||e.code==='Space'){e.preventDefault();cPress()}});
$('cBox').addEventListener('pointerdown',e=>{if(cr){e.preventDefault();cPress()}});
''')
open('lb02/template.html','w').write(page(o))
