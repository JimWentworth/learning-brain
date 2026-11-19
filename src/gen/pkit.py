"""Shared bits for the Perception pages (p01-p12): no video, the activity comes first,
with 'For students' and 'For instructors' tabs."""
import re,sys
sys.path.insert(0,'gen')
from common import page as _page

SERIES='Perception'

def pbase(n,title,h1,em,dek,jumps='',prefix='p',series=None):
    return dict(id=f'{prefix}{n:02d}',n=str(n),label=f'The Learning Brain · {series or SERIES} · Topic {n}',
        title=title,h1=h1,em=em,read='7',mins='',vtitle='',dek=dek,jumps=jumps)

def hero(regions,labs,aria):
    s=''.join(f"BR.R.{k}.lab=[{x},{y}];BR.R.{k}.al='{a}';" for k,((x,y),a) in labs.items())
    lt='{'+','.join(f'{k}:{0.8+0.2*i:.1f}' for i,k in enumerate(regions))+'}'
    r=','.join(f"'{k}'" for k in regions)
    return aria, s+f"\nstage('heroBrain',({{W,H,t}})=>{{brainDraw({{cx:W*0.5,cy:H*0.46,s:fitS(W,H,1.32),t,active:[{r}],labels:[{r}],labelT:{lt},deep:0.5,draw:RM?1:ez(t/1.6),glow:RM?1:0.75+0.25*Math.sin(t*1.6),labSize:Math.max(16,Math.round(15*W/560))}})}});"

TABS_CSS='''
.ptabs{display:flex;gap:6px;margin:18px 0 0;border-bottom:2px solid var(--night-line);flex-wrap:wrap}
.ptabs button{appearance:none;background:transparent;border:0;border-bottom:4px solid transparent;margin-bottom:-2px;color:#C9D3E3;font:700 18px var(--body);padding:10px 16px 8px;cursor:pointer;min-height:48px}
.ptabs button[aria-selected="true"]{color:#fff;border-bottom-color:var(--orange)}
.ptabs button:hover{color:#fff}
.ptabs button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.ppanel{padding-top:6px}
.ppanel:focus-visible{outline:3px solid #FCB316;outline-offset:4px}
.ppanel[hidden]{display:none}
.iguide{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:28px;margin-top:22px}
@media (max-width:760px){.iguide{grid-template-columns:minmax(0,1fr)}}
.iguide h3{font:800 15px var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--orange);margin:0 0 8px}
.iguide ol,.iguide ul{margin:0 0 18px;padding-left:1.3em;color:#E9EEF6;font-size:17px;line-height:1.5}
.iguide li{margin:0 0 8px}
.iguide p{color:#E9EEF6;font-size:17px;line-height:1.5;margin:0 0 16px}
.iguide .itime{display:inline-block;background:#1B2E50;border:1px solid var(--night-line);border-radius:16px;padding:3px 12px;font-weight:700;color:#fff;margin:0 0 14px}
.icard{background:var(--night-2);border:1px solid var(--night-line);border-radius:8px;padding:18px 20px}
.pscreen{position:relative;background:var(--night-2);border:1px solid var(--night-line);border-radius:8px;min-height:340px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:18px}
.pscreen:focus-visible{outline:3px solid #FCB316;outline-offset:3px}
.pchoices{display:flex;gap:10px;flex-wrap:wrap}
.pchoices[hidden]{display:none}
.pchoices button{appearance:none;min-height:48px;padding:6px 18px;text-align:left;border-radius:12px;border:2px solid #8FA3C2;background:#13294B;color:#fff;font:700 17px/1.2 var(--body);cursor:pointer}
.pchoices button:focus-visible{outline:3px solid #FCB316;outline-offset:2px}
.pchoices button.ok{border-color:#7DD3A8;background:#173B33}.pchoices button.no{border-color:#FFB38A;background:#3B2420}
.pchoices button:disabled{cursor:default}
.mtext b.ok{color:#7DD3A8}.mtext b.no{color:#FFB38A}
.nbtn.ghost{background:transparent;color:#fff;border:2px solid #8FA3C2}
.nbtn:disabled{background:#3A4E72;color:#C9D3E3;cursor:default}
.res .row{display:grid;grid-template-columns:150px minmax(0,1fr) 90px;gap:10px;align-items:center;font-size:16px;color:#E9EEF6;margin:6px 0}
@media (max-width:520px){.res .row{grid-template-columns:100px minmax(0,1fr) 76px}}
.res .bar{height:14px;background:#1B2E50;border-radius:7px;overflow:hidden}.res .bar i{display:block;height:100%;border-radius:7px}
.res b{text-align:right;font-variant-numeric:tabular-nums}
'''

