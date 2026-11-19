import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',1,'Tests That Teach: The Testing Effect','Tests that teach','A test is not only a measurement. It is one of the best ways to learn.','Tests that teach',
'We usually think of a test as a measuring stick. Learning happens first, and the test checks it afterwards. But what if the test itself is where much of the learning happens?',
'<span><a href="#eT">Predict the results</a></span><span><a href="#bT">Recall or recognize?</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip','pfc'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the hippocampus, deep inside, which helps store memories, and the prefrontal cortex, at the front, which guides retrieval, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 2006, Henry Roediger and Jeffrey Karpicke had college students read short science passages. Then students either read the passage again, or tried to write down everything they remembered, with no feedback.</p>
  </div>

'''+pred_html('eT','Predict the results','Three quick predictions about the 2006 study, then see the results. About 1 minute.','Reread, or recall?','Ideas recalled, five minutes and one week later.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>81% vs 75%</strong><span>after 5 minutes: rereading ahead</span></div>
      <div role="listitem"><strong>42% vs 56%</strong><span>after a week: testing ahead</span></div>
      <div role="listitem"><strong>118</strong><span>articles, 15,000+ participants, pooled in 2017</span></div>
      <div role="listitem"><strong>Labs and classrooms</strong><span>for retention and for transfer</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Not a one-off</span>118 articles</h2>
    <p>In 2017, Olusola Adesope and colleagues pooled 118 articles with more than 15,000 participants. Practice tests beat rereading and every other comparison, in labs and in classrooms, for retention and for transfer.</p>
    <h2 class="sec"><span class="n">Why it works</span>Strengthening the route back</h2>
    <p>Pulling knowledge out of memory strengthens the route back to it. It also shows students what they don’t yet know, which rereading hides.</p>
    <h2 class="sec"><span class="n">The catch</span>Rereading feels better</h2>
    <p>Rereading feels more effective. In the 2006 study, students who reread were more confident, even though they remembered less. So students rarely choose testing on their own, as Habits of the Learner showed.</p>
  </div>

'''+cls_html('bT','Recall or recognize?','Eight practice questions. For each, decide: does it make students recall from memory, or only recognize something in front of them? You’ll get feedback after each one.',[('C','Makes them recall',''),('G','Only recognize','')],'Recall or recognize?','Recall or recognize?','The question is always: does the student have to bring the answer out of memory?')+GRID_HTML+box('Build short practice tests into every week, and call them practice. Use questions that make students recall, not just recognize. Explain the evidence, so students understand why. Share this tip with students: quiz yourself instead of rereading.'),
tips_h='A test is not only a measurement. It is one of the best ways to learn.',
tips='''      <li><b>Practice tests every week</b><span>Called practice.</span></li>
      <li><b>Recall, not just recognize</b><span>Bring it out of memory.</span></li>
      <li><b>Explain why</b><span>Rereading feels better, but isn’t.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1111/j.1467-9280.2006.01693.x">Roediger, H. L., &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <i>Psychological Science, 17</i>(3), 249–255.</a></li>
        <li><a href="https://doi.org/10.3102/0034654316689306">Adesope, O. O., Trevisan, D. A., &amp; Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. <i>Review of Educational Research, 87</i>(3), 659–701.</a></li>''',
quiz='''[
 {q:'A week later, students who had tested themselves recalled…',o:['More than those who reread','Less','The same'],a:0,f:'56% versus 42%.'},
 {q:'Students who reread felt…',o:['More confident, while remembering less','Less confident','Exactly as confident'],a:0,f:'Why students rarely choose testing.'},
 {q:'Which question makes students recall?',o:['“Explain in your own words how…”','“True or false: …”','“Highlight the key term”'],a:0,f:'Bringing it out of memory.'}]''',
js=BASE+pred_js('''[
 ['Five minutes later, which group recalled more?',['Rereaders','Self-testers','No difference'],0,'Rereaders: 81% versus 75%. Rereading looked better at first.'],
 ['A week later, which group recalled more?',['Rereaders','Self-testers','No difference'],1,'Self-testers: 56% versus 42%. The pattern flipped.'],
 ['Which group felt more confident about remembering?',['Rereaders','Self-testers','Equally confident'],0,'Rereaders, even though they remembered less a week later.']]''',
'''<p class="gh">After 5 minutes</p>${barRow('Reread',81,100,'81%','#C9D3E3')}${barRow('Tested themselves',75,100,'75%','#7DD3A8')}<p class="gh">After 1 week</p>${barRow('Reread',42,100,'42%','#C9D3E3')}${barRow('Tested themselves',56,100,'56%','#7DD3A8')}''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Rereading wins for minutes, testing wins for a week, and rereading feels better throughout.'}
 else if(!got[1]){title='The flip';text=`You got ${n} of 3. A week later, the self-testers remembered more: 56% versus 42%.`}
 else{title='The confidence trap';text=`You got ${n} of 3. Rereading felt better and looked better at first, which is why students keep choosing it.`}''')+cls_js("{C:'Makes them recall',G:'Only recognize'}",'''[
 ['“Without your notes, list the three stages of cell division.”','C','Makes them recall: the answer has to come from memory.'],
 ['“Highlight the key terms in this paragraph.”','G','Only recognize: the terms are right there.'],
 ['“Explain, in two sentences, why the moon has phases.”','C','Makes them recall: and explain, which needs understanding.'],
 ['“Reread the summary at the end of the chapter.”','G','Neither, really: rereading is the comparison that lost.'],
 ['“Draw the circuit from memory, then check it against the book.”','C','Makes them recall: and checking gives feedback.'],
 ['“Which of these words did you see in the reading? Tick them.”','G','Only recognize: familiarity, not recall.'],
 ['“Close the book and write everything you remember about the reading.”','C','Makes them recall: this is exactly what the 2006 study tested.'],
 ['“Look over the worked example once more.”','G','Only recognize: it feels familiar, but nothing is retrieved.']]''','Recall or recognize?',r'''
 if(right>=7){title='You can tell them apart';text=`${right} of 8 right. Recall questions do the work: the answer has to come out of memory.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does the student have to bring the answer out of memory?`}
 else{title='Worth another look';text=`${right} of 8 right. Writing, explaining and drawing from memory make students recall. Rereading, highlighting and ticking only recognize.`}''')+grid('''[
 ['In 2006, students either reread or…',['Wrote down everything they remembered','Watched a video','Took notes'],0,'With no feedback.'],
 ['Five minutes later, rereaders recalled about…',['81% of ideas','42%','100%'],0,'Self-testers, 75%.'],
 ['A week later, self-testers recalled about…',['56%','81%','20%'],0,'Rereaders, 42%.'],
 ['The 2017 meta-analysis pooled how many articles?',['118','18','1,180'],0,'More than 15,000 participants.'],
 ['Practice tests helped…',['In labs and classrooms, for retention and transfer','Only in labs','Only for facts'],0,'Adesope and colleagues.'],
 ['Why don’t students choose testing on their own?',['Rereading feels more effective','Testing is boring','They don’t have time'],0,'Confidence misleads.']]''','The pattern: testing beats rereading over time, even though rereading feels better.'))
open('e01/template.html','w').write(page(o))
