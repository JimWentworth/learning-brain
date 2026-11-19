import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(10,'Online, Blended, Face to Face: Design Over Medium','Online, blended, face to face','It’s not where the course happens. It’s how it’s built.','Online, blended, face to face',
'Online, face to face, or a blend of both. Every institution has had to choose. Which one helps students learn the most?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#bT">Redesign or just record?</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip','pfc'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>A 2010 report for the US Department of Education, led by Barbara Means, searched more than a thousand studies of online learning. It kept only rigorous comparisons that measured learning, yielding 50 contrasts for meta-analysis.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the report, then see the results. About 1 minute.','Online, blended, face to face','Each format is compared with fully face-to-face teaching.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>1,000+</strong><span>studies searched</span></div>
      <div role="listitem"><strong>50</strong><span>rigorous contrasts in the meta-analysis</span></div>
      <div role="listitem"><strong>~0.05</strong><span>fully online vs face to face: essentially no difference</span></div>
      <div role="listitem"><strong>~0.35</strong><span>blended vs face to face: a meaningful advantage</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Why</span>Not the technology</h2>
    <p>The authors warned against crediting the medium. The blended conditions often included extra learning time, extra resources, and more chances to practise. The advantage reflected redesigning the learning experience, not the technology itself.</p>
    <h2 class="sec"><span class="n">A caution</span>Older studies, older learners</h2>
    <p>The studies ran through 2008 and were mostly with older learners, with very few in schools. And they studied planned online courses, not the emergency remote teaching of 2020, which was a different thing.</p>
    <p>The lesson echoes the Belonging series: format matters less than structure. A well-designed online course beats a poorly designed lecture, and a well-designed blend can beat both.</p>
  </div>

'''+cls_html('bT','Redesign, or just record?','Eight ways to move a course online. For each, decide: is it a redesign that uses each setting for what it does well, or does it just move the old course onto a screen? You’ll get feedback after each one.',[('D','Redesign',''),('R','Just recorded','')],'Redesign or just recorded?','Redesign, or just record?','The question is always: does it add practice, feedback or interaction, or only change the screen?')+GRID_HTML+box('When you move material online, redesign it rather than recording it. Use online time for what it does well, like self-paced practice with feedback. Use in-person time for discussion, problem solving and questions. Share this tip with students: treat online work as real class time.'),
tips_h='It’s not where the course happens. It’s how it’s built.',
tips='''      <li><b>Redesign, don’t just record</b><span>Add practice and feedback.</span></li>
      <li><b>Online for self-paced practice</b><span>With feedback.</span></li>
      <li><b>In person for people</b><span>Discussion, problems, questions.</span></li>''',
sources='''        <li><a href="https://www2.ed.gov/rschstat/eval/tech/evidence-based-practices/finalreport.pdf">Means, B., Toyama, Y., Murphy, R., Bakia, M., &amp; Jones, K. (2010). <i>Evaluation of evidence-based practices in online learning: A meta-analysis and review of online learning studies</i> (rev. ed.). US Department of Education.</a></li>''',
quiz='''[
 {q:'Fully online vs fully face to face, learning was…',o:['Essentially the same','Much better online','Much better face to face'],a:0,f:'An effect size of about 0.05.'},
 {q:'Blended courses had an advantage of about…',o:['0.35','0.05','1.5'],a:0,f:'A meaningful advantage.'},
 {q:'The authors credited the blended advantage to…',o:['Redesign: extra time, resources and practice','The technology itself','Younger students'],a:0,f:'Not the medium.'}]''',
js=BASE+pred_js('''[
 ['Fully online versus fully face to face: which did students learn more from?',['Face to face, clearly','Online, clearly','Essentially no difference'],2,'Essentially no difference: an effect size of about 0.05.'],
 ['Blended (part online, part face to face) versus face to face?',['Blended did better','Face to face did better','No difference'],0,'Blended did better: an effect size of about 0.35.'],
 ['Why did blended courses do better, according to the authors?',['The technology','Extra learning time, resources and practice','Students preferred it'],1,'Extra learning time, resources and practice: a redesign, not the medium.']]''',
'''<p class="gh">Effect size compared with face to face</p>${barRow('Fully online',0.05,0.4,'~0.05','#C9D3E3')}${barRow('Blended',0.35,0.4,'~0.35','#7DD3A8')}''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Online alone made little difference. Blended courses did better, but because they were redesigned with more time and practice, not because of the technology.'}
 else if(!got[2]){title='Design, not the medium';text=`You got ${n} of 3. The authors warned against crediting technology. Blended conditions often had extra learning time, resources and practice.`}
 else{title='Format matters less than structure';text=`You got ${n} of 3. Fully online was about the same as face to face. Blended did better when it was redesigned.`}''')+cls_js("{D:'Redesign',R:'Just recorded'}",'''[
 ['Posting last year’s 50-minute lecture recordings, unchanged','R','Just recorded: same lecture, new screen, minus the room.'],
 ['Short videos, each followed by practice questions with instant feedback','D','Redesign: online time used for self-paced practice with feedback.'],
 ['Using in-person time for problem solving in groups, not repeating the videos','D','Redesign: in-person time for what only people in a room can do.'],
 ['Streaming the live lecture so students can watch from home, with nothing else changed','R','Just recorded: the format changed, the learning design didn’t.'],
 ['An online discussion with a clear prompt, roles and a deadline','D','Redesign: structure turns a forum into interaction.'],
 ['Scanning the printed handouts into PDFs','R','Just moved: useful, but not a redesign.'],
 ['Weekly online quizzes that count a little, spaced across the term','D','Redesign: low-stakes, spaced retrieval practice.'],
 ['Live video calls where the instructor lectures for 90 minutes','R','Just moved: a lecture on a smaller screen.']]''','Redesign or just recorded?',r'''
 if(right>=7){title='You can tell redesign from recording';text=`${right} of 8 right. Redesign adds practice, feedback and structured interaction. Moving a lecture to a screen doesn’t.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does it add practice, feedback or interaction, or only change the screen?`}
 else{title='Worth another look';text=`${right} of 8 right. The advantage in the report came from redesign: more time, resources and practice. Recording or streaming the same lecture changes only the screen.`}''')+grid('''[
 ['The 2010 report searched about how many studies?',['More than a thousand','About fifty','About ten'],0,'Only rigorous ones were kept.'],
 ['How many contrasts went into the meta-analysis?',['50','500','5'],0,'From studies that measured learning rigorously.'],
 ['Fully online vs face to face: the effect size was about…',['0.05','0.5','1.0'],0,'Essentially no difference.'],
 ['Blended vs face to face: the effect size was about…',['0.35','0.05','Negative'],0,'A meaningful advantage.'],
 ['The studies were mostly with…',['Older learners, few in schools','Young children','Teachers only'],0,'And ran through 2008.'],
 ['Did they study the emergency remote teaching of 2020?',['No','Yes','Partly'],0,'That was a different thing.']]''','The pattern: the medium matters little; redesign with more practice and feedback matters a lot.'))
open('d10/template.html','w').write(page(o))
