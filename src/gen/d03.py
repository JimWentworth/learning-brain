import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(3,'Don’t Read Your Slides: Redundancy and Modality','Don’t read your slides','The slide supports the speaker. It shouldn’t be the script.','Don’t read your slides',
'A slide full of text, and an instructor reading it aloud, word for word. Students hear it and read it at the same time. Twice the input. Twice the learning?',
'<span><a href="#sT">Make over a slide</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','tem'],{'occ':([900,-60],'right'),'tem':([600,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision starts, and the temporal lobe, at the side, where speech is processed, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.sform{display:grid;gap:10px;width:100%;max-width:560px}
.sform fieldset{border:1px solid #3A4E72;border-radius:10px;padding:8px 12px 10px;margin:0}
.sform legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.sform label{display:flex;gap:10px;align-items:flex-start;padding:4px 0;color:#E9EEF6;font-size:16px;line-height:1.35;cursor:pointer}
.sform input{margin-top:3px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.slide{background:#fff;color:#13294B;border-radius:8px;padding:12px 14px;width:100%;max-width:560px;box-sizing:border-box;min-height:200px;display:grid;grid-template-rows:auto 1fr auto;gap:6px}
.slide .stitle{font:800 18px var(--display);margin:0;color:#13294B}
.slide .bd{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;min-height:0}
.slide .tx{font-size:13px;line-height:1.35;margin:0;color:#13294B}
.slide .tx.big{font:700 17px/1.45 var(--body);color:#13294B}
.slide svg{width:130px;height:auto}
@media (max-width:480px){.slide .bd{grid-template-columns:1fr}.slide svg{justify-self:center}}
.slide .cap{background:#13294B;color:#fff;font-size:12px;padding:3px 8px;border-radius:4px;justify-self:center}
.slide .cap[hidden]{display:none}
.say{color:#C9D3E3;font-size:15px;margin:6px 0 0;max-width:560px}''',
body='''  <div class="col lede">
    <p>In Richard Mayer’s research, adding on-screen text that repeats the narration word for word to an animation tended to hurt learning on transfer tests. He calls this the redundancy principle.</p>
    <p>A related finding is the modality principle. Students learned better from graphics with spoken words than from graphics with printed words. In Mayer’s summary, the median effect was 1.0, positive in 18 of 19 tests.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Redundancy</strong><span>narration plus the same words on screen tended to hurt</span></div>
      <div role="listitem"><strong>1.0</strong><span>median effect size for spoken over printed words with graphics</span></div>
      <div role="listitem"><strong>18 of 19</strong><span>tests favoured spoken words</span></div>
      <div role="listitem"><strong>Captions</strong><span>are different: optional, and needed by many students</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why</span>Reading and listening compete</h2>
    <p>Reading and listening to the same words compete for attention. And when the eyes are busy reading, they are not looking at the graphic that the words describe.</p>
    <h2 class="sec"><span class="n">An important caveat</span>Keep captions available</h2>
    <p>These studies tested verbatim text on screen for everyone. Optional captions are different. They support students who are deaf or hard of hearing, and others who need them, and some research suggests they can help non-native speakers. Keep captions available.</p>
  </div>

  <section class="night" aria-labelledby="sT">
    <div class="col">
      <h2 class="sec" id="sT"><span class="n">Try it</span>Make over a slide</h2>
      <p>Here is a slide on how vaccines work. Change how it is built and delivered, and see what the research suggests about each choice.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="sScreen">
          <div class="slide" id="sSlide" aria-live="polite">
            <p class="stitle">How a vaccine trains the immune system</p>
            <div class="bd"><p class="tx" id="sTx"></p><svg id="sPic" viewBox="0 0 130 90" role="img" aria-label="Diagram: a vaccine shows the immune system a harmless piece of a virus; antibodies form and later lock onto the real virus."><circle cx="30" cy="45" r="16" fill="none" stroke="#13294B" stroke-width="3"/><path d="M14 45h-6M46 45h6M30 29v-6M30 61v6" stroke="#13294B" stroke-width="3"/><path d="M58 45h22" stroke="#C84A00" stroke-width="3"/><path d="M76 39l8 6-8 6" fill="#C84A00"/><path d="M96 30v14M96 44l-8 10M96 44l8 10" stroke="#FF5F05" stroke-width="4" fill="none"/><text x="4" y="86" font-size="11" fill="#13294B">virus piece</text><text x="82" y="86" font-size="11" fill="#13294B">antibody</text></svg></div>
            <p class="cap" id="sCap">[captions] The vaccine shows your immune system a harmless piece…</p>
          </div>
          <form class="sform" id="sF">
            <fieldset><legend>Slide text</legend>
              <label><input type="radio" name="st" value="full" checked>A full paragraph</label>
              <label><input type="radio" name="st" value="key">A few key words</label></fieldset>
            <fieldset><legend>Picture</legend>
              <label><input type="radio" name="sp" value="none" checked>No picture</label>
              <label><input type="radio" name="sp" value="dia">A labelled diagram</label></fieldset>
            <fieldset><legend>You say</legend>
              <label><input type="radio" name="sy" value="read" checked>The slide text, word for word</label>
              <label><input type="radio" name="sy" value="own">The explanation in your own words</label></fieldset>
            <fieldset><legend>Captions on the recording</legend>
              <label><input type="radio" name="sc" value="on" checked>Available</label>
              <label><input type="radio" name="sc" value="off">Off</label></fieldset>
          </form>
        </div>
        <div>
          <p class="phase">Your slide</p>
          <p class="mtitle" id="sTitle"></p>
          <div class="mtext" id="sText" aria-live="polite"></div>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Short animations, not live lectures</h2>
    <p>Most of this research used short narrated animations, not live lectures. Applying it to a live class is a reasonable extension, but an extension.</p>
  </div>

'''+GRID_HTML+box('Put a few key words and a strong visual on each slide, and say the rest. Don’t read your slides aloud. Move detailed text into a handout or notes. And keep captions on for recorded video. Share this tip with students: turn dense slides into your own words.'),
tips_h='The slide supports the speaker. It shouldn’t be the script.',
tips='''      <li><b>Key words and a strong visual</b><span>Say the rest.</span></li>
      <li><b>Detail in a handout</b><span>Not on the slide.</span></li>
      <li><b>Keep captions available</b><span>They are not the same as redundant text.</span></li>''',
sources='''        <li>Mayer, R. E. (2021). <i>Multimedia learning</i> (3rd ed.). Cambridge University Press.</li>
        <li>Mayer, R. E. (2023). Research-based principles for designing multimedia instruction. In C. E. Overson, C. M. Hakala, L. L. Kordonowy, &amp; V. A. Benassi (Eds.), <i>In their own words</i> (pp. 143–157). Society for the Teaching of Psychology.</li>''',
quiz='''[
 {q:'Narration plus the same words on screen tended to…',o:['Hurt learning on transfer tests','Double learning','Make no difference'],a:0,f:'The redundancy principle.'},
 {q:'With a graphic, students learned better from words that were…',o:['Spoken','Printed','Both, word for word'],a:0,f:'The modality principle: 18 of 19 tests.'},
 {q:'Optional captions…',o:['Should stay available','Should be switched off','Are the same as reading the slide aloud'],a:0,f:'Many students need them.'}]''',
js=BASE+r'''
/* ---------- make over a slide ---------- */
const FULL='A vaccine contains a harmless piece of a virus, or instructions to make one. The immune system responds by making antibodies and memory cells. If the real virus arrives later, the memory cells recognize it and the body responds faster and more strongly.';
const KEY='Harmless piece → antibodies → faster response later';
function sUpd(){const v=n=>document.querySelector(`input[name="${n}"]:checked`).value;const st=v('st'),sp=v('sp'),sy=v('sy'),sc=v('sc');
 const tx=$('sTx');tx.textContent=st==='full'?FULL:KEY;tx.className='tx'+(st==='key'?' big':'');$('sPic').style.display=sp==='dia'?'':'none';$('sCap').hidden=sc!=='on';
 const pts=[];let good=0;
 if(st==='full'&&sy==='read')pts.push('<b>Full text, read aloud word for word:</b> this is the redundancy the studies tested. Students read and listen to the same words at once, and the two compete.');
 else if(st==='full')pts.push('<b>Full text on the slide:</b> even if you explain in your own words, students may read instead of listening. Move the detail to a handout.');
 else{good++;pts.push('<b>A few key words:</b> they signal the structure without competing with what you say.')}
 if(sp==='dia'){good++;pts.push('<b>A labelled diagram:</b> words and a picture that explains help most (topic 1). With spoken words, eyes are free to look at it.')}
 else pts.push('<b>No picture:</b> a simple diagram of how the parts connect would help, especially for beginners.');
 if(sy==='own'){good++;pts.push('<b>Your own words:</b> spoken explanation with a graphic is the modality principle at work.')}
 else if(st==='key')pts.push('<b>Reading the key words aloud:</b> that’s too little to explain. Say the explanation in full, in your own words.');
 if(sc==='on'){good++;pts.push('<b>Captions available:</b> good. Optional captions are not the redundancy the studies tested, and many students need them.')}
 else pts.push('<b>Captions off:</b> keep them available for recorded video. Students who are deaf or hard of hearing, and many others, rely on them.');
 $('sTitle').textContent=good===4?'A slide that supports the speaker':good>=2?'Getting there':'The slide is the script';
 $('sText').innerHTML='<ul class="slist">'+pts.map(p=>`<li>${p}</li>`).join('')+'</ul>'}
$('sF').addEventListener('change',sUpd);sUpd();
'''+grid('''[
 ['Adding on-screen text that repeats the narration tended to…',['Hurt learning','Help learning','Make no difference'],0,'Mayer’s redundancy principle.'],
 ['With a graphic, which worked better?',['Spoken words','Printed words','No words'],0,'The modality principle.'],
 ['In how many of 19 tests did spoken words win?',['18','10','3'],0,'Median effect size 1.0.'],
 ['Why does reading and hearing the same words hurt?',['They compete for attention','It is too slow','Students fall asleep'],0,'And the eyes leave the graphic.'],
 ['Do these findings mean captions should be turned off?',['No: optional captions are different','Yes, always','Only for lectures'],0,'Many students need them.'],
 ['Most of this research used…',['Short narrated animations','Full-semester live lectures','Textbooks only'],0,'Applying it to live classes is an extension.']]''','The pattern: say the words, show the picture, keep the slide lean, and keep captions available.'))
o['css']+='''
.slist{margin:0;padding-left:20px}.slist li{margin:0 0 8px}'''
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['d03']
open('d03/template.html','w').write(page(o))
