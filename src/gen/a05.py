import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a05',n='5',label='The Learning Brain · Generative AI · Topic 5',epi='The Learning Brain, Generative AI, episode 5',
title='A Tutor Built on Learning Science: When AI Doubles Learning',h1='A tutor built on learning science',em='Design decides',read='7',mins='2 minutes',vtitle='A tutor built on learning science',
dek='In a Harvard physics course, students learned more than twice as much from an AI tutor as from a strong active-learning class, in less time. The tutor was built to make them think.',
jumps='<span><a href="#bT">Build the tutor</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, and the parietal lobe, at the top, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[60,730];BR.R.pfc.al='left';BR.R.par.lab=[560,-70];BR.R.par.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc','par'],labels:['pfc','par'],labelT:{pfc:0.8,par:1.0},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In Harvard’s largest introductory physics course, 194 students took two lessons each. One week they learned in an active-learning class; the other week, at home with an AI tutor. Then they swapped. Greg Kestin, Kelly Miller and colleagues reported the results in 2025.</p>
    <p>The class was not a weak comparison. It already used research-based active learning.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>194</strong><span>students in a crossover experiment, each taught both ways</span></div>
      <div role="listitem"><strong>More than double</strong><span>the median learning gain with the AI tutor</span></div>
      <div role="listitem"><strong>4.5 vs 3.5</strong><span>median scores out of 6, up from 2.75 before the lesson</span></div>
      <div role="listitem"><strong>49 minutes</strong><span>median time with the tutor, against a 60-minute class</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The design</span>Not an off-the-shelf chatbot</h2>
    <p>The tutor was built on learning science. It worked one step at a time and made students do the thinking. It managed cognitive load, gave immediate feedback, and let students set their own pace. It had the correct solutions built in, to keep it accurate. Students also said they felt more engaged and more motivated.</p>
    <p>Set beside the previous topic, the lesson is clear. The same technology can harm learning, or double it. Design decides.</p>
  </div>

'''+cls_html('bT','Build the tutor','Ten design choices for an AI tutor. For each, decide: does it build learning, or undermine it? You’ll get feedback after each one.',[('B','Builds learning',''),('U','Undermines it','')],'Builds learning or undermines it?','Build the tutor','The question is always: what does it make the student do?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Notable, not a general law</h2>
    <p>This was one course, two topics and short-term tests, with highly motivated students. The comparison class was already strong, which makes the gain notable, but not a general law.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Choose a tutor that asks before it tells</h3>
      <p>If you build or choose an AI tutor, require that it asks before it tells. Load it with your own correct solutions. Use it for first exposure to content, and spend class time on discussion and harder problems. And tell students why the tutor holds back the answer, so they don’t route around it.</p>
    </aside>
  </div>
''',
tips_h='A tutor is defined by what it makes the student do',
tips='''      <li><b>Asks before it tells</b><span>The student does the thinking.</span></li>
      <li><b>Your own correct solutions</b><span>Built in, to keep it accurate.</span></li>
      <li><b>Explain the design</b><span>So students don’t route around it.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/s41598-025-97652-6">Kestin, G., Miller, K., Klales, A., Milbourne, T., &amp; Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. <i>Scientific Reports, 15</i>, 17458.</a></li>
        <li><a href="https://doi.org/10.1073/pnas.2422633122">Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., &amp; Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. <i>Proceedings of the National Academy of Sciences, 122</i>(26), e2422633122.</a></li>''',
quiz='''[
 {q:'Compared with a research-based active-learning class, the AI tutor produced…',o:['More than double the median learning gain','About the same gain','A smaller gain'],a:0,f:'In less time: a median of 49 minutes, against a 60-minute class.'},
 {q:'Which was part of the tutor’s design?',o:['It made students do the thinking, one step at a time','It gave full answers on request','It replaced the instructor’s solutions with its own'],a:0,f:'It also had the correct solutions built in.'},
 {q:'What decides whether AI harms or helps learning?',o:['How it is designed and used','Whether it is AI at all','How new the model is'],a:0,f:'The same technology can harm learning, or double it.'}]''',
js=BASE+cls_js("{B:'Builds learning',U:'Undermines it'}",'''[
 ['Gives the full worked solution as soon as the student asks','U','Undermines it: the student skips the thinking. Hints first, and the solution only after a real attempt.'],
 ['Breaks each problem into one step at a time','B','Builds learning: small steps keep the load on working memory manageable.'],
 ['Asks the student to try the next step before showing it','B','Builds learning: asking before telling makes the student generate the answer.'],
 ['Gives feedback right after each step','B','Builds learning: errors are caught before they settle in.'],
 ['Is loaded with the instructor’s own correct solutions','B','Builds learning: it keeps the tutor accurate. A confident wrong answer teaches the wrong thing.'],
 ['Works out its own solutions, with no answer key to check against','U','Undermines it: an unchecked AI can be confidently wrong, and a novice can’t tell.'],
 ['Opens with a long explanation of every concept at once','U','Undermines it: too much at once overloads working memory.'],
 ['Lets each student move at their own pace','B','Builds learning: students can slow down where they need to.'],
 ['Praises every answer, right or wrong','U','Undermines it: feedback only helps if it is accurate.'],
 ['Tells students why it holds back the answer','B','Builds learning: students who know why are less likely to route around it.']]''','Builds learning or undermines it?',r'''
 if(right>=9){title='You’d build a good tutor';text=`${right} of 10 right. Every good choice makes the student think, keeps the load manageable, or keeps the feedback accurate.`}
 else if(right>=6){title='Mostly there';text=`${right} of 10 right. You missed ${missed}. Ask: does it make the student think? Is the load manageable? Is the feedback accurate?`}
 else{title='Worth another look';text=`${right} of 10 right. Good tutor design asks before it tells, works one step at a time, and keeps its feedback accurate.`}''')+grid('''[
 ['Students learning from the AI tutor, compared with the active-learning class',['More than double the median learning gain','About the same gain','A smaller gain'],0,'Kestin, Miller and colleagues, 2025.'],
 ['Median scores out of 6, from 2.75 before the lesson',['4.5 with the tutor, 3.5 in class','3.5 with the tutor, 4.5 in class','About 4 in both'],0,'The class already used research-based active learning.'],
 ['Time spent',['Less with the tutor: a median of 49 minutes, against a 60-minute class','More with the tutor','The same'],0,'Students learned more, in less time.'],
 ['The tutor’s answers were kept accurate by…',['Correct solutions built in','A newer model','Letting it search the web'],0,'Load a tutor with your own correct solutions.'],
 ['How did students feel about the tutor?',['More engaged and more motivated','Bored','Confused'],0,'Students reported this themselves, alongside learning more.'],
 ['These results came from…',['One course, two topics, short-term tests','Many courses over a year','Primary schools'],0,'With highly motivated students: notable, but not a general law.']]''','The pattern: a tutor built to make students think, step by step, with accurate feedback, can beat a strong class. The design decides.'))
open('a05/template.html','w').write(page(o))
