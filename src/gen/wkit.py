"""Language and Learning (w01-w12): same format as Perception, plus a generic case runner."""
import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
def wbase(n,title,h1,em,dek):
    return pbase(n,title,h1,em,dek,'<span><a href="#brT">Predict the findings</a></span>',prefix='w',series='Language and Learning')
TEXT_SCREEN='''            <p id="csS" style="font:600 clamp(19px,2.4vw,22px)/1.45 var(--body);color:#fff;max-width:40ch;margin:0;min-height:5.8em" aria-live="polite">Press Start.</p>
            <p class="prog" id="csP"></p>'''
def cases_js(cases,opts,question,summary):
    """cases: JS array [text, correctIndex, feedback, (optional options array)]. opts: JS array of default options.
    summary: JS using right,n to set title,text."""
    return r'''
/* ---------- cases ---------- */
const CASES='''+cases+''',OPTS='''+opts+r''';
startRun(async()=>{const order=shuf([...CASES]);let right=0;const n=order.length;
 for(let i=0;i<n;i++){const [t,k,ex,o]=order[i];$('csS').innerHTML=t;$('csP').textContent=`${i+1} of ${n}`;
  say(`${i+1} of ${n}`,'''+repr(question)+r''','');
  const a=await ask(o||OPTS,'''+repr(question)+r''');if(!RUN)return;mark(k,a);if(a===k)right++;
  say(null,null,(a===k?'<b class="ok">Right.</b> ':'<b class="no">Not quite.</b> ')+ex);
  if(i<n-1){await nextBtn('Next');if(!RUN)return;hideCh()}}
 $('csS').textContent='Done.';$('csP').textContent='';let title,text;
'''+summary+r'''
 say('Your results',title,text)});
'''
STD_SUM=r''' title=`${right} of ${n} right`;text=right>=n-1?'You have the idea. The sections below explain the evidence.':right>=n/2?'Mostly there. The sections below explain the ones you missed.':'Worth another look. The sections below explain each one.';'''
