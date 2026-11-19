import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',10,'“It’s All Over by Age Three”: The First-Three-Years Myth','It’s all over by age three','The early years open doors. They do not close the others.','It’s all over by age three',
'The first three years build the brain for life. Miss that window, and the doors close. It is a powerful message. Is it true?',
'<span><a href="#eT">Check the three pillars</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['occ','hip'],{'occ':([900,-60],'right'),'hip':([640,770],'left')},'Drawing of the side of the brain with the occipital lobe, at the back, where vision has a real early critical period, and the hippocampus, deep inside, which keeps forming new memories throughout life, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS,
body='''  <div class="col lede">
    <p>In the 1990s, this idea spread through reports, campaigns and a 1997 White House conference. In 1999, John Bruer examined its three pillars in his book, <i>The Myth of the First Three Years</i>.</p>
  </div>

'''+pred_html('eT','Check the three pillars','Three quick predictions, one for each pillar of the myth, then see what the evidence shows. About 1 minute.','Synapses, windows, enrichment','The three pillars Bruer examined.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~50% higher</strong><span>synapse density in early childhood than in adults</span></div>
      <div role="listitem"><strong>Vision</strong><span>the classic example of a real critical period</span></div>
      <div role="listitem"><strong>Rats</strong><span>in barren versus normal cages: the “enrichment” evidence</span></div>
      <div role="listitem"><strong>Lifelong</strong><span>the brain stays plastic</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Pillar 1</span>Synapses</h2>
    <p>It is true that connections form rapidly after birth. In early childhood, synapse density peaks at levels roughly 50% higher than in adults, and stays high until puberty. But more synapses do not mean more learning, and learning continues as connections are pruned and refined.</p>
    <h2 class="sec"><span class="n">Pillar 2</span>Critical periods</h2>
    <p>They are real for some sensory and motor systems. Vision is the classic example. But there is little evidence of such windows for most of what we learn in school, like reading, history or chemistry.</p>
    <h2 class="sec"><span class="n">Pillar 3</span>Enriched environments</h2>
    <p>The research was largely with rats, comparing barren cages to more normal ones. It does not show that extra stimulation builds super brains.</p>
    <h2 class="sec"><span class="n">The grain of truth</span>Early experience matters</h2>
    <p>Early experience does matter, and good early education helps many children. But the brain stays plastic. Adults learn new languages, skills and whole fields, as The Learning Brain series showed.</p>
  </div>

'''+GRID_HTML+box('Tell students, especially returning and adult learners, that it is not too late. Build on what they already know. And design for steady practice over time, rather than a single window. Share this tip with students: it’s never too late to learn something hard.'),
tips_h='The early years open doors. They do not close the others.',
tips='''      <li><b>It’s not too late</b><span>Say it to adult learners.</span></li>
      <li><b>Build on what they know</b><span>Prior knowledge is an asset.</span></li>
      <li><b>Steady practice</b><span>Not a single window.</span></li>''',
sources='''        <li>Bruer, J. T. (1999). <i>The myth of the first three years: A new understanding of early brain development and lifelong learning</i>. Free Press.</li>''',
quiz='''[
 {q:'More synapses in early childhood means…',o:['Not necessarily more learning','Children learn everything faster','Adults can’t learn'],a:0,f:'Learning continues as connections are pruned.'},
 {q:'Critical periods are well established for…',o:['Some sensory systems, like vision','Reading and chemistry','Everything learned in school'],a:0,f:'Few such windows for school subjects.'},
 {q:'The “enrichment” evidence came mostly from…',o:['Rats in barren versus normal cages','Gifted toddlers','Classrooms'],a:0,f:'It doesn’t show extra stimulation builds super brains.'}]''',
js=BASE+pred_js('''[
 ['Pillar 1: in early childhood, synapse density peaks at about what level compared with adults?',['About the same','About 50% higher','About ten times higher'],1,'About 50% higher. But more synapses do not mean more learning; learning continues as connections are pruned.'],
 ['Pillar 2: for which of these is there good evidence of a critical period?',['Learning to read','Early vision','Learning chemistry'],1,'Early vision. There is little evidence of such windows for most school subjects.'],
 ['Pillar 3: most of the “enriched environment” evidence came from…',['Toddlers in special programs','Rats in barren versus more normal cages','Brain scans of gifted children'],1,'Rats. It does not show that extra stimulation builds super brains.']]''',
'''<p class="gh">The three pillars</p><p class="mtext"><b>Synapses:</b> real, but more is not better. <b>Critical periods:</b> real for vision, rare for school subjects. <b>Enrichment:</b> mostly rats, not super brains.</p>''',
r''' if(n===3){title='All three pillars checked';text='All 3 right. Each pillar has a grain of truth, but none shows that learning closes at age three.'}
 else{title='Each pillar is a stretch';text=`You got ${n} of 3. Each pillar starts from something real, then stretches it. The brain stays plastic for life.`}''')+grid('''[
 ['A White House conference on early brain development was held in…',['1997','1957','2017'],0,'Part of the 1990s campaigns.'],
 ['Who examined the myth’s three pillars in a 1999 book?',['John Bruer','Howard Gardner','Roger Sperry'],0,'The Myth of the First Three Years.'],
 ['After the early peak, synapse density…',['Stays high until puberty, then declines','Drops at age three','Never changes'],0,'Pruning refines connections.'],
 ['The classic example of a real critical period is…',['Vision','Reading','History'],0,'Some sensory and motor systems.'],
 ['Does good early education help many children?',['Yes','No','Only after age three'],0,'Early experience matters.'],
 ['Can adults learn new languages, skills and whole fields?',['Yes: the brain stays plastic','No','Only before 30'],0,'It’s never too late.']]''','The pattern: early experience matters, but the brain stays plastic for life.'))
open('n10/template.html','w').write(page(o))