TABS_JS=r'''
/* ---------- tabs ---------- */
(function(){const tl=document.querySelector('.ptabs');if(!tl)return;const tabs=[...tl.querySelectorAll('[role=tab]')];
 function sel(t,focus){tabs.forEach(b=>{const on=b===t;b.setAttribute('aria-selected',on);b.tabIndex=on?0:-1;$(b.getAttribute('aria-controls')).hidden=!on});if(focus)t.focus()}
 tabs.forEach((b,i)=>{b.addEventListener('click',()=>sel(b));b.addEventListener('keydown',e=>{let j=null;if(e.key==='ArrowRight')j=(i+1)%tabs.length;else if(e.key==='ArrowLeft')j=(i-1+tabs.length)%tabs.length;else if(e.key==='Home')j=0;else if(e.key==='End')j=tabs.length-1;if(j!==null){e.preventDefault();sel(tabs[j],true)}})})})();
const barRow=(l,val,mx,lab,c)=>`<div class="row"><span>${l}</span><div class="bar"><i style="width:${mx?Math.min(100,val/mx*100):0}%;background:${c}"></i></div><b>${lab}</b></div>`;
const sw=ms=>new Promise(r=>setTimeout(r,ms));
const shuf=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
'''

def tabs(title,intro,student,time,steps,ask,connect,note=''):
    """student: HTML of the student activity. steps/ask: lists of strings."""
    st=''.join(f'<li>{s}</li>' for s in steps)
    ak=''.join(f'<li>{s}</li>' for s in ask)
    nt=f'<h3>Good to know</h3><p>{note}</p>' if note else ''
    return f'''  <section class="night" aria-labelledby="tryT" style="margin-top:0">
    <div class="col">
      <h2 class="sec" id="tryT"><span class="n">Try it first</span>{title}</h2>
      <p>{intro}</p>
    </div>
    <div class="wide">
      <div class="ptabs" role="tablist" aria-label="Versions of this activity">
        <button type="button" role="tab" id="tabS" aria-controls="panS" aria-selected="true">For students</button>
        <button type="button" role="tab" id="tabI" aria-controls="panI" aria-selected="false" tabindex="-1">For instructors</button>
      </div>
      <div class="ppanel" role="tabpanel" id="panS" aria-labelledby="tabS" tabindex="0">
{student}
      </div>
      <div class="ppanel" role="tabpanel" id="panI" aria-labelledby="tabI" tabindex="0" hidden>
        <div class="iguide">
          <div>
            <span class="itime">{time}</span>
            <h3>Run it in class</h3>
            <ol>{st}</ol>
          </div>
          <div class="icard">
            <h3>Ask the room</h3>
            <ul>{ak}</ul>
            <h3>Connect it to your course</h3>
            <p>{connect}</p>
            {nt}
          </div>
        </div>
      </div>
    </div>
  </section>
'''

def lab(screen,phase,mtitle,mtext,go='Start',extra=''):
    """Standard two-column activity: a screen on the left, a side panel with ids sPhase/sTitle/sText/sRes/sGo."""
    return f'''        <div class="lab">
          <div class="pscreen" id="sScreen">
{screen}
          </div>
          <div>
            <p class="phase" id="sPhase">{phase}</p>
            <p class="mtitle" id="sTitle">{mtitle}</p>
            <p class="mtext" id="sText" aria-live="polite">{mtext}</p>
            <div class="pchoices" id="sCh" role="group" aria-label="Your answer" hidden></div>
            <div id="sRes"></div>
            <div class="mrow"><button class="nbtn" id="sGo" type="button">{go}</button>{extra}</div>
          </div>
        </div>'''

