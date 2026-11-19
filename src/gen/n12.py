import sys,json;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
def L(mid,text):
    u=f'@@LB:{mid}@@'
    return f'<a href="{u}">{text}</a>' if u else text
MAP=[('n01','Why neuromyths stick','ask what was tested'),('n02','Learning styles','fit the format to the content'),('n03','The 10% myth','the whole brain is in use'),
 ('n04','Left brain, right brain','skills, not sides'),('n05','Brain-training games','practise the real skill'),('n06','The Mozart effect','music for mood, not IQ'),
 ('n07','Sugar highs','notice your expectations'),('n08','Brain Gym','keep the movement, drop the claims'),('n09','Multiple intelligences','representations for the content'),
 ('n10','It’s all over by age three','never too late'),('n11','Digital natives and multitaskers','teach information skills')]
maphtml='\n'.join(f'      <li><b>{i+1}. {L(m,t)}</b><span>{d}</span></li>' for i,(m,t,d) in enumerate(MAP))
QS=['Who is making the claim, and are they selling something?','Was it tested against a comparison group, not just before and after?','Did it change the outcome you care about, like learning, not just a game score or a feeling?','Has anyone else replicated it?','Take out the brain language. Does the claim still make sense, with evidence for it?']
qhtml='\n'.join(f'''        <fieldset><legend>Question {i+1}</legend><p class="qx">{q}</p>
          <label><input type="radio" name="q{i}" value="y">{['Independent, not selling','Yes, a comparison group','Yes, a real outcome','Yes, replicated','Yes, it still holds'][i]}</label>
          <label><input type="radio" name="q{i}" value="n">{['Selling it, or can’t tell','No comparison, or can’t tell','No, or can’t tell','No, or can’t tell','No, it falls apart'][i]}</label></fieldset>''' for i,q in enumerate(QS))
