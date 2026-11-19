import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='m10',n='10',label='The Learning Brain · Memory · Topic 10',epi='The Learning Brain, Memory, episode 10',
title='Cues and Context: How Memories Come Back',h1='Cues and context',em='A memory comes back through its cues',read='7',mins='2 minutes',vtitle='Cues and context',
dek='A cue helps only if it was part of what got stored. Place matters a little; the cues inside the material matter more.',
jumps='<span><a href="#kT">The right cue</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the hippocampus, deep inside, and the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';BR.R.hip.lab=[640,770];BR.R.hip.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['hip','pfc'],labels:['hip','pfc'],labelT:{hip:0.8,pfc:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+'''
.sent{font:600 clamp(20px,2.6vw,26px)/1.4 var(--body);color:#fff;text-align:center;max-width:26ch;margin:0}
.cue{font:700 24px/1.3 var(--body);color:#FCB316;text-align:center;margin:0}
.cue small{display:block;font:800 14px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#C9D3E3;margin-bottom:6px}
.kin{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.kin[hidden]{display:none}
.kin input{width:200px;min-height:50px;font:700 22px var(--body);text-align:center;border-radius:10px;border:2px solid #8FA3C2;background:#0F2240;color:#fff}
.kin input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}''',
body='''  <div class="col lede">
    <p>Divers learned lists of words either on a beach or under water, then recalled them in the same place or the other. In Duncan Godden and Alan Baddeley’s 1975 study, recall was best when the two settings matched: words learned under water came back better under water.</p>
    <p>The principle is called encoding specificity. A cue helps only if it was part of what got stored.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>93</strong><span>effects in a 2001 review of how much place matters</span></div>
      <div role="listitem"><strong>0.28</strong><span>of a standard deviation: small but reliable</span></div>
      <div role="listitem"><strong>No effect</strong><span>of setting when the divers recognized words instead of recalling them</span></div>
      <div role="listitem"><strong>Two rooms</strong><span>of study beat one, when tested in a new room</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Encoding specificity</span>The cue that was stored with it</h2>
    <p>When people learned a word alongside one cue, that cue brought it back better than another word that seemed more obviously related, as Endel Tulving and Donald Thomson showed in 1973. Meaning works the same way: read “The man lifted the piano” and <i>something heavy</i> is a good cue for <i>piano</i>; read “The man tuned the piano” and it isn’t. John Barclay and colleagues showed this in 1974.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>The right cue</h2>
      <p>Read 12 short sentences. After a 30-second break, you’ll get a hint for each one, like “something heavy”, and type the object it describes. Some hints match the sentence you read; some don’t. About 2½ minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <p class="sent" id="kS" aria-live="polite"></p>
          <p class="cue" id="kC" aria-live="polite"></p>
          <form class="kin" id="kGen" hidden><label class="sr-only" for="kGi">The object</label><input id="kGi" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="nbtn" type="submit">OK</button></form>
'''+recall_screen('k')+'''
'''+tail('k')+'''
        </div>
        <div>
          <p class="phase" id="kPhase">Ready</p>
          <p class="mtitle" id="kTitle">Does the hint have to match?</p>
          <p class="mtext" id="kText" aria-live="polite">Each sentence stays up for 4 seconds. Read it and picture it.</p>
          <div id="kRes"></div>
          <div class="mrow"><button class="nbtn" id="kGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">Place</span>Small but reliable</h2>
    <p>How big is the effect of place? Steven Smith and Edward Vela’s 2001 review of 93 effects found it small but reliable, about 0.28 of a standard deviation. It shrinks when other good cues are present, and when people picture the original setting before recalling.</p>
    <p>Context matters most for recall. When Godden and Baddeley had divers recognize the words instead, in 1980, the setting made no difference. And varying the setting can help: in 1978, Smith, Arthur Glenberg and Robert Bjork found that people who studied a list in two different rooms recalled more in a new room than people who studied twice in the same room.</p>
    <h2 class="sec"><span class="n">A caution</span>A weak lever</h2>
    <p>Changing the room is a weak lever, and some studies find no effect at all. What matters more is whether the right cues are present at test, inside the material itself.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Build cues that travel</h3>
      <p>Practise retrieval in more than one setting and format, so knowledge doesn’t depend on one room or one slide. When students are stuck, have them picture where they learned it. And build meaningful cues into the material, like questions and categories, that will still be there at the exam.</p>
    </aside>
  </div>
''',
tips_h='Memory comes back through the cues it was stored with',
tips='''      <li><b>Vary setting and format</b><span>So knowledge doesn’t depend on one room or one slide.</span></li>
      <li><b>Picture where you learned it</b><span>When stuck.</span></li>
      <li><b>Build cues into the material</b><span>Questions and categories that will be there at the exam.</span></li>''',
sources='''        <li><a href="https://scispace.com/pdf/context-dependent-memory-in-two-natural-environments-on-land-16ihazeqen.pdf">Godden, D. R., &amp; Baddeley, A. D. (1975). Context-dependent memory in two natural environments: On land and underwater. <i>British Journal of Psychology</i>.</a></li>
        <li><a href="https://doi.org/10.1037/h0020071">Tulving, E., &amp; Thomson, D. M. (1973). Encoding specificity and retrieval processes in episodic memory. <i>Psychological Review</i>.</a></li>
        <li><a href="https://doi.org/10.1016/s0022-5371(74)80024-1">Barclay, J. R., Bransford, J. D., Franks, J. J., McCarrell, N. S., &amp; Nitsch, K. (1974). Comprehension and semantic flexibility. <i>Journal of Verbal Learning and Verbal Behavior</i>.</a></li>
        <li><a href="https://doi.org/10.3758/bf03196157">Smith, S. M., &amp; Vela, E. (2001). Environmental context-dependent memory: A review and meta-analysis. <i>Psychonomic Bulletin &amp; Review</i>.</a></li>
        <li><a href="https://link.springer.com/content/pdf/10.3758/bf03197465.pdf">Smith, S. M., Glenberg, A., &amp; Bjork, R. A. (1978). Environmental context and human memory. <i>Memory &amp; Cognition</i>.</a></li>''',
quiz='''[
 {q:'Divers learned words on land or under water. When was recall best?',o:['When learning and recall happened in the same place','Always on land','Always under water'],a:0,f:'Encoding specificity: the setting was part of what got stored.'},
 {q:'How big is the effect of place, across 93 effects?',o:['Small but reliable','Large','None'],a:0,f:'About 0.28 of a standard deviation.'},
 {q:'What usually matters more than the room?',o:['Whether the right cues are in the material at test','The time of day','The colour of the walls'],a:0,f:'Build meaningful cues into the material.'}]''',
js=BASE+recall_kit('k','kr')+r'''
/* ---------- the right cue ----------
   12 objects, each with two sentences that highlight different properties, and a hint for each property.
   Study one sentence per object (random), 4 s each. 30 s break. Cued recall: 6 hints match the sentence read, 6 don't. */
const OB=[['piano','The man lifted the piano.','something heavy','The man tuned the piano.','something that makes music'],
 ['egg','She dropped the egg on the kitchen floor.','something that breaks easily','She boiled an egg for breakfast.','something you can eat'],
 ['rope','The climber’s life depended on the rope.','something strong','The children skipped with a rope in the playground.','something to play with'],
 ['knife','He sliced the bread with the knife.','something sharp','He polished the silver knife until it gleamed.','something shiny'],
 ['newspaper','She swatted the fly with a rolled-up newspaper.','something you can hit with','She read the newspaper on the train.','something you read'],
 ['ice','He slipped on the ice outside the door.','something slippery','He cooled his drink with ice.','something cold'],
 ['balloon','The balloon floated up over the trees.','something that rises','The balloon burst with a bang.','something that pops'],
 ['candle','The candle lit up the dark room.','something that gives light','The candle filled the room with the smell of vanilla.','something with a scent'],
 ['brick','The builder laid one brick on top of another.','a building material','The thief threw a brick through the window.','something you can throw'],
 ['coat','She wrapped herself in her coat against the wind.','something that keeps you warm','She paid a fortune for the designer coat.','something expensive'],
 ['tomato','The ripe tomato was bright red.','something red','She sliced a tomato into the salad.','something that goes in a salad'],
 ['drum','The drum boomed across the field.','something loud','The drum was round, with a flat top.','something round']];
let kr=null;
function kAsk(){return new Promise(res=>{kr.gres=res;$('kGen').hidden=false;$('kGi').value='';$('kGi').focus()})}
$('kGen').addEventListener('submit',e=>{e.preventDefault();if(!kr||!kr.gres)return;const r=kr.gres;kr.gres=null;$('kGen').hidden=true;r($('kGi').value.trim().toLowerCase())});
$('kGo').addEventListener('click',async()=>{if(kr)return;kr={};const g=$('kGo');g.disabled=true;g.textContent='In progress';$('kRes').innerHTML='';
 const m=shuf([...Array(6).fill(1),...Array(6).fill(0)]);const items=shuf(OB.map((o,i)=>{const v=Math.random()<0.5?0:1;return{w:o[0],sent:o[1+v*2],cue:m[i]?o[2+v*2]:o[4-v*2],match:!!m[i],got:false}}));
 $('kPhase').textContent='Step 1 of 3 · Read';$('kTitle').textContent='Read and picture it';
 for(let i=0;i<items.length;i++){$('kS').textContent=items[i].sent;$('kProg').textContent=`Sentence ${i+1} of 12`;if(!await kHold(4))return}
 $('kS').textContent='';$('kPhase').textContent='Step 2 of 3 · Break';$('kTitle').textContent='Step away';$('kText').textContent='An easy, 30-second task.';await kBreak();if(!kr)return;
 $('kPhase').textContent='Step 3 of 3 · Recall';$('kTitle').textContent='Which object?';$('kText').textContent='Each hint describes one object from the sentences. Type it, or leave it blank.';
 const test=shuf([...items]);
 for(let i=0;i<test.length;i++){const it=test[i];$('kProg').textContent=`Hint ${i+1} of 12`;$('kC').innerHTML=`<small>A hint</small>${it.cue}`;const v=await kAsk();if(!kr)return;it.got=!!v&&match(v,it.w)}
 $('kC').textContent='';$('kW').textContent='Done';$('kProg').textContent='';$('kPhase').textContent='Your results';
 const M=items.filter(x=>x.match&&x.got).length,X=items.filter(x=>!x.match&&x.got).length,tot=M+X,d=M-X;
 $('kRes').innerHTML=`<div class="res wl2"><p class="gh">Objects recalled, out of 6</p>${barRow('Hint matched',M,6,M+' of 6','#FCB316')}${barRow('Hint didn’t',X,6,X+' of 6','#C9D3E3')}</div>`;
 let title,text;
 if(tot<3){title='Too few to compare';text=`You recalled ${tot} of 12, too few to compare the hints. Try again, and picture each sentence as you read it.`}
 else if(d>=2){title='The matching hint worked better';text=`With a hint that matched the sentence, you recalled ${M} of 6; with one that didn’t, ${X} of 6. The same object, stored through a different property, needed a different way back in.`}
 else if(d>=-1){title=tot>=11?'Every hint worked':'About the same this time';text=tot>=11?`You recalled ${M} with matching hints and ${X} with mismatched ones. With only 12 everyday objects, you may have remembered the whole list, so any hint was enough; in the original study, the mismatch cost was clear.`:`You recalled ${M} with matching hints and ${X} with mismatched ones. With 6 of each, chance plays a big part, and some hints fit more than one object. In the original study, matching hints worked clearly better.`}
 else{title='The mismatched hints did better';text=`You recalled ${X} with mismatched hints and ${M} with matching ones, the reverse of the usual result. With 6 of each, chance plays a big part, and you may have pictured more than the sentence said. Try again; the sentences change.`}
 $('kTitle').textContent=title;$('kText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();kr=null});
'''+grid('''[
 ['Divers who learned words under water, recalling them under water rather than on land',['Recalled more','Recalled less','Recalled the same'],0,'Godden and Baddeley, 1975.'],
 ['The same divers recognizing words instead of recalling them',['The setting made no difference','The setting mattered even more','They recognized nothing'],0,'Context matters most for recall.'],
 ['Across 93 effects, how much does the place of learning matter?',['A small but reliable amount','A large amount','Not at all'],0,'About 0.28 of a standard deviation.'],
 ['Picturing the original setting before recalling',['Shrinks the effect of changing rooms','Makes it bigger','Has no effect'],0,'Mental reinstatement brings the cues back.'],
 ['Studying a list in two different rooms, tested in a new room, compared with studying twice in one room',['Recalled more','Recalled less','Recalled the same'],0,'Varied settings meant more cues.'],
 ['After reading “The man lifted the piano,” which hint works better for piano?',['Something heavy','Something that makes music','Both equally'],0,'The cue that was stored with it.']]''','The pattern: a memory comes back through the cues it was stored with, so build cues that will be there when it’s needed.'))
open('m10/template.html','w').write(page(o))
