import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m05',n='5',label='The Learning Brain · Memory · Topic 5',epi='The Learning Brain, Memory, episode 5',
title='Building on What’s There: Prior Knowledge and Memory',h1='Building on what’s there',em='Build the frame first',read='8',mins='2½ minutes',vtitle='Building on what’s there',
dek='What you already know decides what new learning can hold on to. Knowledge helps only if it is active while you learn, and only if it is accurate.',
jumps='<span><a href="#fT">Frame first or frame after</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled. In rats, a well-learned schema let new memories stop depending on the hippocampus within two days.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.ptext{font:500 clamp(17px,2.1vw,19px)/1.55 var(--body);color:#fff;max-width:46ch;margin:0}
.ptopic{font:700 26px/1.3 var(--body);color:#FCB316;text-align:center;margin:0}
.ptopic small{display:block;font:800 14px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-bottom:6px}
.bopts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;width:100%;max-width:520px}
@media (max-width:520px){.bopts{grid-template-columns:1fr}}
.bopts[hidden]{display:none}
.bopts button{min-height:52px;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;font:700 17px/1.25 var(--body);cursor:pointer;padding:6px 10px}
.bopts button small{display:block;font-size:13px;color:#C9D3E3;font-weight:600}
.bopts button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.bopts.r5{grid-template-columns:repeat(5,minmax(0,1fr));max-width:460px}
@media (max-width:520px){.bopts.r5{grid-template-columns:repeat(5,minmax(0,1fr))}}''',
body='''  <div class="col lede">
    <p>In a classic 1972 study by John Bransford and Marcia Johnson, people heard a passage written in deliberately vague terms: sort the items into groups; one pile may be enough; mistakes can be costly. Most found it hard to follow, and harder to remember.</p>
    <p>Then some were told the topic: washing clothes. People told before the passage understood it and remembered far more. People told afterwards did no better than people never told.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>8.0 vs 3.6</strong><span>ideas recalled, out of 14, with a picture shown before vs after a passage</span></div>
      <div role="listitem"><strong>5 seconds</strong><span>was enough for chess masters to rebuild a real game position almost perfectly</span></div>
      <div role="listitem"><strong>1 trial</strong><span>for rats with a well-learned map to learn a new flavour’s place</span></div>
      <div role="listitem"><strong>2 days</strong><span>until that new memory no longer needed the hippocampus</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Timing</span>Knowledge helps only while you learn</h2>
    <p>In a version of the study with a picture, people who saw it before hearing the passage recalled about 8 of its 14 ideas. People who saw it afterwards recalled under 4, the same as people who never saw it. Knowledge helps only if it is active while you learn. An organized body of knowledge like this is called a schema.</p>
  </div>

  <section class="night" aria-labelledby="fT">
    <div class="col">
      <h2 class="sec" id="fT"><span class="n">Try it</span>Frame first or frame after</h2>
      <p>Read two short, vague passages. For one, you’ll be told the topic before you read; for the other, after. Rate how well you understood each, then answer five questions on each. About 3 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="fScreen">
          <p class="ptopic" id="fTop" hidden></p>
          <p class="ptext" id="fP" aria-live="polite"></p>
          <div class="bopts" id="fOpts" hidden role="group" aria-label="Choose an answer"></div>
          <p class="prog" id="fProg" aria-live="polite">Press Start.</p>
        </div>
        <div>
          <p class="phase" id="fPhase">Ready</p>
          <p class="mtitle" id="fTitle">Does the frame have to come first?</p>
          <p class="mtext" id="fText" aria-live="polite">Read at your own pace; press “Done reading” when you’ve finished. Which passage gets the topic first is chosen at random.</p>
          <div id="fRes"></div>
          <div class="mrow"><button class="nbtn" id="fGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Experts</span>Patterns, not better memories</h2>
    <p>Chess masters shown a board from a real game for five seconds could rebuild it almost perfectly; weaker players placed only a few pieces. But when the same pieces were scattered at random, the masters’ advantage nearly vanished, as William Chase and Herbert Simon reported in 1973. Their memory wasn’t better in general. It was built on patterns they already knew.</p>
    <h2 class="sec"><span class="n">In the brain</span>A schema speeds up consolidation</h2>
    <p>In 2007, Dorothy Tse, Richard Morris and colleagues spent many sessions teaching rats where six flavours were hidden in an arena. Once that map was in place, the rats learned a new flavour’s location in a single trial, and within two days the memory no longer needed the <a href="@@LB:hippocampus@@">hippocampus</a>. Rats trained in an arena where the layout kept changing couldn’t do this. Later work from the same lab pointed to regions of the cortex, including the front of the brain, as where the new information was being added.</p>
    <h2 class="sec"><span class="n">A caution</span>When the frame is wrong</h2>
    <p>Prior knowledge helps when it is accurate. When it is wrong, new material gets bent to fit the old schema, and misconceptions can survive instruction.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">New learning needs something to hold on to</h3>
      <p>Before new material, bring to mind what students already know: a question, a familiar example, the big picture first. Give the topic and structure before the details, not after. Check prior knowledge for errors, not just gaps. And build courses so early ideas become the frame for later ones.</p>
    </aside>
  </div>
''',
tips_h='Build the frame first',
tips='''      <li><b>Topic and structure first</b><span>Then the details.</span></li>
      <li><b>Bring prior knowledge to mind</b><span>A question or a familiar example.</span></li>
      <li><b>Check it for errors</b><span>Not just gaps.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/S0022-5371(72)80006-9">Bransford, J. D., &amp; Johnson, M. K. (1972). Contextual prerequisites for understanding: Some investigations of comprehension and recall. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://doi.org/10.1016/0010-0285(73)90004-2">Chase, W. G., &amp; Simon, H. A. (1973). Perception in chess. <i>Cognitive Psychology</i>.</a></li>
        <li><a href="https://pubmed.ncbi.nlm.nih.gov/17412951/">Tse, D., Langston, R. F., Kakeyama, M., et al. (2007). Schemas and memory consolidation. <i>Science</i>.</a></li>''',
quiz='''[
 {q:'People were told a vague passage was about washing clothes. When did it help?',o:['Only when told before the passage','Only when told after','Either way'],a:0,f:'Told afterwards did no better than never told.'},
 {q:'Chess masters recalled real positions almost perfectly. What about random positions?',o:['Their advantage nearly vanished','They were still far better','They did worse than novices'],a:0,f:'Their memory was built on familiar patterns.'},
 {q:'When can prior knowledge hurt?',o:['When it is wrong','When it is detailed','When it is recent'],a:0,f:'New material gets bent to fit a wrong schema.'}]''',
js=BASE+r'''
/* ---------- frame first or frame after ----------
   Two vague passages (written for this page). One gets its topic before reading, the other after (random).
   Self-paced reading; understanding rating 1-5; then 5 multiple-choice questions per passage. */
const PS=[
 {t:'Putting up a tent',p:'First, find a spot that is flat and free of anything sharp. Lay the large piece out with the smooth side down. The long thin pieces fit together into longer ones; slide them through the sleeves so that they cross in the middle. Bend them until the ends sit in the corners, and the whole thing will rise. Then push the short pointed pieces through the loops at an angle, leaning away from the centre. If it looks like rain, the extra layer goes over the top. Done badly, you will find out in the middle of the night.',
  q:[['What should the spot be free of?',['Anything sharp','Water','Shade','Noise']],['Which side of the large piece goes down?',['The smooth side','The rough side','The coloured side','The short side']],['Where do the long pieces cross?',['In the middle','At the corners','At one end','Underneath']],['How do the short pointed pieces go in?',['At an angle, leaning away from the centre','Straight down','At an angle, leaning toward the centre','Flat on the ground']],['When does the extra layer go on?',['If it looks like rain','At night','Before anything else','Only when it is windy']]]},
 {t:'Painting a room',p:'Begin by moving everything away from the edges, and cover whatever you cannot move. The thin sticky strip goes wherever you do not want the colour to reach. Stir well, because what has settled at the bottom matters. Start at the top and work down, and do the edges with the small one before you use the big one. Two thin layers are better than one thick one, so wait for the first to dry. Keep the window open. Cleaning up is much easier while everything is still wet.',
  q:[['Where does the sticky strip go?',['Wherever the colour shouldn’t reach','Along the floor only','On the window','On the handle']],['Why stir well?',['What has settled at the bottom matters','To warm it up','To remove bubbles','To thin it with water']],['Where do you start?',['At the top','At the bottom','Near the window','In the middle']],['Which is better?',['Two thin layers','One thick layer','Three thick layers','It makes no difference']],['When is cleaning up easiest?',['While everything is still wet','After it has dried','The next day','Before you start']]]}];
let fr=null;
function choose(opts,cls){return new Promise(res=>{fr.res=res;const o=$('fOpts');o.className='bopts'+(cls?' '+cls:'');o.innerHTML=opts.map(([l,v])=>`<button type="button" data-v="${v}">${l}</button>`).join('');o.hidden=false;o.querySelector('button').focus()})}
$('fOpts').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!fr||!fr.res)return;const r=fr.res;fr.res=null;$('fOpts').hidden=true;r(b.dataset.v)});
async function showTopic(t,when){$('fP').textContent='';$('fTop').innerHTML=`<small>${when}</small>This passage is about: ${t}`;$('fTop').hidden=false;$('fProg').textContent='';
 await choose([['Got it',1]]);$('fTop').hidden=true}
