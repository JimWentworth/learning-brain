import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(2,'Filling In: The Blind Spot','Filling in:','the blind spot',
'Each eye has a patch with no light receptors at all. You have never noticed it, because your brain fills the hole with a guess based on what surrounds it.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['v1','tha'],{'v1':([960,770],'right'),'tha':([560,-40],'left')},'Drawing of the side of the brain with the visual cortex, at the back, and the thalamus, deep in the middle, which relays signals from the eyes, glowing orange and labelled.')

screen='''            <svg id="bsSvg" viewBox="0 0 520 240" width="100%" style="max-width:560px;display:block;background:#fff;border-radius:6px" role="img" aria-labelledby="bsDesc">
              <desc id="bsDesc">A white panel with a black cross on the left and a target on the right. With the left eye closed and the right eye fixed on the cross, the target on the right falls in the blind spot at the right distance and disappears.</desc>
              <g id="bsCross" stroke="#13294B" stroke-width="6"><line x1="44" y1="120" x2="84" y2="120"/><line x1="64" y1="100" x2="64" y2="140"/></g>
              <g id="bsS1"><circle cx="420" cy="120" r="15" fill="#13294B"/></g>
              <g id="bsS2" display="none"><rect x="300" y="113" width="105" height="14" fill="#FF5F05"/><rect x="435" y="113" width="80" height="14" fill="#FF5F05"/></g>
              <g id="bsS3" display="none"><rect x="330" y="40" width="180" height="160" fill="#FF5F05"/><circle cx="420" cy="120" r="15" fill="#13294B"/></g>
            </svg>
            <p class="prog" id="bsNote">Close your left eye. Keep your right eye on the cross.</p>'''
student=lab(screen,'Ready','Find your blind spot','Close your <b>left</b> eye and look at the cross with your right eye. Keep looking at the cross the whole time, and notice the target only out of the corner of your eye.','Start')

o.update(body=tabs('Find your blind spot','A cross, a dot and one closed eye. At the right distance, the dot disappears, and your brain paints over the hole.',student,
 'About 5–10 minutes',
 ['Students use their own screens; the right viewing distance depends on screen size. A laptop usually works at about 30 to 40 cm; a phone much closer.',
  'Everyone closes the left eye, looks at the cross with the right eye, and slowly moves closer to or farther from the screen until the dot vanishes.',
  'Move through the line and the orange patch. Ask what they saw in the gap each time.',
  'Debrief: the hole was always there. What did the brain put in it, and where did that guess come from?'],
 ['Why have you never noticed this hole before?',
  'What did your brain use to fill it in?',
  'Where else might we fill a gap without noticing there was one?'],
 'An analogy, not a finding: when an explanation skips a step, students fill the gap with what seems to fit, often without noticing a step was missing. Ask students to explain a process back to you in full, and show every step in worked examples.',
 'A student with sight in only the left eye can do it the other way round: look at the dot, and the cross will disappear at the right distance. On a projector, the right distance is several metres, so it only works for some seats.')+'''
  <div class="col lede">
    <p>Where the optic nerve leaves the back of the eye there are no photoreceptors, so the retina cannot respond to light there. In the visual field, that patch sits about 15 degrees from the point you are looking at, toward the side of your head, and covers roughly 5 degrees across and 7 degrees high.</p>
    <p>That is far bigger than the dot you just made disappear. Yet the world never shows a hole.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>None</strong><span>photoreceptors where the optic nerve leaves the eye</span></div>
      <div role="listitem"><strong>~15°</strong><span>from the point you look at, toward the temple</span></div>
      <div role="listitem"><strong>~5° × 7°</strong><span>the size of the blind spot in the visual field</span></div>
      <div role="listitem"><strong>Filled</strong><span>even with the other eye closed</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why you don’t notice</span>Two eyes, and a brain that fills in</h2>
    <p>The blind spots of your two eyes sit on opposite sides of where you are looking, so they don’t overlap: each eye covers the other’s hole. But the hole stays hidden even with one eye shut. That can only be explained by the brain compensating, filling the gap with what surrounds it: the colour of the background, the line running through.</p>
    <h2 class="sec"><span class="n">The point</span>A seamless picture is partly made up</h2>
    <p>What you experience as a complete view is partly the brain’s reconstruction. Usually that reconstruction is a good one. It fails only when something important sits exactly in the gap.</p>
    <h2 class="sec"><span class="n">For learning</span>An analogy worth using carefully</h2>
    <p>The blind spot is about vision, not reasoning. But it is a vivid way to make a point that also holds for understanding: people can fill gaps without noticing there was a gap. Students reading a dense explanation may join step 2 to step 4 and feel that it all made sense. The fix is to make gaps visible: ask them to explain back, step by step.</p>
  </div>

'''+pgrid_html(),
tips_h='The brain fills gaps you never see. Make gaps visible.',
tips='''      <li><b>Show every step</b><span>In worked examples, don’t leave the middle for students to fill in.</span></li>
      <li><b>Ask for the explanation back</b><span>A gap shows up when a student has to say it in full.</span></li>
      <li><b>Use it as a hook</b><span>Two minutes with a cross and a dot makes “your brain fills in” memorable.</span></li>''',
sources='''        <li><a href="https://cie.co.at/node/6741">International Commission on Illumination (CIE). Blind spot. In <i>International Lighting Vocabulary</i>.</a></li>
        <li><a href="https://www.encyclopedia.com/arts/culture-magazines/blind-spot">Blind spot. In C. Blakemore &amp; S. Jennett (Eds.), <i>The Oxford companion to the body</i>. Oxford University Press.</a></li>''',
foot='The cross-and-dot display is the standard blind-spot demonstration, drawn for this page. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'Why is there a blind spot?',o:['No photoreceptors where the optic nerve leaves the eye','The lens is cloudy there','The brain switches it off'],a:0,f:'The optic disc has no light-sensitive cells.'},
 {q:'With one eye closed, the blind spot looks…',o:['Filled in with the surroundings','Black','White'],a:0,f:'The brain fills it in.'},
 {q:'Do the blind spots of your two eyes overlap?',o:['No, they sit on opposite sides','Yes, exactly','Only in dim light'],a:0,f:'Each eye covers the other’s hole.'}]''',
js=PANEL_JS+r'''
/* ---------- blind spot ---------- */
const show=k=>['bsS1','bsS2','bsS3'].forEach(id=>$(id).setAttribute('display',id===k?'inline':'none'));
startRun(async()=>{show('bsS1');
 say('Step 1 of 3','Make the dot disappear','Close your left eye. Look at the cross with your right eye. Start about an arm’s length away and move slowly closer, or farther, until the dot vanishes. On a phone, hold it close.');
 let a=await ask(['It vanished','Not yet'],'Did the dot disappear?');if(!RUN)return;
 if(a===1){hideCh();say(null,'Keep going slowly','Keep your eye fixed on the cross; if you glance at the dot, it comes back. Try moving slowly toward the screen and away again. It disappears in a narrow band of distances.');
  a=await ask(['It vanished','Still not'],'Did the dot disappear now?');if(!RUN)return;
  if(a===1){hideCh();say(null,'That’s OK','Some screens are too small or too big for the right distance. Read on: the next two steps describe what most people see.')}}
 if(a===0){hideCh();say(null,'That’s your blind spot','The dot fell on the patch of your retina with no light receptors. Notice what you saw there instead: plain white, like the surroundings.')}
 await nextBtn('Next: a line');show('bsS2');
 say('Step 2 of 3','A broken line','The orange line has a gap. Find the distance where the dot vanished, and look at the cross again.');
 const b=await ask(['The line looked joined up','I saw the gap','I couldn’t tell'],'What did you see where the gap was?');if(!RUN)return;
 hideCh();say(null,b===0?'Your brain joined it up':'Most people see it joined up','When the gap falls in the blind spot, most people see one unbroken line. The brain continued the line across a hole it has no information about.');
 await nextBtn('Next: a coloured patch');show('bsS3');
 say('Step 3 of 3','A dot on orange','Same again: left eye closed, right eye on the cross.');
 const c=await ask(['Orange, like the patch','Navy, the dot','A black or empty hole'],'When the dot vanished, what filled the spot?');if(!RUN)return;
 hideCh();say('What happened','The brain paints with the surroundings','Most people see plain orange: the brain fills the hole with the colour around it. There is always a gap in each eye’s view. You never see it, because the brain fills it with its best guess about what is there.')});
'''+grid('''[
 ['How many photoreceptors are in the blind spot?',['None','About half the usual number','The same as elsewhere'],0,'Where the optic nerve leaves the eye, there are none.'],
 ['How far is the blind spot from the point you look at?',['About 15 degrees','Right at the centre','About 90 degrees'],0,'Toward the temple of each eye.'],
 ['How big is the blind spot in the visual field?',['About 5 degrees wide and 7 high','Half a degree','About 30 degrees'],0,'Much bigger than the dot in the activity.'],
 ['With the other eye closed, the hole looks…',['Filled in by the brain','Black','White, always'],0,'Only a compensating process in the brain explains that.'],
 ['Do the blind spots of your two eyes overlap?',['No: they sit on opposite sides','Yes, exactly','Only in bright light'],0,'So with both eyes open, each covers the other.']]''','The pattern: there is always a hole, and the brain always fills it.'))
write(o)
