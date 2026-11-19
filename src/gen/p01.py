import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(1,'Perception Is a Best Guess','Perception is','a best guess',
'Your eyes send the brain patchy, ambiguous signals. What you see is the brain’s best interpretation of them, built from context and past experience. Usually it’s right. It’s also why a student and an expert can look at the same diagram and see different things.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['v1','pfc'],{'v1':([960,770],'right'),'pfc':([40,-60],'left')},'Drawing of the side of the brain with the visual cortex, at the back, and the prefrontal cortex, at the front, glowing orange and labelled.')

# The student activity is a short narrated video of the checker-shadow demonstration.
# Video source (scenes, narration script, renderer): src/video/p01/. Files served from site/p01/.
TRANSCRIPT='Perception is a best guess. Here’s a checkerboard, with a cylinder standing on it. The cylinder casts a shadow across the board. Look at the two squares marked A and B. Which one is lighter? Decide before we go on. Most people say B. It looks much lighter than A. Now let’s cover everything except the two squares. Without the board and the shadow, A and B look the same. Because they are the same. Exactly the same grey. Bring the scene back, and join the squares with a bar of that same grey. Follow the bar from A to B. There’s no edge where the colour changes. Even now that you know, B probably still looks lighter. Knowing the answer doesn’t switch the effect off. The same amount of light reaches your eye from both squares. But your brain sees that B is in shadow. So it infers that B is a light square in dim light, and A is a dark square in bright light. It reports what the surfaces are probably like, not how much light reaches your eye. That’s perception. A best guess, built from context, and from what usually happens in the world. Usually, it’s a very good guess. Your students make guesses like this whenever they look at a new diagram or graph. You already know what matters. Their eyes are still guessing. So tell them what to look at. Based on Edward Adelson’s checker-shadow illusion, from 1995.'
student=f'''        <div class="vidwrap">
          <video controls playsinline preload="metadata" poster="poster.jpg" aria-describedby="vidHow">
            <source src="episode.mp4" type="video/mp4">
            <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
          </video>
        </div>
        <ol class="ytsteps" id="vidHow">
          <li><b>Watch and decide.</b> When the video asks which square is lighter, pause it and choose before it goes on.</li>
          <li><b>Watch the reveal.</b> The board is covered, then the squares are joined with a bar of the same grey.</li>
          <li><b>Look once more.</b> Now that you know, does B still look lighter?</li>
        </ol>
        <details class="transcript vtrans"><summary>Read the transcript</summary><p>{TRANSCRIPT}</p></details>'''

o.update(css='.vidwrap{max-width:860px;margin:0 auto;border-radius:8px;overflow:hidden;background:#000}.vidwrap video{display:block;width:100%;height:auto}.ytsteps{max-width:860px;margin:18px auto 0;padding-left:1.4em;font-size:18px;line-height:1.5}.ytsteps li{margin:6px 0}.vtrans{max-width:860px;margin:14px auto 0}',
body=tabs('Which square is lighter?','A short video: two squares on a checkerboard, one in shadow. Decide which is lighter, then watch the test.',student,
 'About 10 minutes',
 ['Play the video full screen. When it asks which square is lighter, pause it, ask everyone to decide privately, then take a show of hands.',
  'Play on: the board is covered, and the two squares look the same. Then a bar of the same grey joins them.',
  'Pause after the reveal and ask: now that you know, does B still look lighter in the full picture?',
  'In pairs, students explain what their brain assumed about the light and the shadow.',
  'Bridge to your subject: where might a beginner “see” something different from what you see?'],
 ['Why might a visual system that gets this “wrong” still be a good design?',
  'What did your brain assume about the shadow?',
  'Where in this course might a beginner see something different from what an expert sees?'],
 'Before you show a diagram, graph, specimen or text, say what to look at and what to ignore. Your eye already knows what matters. Your students’ eyes are still guessing.',
 'Projectors change contrast. Check the effect on your room’s projector beforehand; if it washes out, have students use their own screens.')+'''
  <div class="col lede">
    <p>More than 150 years ago, Hermann von Helmholtz described what we see as “unconscious inferences”: conclusions the brain draws from sensory data and past knowledge. The psychologist Richard Gregory later compared perceptions to the hypotheses of science: predictions about what is out there.</p>
    <p>The checker-shadow picture, published by Edward Adelson at MIT in 1995, shows this at work. Squares A and B are the same grey. Your brain takes the shadow into account and reports what the surfaces are probably like, not how much light reaches your eye.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Same grey</strong><span>squares A and B, in Adelson’s 1995 picture and in the version above</span></div>
      <div role="listitem"><strong>1860s</strong><span>Helmholtz describes perception as unconscious inference</span></div>
      <div role="listitem"><strong>Hollow</strong><span>a hollow mask still looks like a face that bulges out</span></div>
      <div role="listitem"><strong>Upside down</strong><span>is when the hollow-face illusion is weakest</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why guess?</span>The signal is ambiguous</h2>
    <p>The same pattern on the retina could come from many different scenes: a dark square in bright light, or a light square in shadow. The brain can’t measure which. It settles the question with context and with what usually happens in the world.</p>
    <h2 class="sec"><span class="n">Knowledge wins</span>The hollow face</h2>
    <p>Look at the inside of a hollow mask and you will usually see a normal face bulging toward you. Gregory called this evidence for the power of top-down knowledge in vision: we have seen so many faces that bulge out that this expectation overrides shading and even the depth cues from two eyes. The illusion is strongest right side up and weakest upside down, where our experience of faces helps least.</p>
    <h2 class="sec"><span class="n">A caution</span>Illusions are not failures</h2>
    <p>The same machinery that makes square B look lighter is what lets you recognise a white page in candlelight and in sunshine. Illusions are cases where a usually good guess goes wrong. They let us see the guessing.</p>
    <h2 class="sec"><span class="n">For learning</span>Experts and beginners guess differently</h2>
    <p>If perception depends on what you already know, then a beginner and an expert don’t see the same diagram. The expert’s brain fills in structure the beginner can’t yet see. Later topics in this series look at how that changes with practice, and at how to point students to what matters.</p>
  </div>

'''+pgrid_html(),
tips_h='Say what to look at. The beginner’s brain is still guessing.',
tips='''      <li><b>Name what matters</b><span>Before showing an image, say what to look for and what to ignore.</span></li>
      <li><b>Show the context</b><span>The surrounding information is what makes the right reading obvious.</span></li>
      <li><b>Expect other readings</b><span>Ask students what they see before you tell them.</span></li>''',
sources='''        <li><a href="https://persci.mit.edu/gallery/checkershadow">Adelson, E. H. (1995). Checkershadow illusion. MIT Perceptual Science Group.</a></li>
        <li><a href="https://doi.org/10.1098/rstb.1997.0095">Gregory, R. L. (1997). Knowledge in perception and illusion. <i>Philosophical Transactions of the Royal Society B, 352</i>, 1121–1127.</a></li>
        <li>Gregory, R. L. (1970). <i>The intelligent eye</i>. Weidenfeld and Nicolson.</li>''',
foot='The checkerboard in the video is our own drawing in the style of Adelson’s illusion; squares A and B are set to exactly the same grey. The narration uses a synthetic voice. The brain drawing is a simplified illustration.',
quiz='''[
 {q:'In the checker-shadow picture, squares A and B are…',o:['The same grey','Slightly different','Very different'],a:0,f:'The brain discounts the shadow.'},
 {q:'Helmholtz described perceptions as…',o:['Unconscious inferences','Exact copies of the world','Memories'],a:0,f:'Conclusions from data plus knowledge.'},
 {q:'A hollow mask usually looks…',o:['Like a normal face, bulging out','Hollow','Flat'],a:0,f:'Knowledge of faces overrides depth cues.'}]''',
js=r'''
'''+grid('''[
 ['In Adelson’s checker-shadow picture, squares A and B are…',['The same grey','Different by a little','Different by a lot'],0,'Exactly the same. The shadow changes how the brain interprets them.'],
 ['A hollow mask, seen from the front, usually looks…',['Like a normal face, bulging out','Hollow','Flat'],0,'Gregory took this as evidence for the power of top-down knowledge.'],
 ['The hollow-face illusion is weakest when the face is…',['Upside down','Lit from below','Right side up'],0,'Our experience with faces helps least upside down.'],
 ['Lighting a hollow mask from below makes the illusion…',['Stronger','Weaker','Disappear'],0,'It reverses the shading, so it looks like a normal face lit from above.'],
 ['Who first described perceptions as unconscious inferences?',['Hermann von Helmholtz','Max Wertheimer','Richard Gregory'],0,'In the 19th century. Gregory built on the idea.']]''','The pattern: what you see is an inference, and what you already know shapes it.'))
write(o)
