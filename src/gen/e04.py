import sys;sys.path.insert(0,'gen')
from common import page
from memjs import *
from dlkit import *
o=sbase('e','Assessment That Teaches',4,'Test Before You Teach: The Pretesting Effect','Test before you teach','A wrong answer, followed by the right one, can be the start of learning.','Test before you teach',
'Here is a strange idea. Test students on material before you teach it, when they will mostly get the answers wrong. Could that help them learn?',
'<span><a href="#tT">Try a pretest</a></span><span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['hip','pfc'],{'pfc':([40,-60],'left'),'hip':([640,770],'left')},'Drawing of the side of the brain with the prefrontal cortex, at the front, which directs attention, and the hippocampus, deep inside, which helps store memories, glowing orange and labelled.')
o.update(css=RECALL_CSS+'''
.pq{width:100%;max-width:560px;text-align:left}
.pq .qq{font:600 clamp(17px,2vw,20px)/1.45 var(--body);color:#fff;margin:0 0 10px}
.pq .ops{display:grid;gap:8px}
.pq .ops button{text-align:left}
.pq .psg{background:#fff;color:#13294B;border-radius:8px;padding:12px 14px;font-size:16px;line-height:1.55}
.pq .psg p{margin:0 0 8px;color:#13294B}
.pq .tag{font:800 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:#FCB316;margin:0 0 6px}
.pq .fb{color:#E9EEF6;margin:8px 0 0}
.pq .fb b.ok{color:#7DD3A8}.pq .fb b.no{color:#FFB38A}''',
body='''  <div class="col lede">
    <p>In 2009, Lindsey Richland, Nate Kornell and Liche Sean Kao gave students questions about a science passage before they read it. Students got almost all of the pretest questions wrong.</p>
    <p>But after reading, they remembered the pretested information better than students who simply read the passage for longer. The benefit held even for the questions they had answered incorrectly.</p>
  </div>

  <section class="night" aria-labelledby="tT">
    <div class="col">
      <h2 class="sec" id="tT"><span class="n">Try it</span>Try a pretest</h2>
      <p>Three questions about a famous case in memory research, before you read about it. Guess; you’re not expected to know. Then read a short passage, and take a final quiz. About 2 minutes.</p>
    </div>
    <div class="wide">
      <div class="lab">
        <div class="screen" id="tScreen"><div class="pq" id="tBox"><p class="qq">Press Start.</p></div></div>
        <div>
          <p class="phase" id="tPhase">Ready</p>
          <p class="mtitle" id="tTitle">Guess first</p>
          <p class="mtext" id="tText" aria-live="polite">A pretest, a short reading, then a final quiz with four questions.</p>
          <div class="mrow"><button class="nbtn" id="tGo">Start</button></div>
        </div>
      </div>
    </div>
  </section>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>Mostly wrong</strong><span>on the pretest, in 2009</span></div>
      <div role="listitem"><strong>Better</strong><span>memory for pretested information after reading</span></div>
      <div role="listitem"><strong>Texts, videos, lectures</strong><span>the effect shows up across materials</span></div>
      <div role="listitem"><strong>One condition</strong><span>a chance to study the correct answers afterwards</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">The review</span>With one key condition</h2>
    <p>A 2023 review by Steven Pan and Shana Carpenter found the pretesting effect across texts, videos and lectures, with one key condition: students need a chance to study the correct answers afterwards.</p>
    <h2 class="sec"><span class="n">Why</span>A wrong guess points the way</h2>
    <p>A pretest tells students what matters, so they pay attention when it comes up. And searching memory, even unsuccessfully, primes the connections that the right answer will attach to. It also changes how students see errors: a mistake on a pretest costs nothing, and becomes the start of learning, not a judgment.</p>
    <h2 class="sec"><span class="n">A caution</span>Ungraded, followed up</h2>
    <p>Pretests should be ungraded, and followed by the material that answers them. Students tend to dislike guessing, so explain why you are doing it. And the clearest benefit is for the pretested information itself, so ask about the ideas that matter most.</p>
  </div>

'''+GRID_HTML+box('Start a unit or a video with two or three questions students can’t yet answer. Don’t grade them. Then teach, and return to the questions at the end. Share this tip with students: guess first, then check the answer.'),
tips_h='A wrong answer, followed by the right one, can be the start of learning.',
tips='''      <li><b>Two or three questions first</b><span>On the ideas that matter most.</span></li>
      <li><b>Don’t grade them</b><span>And explain why you’re asking.</span></li>
      <li><b>Teach, then return</b><span>The answers must follow.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1037/a0016496">Richland, L. E., Kornell, N., &amp; Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? <i>Journal of Experimental Psychology: Applied, 15</i>(3), 243–257.</a></li>
        <li><a href="https://doi.org/10.1007/s10648-023-09814-5">Pan, S. C., &amp; Carpenter, S. K. (2023). Prequestioning and pretesting effects: A review of empirical research, theoretical perspectives, and implications for educational practice. <i>Educational Psychology Review, 35</i>, 97.</a></li>''',
quiz='''[
 {q:'In 2009, students who took a pretest first…',o:['Remembered the pretested information better','Remembered less','Gave up'],a:0,f:'Even for questions they got wrong.'},
 {q:'The key condition for a pretest to help is…',o:['A chance to study the correct answers afterwards','Getting the answers right','A high grade'],a:0,f:'Pan and Carpenter, 2023.'},
 {q:'Pretests should be…',o:['Ungraded','Worth a lot','Secret'],a:0,f:'A mistake should cost nothing.'}]''',
js=BASE+r'''
/* ---------- try a pretest ---------- */
const TQ=[['In what year did H.M. have the surgery that changed his memory?',['1923','1953','1983'],1],
 ['Why was the surgery done?',['To treat severe epilepsy','To remove a tumour','After a car accident'],0],
 ['Which new thing could H.M. still learn after the surgery?',['New facts about current events','A new motor skill, like mirror drawing','The names of new people he met'],1],
 ['Which brain structure was largely removed, on both sides?',['The cerebellum','The hippocampus','The occipital lobe'],1]];
const PRE=[0,1,2];
const PSG=`<p class="tag">Read this</p><div class="psg"><p>In 1953, a young man known for decades as H.M., Henry Molaison, had surgery to treat severe epilepsy. Surgeons removed parts of the temporal lobes on both sides of his brain, including much of the hippocampus.</p><p>His seizures improved, but he could no longer form new long-term memories of facts and events. He could not remember people he met after the surgery, or recent news.</p><p>Yet the psychologist Brenda Milner found he could still learn new motor skills. Practising mirror drawing over several days, he got steadily better, while not remembering he had practised before.</p></div>`;
let tr=null;
function tAsk(i,mode){return new Promise(res=>{const [q,o]=TQ[i];$('tBox').innerHTML=`<p class="tag">${mode}</p><p class="qq">${q}</p><div class="ops" role="group" aria-label="Answers">${o.map((t,j)=>`<button class="nbtn ghost" type="button" data-v="${j}">${t}</button>`).join('')}</div>`;
 $('tBox').querySelector('button').focus();$('tBox').querySelector('.ops').onclick=e=>{const b=e.target.closest('button');if(!b)return;res(+b.dataset.v)}})}
function tNext(label){return new Promise(res=>{const g=$('tGo');g.textContent=label;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.disabled=true;g.textContent='In progress';res()}})}
$('tGo').addEventListener('click',async()=>{if(tr||$('tGo').onclick)return;tr={};const g=$('tGo');g.disabled=true;g.textContent='In progress';
 $('tPhase').textContent='Pretest';$('tTitle').textContent='Guess';$('tText').textContent='No feedback yet. Just guess.';
 const pre=[];for(const i of PRE){pre.push((await tAsk(i,`Pretest ${pre.length+1} of 3`))===TQ[i][2])}
 $('tPhase').textContent='Read';$('tTitle').textContent='Now read';$('tText').textContent='Read the passage. The pretest questions are answered in it.';
 $('tBox').innerHTML=PSG;await tNext('I’ve read it');
 $('tPhase').textContent='Final quiz';$('tTitle').textContent='Final quiz';$('tText').textContent='Four questions: the three you guessed on, and one new one.';
 const fin=[];for(let i=0;i<4;i++){fin.push((await tAsk(i,`Final quiz ${i+1} of 4`))===TQ[i][2])}
 const preR=pre.filter(Boolean).length,finP=fin.slice(0,3).filter(Boolean).length,fixed=pre.map((p,k)=>!p&&fin[k]).filter(Boolean).length;
 $('tBox').innerHTML=`<p class="tag">Your results</p><div class="res wl2" style="width:100%">${barRow('Pretest (guesses)',preR,3,preR+' of 3','#C9D3E3')}${barRow('Same questions, after reading',finP,3,finP+' of 3','#7DD3A8')}${barRow('New question, not pretested',fin[3]?1:0,1,fin[3]?'right':'missed','#FCB316')}</div>`;
 $('tPhase').textContent='What happened';
 let title,text;
 if(fixed>0){title=`${fixed} wrong guess${fixed>1?'es':''} turned right`;text=`You missed ${3-preR} on the pretest, and ${fixed===3-preR?'fixed all of them':`fixed ${fixed}`} after reading. In the 2009 study, pretested facts were remembered better, even ones first answered wrong. One quick demo can’t show the effect, but it shows the steps: guess, read with a purpose, check.`}
 else if(preR===3){title='You knew them already';text='All 3 right on the pretest. In class, most students get pretest questions wrong, and that’s fine: the guess points attention to what matters.'}
 else{title='The answers have to follow';text='Look back at the passage: the answers are all there. A pretest only helps if students then study the correct answers, which Pan and Carpenter call the key condition.'}
 $('tTitle').textContent=title;$('tText').textContent=text;g.textContent='Try again';g.disabled=false;g.focus();tr=null});
'''+grid('''[
 ['In 2009, students took questions about a passage…',['Before reading it','After reading it','Instead of reading it'],0,'Richland, Kornell and Kao.'],
 ['On the pretest, students got…',['Almost all wrong','Almost all right','Half right'],0,'As expected: they hadn’t read it yet.'],
 ['After reading, pretested information was remembered…',['Better than by students who just read longer','Worse','The same'],0,'Even when the pretest answer was wrong.'],
 ['The 2023 review found the effect with…',['Texts, videos and lectures','Texts only','No materials'],0,'Pan and Carpenter.'],
 ['Students tend to…',['Dislike guessing','Love guessing','Not notice'],0,'So explain why you do it.'],
 ['The clearest benefit is for…',['The pretested information itself','Everything in the course','Unrelated topics'],0,'Ask about what matters most.']]''','The pattern: guessing first, then learning the answer, helps memory for what was asked.'))
open('e04/template.html','w').write(page(o))
