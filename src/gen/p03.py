import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(3,'Looking Without Seeing: Inattentional and Change Blindness','Looking without seeing:','inattentional and change blindness',
'We feel that we see everything in front of us. Yet people regularly miss big, obvious things, a gorilla, a stranger, a change in a picture, when their attention is elsewhere.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['par','pfc'],{'par':([560,-70],'left'),'pfc':([60,730],'left')},'Drawing of the side of the brain with the parietal lobe, at the top, and the prefrontal cortex, at the front, which steer attention, glowing orange and labelled.')

screen='''            <svg id="cbS" viewBox="0 0 520 330" width="100%" style="max-width:540px;display:block;border-radius:6px" role="img" aria-labelledby="cbD">
              <desc id="cbD">A drawing of a study desk in front of a window. The picture alternates with a brief grey screen. Between versions, one object changes.</desc>
              <g id="scene">
                <rect width="520" height="330" fill="#E8EDF4"/>
                <g id="o_win"><rect x="40" y="30" width="170" height="130" fill="#BFD6EE" stroke="#13294B" stroke-width="6"/><line id="o_bar" x1="125" y1="30" x2="125" y2="160" stroke="#13294B" stroke-width="6"/><line x1="40" y1="95" x2="210" y2="95" stroke="#13294B" stroke-width="6"/></g>
                <g id="o_clock"><circle cx="300" cy="70" r="34" fill="#fff" stroke="#13294B" stroke-width="5"/><line x1="300" y1="70" x2="300" y2="48" stroke="#13294B" stroke-width="4"/><line x1="300" y1="70" x2="316" y2="78" stroke="#13294B" stroke-width="4"/></g>
                <g id="o_pic"><rect x="380" y="34" width="100" height="74" fill="#FCB316" stroke="#13294B" stroke-width="5"/><path d="M385 103 L420 64 L445 88 L460 72 L475 103 Z" fill="#13294B"/></g>
                <rect x="0" y="230" width="520" height="22" fill="#8C6A4A"/><rect x="20" y="252" width="16" height="78" fill="#6E5238"/><rect x="484" y="252" width="16" height="78" fill="#6E5238"/>
                <g id="o_lamp"><rect x="70" y="222" width="60" height="10" fill="#13294B"/><rect x="96" y="160" width="8" height="64" fill="#13294B"/><path id="o_shade" d="M66 168 L134 168 L118 128 L82 128 Z" fill="#FF5F05"/></g>
                <g id="o_books"><rect x="170" y="196" width="90" height="16" fill="#13294B"/><rect x="176" y="180" width="80" height="16" fill="#FF5F05"/><rect x="166" y="212" width="98" height="18" fill="#3E6B9E"/></g>
                <g id="o_laptop"><path d="M290 140 L410 140 L410 216 L290 216 Z" fill="#2B3A55"/><rect x="298" y="148" width="104" height="60" fill="#9FC3E8"/><path d="M276 216 L424 216 L436 230 L264 230 Z" fill="#5A6B85"/></g>
                <g id="o_mug"><rect x="440" y="194" width="30" height="36" rx="4" fill="#fff" stroke="#13294B" stroke-width="4"/><path d="M470 202 q14 8 0 18" fill="none" stroke="#13294B" stroke-width="4"/></g>
              </g>
              <rect id="blank" width="520" height="330" fill="#C9D1DC" display="none"/>
            </svg>
            <p class="prog" id="cbT" aria-live="off">&nbsp;</p>'''
student=lab(screen,'Ready','Spot the change','The picture will flicker between two versions. One thing is different. Press “I see it” as soon as you spot it, then say what changed.','Start',
 '<button class="nbtn ghost" id="cbSee" type="button" hidden>I see it</button>')

o.update(body=tabs('Spot the change','Two versions of the same picture alternate, with a blink in between. Something big changes. How long does it take you to see it?',student,
 'About 10 minutes',
 ['Project the student version. Tell the class that one object changes between the two pictures, and to raise a hand when they see it. Don’t point.',
  'Note roughly how long it takes for most hands to go up. Repeat with round 2.',
  'Before round 3, say out loud where to look. Compare how fast hands go up.',
  'Debrief: the change was big and repeated many times. What was missing until they found it?'],
 ['Why was such a big change so hard to see?',
  'What made round 3 easier?',
  'When you change one part of a slide or diagram, how would your students know?'],
 'When you build up a diagram or change a slide, say what changed and point to it. Students can’t compare two versions they never attended to, so an unannounced change may simply not be seen.',
 'The picture flickers about once a second against a mid-grey screen. If anyone in the room is sensitive to flicker, describe the activity instead, or use the predictions section below.')+'''
  <div class="col lede">
    <p>In 1999, Daniel Simons and Christopher Chabris asked people to count basketball passes in a short video. Partway through, a person in a gorilla suit walked through the game. Across all the versions of the test, 46% of observers failed to notice the unexpected event.</p>
    <p>This is inattentional blindness: failing to see something unexpected because attention is busy elsewhere. Its cousin is change blindness: failing to notice that something has changed.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>46%</strong><span>of observers missed the unexpected event while counting passes</span></div>
      <div role="listitem"><strong>~Half</strong><span>of pedestrians missed that the stranger asking directions had been swapped</span></div>
      <div role="listitem"><strong>20 of 24</strong><span>radiologists missed a gorilla in a lung scan</span></div>
      <div role="listitem"><strong>Faster</strong><span>change spotting when people are told where to look</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The door study</span>A different person, mid-conversation</h2>
    <p>In 1998, Simons and Daniel Levin had an experimenter ask a pedestrian for directions. Two people carrying a door walked between them, and during that moment the experimenter was replaced by someone else. About half of the pedestrians did not notice they were now talking to a different person.</p>
    <h2 class="sec"><span class="n">Even experts</span>The gorilla in the scan</h2>
    <p>Trafton Drew, Melissa Võ and Jeremy Wolfe asked 24 radiologists to search lung scans for nodules. In the last case they inserted a gorilla 48 times the size of an average nodule. Twenty of the 24 did not report it, and eye tracking showed that most of those who missed it had looked directly at it. Experts are searching for something specific, and that focus works as blinders.</p>
    <h2 class="sec"><span class="n">The flicker</span>Big changes, many repeats</h2>
    <p>Ronald Rensink, Kevin O’Regan and James Clark put a brief blank between two versions of a scene, as in the activity above. People found even large, repeated changes very hard to identify. They found them much faster when given a verbal cue about where to look. Poor visibility was not the problem; attention was.</p>
    <h2 class="sec"><span class="n">For learning</span>Looking is not seeing</h2>
    <p>Students who are busy copying notes, or following one part of a demonstration, can miss what you most want them to notice. We don’t store a detailed copy of everything in view; we keep what we attended to. So say what to look for, and say when something has changed.</p>
  </div>

'''+pgrid_html(),
tips_h='Say what to look for, and say when it changes.',
tips='''      <li><b>Point before you show</b><span>Name what to watch in a demonstration or video.</span></li>
      <li><b>Announce changes</b><span>When a slide builds or a diagram changes, show what’s new.</span></li>
      <li><b>Free attention for the key moment</b><span>Pause note-taking when the important thing happens.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1068/p281059">Simons, D. J., &amp; Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. <i>Perception, 28</i>(9), 1059–1074.</a></li>
        <li><a href="https://doi.org/10.3758/BF03208840">Simons, D. J., &amp; Levin, D. T. (1998). Failure to detect changes to people during a real-world interaction. <i>Psychonomic Bulletin &amp; Review, 5</i>(4), 644–649.</a></li>
        <li><a href="https://doi.org/10.1111/j.1467-9280.1997.tb00427.x">Rensink, R. A., O’Regan, J. K., &amp; Clark, J. J. (1997). To see or not to see: The need for attention to perceive changes in scenes. <i>Psychological Science, 8</i>(5), 368–373.</a></li>
        <li><a href="https://doi.org/10.1177/0956797613479386">Drew, T., Võ, M. L.-H., &amp; Wolfe, J. M. (2013). The invisible gorilla strikes again: Sustained inattentional blindness in expert observers. <i>Psychological Science, 24</i>(9), 1848–1853.</a></li>''',
quiz='''[
 {q:'Failing to notice something unexpected because attention is elsewhere is called…',o:['Inattentional blindness','Colour blindness','The blind spot'],a:0,f:'As with the gorilla.'},
 {q:'In the flicker studies, what helped people find the change fastest?',o:['Being told where to look','Looking longer at the whole picture','Bigger screens'],a:0,f:'Attention, not visibility, was the problem.'},
 {q:'Most radiologists who missed the gorilla…',o:['Looked right at it','Never looked at that area','Were not experts'],a:0,f:'Looking is not the same as seeing.'}]''',
js=PANEL_JS+r'''
/* ---------- change blindness ---------- */
const OBJ=[['o_clock','The clock'],['o_shade','The lamp'],['o_bar','The window'],['o_books','The books'],['o_mug','The mug'],['o_pic','The picture']];
const ROUNDS=[{id:'o_clock',type:'gone',cue:''},{id:'o_shade',type:'colour',cue:''},{id:'o_bar',type:'gone',cue:'Hint: watch the window.'}];
let flick=null,showB=false;
function applyB(r,on){OBJ.forEach(([id])=>{$(id).removeAttribute('display');});$('o_shade').setAttribute('fill','#FF5F05');
 if(on){if(r.type==='gone')$(r.id).setAttribute('display','none');else $(r.id).setAttribute('fill','#3E6B9E')}}
function startFlicker(r){stopFlicker();let k=0;const step=()=>{const ph=k%4;$('blank').setAttribute('display',ph%2?'inline':'none');if(ph===0)applyB(r,false);if(ph===2)applyB(r,true);k++;flick=setTimeout(step,ph%2?150:600)};step()}
function stopFlicker(){if(flick)clearTimeout(flick);flick=null;$('blank').setAttribute('display','none')}
function waitSee(t0,cap){return new Promise(res=>{const b=$('cbSee');b.hidden=false;b.disabled=false;b.focus();
 const iv=setInterval(()=>{const s=(performance.now()-t0)/1000;$('cbT').textContent=`${Math.floor(s)} s`;if(s>cap){clearInterval(iv);b.hidden=true;b.onclick=null;res(false)}},250);
 b.onclick=()=>{clearInterval(iv);b.onclick=null;b.hidden=true;res(true)}})}
startRun(async()=>{const times=[];
 for(let i=0;i<ROUNDS.length;i++){const r=ROUNDS[i];applyB(r,false);
  say(`Round ${i+1} of 3`,i===2?'This time, with a hint':'Find the change',(r.cue?'<b>'+r.cue+'</b> ':'')+'Press “I see it” when you spot what’s changing.');
  if(i>0){await nextBtn('Start round '+(i+1));if(!RUN)return}
  startFlicker(r);const t0=performance.now();let found=false,secs=null;
  while(!found){const saw=await waitSee(t0,45);if(!RUN){stopFlicker();return}
   if(!saw){secs=null;break}
   const a=await ask(OBJ.map(x=>x[1]),'What changed?');if(!RUN){stopFlicker();return}
   if(OBJ[a][0]===r.id){found=true;secs=(performance.now()-t0)/1000;mark(a,a)}else{mark(-1,a);say(null,null,'<b class="no">Not that one.</b> Keep looking; the timer is still running.');await sw(900);hideCh()}}
  stopFlicker();applyB(r,true);hideCh();times.push(secs);
  const what=r.id==='o_clock'?'The clock appeared and disappeared.':r.id==='o_shade'?'The lamp shade changed from orange to blue.':'The middle bar of the window appeared and disappeared.';
  say(null,secs!=null?`Found in ${secs.toFixed(1)} seconds`:'Time’s up',what+(secs!=null?'':' Many people never find it without help.'))}
 $('cbT').textContent='\u00a0';const mx=Math.max(...times.map(t=>t==null?45:t));
 $('sRes').innerHTML='<div class="res">'+times.map((t,i)=>barRow(i===2?'Round 3, hint':'Round '+(i+1),t==null?45:t,mx,t==null?'not found':t.toFixed(1)+' s','#FCB316')).join('')+'</div>';
 const hintFaster=times[2]!=null&&times.slice(0,2).some(t=>t==null||t>times[2]);
 say('What happened','Big changes, missed',(hintFaster?'The hint made it faster, as in the original studies. ':'')+'The changes were large and repeated every second. Without attention on the right spot, the brain never compared the two versions. Being told where to look is what helped people most in the original flicker studies.')});
'''+grid('''[
 ['Counting basketball passes, what share of observers missed the unexpected person walking through?',['About half','About 5%','Almost everyone'],0,'46% across all the versions of the video.'],
 ['When a stranger asking directions was swapped behind a door, how many people noticed?',['About half','Nearly all','Almost none'],0,'Simons and Levin, 1998.'],
 ['How many of 24 radiologists missed a gorilla drawn into a lung scan?',['20','2','12'],0,'83%, even though it was 48 times the size of a typical nodule.'],
 ['Did the radiologists who missed it look at it?',['Most looked right at it','None looked at it','They weren’t tracked'],0,'Eye tracking showed most fixated on it.'],
 ['In the flicker studies, what made changes much easier to find?',['A verbal cue about where to look','A larger image','Slower flicker'],0,'So visibility was not the problem.']]''','The pattern: we see what we attend to, and miss even big things outside it.'))
write(o)
