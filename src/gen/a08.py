import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='a08',n='8',label='The Learning Brain · Generative AI · Topic 8',epi='The Learning Brain, Generative AI, episode 8',
title='Thinking Alongside AI: Where Critical Thinking Goes',h1='Thinking alongside AI',em='From making to checking',read='7',mins='2 minutes',vtitle='Thinking alongside AI',
dek='Knowledge workers who trusted AI more reported less critical thinking; those more confident in their own ability reported more. The thinking did not vanish. It moved, from making to checking.',
jumps='<span><a href="#bT">Where did the thinking go?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the prefrontal cortex, at the front, glowing orange and labelled.',
hero_js="BR.R.pfc.lab=[40,-60];BR.R.pfc.al='left';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['pfc'],labels:['pfc'],labelT:{pfc:0.8},draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS+'''
.shift{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0 6px}
@media (max-width:640px){.shift{grid-template-columns:1fr}}
.shift div{border:1px solid #C9D3E3;border-radius:10px;padding:12px 14px;background:#fff}
.shift b{display:block;font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#13294B;margin-bottom:4px}
.shift span{color:#3A4E72}.shift strong{color:#13294B}''',
body='''  <div class="col lede">
    <p>Three hundred and nineteen knowledge workers described 936 real examples of using generative AI at work, and how much critical thinking each one took. All of them used AI at work at least once a week. Hao-Ping Lee and colleagues at Carnegie Mellon University and Microsoft Research reported the results in 2025.</p>
    <p>Two kinds of confidence pulled in opposite directions. The more people trusted the AI on a task, the less critical thinking they reported. The more confident they were in their own ability, the more critical thinking they reported.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>319</strong><span>knowledge workers who used AI at work every week</span></div>
      <div role="listitem"><strong>936</strong><span>real examples of AI use at work</span></div>
      <div role="listitem"><strong>More trust in AI</strong><span>went with less critical thinking</span></div>
      <div role="listitem"><strong>More self-confidence</strong><span>went with more critical thinking</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Less effort</span>Freed up, or switched off</h2>
    <p>In most examples, workers felt that AI reduced the effort of critical thinking. That can free effort for higher-level work. Or it can mean the thinking simply stops.</p>
    <h2 class="sec"><span class="n">A shift</span>Critical thinking moved</h2>
    <p>Critical thinking did not vanish. It shifted in three ways:</p>
    <div class="shift" role="list">
      <div role="listitem"><b>Verifying</b><span>From <strong>gathering</strong> information to <strong>verifying</strong> it.</span></div>
      <div role="listitem"><b>Integrating</b><span>From <strong>solving</strong> problems to <strong>integrating</strong> AI responses.</span></div>
      <div role="listitem"><b>Stewarding</b><span>From <strong>doing</strong> tasks to <strong>stewarding</strong> them: deciding what the AI should do, and judging whether it did it.</span></div>
    </div>
  </div>

'''+cls_html('bT','Where did the thinking go?','Nine examples of people working with AI. For each, decide where the person’s critical thinking went: verifying, integrating, or stewarding. You’ll get feedback after each one.',[('V','Verifying','checking what the AI said'),('I','Integrating','fitting its output into a solution'),('S','Stewarding','directing and judging the task')],'Verifying, integrating or stewarding?','Where did the thinking go?','The question is always: what is the person still doing with their own head?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">Barriers</span>Why people didn’t check</h2>
    <p>People also named the barriers: lack of time; a sense that thinking critically was not part of the job; and difficulty judging AI output in areas where they lacked expertise. Some even said AI added effort, because its answers had to be verified.</p>
    <h2 class="sec"><span class="n">A caution</span>Self-reports, not causes</h2>
    <p>This is a survey of self-reports. It shows associations, not causes, and people may not judge their own thinking accurately.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">Make checking visible</h3>
      <p>Make verification visible and graded: ask students to show what they checked, and how. Build their confidence in the subject itself, since self-confidence went with more critical thinking. And teach stewardship explicitly: deciding what the AI should do, and judging whether it did it.</p>
    </aside>
  </div>
''',
tips_h='Students still need to know enough to check',
tips='''      <li><b>Grade the checking</b><span>What did students check, and how?</span></li>
      <li><b>Build subject confidence</b><span>It went with more critical thinking.</span></li>
      <li><b>Teach stewardship</b><span>Decide what the AI should do, and judge whether it did it.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1145/3706598.3713778">Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., &amp; Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. <i>Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems</i>.</a></li>''',
quiz='''[
 {q:'People who trusted the AI more on a task reported…',o:['Less critical thinking','More critical thinking','No difference'],a:0,f:'Confidence in their own ability went the other way.'},
 {q:'Critical thinking with AI shifted from gathering information to…',o:['Verifying it','Ignoring it','Memorizing it'],a:0,f:'And from solving to integrating, and from doing to stewarding.'},
 {q:'Which was a barrier to critical thinking?',o:['Difficulty judging AI output outside one’s expertise','Too much time','Too much training'],a:0,f:'Along with lack of time, and feeling it wasn’t part of the job.'}]''',
js=BASE+cls_js("{V:'Verifying',I:'Integrating',S:'Stewarding'}",'''[
 ['A policy analyst asks an AI for statistics, then checks each one against the original government source.','V','Verifying: the analyst didn’t gather the figures, but checked every one.'],
 ['A student reads an AI summary of a paper, then opens the paper to check the key claim.','V','Verifying: checking the summary against the source.'],
 ['A nurse checks an AI-drafted patient leaflet against the hospital’s clinical guidance.','V','Verifying: the draft is only safe once it matches the guidance.'],
 ['A programmer gets three AI-suggested fixes and works out which one fits the existing code.','I','Integrating: the thinking is in fitting a suggestion to the real system.'],
 ['A marketer takes an AI’s draft slogans and adapts one to the brand’s voice and audience.','I','Integrating: shaping AI output to fit the real goal.'],
 ['An engineer combines an AI’s calculation with site measurements to decide on a design.','I','Integrating: AI output is one input to the solution, not the solution.'],
 ['A manager writes a clear brief for the AI: the goal, the audience, and what to avoid.','S','Stewarding: deciding what the AI should do.'],
 ['A teacher decides which parts of a lesson the AI should draft, then reviews the draft against her learning goals.','S','Stewarding: directing the task, and judging whether it was done well.'],
 ['A researcher sets out what a good literature search should find, then judges whether the AI found it.','S','Stewarding: setting the standard first, then judging against it.']]''','Verifying, integrating or stewarding?',r'''
 if(right>=8){title='You can see where it went';text=`${right} of 9 right. In every case the thinking moved rather than vanished, and each move needs enough knowledge of the subject to do well.`}
 else if(right>=5){title='Mostly there';text=`${right} of 9 right. You missed ${missed}. Verifying checks what the AI said; integrating fits it into a solution; stewarding decides what it should do and judges the result.`}
 else{title='Worth another look';text=`${right} of 9 right. The shifts overlap, but ask: is the person checking facts (verifying), fitting output into a solution (integrating), or directing and judging the task (stewarding)?`}''')+grid('''[
 ['People who trusted the AI more on a task reported…',['Less critical thinking','More critical thinking','No difference'],0,'Lee and colleagues, 2025.'],
 ['People more confident in their own ability reported…',['More critical thinking','Less critical thinking','No difference'],0,'Two kinds of confidence pulled in opposite directions.'],
 ['In most examples, people felt AI made critical thinking…',['Less effortful','More effortful','No different'],0,'That can free effort, or mean the thinking stops.'],
 ['From solving problems, critical thinking shifted to…',['Integrating AI responses','Avoiding problems','Memorizing answers'],0,'Along with verifying and stewarding.'],
 ['Which was a barrier to checking AI output?',['Lack of expertise in the area','Too much time','Too little AI'],0,'Also lack of time, and feeling it wasn’t part of the job.'],
 ['This study shows…',['Associations from self-reports','Causes, from an experiment','Brain scans'],0,'People may not judge their own thinking accurately.']]''','The pattern: AI moves critical thinking from making to checking, and checking takes knowledge of the subject.'))
open('a08/template.html','w').write(page(o))
