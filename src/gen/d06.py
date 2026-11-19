import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=base(6,'Speed-Watching: Lecture Videos at Double Speed','Speed-watching','Faster is fine. Faster with practice is better.','Speed-watching',
'Many students watch lecture videos at one and a half or double speed. Many instructors wince. Are students learning less?',
'<span><a href="#eT">Predict the scores</a></span><span><a href="#kT">Where does the time go?</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','hip'],{'tem':([600,770],'left'),'hip':([900,-60],'right')},'Drawing of the side of the brain with the temporal lobe, at the side, where speech is processed, and the hippocampus, deep inside, which helps form memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+PRED_CSS+'''
.kp{display:grid;gap:10px;width:100%;max-width:560px}
.kp .row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.kp label{display:block;font:600 14px var(--body);color:#C9D3E3}
.kp select{display:block;width:100%;margin-top:4px;min-height:42px;font:600 16px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 6px}
.kp select:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
#kRes{width:100%;max-width:560px}''',
body='''  <div class="col lede">
    <p>In a 2022 study at UCLA, Dillon Murphy, Alan Castel and colleagues tested it. Students watched short lecture videos at normal speed, one and a half times, double, or two and a half times speed, then took a 40-question test.</p>
    <p>About 85% of the students they surveyed said they already speed-watch.</p>
  </div>

'''+pred_html('eT','Predict the scores','Three quick predictions about the study, then see the results. About 1 minute.','Normal speed vs faster','Each group took the same 40-question test right after watching.')+'''
  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>~85%</strong><span>of students surveyed already speed-watch</span></div>
      <div role="listitem"><strong>~26 vs ~25</strong><span>of 40 correct, at normal and double speed</span></div>
      <div role="listitem"><strong>~22</strong><span>of 40 at two and a half times speed</span></div>
      <div role="listitem"><strong>Twice at 2×</strong><span>shortly before the test beat once at 1× a week earlier</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Short videos, lab tests</h2>
    <p>These were short videos and lab tests. The authors warn that faster playback may not suit complex material, and they did not recommend speeding up simply to save time. The real question is what students do with the time they save.</p>
  </div>

  <section class="night" aria-labelledby="kT">
    <div class="col">
      <h2 class="sec" id="kT"><span class="n">Try it</span>Where does the time go?</h2>
      <p>Pick how many minutes of lecture video a week, and a playback speed. See how much time it saves, and what that time could buy.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="kScreen">
          <form class="kp" id="kF"><div class="row2">
            <label for="kM">Video per week<select id="kM"></select></label>
            <label for="kS">Playback speed<select id="kS"></select></label></div>
          </form>
          <div id="kRes"></div>
        </div>
        <div>
          <p class="phase">Your week</p>
          <p class="mtitle" id="kTitle"></p>
          <p class="mtext" id="kText" aria-live="polite"></p>
        </div>
      </div>
    </div>
  </section>

'''+GRID_HTML+box('Don’t ban speed controls. Instead, tell students the evidence: up to double speed is usually fine, slow down for hard parts, and use the saved time for practice. Keep your own speech clear, so faster playback stays understandable. Share this tip with students: if you speed up, spend the saved time on practice.'),
tips_h='Faster is fine. Faster with practice is better.',
tips='''      <li><b>Up to 2× is usually fine</b><span>Slow down for hard parts.</span></li>
      <li><b>Spend the saved time on practice</b><span>Quiz yourself.</span></li>
      <li><b>Speak clearly</b><span>So fast playback still works.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1002/acp.3899">Murphy, D. H., Hoover, K. M., Agadzhanyan, K., Kuehn, J. C., &amp; Castel, A. D. (2022). Learning in double time: The effect of lecture video speed on immediate and delayed comprehension. <i>Applied Cognitive Psychology, 36</i>(1).</a></li>''',
quiz='''[
 {q:'Compared with normal speed, double speed scores were…',o:['About the same','Much lower','Much higher'],a:0,f:'About 26 vs 25 of 40.'},
 {q:'Scores clearly dropped at…',o:['2.5× speed','1.5× speed','Never'],a:0,f:'About 22 of 40.'},
 {q:'The best use of saved time is…',o:['Practice, like quizzing yourself','Nothing','Watching more videos at 3×'],a:0,f:'The time is only as good as what you do with it.'}]''',
js=BASE+pred_js('''[
 ['Normal speed averaged about 26 of 40. Double speed averaged about…',['25','18','12'],0,'About 25: almost the same.'],
 ['At two and a half times speed, scores were…',['About the same again','Lower: about 22','Higher: about 30'],1,'Lower: about 22 of 40. Costs were minimal up to double speed, and performance declined beyond it.'],
 ['Which did better on a test a week later?',['Watching once at normal speed, a week before','Watching twice at double speed, the second time shortly before the test','No difference'],1,'Watching twice at double speed, the second time shortly before the test.']]''',
'''<p class="gh">Immediate test, of 40 questions</p>${barRow('Normal speed',26,40,'~26','#C9D3E3')}${barRow('Double speed',25,40,'~25','#7DD3A8')}${barRow('2.5× speed',22,40,'~22','#FFB38A')}''',
r''' if(n===3){title='You saw it coming';text='All 3 right. Up to double speed, costs were minimal. Beyond it, scores fell. And a second, fast viewing close to the test beat one slow viewing long before.'}
 else if(!got[0]){title='Double speed held up';text=`You got ${n} of 3. Many instructors expect double speed to hurt. In this study, scores at double speed were almost the same as at normal speed.`}
 else{title='There is a limit, and a twist';text=`You got ${n} of 3. Scores fell beyond double speed. And how students spend the time matters: a quick second viewing near the test helped.`}''')+r'''
/* ---------- where does the time go? ---------- */
$('kM').innerHTML=[30,60,90,120,180,240].map(m=>`<option value="${m}"${m===120?' selected':''}>${m} minutes</option>`).join('');
$('kS').innerHTML=[[1,'Normal (1×)'],[1.25,'1.25×'],[1.5,'1.5×'],[2,'Double (2×)'],[2.5,'2.5×']].map(([v,t])=>`<option value="${v}"${v===1.5?' selected':''}>${t}</option>`).join('');
function kUpd(){const M=+$('kM').value,S=+$('kS').value,W=Math.round(M/S),sav=M-W;
 $('kRes').innerHTML=`<div class="res wl2">${barRow('Time watching',W,M,W+' min','#C9D3E3')}${barRow('Time saved',sav,M,sav+' min','#7DD3A8')}</div>`;
 let title,text;
 if(S===1){title='No time saved';text=`${M} minutes of watching. That’s fine. If you have time for one thing more, make it a short self-quiz after each video.`}
 else if(S>2){title='Past the limit';text=`You save ${sav} minutes, but at 2.5× scores fell in the study. Drop back to double speed or less, especially for hard material.`}
 else{const q=Math.floor(sav/10);title=`${sav} minutes saved`;text=`Spend them on practice: that’s ${q>=1?`about ${q} ten-minute self-quiz${q>1?'zes':''}`:'a short self-quiz'}, or a second fast viewing shortly before the test. Spent on nothing, it’s just a faster way to watch.`}
 $('kTitle').textContent=title;$('kText').textContent=text}
$('kF').addEventListener('change',kUpd);kUpd();
'''+grid('''[
 ['About what share of the students surveyed already speed-watch?',['85%','15%','50%'],0,'Murphy and colleagues, 2022.'],
 ['At 1.5×, scores were…',['About the same as normal speed','Much lower','Much higher'],0,'Costs were minimal up to double speed.'],
 ['Did the authors recommend speeding up just to save time?',['No','Yes','They didn’t say'],0,'The point is what you do with the time.'],
 ['Faster playback may not suit…',['Complex material','Short videos','Any videos'],0,'The authors’ own caution.'],
 ['The videos in the study were…',['Short lecture videos','Full-length courses','Silent'],0,'Tested in the lab.'],
 ['Watching twice at double speed shortly before the test, compared with once at normal speed a week earlier, did…',['Better','Worse','The same'],0,'Timing of review matters.']]''','The pattern: up to double speed costs little; what matters is how students spend the time saved.'))
open('d06/template.html','w').write(page(o))
