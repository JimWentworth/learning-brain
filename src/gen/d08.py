import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(8,'The Laptop Next to You: Devices and Attention in Class','The laptop next to you','Attention is shared in a classroom. So are distractions.','The laptop next to you',
'A student opens a laptop to take notes, then a browser tab, then another. Who pays the price? Not only that student.',
'<span><a href="#bT">Does it protect attention?</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['par','pfc'],{'par':([560,-70],'left'),'pfc':([60,730],'left')},'Drawing of the side of the brain with the parietal lobe, at the top, and the prefrontal cortex, at the front, both involved in directing attention, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In 2013, Faria Sana, Tina Weston and Nicholas Cepeda ran a simulated lecture. Students who multitasked on a laptop scored lower on a comprehension test.</p>
    <p>More surprising: students seated where they could see a multitasking classmate’s screen also scored lower, even though they were not multitasking themselves.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Nearby</strong><span>students who could see a multitasking screen scored lower too</span></div>
      <div role="listitem"><strong>50</strong><span>West Point classrooms, randomly assigned</span></div>
      <div role="listitem"><strong>726</strong><span>students in an economics course</span></div>
      <div role="listitem"><strong>0.18</strong><span>standard deviations lower on the final exam, where devices were allowed</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">A field experiment</span>West Point</h2>
    <p>Susan Payne Carter and colleagues randomly assigned 50 classrooms of an economics course, with 726 students, to allow laptops and tablets, to allow only tablets lying flat, or to ban devices.</p>
    <p>On the final exam, students in classrooms that allowed devices scored 0.18 standard deviations lower than those in device-free rooms. Restricting to flat tablets barely helped. No subgroup of students benefited from having devices available.</p>
    <h2 class="sec"><span class="n">Why</span>Screens compete for attention</h2>
    <p>Attention is limited, and screens compete for it, including the screens of others. This fits what earlier series showed about notifications and multitasking.</p>
  </div>

'''+cls_html('bT','Does it protect attention?','Eight classroom device policies and habits. For each, decide: does it protect attention, or put it at risk? You’ll get feedback after each one.',[('P','Protects attention',''),('R','Puts it at risk','')],'Protects attention or puts it at risk?','Does it protect attention?','The question is always: does it limit open-ended screen use during lecture, while keeping devices for real needs?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Open-ended access, not all use</h2>
    <p>The authors were careful: they did not claim all classroom computer use is harmful. Exercises that use devices on purpose may help. The problem is open-ended access during lecture.</p>
  </div>

'''+GRID_HTML+box('Set clear device norms on the first day, and explain the evidence. Use devices on purpose, for polls or problems, then put them away. Consider a section of the room for laptop users, so screens are not in everyone’s view. Protect accommodations. Share this tip with students: sit where you can’t see other screens.'),
tips_h='Attention is shared in a classroom. So are distractions.',
tips='''      <li><b>Clear norms, day one</b><span>With the evidence.</span></li>
      <li><b>Devices on purpose</b><span>Then put them away.</span></li>
      <li><b>A laptop section</b><span>And accommodations protected.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1016/j.compedu.2012.10.003">Sana, F., Weston, T., &amp; Cepeda, N. J. (2013). Laptop multitasking hinders classroom learning for both users and nearby peers. <i>Computers &amp; Education, 62</i>, 24–31.</a></li>
        <li><a href="https://doi.org/10.1016/j.econedurev.2016.12.005">Carter, S. P., Greenberg, K., &amp; Walker, M. S. (2017). The impact of computer usage on academic performance: Evidence from a randomized trial at the United States Military Academy. <i>Economics of Education Review, 56</i>, 118–132.</a></li>''',
quiz='''[
 {q:'Students who could see a classmate multitasking…',o:['Scored lower too','Scored higher','Were unaffected'],a:0,f:'Sana and colleagues, 2013.'},
 {q:'Allowing devices at West Point lowered final exam scores by…',o:['0.18 standard deviations','Nothing','Two letter grades'],a:0,f:'50 classrooms, 726 students.'},
 {q:'Restricting to flat tablets…',o:['Barely helped','Fixed the problem','Made it worse'],a:0,f:'Open-ended access is the issue.'}]''',
js=BASE+cls_js("{P:'Protects attention',R:'Puts it at risk'}",'''[
 ['Laptops open all lecture, with no stated norms','R','Puts it at risk: open-ended access during lecture is what lowered exam scores at West Point.'],
 ['A short device activity, like a poll, then “lids down”','P','Protects attention: devices used on purpose, then put away.'],
 ['A section of the room for laptop users, toward the back or side','P','Protects attention: fewer students see other people’s screens.'],
 ['Allowing only tablets lying flat on the desk','R','Barely helped at West Point: restricting the device is not the same as removing open-ended access.'],
 ['Explaining the evidence on the first day, including the effect on neighbours','P','Protects attention: students can make informed choices, and know their screen affects others.'],
 ['Banning all devices, with no exceptions for accommodations','R','A problem: for some students, a laptop is an accommodation. Any policy needs to protect that.'],
 ['Notifications turned off for the class session','P','Protects attention: alerts are among the clearest costs.'],
 ['Letting students check messages “just quickly” whenever they like','R','Puts it at risk: each check pulls attention, for the student and anyone watching.']]''','Protects attention or puts it at risk?',r'''
 if(right>=7){title='You can protect attention';text=`${right} of 8 right. Clear norms, devices on purpose, a laptop section, and protected accommodations.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Open-ended access is the risk; purposeful use and clear norms protect attention.`}
 else{title='Worth another look';text=`${right} of 8 right. The evidence points to open-ended screen access during lecture, including the screens of neighbours, while accommodations must be protected.`}''')+grid('''[
 ['In the 2013 simulated lecture, laptop multitaskers scored…',['Lower','Higher','The same'],0,'Sana, Weston and Cepeda.'],
 ['Students who could see a multitasker’s screen…',['Also scored lower','Scored higher','Were unaffected'],0,'Even though they weren’t multitasking.'],
 ['The West Point study randomly assigned about how many classrooms?',['50','5','500'],0,'With 726 students.'],
 ['Where devices were allowed, final exam scores were…',['0.18 standard deviations lower','The same','Higher'],0,'Compared with device-free rooms.'],
 ['Did any subgroup of students benefit from having devices?',['No','Yes, strong students','Yes, weaker students'],0,'No subgroup benefited.'],
 ['Did the authors say all classroom computer use is harmful?',['No','Yes','They didn’t comment'],0,'Devices used on purpose may help.']]''','The pattern: open-ended screen access during lecture costs attention, for users and for the people around them.'))
open('d08/template.html','w').write(page(o))
