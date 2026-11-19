import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(2,'Cut the Extras: Seductive Details and Coherence','Cut the extras','Make it interesting, by making the idea itself interesting','Cut the extras',
'A funny cartoon on a slide. A dramatic story at the start of a lecture. Background music under a video. They make a lesson more interesting. Do they make it more memorable?',
'<span><a href="#bT">Keep it or cut it?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','par'],{'pfc':([60,730],'left'),'par':([560,-70],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the parietal lobe, at the top, both involved in attention, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>Richard Mayer calls the principle coherence: people learn better when extraneous material is left out. In his summary, the median effect size was 0.86, and the result was positive in 18 of 19 tests.</p>
    <p>Interesting but irrelevant additions have a name: seductive details. In 2020, Kripa Sundararajan and Olusola Adesope pooled 58 studies with more than 7,500 students. Students who learned with seductive details did worse on learning measures.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>0.86</strong><span>median effect size for leaving extras out</span></div>
      <div role="listitem"><strong>18 of 19</strong><span>tests favoured the leaner lesson</span></div>
      <div role="listitem"><strong>58</strong><span>studies of seductive details, with more than 7,500 students</span></div>
      <div role="listitem"><strong>Worse</strong><span>when the extra sat right next to an important diagram</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">When it hurts most</span>Short lessons, new topics, next to key content</h2>
    <p>The harm was larger in short lessons, for students new to a topic, and when the extra was placed right next to an important diagram. The authors also note that the overall effect was fairly small.</p>
    <h2 class="sec"><span class="n">Why</span>Attention is limited</h2>
    <p>Attention and working memory are limited. A vivid detail can pull attention away, and can even become the frame students remember the lesson by.</p>
    <h2 class="sec"><span class="n">A trade-off</span>Interest is not the enemy</h2>
    <p>A joke can lower anxiety or build connection, and researchers are studying whether those emotional benefits make up for the cost. Interest is not the enemy. Irrelevant interest is.</p>
  </div>

'''+cls_html('bT','Keep it or cut it?','Eight additions to a lesson on how vaccines train the immune system. For each, decide: keep it, because it explains the idea, or cut it (or move it away from key content). You’ll get feedback after each one.',[('K','Keep it',''),('C','Cut or move it','')],'Keep it or cut it?','Keep it or cut it?','The question is always: does it explain the idea?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>A fairly small average effect</h2>
    <p>The overall effect of seductive details was fairly small. Not every story or image will hurt. The safest rule is to connect each one to the learning goal.</p>
  </div>

'''+GRID_HTML+box('Before you add an image, story or sound, ask: does it explain the idea? If not, cut it, or move it away from key content. When you use a hook, connect it directly to the learning goal. And share this tip with students: when studying, skip the tangents first.'),
tips_h='Make it interesting, by making the idea itself interesting.',
tips='''      <li><b>Ask: does it explain?</b><span>If not, cut it or move it.</span></li>
      <li><b>Keep extras away from key diagrams</b><span>That’s where they hurt most.</span></li>
      <li><b>Tie hooks to the goal</b><span>A story that is the idea, not beside it.</span></li>''',
sources='''        <li>Mayer, R. E. (2021). <i>Multimedia learning</i> (3rd ed.). Cambridge University Press.</li>
        <li><a href="https://doi.org/10.1007/s10648-020-09522-4">Sundararajan, N., &amp; Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. <i>Educational Psychology Review, 32</i>(3), 707–734.</a></li>''',
quiz='''[
 {q:'A seductive detail is…',o:['Interesting but irrelevant','Relevant but boring','A key diagram'],a:0,f:'It pulls attention away from the idea.'},
 {q:'Seductive details hurt most when placed…',o:['Right next to an important diagram','At the end of a long lesson','In a separate handout'],a:0,f:'And in short lessons, for beginners.'},
 {q:'Is interest the enemy?',o:['No: irrelevant interest is','Yes: lessons should be dull','Only in science'],a:0,f:'Make the idea itself interesting.'}]''',
js=BASE+cls_js("{K:'Keep it',C:'Cut or move it'}",'''[
 ['A labelled diagram of an antibody locking onto a virus','K','Keep it: it shows how the parts fit together.'],
 ['A cartoon of a superhero cell punching a germ, next to the key diagram','C','Cut or move it: a vivid extra right beside key content is where the harm was largest.'],
 ['A dramatic story about a famous outbreak that the lesson never returns to','C','Cut it, or tie it to the goal: a story that isn’t the idea can become the frame students remember.'],
 ['A short story of how a vaccine trial showed the immune response, linked to each step','K','Keep it: a story can teach when it is the idea itself.'],
 ['Background music under the narrated animation','C','Cut it: sounds that don’t explain compete for attention.'],
 ['A graph of antibody levels after a first and a second dose','K','Keep it: it shows why a booster matters.'],
 ['A fun fact about the size of the world’s largest syringe','C','Cut it: interesting, but irrelevant.'],
 ['A one-line joke at the start, then straight into the lesson','C','Cut it, or move it away from key content: a quick joke at the start may help mood, but it doesn’t explain. Researchers are still weighing that trade-off.']]''','Keep it or cut it?',r'''
 if(right>=7){title='You can spot a seductive detail';text=`${right} of 8 right. Keep what explains. Cut the rest, or move it away from key content.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does it explain the idea? Interesting is not the same as relevant.`}
 else{title='Worth another look';text=`${right} of 8 right. Diagrams, graphs and stories that are the idea itself explain. Jokes, music and fun facts beside the idea pull attention away.`}''')+grid('''[
 ['Leaving out extraneous material helped in how many of Mayer’s 19 tests?',['18','9','2'],0,'Median effect size 0.86.'],
 ['In the 2020 analysis of 58 studies, students with seductive details did…',['Worse','Better','The same'],0,'Sundararajan and Adesope.'],
 ['The harm was larger in…',['Short lessons','Long lessons','Neither'],0,'And for students new to a topic.'],
 ['The harm was larger when the extra was placed…',['Next to an important diagram','On a separate slide','At the very end'],0,'Placement matters.'],
 ['How big was the overall effect of seductive details?',['Fairly small','Very large','Zero'],0,'The authors note it is fairly small.'],
 ['Could a joke have any benefit?',['Possibly, on mood: researchers are studying it','No, never','Yes, it always helps learning'],0,'An open question.']]''','The pattern: extras that don’t explain usually cost a little learning, most of all next to key content.'))
open('d02/template.html','w').write(page(o))