$('fGo').addEventListener('click',async()=>{if(fr)return;fr={};const g=$('fGo');g.disabled=true;g.textContent='In progress';$('fRes').innerHTML='';
 const order=shuf([0,1]);const beforeIdx=Math.random()<0.5?0:1;const res=PS.map(()=>({rate:0,right:0,ms:0}));
 for(let k=0;k<2;k++){const i=order[k],P=PS[i],before=i===beforeIdx;
  $('fPhase').textContent=`Passage ${k+1} of 2`;$('fTitle').textContent=before?'Topic first':'Topic after';$('fText').textContent=before?'You’ll see the topic, then the passage.':'Read the passage; you’ll see the topic afterwards.';
  if(before){await showTopic(P.t,'Before you read');if(!fr)return}
  $('fP').textContent=P.p;$('fProg').textContent='Read it once, at your own pace.';const t0=performance.now();await choose([['Done reading',1]]);if(!fr)return;res[i].ms=performance.now()-t0;$('fP').textContent='';
  if(!before){await showTopic(P.t,'Now that you’ve read it');if(!fr)return}
  $('fP').textContent='How well did you understand the passage while reading it?';$('fProg').textContent='1 = not at all, 5 = completely';
  res[i].rate=+await choose([1,2,3,4,5].map(n=>[n,n]),'r5');if(!fr)return}
 $('fPhase').textContent='Questions';$('fTitle').textContent='What do you remember?';$('fText').textContent='Five questions on each passage. Choose the best answer.';
 let n=0;for(const i of order){for(const [q,opts] of PS[i].q){n++;$('fP').textContent=`${PS[i].t}: ${q}`;$('fProg').textContent=`Question ${n} of 10`;
  const v=+await choose(shuf(opts.map((o,j)=>[o,j])));if(!fr)return;if(v===0)res[i].right++}}
 $('fP').textContent='Done.';$('fProg').textContent='';$('fPhase').textContent='Your results';
 const B=res[beforeIdx],A=res[1-beforeIdx],d=B.right-A.right,dr=B.rate-A.rate;
 $('fRes').innerHTML=`<div class="res wl2"><p class="gh">Understanding, 1 to 5</p>${barRow('Topic first',B.rate,5,B.rate+' of 5','#FCB316')}${barRow('Topic after',A.rate,5,A.rate+' of 5','#C9D3E3')}<p class="gh">Questions right, out of 5</p>${barRow('Topic first',B.right,5,B.right+' of 5','#FCB316')}${barRow('Topic after',A.right,5,A.right+' of 5','#C9D3E3')}</div>`;
 const pb=PS[beforeIdx].t.toLowerCase(),pa=PS[1-beforeIdx].t.toLowerCase();
 const felt=dr>=1?` You also rated the topic-first passage easier to understand (${B.rate} against ${A.rate}).`:dr<=-1?` Oddly, you rated the topic-after passage as easier to understand (${A.rate} against ${B.rate}); perhaps you guessed its topic early.`:'';
 let title,text;
 if(d>=2){title='The frame helped most when it came first';text=`With the topic first (${pb}), you got ${B.right} of 5 right; with the topic after (${pa}), ${A.right} of 5.`+felt+' Being told afterwards came too late: the passage was already stored as a jumble.'}
 else if(d<=-2){title='The topic-after passage did better';text=`You got ${A.right} of 5 right on the passage whose topic came after (${pa}), and ${B.right} of 5 with the topic first (${pb}), the reverse of the usual result.`+(dr<=-1?felt:felt+' Perhaps you guessed that topic as you read, which gives you the frame anyway.')+' With 5 questions each, chance plays a part. Try again: the order changes at random.'}
 else{title=dr>=1?'It felt clearer, but scores were close':'No clear difference this time';text=`You got ${B.right} of 5 with the topic first (${pb}) and ${A.right} of 5 with the topic after (${pa}).`+felt+' Choosing from options is easier than writing down every idea you remember, which is what the original study asked for. And many readers guess these topics part-way through, which gives them the frame anyway.'}
 $('fTitle').textContent=title;$('fText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();fr=null});
'''+grid('''[
 ['A vague passage about washing clothes: people told the topic before hearing it',['Understood and remembered far more','No difference','Remembered less'],0,'The frame let them make sense of each sentence.'],
 ['People told the topic only after hearing the passage',['Did no better than people never told','Did as well as those told first','Did best of all'],0,'Knowledge has to be active while you learn.'],
 ['Chess masters, after 5 seconds looking at a board from a real game',['Rebuilt it almost perfectly','Placed about half the pieces','Did no better than novices'],0,'They saw familiar patterns, not separate pieces.'],
 ['The same pieces scattered at random',['The masters’ advantage nearly vanished','Masters still far ahead','Novices did better'],0,'Their memory wasn’t better in general.'],
 ['Rats that had learned a map of six flavour locations, given a new one',['Learned it in a single trial','Needed many sessions again','Couldn’t learn it'],0,'The schema gave the new memory a place to go.'],
 ['Rats trained where the layout kept changing',['Couldn’t learn new locations in one trial','Learned even faster','Did the same'],0,'No stable schema, no rapid learning.']]''','The pattern: new learning sticks when it has a frame to hold on to, given in time and accurate.'))
open('m05/template.html','w').write(page(o))
