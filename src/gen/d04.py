import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(4,'How Long Should a Video Be? Engagement and Segmenting','How long should a video be?','Short is not shallow. Short is focused.','How long should a video be?',
'You record a 50-minute lecture and post it online. How much of it will students actually watch? One of the largest studies of educational video suggests: less than you might hope.',
'<span><a href="#vT">Split a lecture</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc'],{'pfc':([40,-60],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which helps sustain attention, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.vp{display:grid;gap:10px;width:100%;max-width:560px}
.vp .row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.vp label{display:block;font:600 14px var(--body);color:#C9D3E3}
.vp select{display:block;width:100%;margin-top:4px;min-height:42px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 6px}
.vp select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.vlist{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:6px;width:100%;max-width:560px;text-align:left}
.vlist li{display:grid;grid-template-columns:minmax(0,9.5em) minmax(0,1fr);gap:10px;align-items:center;color:#E9EEF6;font-size:16px}
.vlist .vt{display:block;height:14px;border-radius:7px;background:#1D355C}
.vlist .vb{display:block;height:14px;border-radius:7px;background:#7DD3A8}
.vlist .vb.long{background:#FFB38A}
.vlist .q{color:#FCB316;font-size:14px;grid-column:1/-1;padding-left:8px}
.say{color:#C9D3E3;font-size:15px;margin:6px 0 0}
#vOut{width:100%;max-width:560px}''',
body='''  <div class="col lede">
    <p>In 2014, Philip Guo, Juho Kim and Rob Rubin analyzed 6.9 million video-watching sessions from four edX courses: 862 videos and almost 128,000 students.</p>
    <p>Their clearest finding: shorter videos were much more engaging. Engagement dropped sharply after about six minutes. For longer videos, many students stopped well before the end.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>6.9 million</strong><span>video-watching sessions</span></div>
      <div role="listitem"><strong>862</strong><span>videos from four edX courses</span></div>
      <div role="listitem"><strong>~128,000</strong><span>students</span></div>
      <div role="listitem"><strong>~6 minutes</strong><span>after which engagement dropped sharply</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">Style</span>What held attention</h2>
    <p>Style mattered too. Videos that mixed slides with the instructor’s face were more engaging than slides alone. Hand-drawn tablet explanations held attention. And instructors who spoke fairly fast, with enthusiasm, kept students watching. Even well-produced recordings of classroom lectures were less engaging than videos made for online viewing.</p>
    <h2 class="sec"><span class="n">Segmenting</span>Short videos are segments</h2>
    <p>This connects to the segmenting principle: people learn better when a lesson is broken into learner-paced parts. Short videos are segments, with a natural pause between them.</p>
  </div>

  <section class="night" aria-labelledby="vT">
    <div class="col">
      <h2 class="sec" id="vT"><span class="n">Try it</span>Split a lecture</h2>
      <p>Pick the length of a recorded lecture and how many main ideas it covers. The page splits it into one video per idea, and flags any that run past about six minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="vScreen">
          <form class="vp" id="vF"><div class="row2">
            <label for="vL">Lecture length<select id="vL"></select></label>
            <label for="vI">Main ideas<select id="vI"></select></label></div>
          </form>
          <div id="vOut"></div>
        </div>
        <div>
          <p class="phase">Your plan</p>
          <p class="mtitle" id="vTitle"></p>
          <p class="mtext" id="vText" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Watching is not learning</h2>
    <p>This study measured watching, not learning. It came from massive open online courses, whose students differ from those in a for-credit class. Still, the pattern fits what we know about attention.</p>
  </div>

'''+GRID_HTML+box('Plan each video around one idea, and aim for six minutes or less. Split long lectures into a series of short ones, with a question or activity between them. Show your face at key moments, and talk to students, not to the slides. Share this tip with students: watch in short, focused chunks.'),
tips_h='Short is not shallow. Short is focused.',
tips='''      <li><b>One idea per video</b><span>Six minutes or less.</span></li>
      <li><b>A question between videos</b><span>A natural pause.</span></li>
      <li><b>Your face, your energy</b><span>Talk to students, not the slides.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1145/2556325.2566239">Guo, P. J., Kim, J., &amp; Rubin, R. (2014). How video production affects student engagement: An empirical study of MOOC videos. <i>Proceedings of the First ACM Conference on Learning @ Scale</i>, 41–50.</a></li>
        <li>Mayer, R. E. (2021). <i>Multimedia learning</i> (3rd ed.). Cambridge University Press.</li>''',
quiz='''[
 {q:'Engagement with edX videos dropped sharply after about…',o:['6 minutes','20 minutes','1 minute'],a:0,f:'Guo, Kim and Rubin, 2014.'},
 {q:'Recordings of classroom lectures were…',o:['Less engaging than videos made for online viewing','The most engaging','Just as engaging'],a:0,f:'Even well-produced ones.'},
 {q:'The study measured…',o:['Watching, not learning','Exam scores','Grades'],a:0,f:'A reason for caution.'}]''',
js=BASE+r'''
/* ---------- split a lecture ---------- */
$('vL').innerHTML=[10,15,20,30,40,50,60,75,90].map(m=>`<option value="${m}"${m===50?' selected':''}>${m} minutes</option>`).join('');
$('vI').innerHTML=[1,2,3,4,5,6,7,8,9,10,12,15].map(m=>`<option value="${m}"${m===4?' selected':''}>${m} idea${m>1?'s':''}</option>`).join('');
function vUpd(){const L=+$('vL').value,I=+$('vI').value,per=L/I,long=per>6.5,mx=Math.max(per,6);
 const pr=Math.round(per*10)/10,txt=Number.isInteger(pr)?pr:pr.toFixed(1);
 const show=Math.min(I,8);let h='<ol class="vlist" aria-label="Your videos">';
 for(let i=0;i<show;i++)h+=`<li><span>Video ${i+1} · ${txt} min</span><span class="vt" aria-hidden="true"><span class="vb${long?' long':''}" style="width:${Math.max(6,Math.round(per/Math.max(mx,12)*100))}%"></span></span>${i<show-1?'<span class="q">then a question</span>':''}</li>`;
 h+='</ol>'+(I>show?`<p class="say">…and ${I-show} more.</p>`:'');$('vOut').innerHTML=h;
 let title,text;
 if(I===1&&L>6.5){title='One long video';text=`One ${L}-minute video on one idea. In the edX data, engagement dropped sharply after about six minutes. Can the idea be split into parts, each with its own short video?`}
 else if(long){title='Still long per video';text=`${I} videos of about ${txt} minutes each. That’s past the six-minute mark where engagement dropped. Split the bigger ideas, or trim what doesn’t explain (topic 2).`}
 else if(per<2){title='Very short videos';text=`${I} videos of about ${txt} minutes each. Short is fine, but check each one has a whole idea, and a question to go with it.`}
 else{title='Focused segments';text=`${I} videos of about ${txt} minutes each, one idea per video, with a question between them. That fits both the engagement data and the segmenting principle.`}
 $('vTitle').textContent=title;$('vText').textContent=text}
$('vF').addEventListener('change',vUpd);vUpd();
'''+grid('''[
 ['The 2014 study analyzed about how many video-watching sessions?',['6.9 million','69,000','690'],0,'Across four edX courses.'],
 ['Engagement dropped sharply after about…',['6 minutes','15 minutes','30 minutes'],0,'Shorter videos were much more engaging.'],
 ['Slides with the instructor’s face, compared with slides alone, were…',['More engaging','Less engaging','The same'],0,'Showing a person helped.'],
 ['Hand-drawn tablet explanations…',['Held attention','Lost attention quickly','Were not studied'],0,'Khan-style drawings.'],
 ['Recordings of classroom lectures were…',['Less engaging than videos made for online','More engaging','Not included'],0,'Even well-produced ones.'],
 ['This study measured…',['Watching, not learning','Exam scores','Course grades'],0,'And the students were in MOOCs, not for-credit classes.']]''','The pattern: short, personal videos built for the screen hold attention best.'))
open('d04/template.html','w').write(page(o))