# A small async helper set for the side panel: ask(options) -> index; next(label) waits for the button.
PANEL_JS=r'''
let RUN=null;
function ask(opts,lab){return new Promise(res=>{const c=$('sCh');c.setAttribute('aria-label',lab||'Your answer');c.innerHTML=opts.map((t,j)=>`<button type="button" data-v="${j}">${t}</button>`).join('');c.hidden=false;RUN.res=res;c.querySelector('button').focus()})}
$('sCh').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||!RUN||!RUN.res||b.disabled)return;const r=RUN.res;RUN.res=null;$('sCh').querySelectorAll('button').forEach(x=>x.disabled=true);r(+b.dataset.v)});
function mark(right,chosen){$('sCh').querySelectorAll('button').forEach((b,j)=>{if(j===right)b.classList.add('ok');else if(j===chosen)b.classList.add('no')})}
function hideCh(){$('sCh').hidden=true;$('sCh').innerHTML=''}
function nextBtn(label){return new Promise(res=>{const g=$('sGo');g.textContent=label;g.hidden=false;g.disabled=false;g.focus();g.onclick=()=>{g.onclick=null;g.hidden=true;res()}})}
function say(phase,title,text){if(phase!=null)$('sPhase').textContent=phase;if(title!=null)$('sTitle').textContent=title;if(text!=null)$('sText').innerHTML=text}
function startRun(fn){$('sGo').addEventListener('click',async()=>{if(RUN)return;RUN={};const g=$('sGo');g.hidden=true;$('sRes').innerHTML='';try{await fn()}finally{hideCh();g.onclick=null;g.textContent='Try again';g.hidden=false;g.disabled=false;RUN=null}})}
'''

def pgrid_html(intro='For each study on this page, predict what was found. Then check.'):
    return f'''  <section aria-labelledby="brT" style="margin:24px 0 40px">
    <div class="col">
      <h2 class="sec" id="brT"><span class="n">Check your intuition</span>Predict the findings</h2>
      <p>{intro}</p>
    </div>
    <div class="wide">
      <form class="pgrid" id="pGrid"></form>
      <div class="qrow"><button class="pbtn" id="pCheck" type="button">Check my predictions</button><button class="pbtn" id="pReset" type="button" hidden>Try again</button></div>
      <p class="pmsg" id="pSum" aria-live="polite"></p>
    </div>
  </section>
'''

def ppage(o):
    o=dict(o);o['js']=TABS_JS+o['js']
    o['css']=TABS_CSS+o.get('css','')
    h=_page(o)
    # no video: drop the watch section, the transcript code and the srt placeholder
    h=re.sub(r'<section class="watch".*?</section>\n\n','',h,flags=re.S)
    h=h.replace('const EP_SRT = __SRT__;\n','')
    a=h.index("(function(){const v=$('ep');");b=h.index("slice(3).join(' ')})();",a)+len("slice(3).join(' ')})();")
    h=h[:a]+h[b:]
    h=h.replace('<span><a href="#watchT">Watch the video</a></span>','<span><a href="#tryT">Try it first</a></span>')
    h=h.replace('<style>.vnote{','<style>.xvnote{')
    h=h.replace('The brain drawing and both activities are simplified illustrations, not the original experiments.',
                o.get('foot','The brain drawing and the activities are simplified illustrations drawn for this page, not the original experiments or images.'))
    assert '$(\'ep\')' not in h and 'watchT' not in h and '__SRT__' not in h
    return h

def write(o):
    import os
    d=f"{o['id']}";os.makedirs(d,exist_ok=True)
    open(f'{d}/template.html','w').write(ppage(o))
