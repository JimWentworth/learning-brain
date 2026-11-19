import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(1,'Words and Pictures: The Multimedia Principle','Words and pictures','Words tell. Pictures show. Together, they explain.','Words and pictures',
'Here is a short explanation of how a bicycle pump works, in words alone. Now the same words, with a simple diagram. Which one will students understand better?',
'<span><a href="#bT">Explains or decorates?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','tem'],{'occ':([900,-60],'right'),'tem':([600,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision starts, and the temporal lobe, at the side, where language is processed, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS+'''
.pump{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:16px 0 8px}
@media (max-width:640px){.pump{grid-template-columns:1fr}}
.pump figure{margin:0;border:1px solid #C9D3E3;border-radius:10px;background:#fff;padding:12px 14px}
.pump figcaption{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#13294B;margin-bottom:6px}
.pump p{font-size:16px;line-height:1.5;margin:0 0 8px;color:#13294B}
.pump svg{width:100%;height:auto;display:block}''',
body='''  <div class="col lede">
    <p>Richard Mayer’s theory of multimedia learning starts from three ideas. We take in information through two channels, one for words and one for pictures. Each channel has limited capacity. And learning happens when we actively connect the two.</p>
    <p>Across decades of experiments, students who learned from words and pictures did better on transfer tests, which ask them to use what they learned in a new way, than students who got words alone.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2 channels</strong><span>one for words, one for pictures, each with limited capacity</span></div>
      <div role="listitem"><strong>13</strong><span>experimental comparisons in Mayer’s summary</span></div>
      <div role="listitem"><strong>1.35</strong><span>median effect size on transfer tests: a large effect</span></div>
      <div role="listitem"><strong>Beginners</strong><span>gain the most; experts can build the picture in their heads</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">See it</span>The same words, with and without a picture</h2>
    <div class="pump">
      <figure>
        <figcaption>Words alone</figcaption>
        <p>When the handle is pulled up, the piston moves up, the inlet valve opens and air enters the cylinder. When the handle is pushed down, the piston moves down, the inlet valve closes, and air is forced out through the outlet valve into the hose.</p>
      </figure>
      <figure>
        <figcaption>Words and a labelled diagram</figcaption>
        <svg viewBox="0 0 300 200" role="img" aria-labelledby="pumpT"><title id="pumpT">Diagram of a bicycle pump: a handle on top of a rod, a piston inside a cylinder, an inlet valve in the piston and an outlet valve at the bottom leading to the hose. Arrows show air going in on the way up and out to the hose on the way down.</title>
          <rect x="90" y="40" width="60" height="130" rx="6" fill="none" stroke="#13294B" stroke-width="3"/>
          <rect x="60" y="14" width="120" height="12" rx="4" fill="#13294B"/><line x1="120" y1="26" x2="120" y2="80" stroke="#13294B" stroke-width="5"/>
          <rect x="94" y="80" width="52" height="12" fill="#FF5F05"/>
          <path d="M150 165 h40 q20 0 20 -20 v-20" fill="none" stroke="#13294B" stroke-width="4"/>
          <path d="M120 120 v35" stroke="#C84A00" stroke-width="3" marker-end="url(#ah)"/><path d="M200 130 v-25" stroke="#C84A00" stroke-width="3" marker-end="url(#ah)"/>
          <defs><marker id="ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#C84A00"/></marker></defs>
          <g font-family="Source Sans 3, sans-serif" font-size="14" fill="#13294B"><text x="186" y="24">handle</text><text x="4" y="90">piston and</text><text x="4" y="106">inlet valve</text><text x="4" y="150">cylinder</text><text x="158" y="186">outlet valve</text><text x="216" y="100">to hose</text></g>
          <line x1="76" y1="94" x2="94" y2="88" stroke="#13294B"/><line x1="62" y1="146" x2="90" y2="140" stroke="#13294B"/>
        </svg>
        <p>When the handle is pulled up, the piston moves up, the inlet valve opens and air enters the cylinder. When the handle is pushed down, the piston moves down, the inlet valve closes, and air is forced out through the outlet valve into the hose.</p>
      </figure>
    </div>
    <p>The diagram does not add new facts. It shows how the parts connect, which is the hard part to build from words alone.</p>

    <h2 class="sec"><span class="n">Which pictures</span>Pictures that explain</h2>
    <p>Not just any picture helps. The useful ones show how something works or how parts relate: a diagram, a process, a graph. Decorative images do not count, and they can get in the way (topic 2).</p>
    <h2 class="sec"><span class="n">Not learning styles</span>Everyone benefits</h2>
    <p>This is not learning styles. Every student benefits from words and pictures together, because the content has both a verbal and a visual side.</p>
  </div>

'''+cls_html('bT','Explains or decorates?','Eight pictures an instructor might add. For each, decide: does it help explain the idea, or just decorate the slide? You’ll get feedback after each one.',[('X','Explains',''),('D','Decorates','')],'Explains or decorates?','Explains or decorates?','The question is always: does the picture show how something works or how the parts relate?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>A boundary</h2>
    <p>The effect is stronger for beginners than for experts. Students who already know a topic can build the picture in their heads; beginners need it on the page. And most of these experiments used short lessons on how things work.</p>
  </div>

'''+GRID_HTML+box('Pair your key explanations with a simple diagram that shows how the parts connect. Put labels on the diagram, close to what they describe. Give beginners more visuals than advanced students. And share this tip with students: sketch a diagram next to your notes.'),
tips_h='Words tell. Pictures show. Together, they explain.',
tips='''      <li><b>A diagram for key ideas</b><span>One that shows how parts connect.</span></li>
      <li><b>Labels close to the parts</b><span>Not in a legend off to the side.</span></li>
      <li><b>More visuals for beginners</b><span>Experts need fewer.</span></li>''',
sources='''        <li>Mayer, R. E. (2021). <i>Multimedia learning</i> (3rd ed.). Cambridge University Press.</li>
        <li>Mayer, R. E. (2023). Research-based principles for designing multimedia instruction. In C. E. Overson, C. M. Hakala, L. L. Kordonowy, &amp; V. A. Benassi (Eds.), <i>In their own words</i> (pp. 143–157). Society for the Teaching of Psychology.</li>''',
quiz='''[
 {q:'Mayer’s theory says we take in information through…',o:['Two channels, one for words and one for pictures','One channel for everything','Whichever channel suits our learning style'],a:0,f:'Each with limited capacity.'},
 {q:'Which picture is most likely to help?',o:['A labelled diagram of how the parts connect','A stock photo on the title slide','A cartoon in the corner'],a:0,f:'Pictures help when they explain.'},
 {q:'Who gains most from words and pictures?',o:['Beginners','Experts','Nobody in particular'],a:0,f:'Experts can build the picture in their heads.'}]''',
js=BASE+cls_js("{X:'Explains',D:'Decorates'}",'''[
 ['A labelled diagram showing how blood flows through the heart','X','Explains: it shows how the parts relate.'],
 ['A stock photo of smiling students on a slide about study skills','D','Decorates: it shows nothing about the idea.'],
 ['A flowchart of the steps in cell division','X','Explains: it shows a process, step by step.'],
 ['A graph of how supply and demand set a price','X','Explains: a graph shows how two things relate.'],
 ['A picture of a lightbulb next to the word “ideas”','D','Decorates: a visual cliché, not an explanation.'],
 ['The university logo in the corner of every slide','D','Decorates: fine for branding, but it explains nothing.'],
 ['A map showing where an epidemic spread, week by week','X','Explains: it shows change across place and time.'],
 ['A photo of the author of the theory','D','Usually decorates: it shows who, not how the theory works.']]''','Explains or decorates?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Pictures help when they show how something works or how parts relate. Decoration adds load without adding understanding.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does the picture show how something works, or how the parts relate?`}
 else{title='Worth another look';text=`${right} of 8 right. Diagrams, processes, graphs and maps explain. Photos, icons and logos that don’t show the idea only decorate.`}''')+grid('''[
 ['In Mayer’s experiments, students who got words and pictures did…',['Better on transfer tests','The same','Worse, because of overload'],0,'Better at using what they learned in new ways.'],
 ['The median effect size for words and pictures was about…',['1.35: a large effect','0.1: a tiny effect','Zero'],0,'Mayer’s 2021 summary.'],
 ['Which kind of picture helps most?',['One that shows how parts relate','Any picture at all','A decorative photo'],0,'Diagrams, processes and graphs.'],
 ['The benefit is larger for…',['Beginners','Experts','Both equally'],0,'Experts can build the picture in their heads.'],
 ['Is this the same as learning styles?',['No: everyone benefits','Yes: it only helps visual learners','Only for some subjects'],0,'The content has both a verbal and a visual side.'],
 ['The theory says learning happens when students…',['Connect words and pictures','See as many pictures as possible','Hear words only'],0,'Actively linking the two channels.']]''','The pattern: words with pictures that explain help everyone, and beginners most.'))
open('d01/template.html','w').write(page(o))
