import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
o=dict(id='b03',n='3',label='The Learning Brain · Belonging · Topic 3',epi='The Learning Brain, Belonging, episode 3',
title='What the Room Says: Ambient Belonging',h1='What the room says',em='Every room sends a message; choose yours',read='7',mins='2 minutes',vtitle='What the room says',
dek='Walk into a room and, within seconds, you sense whether people like you belong there. It happens before anyone says a word. Researchers call it ambient belonging.',
jumps='<span><a href="#bT">Narrow or wide?</a></span><span><a href="#brT">Predict the findings</a></span>',
hero_aria='Drawing of the side of the brain with the occipital lobe, at the back, where vision is processed, and the amygdala, deep inside, glowing orange and labelled.',
hero_js="BR.R.amy.lab=[330,740];BR.R.amy.al='left';BR.R.occ.lab=[900,-60];BR.R.occ.al='right';\nstage('heroBrain',({W,H,t})=>{brainDraw({cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:['occ','amy'],labels:['occ','amy'],labelT:{occ:0.8,amy:1.0},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))})});",
css=RECALL_CSS+CLS_CSS,
body='''  <div class="col lede">
    <p>In a 2009 study by Sapna Cheryan, Victoria Plaut, Paul Davies and Claude Steele, students who were not studying computer science filled out a career survey in a small classroom. For some, the room held objects stereotyped as computer science: a Star Trek poster, video game boxes, soda cans. For others, the same room held a nature poster, water bottles, and general magazines.</p>
    <p>Women in the stereotyped room reported less interest in computer science. In the other room, their interest rose to the level of men’s.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>4</strong><span>experiments with more than 250 students not studying computer science</span></div>
      <div role="listitem"><strong>Equal</strong><span>interest to men’s, for women in the non-stereotyped room</span></div>
      <div role="listitem"><strong>82%</strong><span>of women chose the team whose workroom lacked the stereotyped objects</span></div>
      <div role="listitem"><strong>Belonging</strong><span>explained the drop in women’s interest</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Teams</span>Not who, but what</h2>
    <p>In another study, women chose between two all-female teams that differed only in the objects in their workrooms. Eighty-two percent picked the team without the stereotyped objects. So it was not only about who was in the room. It was what the room said.</p>
    <p>The objects broadcast a narrow image of who does computer science. Women felt less sense of belonging there, and that is what lowered their interest.</p>
  </div>

'''+cls_html('bT','Narrow or wide?','Eight cues in a course: the room, the slides, the examples, the talk. For each, decide: does it narrow the image of who belongs in the field, or widen it? You’ll get feedback after each one.',[('N','Narrows','one kind of person'),('W','Widens','many kinds of people')],'Narrows or widens?','Narrow or wide?','The question is always: what does it say about who does this field?')+'''
  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>One field, one stereotype</h2>
    <p>These were short studies with college students, about one field and one stereotype. Objects are one cue among many. But cues are cheap to change.</p>
  </div>

'''+GRID_HTML+'''
  <div class="col">
    <aside class="box" aria-labelledby="exT">
      <h3 id="exT">For teaching</h3>
      <p>Look at your room, your slides, and your examples with fresh eyes. Who appears in your images and case studies? Vary the names and contexts in your problems. Show the range of people who do your field. And ask a few students what your space says to them.</p>
    </aside>
  </div>
''',
tips_h='Every room sends a message. Choose yours.',
tips='''      <li><b>Fresh eyes</b><span>Room, slides and examples.</span></li>
      <li><b>Vary names and contexts</b><span>In problems and case studies.</span></li>
      <li><b>Ask students</b><span>What does your space say to them?</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/a0016239">Cheryan, S., Plaut, V. C., Davies, P. G., &amp; Steele, C. M. (2009). Ambient belonging: How stereotypical cues impact gender participation in computer science. <i>Journal of Personality and Social Psychology, 97</i>(6), 1045–1060.</a></li>''',
quiz='''[
 {q:'Women in the room with stereotyped objects reported…',o:['Less interest in computer science','More interest','The same interest'],a:0,f:'In the other room, their interest matched men’s.'},
 {q:'Choosing between two all-female teams, 82% of women picked…',o:['The team without the stereotyped objects','The team with them','Neither'],a:0,f:'It was what the room said, not only who was in it.'},
 {q:'What explained the drop in women’s interest?',o:['A lower sense of belonging','Less ability','Less time'],a:0,f:'The objects broadcast a narrow image of who does the field.'}]''',
js=BASE+cls_js("{N:'Narrows',W:'Widens'}",'''[
 ['Every image of a scientist on your slides shows the same kind of person','N','Narrows: students read who belongs from who appears.'],
 ['Word problems that use a wide range of names and everyday contexts','W','Widens: many kinds of people can see themselves in the work.'],
 ['Describing the field as for “natural geniuses” who “just get it”','N','Narrows: brilliance language signals that only a certain kind of person fits.'],
 ['Showing short profiles of people with different backgrounds who use the field','W','Widens: it shows the range of people who do this work.'],
 ['A lab decorated only with one subculture’s memorabilia','N','Narrows: that was the stereotyped room in the study.'],
 ['Asking a few students what the room and materials say to them','W','Widens: you see the space through their eyes, and can change it.'],
 ['In-jokes and references that only some students recognize','N','Narrows: they signal who is already an insider.'],
 ['Case studies drawn from health, art, sport and community problems, not only one industry','W','Widens: the field looks useful to many kinds of people.']]''','Narrows or widens?',r'''
 if(right>=7){title='You can read the room';text=`${right} of 8 right. Images, names, examples and jokes all broadcast who belongs. Cues are cheap to change.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Ask: does this cue show one kind of person, or many?`}
 else{title='Worth another look';text=`${right} of 8 right. Narrowing cues show one kind of person or insider culture. Widening cues show the range of people who do the field.`}''')+grid('''[
 ['Women surveyed in the room with stereotyped computer science objects reported…',['Less interest in computer science','More interest','The same interest'],0,'Cheryan and colleagues, 2009.'],
 ['In the room with neutral objects, women’s interest…',['Rose to the level of men’s','Stayed lower than men’s','Exceeded men’s by far'],0,'The objects alone made the difference.'],
 ['Choosing between two all-female teams, the share of women who picked the one without stereotyped objects was…',['82%','50%','20%'],0,'So it was not only about who was in the room.'],
 ['The drop in women’s interest was explained by…',['A lower sense of belonging','Less ability','Less free time'],0,'The objects broadcast a narrow image of the field.'],
 ['The studies involved…',['Short experiments with college students, about one field','Long-term studies of professionals','School children'],0,'Objects are one cue among many.'],
 ['Changing room cues is…',['Cheap','Expensive','Impossible'],0,'Every room sends a message.']]''','The pattern: what a space displays tells people who belongs there, and that can shift interest. Cues are cheap to change.'))
open('b03/template.html','w').write(page(o))