o=sbase('n','Neuromyths',12,'Spotting the Next Myth: Five Questions','Spotting the next myth','Be most careful when a claim sounds most scientific.','Spotting the next myth',
'Over this series, we have looked at eleven popular ideas about the brain. Most began with something real. Most were stretched. So how do you spot the next one?',
'<span><a href="#bT">Which question catches it?</a></span><span><a href="#qT">Check a claim</a></span>')
o['hero_aria'],o['hero_js']=hero(['pfc'],{'pfc':([40,-60],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which helps us weigh evidence, glowing orange and labelled.')
o.update(css=RECALL_CSS+CLS_CSS+'''
.amap{list-style:none;padding:0;margin:14px 0 6px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 18px}
@media (max-width:640px){.amap{grid-template-columns:1fr}}
.amap li{border-left:3px solid #FF5F05;padding:4px 0 4px 10px}
.amap b{display:block;color:#13294B}.amap span{color:#3A4E72;font-size:16px}
.q5{counter-reset:q;list-style:none;padding:0;margin:14px 0}
.q5 li{counter-increment:q;position:relative;padding:8px 0 8px 46px;border-top:1px solid #C9D3E3}
.q5 li::before{content:counter(q);position:absolute;left:0;top:6px;width:32px;height:32px;border-radius:50%;background:#13294B;color:#fff;font:800 16px/32px var(--body);text-align:center}
.plan fieldset{border:1px solid #3A4E72;border-radius:10px;padding:10px 14px;margin:0 0 12px}
.plan legend{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;padding:0 6px}
.plan .qx{color:#fff;font-weight:600;margin:0 0 4px}
.plan label{display:flex;gap:10px;align-items:flex-start;padding:5px 0;color:#E9EEF6;font-size:17px;line-height:1.4;cursor:pointer}
.plan input[type=radio]{margin-top:4px;width:18px;height:18px;accent-color:#FCB316;flex:none}
.plan .cl{display:block;color:#C9D3E3;font:600 14px var(--body);margin:0 0 12px}
.plan .cl input{display:block;width:100%;box-sizing:border-box;margin-top:4px;min-height:44px;font:500 17px var(--body);border-radius:8px;border:2px solid #8FA3C2;background:#0F2240;color:#fff;padding:0 10px}
.plan .cl input:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.pout{background:#0F2240;border:1px solid #3A4E72;border-radius:10px;padding:12px 14px;color:#E9EEF6;font-size:17px;line-height:1.5;margin:10px 0}
.pout[hidden]{display:none}
.pout ul{margin:6px 0 0;padding-left:22px}''',
body='''  <div class="col lede">
    <p>Start with a warning about ourselves. In 2008, Deena Weisberg and colleagues gave people good and bad explanations of psychology findings. Adding irrelevant brain language made bad explanations seem more satisfying to non-experts. A 2024 replication found the effect real, but smaller.</p>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The tool</span>Five questions</h2>
    <ol class="q5">
'''+'\n'.join(f'      <li>{q}</li>' for q in QS)+'''
    </ol>
    <p>Run the myths through these questions, and most fail fast. Learning styles fails question two. Brain games fail question three. The Mozart effect fails question four. Brain Gym fails questions one and five.</p>
  </div>

'''+cls_html('bT','Which question catches it?','Eight claims. For each, pick the one question from the five that catches it most clearly. You’ll get feedback after each one.',[('1','Q1: Seller?',''),('2','Q2: Comparison?',''),('3','Q3: Outcome?',''),('4','Q4: Replicated?',''),('5','Q5: Without brain words?','')],'Which question catches it?','Which question catches it?','The question is always: what is the weakest link between the claim and the evidence?')+'''
  <section class="night" aria-labelledby="qT">
    <div class="col">
      <h2 class="sec" id="qT"><span class="n">Try it</span>Check a claim</h2>
      <p>Bring a claim you’ve met: from a workshop, a product, a post. Answer the five questions honestly, and see where it stands. Nothing you enter leaves this page.</p>
      <form class="plan" id="qForm">
        <label class="cl" for="qClaim">The claim<input id="qClaim" type="text" maxlength="160" placeholder="For example: this app boosts focus by training your brain"></label>
'''+qhtml+'''
        <div class="mrow"><button class="nbtn" type="submit">Check it</button></div>
      </form>
      <div class="pout" id="qOut" hidden aria-live="polite"></div>
    </div>
  </section>

  <div class="col">
    <h2 class="sec"><span class="n">A caution</span>Skepticism is not cynicism</h2>
    <p>Real findings exist, and this series has relied on them. The aim is not to doubt everything, but to ask for the evidence that matches the claim.</p>
    <h2 class="sec"><span class="n">The map</span>Eleven myths</h2>
    <ul class="amap">
'''+maphtml+'''
    </ul>
  </div>
'''+box('Keep these five questions next to any new teaching idea. Share your checking process with students, so they learn it too. Share this tip with students: be most careful when a claim sounds most scientific.'),
tips_h='Curiosity about the brain is good. Pair it with a habit of asking how we know.',
tips='''      <li><b>Five questions</b><span>Next to any new teaching idea.</span></li>
      <li><b>Share your checking</b><span>So students learn it too.</span></li>
      <li><b>Skeptical, not cynical</b><span>Ask for matching evidence.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1162/jocn.2008.20040">Weisberg, D. S., Keil, F. C., Goodstein, J., Rawson, E., &amp; Gray, J. R. (2008). The seductive allure of neuroscience explanations. <i>Journal of Cognitive Neuroscience, 20</i>(3), 470–477.</a></li>
        <li><a href="https://doi.org/10.1098/rsos.241120">Väth, P. A., von Petersdorff, J., Neumann, C., Mundry, R., &amp; Fischer, J. (2024). Replicating the ‘seductive allure of neuroscience explanations’ effect in a classroom experiment and an online study. <i>Royal Society Open Science, 11</i>(12), 241120.</a></li>
        <li>The studies behind each myth are listed on each topic’s page.</li>''',
quiz='''[
 {q:'Adding irrelevant brain language made bad explanations seem…',o:['More satisfying to non-experts','Less satisfying','No different, in 2008'],a:0,f:'A 2024 replication found it real, but smaller.'},
 {q:'Brain games fail which question most clearly?',o:['Q3: did it change the outcome you care about?','Q1: who is selling it?','Q4: replicated?'],a:0,f:'Better at the game, not at everything.'},
 {q:'The aim of the five questions is…',o:['To ask for evidence that matches the claim','To doubt everything','To reject all brain research'],a:0,f:'Skepticism is not cynicism.'}]''',
js=BASE+cls_js("{'1':'Q1: Seller?','2':'Q2: Comparison?','3':'Q3: Outcome?','4':'Q4: Replicated?','5':'Q5: Without brain words?'}",'''[
 ['Learning styles: “students learn better when teaching matches their style”','2','Q2: very few studies used the comparison design that could test it, and those that did found virtually no support.'],
 ['Brain-training games: “ten minutes a day makes you smarter”','3','Q3: players improved on the games, not on everyday thinking or school outcomes.'],
 ['The Mozart effect: “Mozart makes you smarter”','4','Q4: other labs found it hard to replicate.'],
 ['“Our app’s own study shows it works, and it’s only $9.99 a month”','1','Q1: the people making the claim are selling it. Look for independent studies.'],
 ['“Scores rose after a term with our method” (no comparison class)','2','Q2: scores often rise over a term anyway. Without a comparison group, you can’t tell.'],
 ['“Students said they enjoyed it and felt they learned more”','3','Q3: feelings aren’t learning. What happened on a test of the outcome you care about?'],
 ['“One small study last year found a big effect”','4','Q4: one small study is a start. Has anyone else replicated it?'],
 ['“Activates the hippocampus for deeper, whole-brain learning”','5','Q5: take out the brain words, and there’s no tested claim about learning left.']]''','Which question catches it?',r'''
 if(right>=7){title='You have the toolkit';text=`${right} of 8 right. Seller, comparison, outcome, replication, and the claim without brain words.`}
 else if(right>=5){title='Mostly there';text=`${right} of 8 right. You missed ${missed}. Look for the weakest link between the claim and the evidence.`}
 else{title='Worth another look';text=`${right} of 8 right. Each question catches a different weak link: who’s selling, no comparison, the wrong outcome, no replication, or brain words with nothing underneath.`}''')+r'''
/* ---------- check a claim ---------- */
const QN=['the people making it are selling it, or you can’t tell.','no comparison group.','no change shown in an outcome you care about.','not replicated.','it falls apart without the brain language.'];
$('qForm').addEventListener('submit',e=>{e.preventDefault();const a=[0,1,2,3,4].map(i=>{const c=document.querySelector(`input[name="q${i}"]:checked`);return c?c.value:null});
 const out=$('qOut');const cl=$('qClaim').value.trim();const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const miss=a.map((v,i)=>v?null:i+1).filter(Boolean);
 if(miss.length){out.innerHTML=`<b>Answer every question first.</b> Still to answer: question${miss.length>1?'s':''} ${miss.join(', ')}.`;out.hidden=false;return}
 const fails=a.map((v,i)=>v==='n'?i:null).filter(v=>v!==null);
 let h=cl?`<b>“${esc(cl)}”</b><br>`:'';
 if(!fails.length)h+='<b>Passes all five.</b> That doesn’t make it certain, but it has the kind of evidence that matches the claim. Keep an eye on new studies.';
 else if(fails.length===1)h+=`<b>One weak link.</b> It fails question ${fails[0]+1}: ${QN[fails[0]]} Ask for that evidence before you adopt it.`;
 else h+=`<b>${fails.length} weak links.</b> It fails:<ul>${fails.map(i=>`<li>Question ${i+1}: ${QN[i]}</li>`).join('')}</ul>Treat it as a myth until the evidence catches up.`;
 out.innerHTML=h;out.hidden=false});
''')
open('n12/template.html','w').write(page(o))
