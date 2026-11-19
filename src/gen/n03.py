import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',3,'The 10% Myth: You Use Your Whole Brain','The 10% myth','You already use your whole brain. The question is what you give it to work on.','The 10% myth',
'We only use 10% of our brains. It appears in films, ads and classroom posters. Imagine what we could do with the other 90.',
'<span><a href="#dT">Where is the spare 90%?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['par','tem'],{'par':([560,-70],'left'),'tem':([600,770],'left')},'Drawing of the side of the brain with the parietal lobe, at the top, and the temporal lobe, at the side, glowing orange and labelled, as examples of areas that are all in use.')
o.update(css=RECALL_CSS+'''
.dg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;width:100%;max-width:520px}
.dg button[aria-pressed="true"]{background:#FCB316;color:#13294B;border-color:#FCB316}
.dcount{color:#C9D3E3;font-size:15px;margin:10px 0 0;text-align:center}''',
body='''  <div class="col lede">
    <p>The idea seems to come from a stretch. The psychologist William James wrote that people use only a small part of their mental resources. In 1936, a foreword to a bestselling book turned that into a falsely precise ten percent, credited to James.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Imaging</strong><span>shows activity across the whole brain over a day, even in sleep</span></div>
      <div role="listitem"><strong>Injury</strong><span>almost anywhere causes some loss of ability</span></div>
      <div role="listitem"><strong>Energy</strong><span>the brain uses a large share of the body’s energy</span></div>
      <div role="listitem"><strong>No reserve</strong><span>no silent 90% waiting to be switched on</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Three lines of evidence</span>Imaging, injury, energy</h2>
    <p>Brain imaging tells a different story. Over the course of a day, activity shows up across the whole brain, even during sleep. There is no silent 90% waiting to be switched on.</p>
    <p>Brain injury tells the same story. There is almost no area that can be damaged without some loss of ability. If 90% were spare, most injuries would do nothing.</p>
    <p>And the brain is expensive to run. It uses a large share of the body’s energy. Evolution would not keep paying for tissue that sits idle.</p>
  </div>

  <section class="night" aria-labelledby="dT">
    <div class="col">
      <h2 class="sec" id="dT"><span class="n">Try it</span>Where is the spare 90%?</h2>
      <p>If 90% of the brain were spare, damage to most areas would change nothing. Pick areas one at a time, and see what injury there typically affects. Try to find one that does nothing.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="dScreen">
          <div class="dg" role="group" aria-label="Brain areas" id="dG"></div>
          <p class="dcount" id="dCount" aria-live="polite"></p>
        </div>
        <div>
          <p class="phase">If this area were damaged</p>
          <p class="mtitle" id="dTitle">Pick an area</p>
          <p class="mtext" id="dText" aria-live="polite">Each button is a major brain area.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">The grain of truth</span>Efficiency, not waste</h2>
    <p>Not every neuron fires at once. At any moment, only some areas are working hard. That is efficiency, not waste.</p>
    <h2 class="sec"><span class="n">Why it matters</span>No trick to unlock</h2>
    <p>The myth suggests a hidden reserve, unlocked by a trick. Real gains come from something slower: knowledge and skill built through practice.</p>
  </div>

'''+GRID_HTML+box('Replace the promise of hidden potential with a plan for practice. Show students how much they have already built. And be wary of products that promise to unlock the brain. Share this tip with students: there is no hidden 90%; practice is how ability grows.'),
tips_h='You already use your whole brain. The question is what you give it to work on.',
tips='''      <li><b>A plan for practice</b><span>Not hidden potential.</span></li>
      <li><b>Show what’s been built</b><span>Progress students can see.</span></li>
      <li><b>Wary of “unlock” products</b><span>There’s nothing locked.</span></li>''',
sources='''        <li>Beyerstein, B. L. (1999). Whence cometh the myth that we only use 10% of our brains? In S. Della Sala (Ed.), <i>Mind myths: Exploring popular assumptions about the mind and brain</i> Wiley.</li>''',
quiz='''[
 {q:'Over a day, brain imaging shows activity…',o:['Across the whole brain','In 10% of it','Only while awake'],a:0,f:'Even during sleep.'},
 {q:'If 90% of the brain were spare, most injuries would…',o:['Do nothing','Cause some loss of ability','Improve thinking'],a:0,f:'In fact, almost every area matters.'},
 {q:'At any moment, only some areas work hard. That is…',o:['Efficiency, not waste','Proof of the myth','A sign of low intelligence'],a:0,f:'The grain of truth.'}]''',
js=BASE+r'''
/* ---------- where is the spare 90%? ---------- */
const DA=[['Frontal lobe','Planning, decisions, controlling impulses, and starting and organizing movement. People can lose the ability to plan or to change course.'],
 ['Occipital lobe','Vision. Damage can cause blind areas in what we see, or problems recognizing what we see.'],
 ['Temporal lobe','Hearing, understanding language, recognizing faces and objects, and memory.'],
 ['Parietal lobe','Touch, and knowing where things are in space. Damage can cause people to ignore one side of space.'],
 ['Cerebellum','Coordination, balance and timing of movement. Movements can become clumsy and unsteady.'],
 ['Hippocampus','Forming new memories of facts and events. New learning can become very difficult.'],
 ['Brainstem','Breathing, heart rate, waking and sleeping. Damage here can be life-threatening.'],
 ['Corpus callosum','Connecting the two hemispheres. Damage can disrupt how the two sides share information.']];
const seen=new Set();
$('dG').innerHTML=DA.map(([n],i)=>`<button class="nbtn ghost" type="button" data-i="${i}" aria-pressed="false">${n}</button>`).join('');
$('dG').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const i=+b.dataset.i;seen.add(i);
 $('dG').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 $('dTitle').textContent=DA[i][0];$('dText').textContent=DA[i][1];
 $('dCount').textContent=seen.size<DA.length?`${seen.size} of ${DA.length} areas checked. Spare areas found: none yet.`:`All ${DA.length} areas checked. Spare areas found: none. There is no silent 90%.`});
'''+grid('''[
 ['The 10% figure was first attached to William James in…',['A 1936 foreword to a bestselling book','A brain scan study','A Nobel lecture'],0,'A falsely precise number, credited to James.'],
 ['Over a day, brain imaging shows activity…',['Across the whole brain','In about 10% of it','Only in the frontal lobe'],0,'Even during sleep.'],
 ['Is there an area that can be damaged without some loss of ability?',['Almost none','Most areas','About 90% of areas'],0,'Injury tells the same story.'],
 ['The brain’s energy use is…',['A large share of the body’s total','Almost nothing','Lower than a muscle at rest'],0,'Evolution wouldn’t pay for idle tissue.'],
 ['At any moment, only some areas work hard because…',['The brain is efficient','90% is switched off','We’re lazy'],0,'That’s the grain of truth.'],
 ['Real gains in ability come from…',['Knowledge and skill built through practice','Unlocking a hidden reserve','A special product'],0,'Slower, but real.']]''','The pattern: imaging, injury and energy all show the whole brain is in use.'))
open('n03/template.html','w').write(page(o))
