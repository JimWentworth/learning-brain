import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',6,'Specifications Grading: Promise and Evidence','Specifications grading','Clear standards and a second chance are good ideas. How you build them decides whether they work.','Specifications grading',
'What if, instead of points and partial credit, every assignment were marked either “meets the standard” or “not yet”, with a chance to revise?',
'<span><a href="#bT">Helps or hurts?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc','amy'],{'pfc':([40,-60],'left'),'amy':([330,740],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, involved in planning, and the amygdala, deep inside, involved in stress, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>That is specifications grading. Linda Nilson described the approach in 2014. Each task has clear specifications tied to course outcomes. Work either meets them or does not. Course grades come from how many outcomes, or bundles of tasks, students complete, often with tokens for revisions.</p>
    <p>Advocates claim it reduces anxiety, clarifies expectations, motivates students to master the material, and saves grading time.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>2014</strong><span>Linda Nilson describes specifications grading</span></div>
      <div role="listitem"><strong>STEM-heavy</strong><span>research, varying in rigour, with inconsistent findings</span></div>
      <div role="listitem"><strong>9 courses, 661 students</strong><span>each taught both ways at Carnegie Mellon, 2023–2025</span></div>
      <div role="listitem"><strong>No significant</strong><span>difference in performance, grades or stress, in a first try</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The evidence</span>Mixed, so far</h2>
    <p>Carnegie Mellon’s Eberly Center summarized it this way: research is concentrated in science and engineering, varies in rigour, and yields inconsistent findings. Many claims rest on experience and student surveys.</p>
    <p>Their own study, from fall 2023 to spring 2025, had nine instructors teach the same course both ways, in a randomly assigned order, with 661 students in all. In this first-time implementation, specifications grading made no significant difference to student performance, grades, self-efficacy, motivation or academic stress, or to instructors’ grading workload. The only differences went the other way: students in the traditionally graded sections rated the grading as clearer, and felt more in control of their grade.</p>
    <h2 class="sec"><span class="n">What else is reported</span>Surveys and older research</h2>
    <p>Other reports, often based on student surveys, describe lower anxiety and clearer expectations. That fits older research by Ruth Butler, which found that comments focused on the task supported interest better than grades alone. But in the controlled Carnegie Mellon study, those benefits did not appear, at least in a first attempt.</p>
    <h2 class="sec"><span class="n">A caution</span>Design details matter</h2>
    <p>Specs grading can create its own stress if the bar is unclear or revisions are scarce, and it can add work for instructors.</p>
  </div>

'''+cls_html('bT','Helps or hurts?','Eight design choices for a specs-graded course. For each, decide: is it likely to help the system work, or to undermine it? You’ll get feedback after each one.',[('H','Likely to help',''),('U','Likely to undermine','')],'Helps or undermines?','Helps or hurts?','The question is always: does it keep the bar clear and the second chance real?')+GRID_HTML+box('If you try it, start small: one assignment type, with clear written specifications and examples. Allow at least one revision. Tell students exactly how the course grade is built. And check what happens to learning, not just satisfaction. Share this tip with students: treat “not yet” as a guide to revise.'),
tips_h='Clear standards and a second chance are good ideas. How you build them decides whether they work.',
tips='''      <li><b>Start small</b><span>One assignment type.</span></li>
      <li><b>Clear specs, with examples</b><span>And at least one revision.</span></li>
      <li><b>Check learning</b><span>Not just satisfaction.</span></li>''',
sources='''        <li>Nilson, L. B. (2014). <i>Specifications grading: Restoring rigor, motivating students, and saving faculty time</i>. Stylus.</li>
        <li><a href="https://www.cmu.edu/teaching/teaching-as-research/atscale/specgrading/index.html">Eberly Center, Carnegie Mellon University. Teaching as Research @Scale: Impacts of specifications grading on students and instructors (Fall 2023 – Spring 2025).</a></li>
        <li>Butler, R. (1988). Enhancing and undermining intrinsic motivation: The effects of task-involving and ego-involving evaluation on interest and performance. <i>British Journal of Educational Psychology, 58</i>(1), 1–14.</li>''',
quiz='''[
 {q:'Research on specifications grading so far is…',o:['Mixed, and concentrated in STEM','Overwhelmingly positive','Overwhelmingly negative'],a:0,f:'Eberly Center summary.'},
 {q:'In Carnegie Mellon’s nine-course study, a first try at specs grading…',o:['Made no significant difference to performance, grades or stress','Raised grades a lot','Lowered performance a lot'],a:0,f:'And students rated traditional grading as clearer.'},
 {q:'Specs grading can create its own stress when…',o:['The bar is unclear or revisions are scarce','Specifications are clear','Revisions are allowed'],a:0,f:'Design details matter.'}]''',
js=BASE+cls_js("{H:'Likely to help',U:'Likely to undermine'}",'''[
 ['Written specifications for each task, with an annotated example of work that meets them','H','Likely to help: a clear bar is the point of the system.'],
 ['Vague specs like “shows strong understanding”, with no examples','U','Likely to undermine: an unclear bar creates its own stress.'],
 ['At least one revision token for every student','H','Likely to help: “not yet” only works if there’s a real second chance.'],
 ['Revisions allowed only during one week at the end of term','U','Likely to undermine: scarce revisions turn “not yet” into “no”.'],
 ['A one-page explanation of exactly how the course grade is built','H','Likely to help: students can see the path to each grade.'],
 ['Switching every assignment in every course at once, in your first term','U','Risky: start small, with one assignment type, so you can fix problems.'],
 ['Checking exam performance, not only end-of-term satisfaction','H','Likely to help: you find out whether it changed learning.'],
 ['Marking “not yet” with no comment on what’s missing','U','Likely to undermine: a revision needs to know what to fix.']]''','Helps or undermines?',r'''
 if(right>=7){title='You can build it well';text=`${right} of 8 right. Clear specs, real second chances, a transparent grade, and checking learning.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does it keep the bar clear and the second chance real?`}
 else{title='Worth another look';text=`${right} of 8 right. Unclear specs, scarce revisions and bare “not yet” marks are where specs grading tends to fail.`}''')+grid('''[
 ['Specifications grading was described by Linda Nilson in…',['2014','1984','2024'],0,'Meets the standard, or not yet.'],
 ['Course grades usually come from…',['How many outcomes or bundles students complete','Averaging partial credit','A single final exam'],0,'Often with revision tokens.'],
 ['Research on specs grading is concentrated in…',['Science and engineering','History','Art'],0,'And varies in rigour.'],
 ['Many claims about specs grading rest on…',['Experience and student surveys','Large randomized trials','Brain scans'],0,'Eberly Center summary.'],
 ['In Carnegie Mellon’s study, which sections rated grading as clearer?',['Traditionally graded sections','Specs-graded sections','No difference'],0,'The only significant differences, in a first-time implementation.'],
 ['Ruth Butler found task-focused comments supported interest better than…',['Grades alone','No feedback','Praise'],0,'An older finding that fits.']]''','The pattern: promising ideas, but so far little controlled evidence that specs grading itself changes learning.'))
import json as _j;o['vnote']=_j.load(open('gen/vnotes.json'))['e06']
open('e06/template.html','w').write(page(o))
