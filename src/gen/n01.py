import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('n','Neuromyths',1,'Why Neuromyths Stick','Why neuromyths stick','Interest in the brain needs a partner: a habit of checking.','Why neuromyths stick',
'Here is a puzzle. Teachers who know more about the brain are not less likely to believe brain myths. In one study, they were more likely.',
'<span><a href="#eT">Predict the surveys</a></span><span><a href="#bT">Myth or finding?</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc'],{'pfc':([40,-60],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which helps us weigh evidence, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 2002, an OECD project on the brain and learning gave these ideas a name: neuromyths. They are misreadings of real brain research, stretched into claims about teaching.</p>
    <p>Two surveys show how common they are, and who believes them.</p>
  </div>

'''+pred_html('eT','Predict the surveys','Three quick predictions about two surveys, then see the results. About 1 minute.','Who believes neuromyths?','A survey of teachers interested in the brain, and a larger American study comparing groups.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>242</strong><span>teachers in England and the Netherlands, all interested in the brain</span></div>
      <div role="listitem"><strong>49%</strong><span>of the myths believed, on average</span></div>
      <div role="listitem"><strong>68% / 56% / 46%</strong><span>endorsed by the public, educators, and people with high neuroscience exposure</span></div>
      <div role="listitem"><strong>Reduced</strong><span>by training, but not eliminated</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The surveys</span>Knowledge is not immunity</h2>
    <p>In 2012, Sanne Dekker and colleagues surveyed 242 teachers in England and the Netherlands. On average, they believed 49% of the myths. Teachers with more general brain knowledge believed more myths, not fewer.</p>
    <p>A larger American study in 2017, by Kelly Macdonald and colleagues, compared groups. The general public endorsed 68% of the myths, educators 56%, and people with high exposure to neuroscience 46%. Training helped, but did not eliminate them.</p>
    <h2 class="sec"><span class="n">Why they stick</span>Four reasons</h2>
    <p>Most start from a real finding. They offer a simple story and an easy fix. They are sold in training and products. And brain language makes a claim feel scientific.</p>
    <p>This series takes twelve popular ideas, one at a time: where each came from, what the evidence shows, the grain of truth if there is one, and what to do instead.</p>
  </div>

'''+cls_html('bT','Myth or finding?','Eight statements about the brain and learning. Some are myths; some are well supported. For each, decide which. You’ll get feedback after each one.',[('M','Myth',''),('F','Supported finding','')],'Myth or supported finding?','Myth or finding?','The question is always: what was actually tested, and on what outcome?')+GRID_HTML+box('When a teaching claim mentions the brain, ask what was actually tested, and on what outcome. Look for the original study, not the summary. And be extra careful with ideas that sell a product. Share this tip with students: when a claim mentions the brain, ask how they know.'),
tips_h='Interest in the brain is a good thing. It just needs a partner: a habit of checking.',
tips='''      <li><b>What was tested?</b><span>And on what outcome?</span></li>
      <li><b>The original study</b><span>Not the summary.</span></li>
      <li><b>Extra care with products</b><span>When the claim sells something.</span></li>''',
sources='''        <li>OECD. (2002). <i>Understanding the brain: Towards a new learning science</i>. OECD Publishing.</li>
        <li><a href="https://doi.org/10.3389/fpsyg.2012.00429">Dekker, S., Lee, N. C., Howard-Jones, P., &amp; Jolles, J. (2012). Neuromyths in education: Prevalence and predictors of misconceptions among teachers. <i>Frontiers in Psychology, 3</i>, 429.</a></li>
        <li><a href="https://doi.org/10.3389/fpsyg.2017.01314">Macdonald, K., Germine, L., Anderson, A., Christodoulou, J., &amp; McGrath, L. M. (2017). Dispelling the myth: Training in education or neuroscience decreases but does not eliminate beliefs in neuromyths. <i>Frontiers in Psychology, 8</i>, 1314.</a></li>''',
quiz='''[
 {q:'Teachers with more general brain knowledge believed…',o:['More myths, not fewer','Fewer myths','No myths'],a:0,f:'Dekker and colleagues, 2012.'},
 {q:'Neuroscience training…',o:['Reduced myths, but did not eliminate them','Eliminated them','Made them worse'],a:0,f:'46% were still endorsed.'},
 {q:'The first question to ask of a brain claim is…',o:['What was actually tested, and on what outcome?','Does it sound scientific?','Is it popular?'],a:0,f:'Then find the original study.'}]''',
js=BASE+pred_js('''[
 ['On average, what share of the myths did the 242 brain-interested teachers believe?',['About 10%','About half','Almost all'],1,'About half: 49%.'],
 ['Teachers who knew more about the brain in general believed…',['Fewer myths','More myths','The same number'],1,'More myths, not fewer. Interest without checking can spread myths.'],
 ['In the 2017 American study, which group endorsed the fewest myths?',['The general public','Educators','People with high neuroscience exposure'],2,'People with high neuroscience exposure, at 46%. Still almost half.']]''',
'''<p class="gh">Myths endorsed, 2017 American study</p>${barRow('General public',68,100,'68%','#FFB38A')}${barRow('Educators',56,100,'56%','#FCB316')}${barRow('High neuroscience exposure',46,100,'46%','#7DD3A8')}''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Myths are common, knowledge doesn’t protect you on its own, and training helps without eliminating them.'}
 else if(!got[1]){title='The puzzle';text=`You got ${n} of 3. The surprise: teachers with more general brain knowledge believed more myths. Interest needs a habit of checking.`}
 else{title='Common, even among experts';text=`You got ${n} of 3. Even people with high neuroscience exposure endorsed almost half the myths.`}''')+cls_js("{M:'Myth',F:'Supported finding'}",'''[
 ['Students learn better when teaching matches their learning style','M','Myth: studies designed to test matching found virtually no support (topic 2).'],
 ['Retrieving information from memory strengthens it','F','Supported: retrieval practice is one of the best-tested findings in learning research.'],
 ['We only use 10% of our brains','M','Myth: activity shows up across the whole brain over a day (topic 3).'],
 ['Spreading study over time beats cramming the same hours','F','Supported: the spacing effect has been replicated many times.'],
 ['Some people are left-brained, others right-brained','M','Myth: a scan study of 1,011 people found no left- or right-brained types (topic 4).'],
 ['Sugar makes children hyperactive','M','Myth: double-blind studies found no effect on behaviour (topic 7).'],
 ['The brain keeps changing with learning throughout life','F','Supported: adults learn new languages, skills and whole fields.'],
 ['Listening to Mozart makes you smarter','M','Myth: a brief, small effect on one kind of task, hard to replicate (topic 6).']]''','Myth or supported finding?',r'''
 if(right>=7){title='Sharp eye';text=`${right} of 8 right. You can tell a stretched claim from a tested one. The rest of the series looks at where each myth came from.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Even experts believe some of these. That’s why checking matters.`}
 else{title='You’re in good company';text=`${right} of 8 right. In surveys, even people with neuroscience training endorsed almost half the myths. This series takes them one at a time.`}''')+grid('''[
 ['Who named these ideas “neuromyths” in 2002?',['An OECD project','A toy company','A newspaper'],0,'On the brain and learning.'],
 ['How many teachers did Dekker and colleagues survey?',['242','24','2,420'],0,'In England and the Netherlands.'],
 ['On average, those teachers believed…',['49% of the myths','5% of the myths','95% of the myths'],0,'About half.'],
 ['In 2017, educators endorsed about…',['56% of the myths','10% of the myths','90% of the myths'],0,'The public, 68%.'],
 ['Most neuromyths start from…',['A real finding, stretched','Nothing at all','A deliberate hoax'],0,'That’s part of why they stick.'],
 ['Brain language makes a claim…',['Feel more scientific','Easier to test','Less believable'],0,'Even when it adds nothing.']]''','The pattern: myths are common, even among experts, and checking is the cure.'))
open('n01/template.html','w').write(page(o))
