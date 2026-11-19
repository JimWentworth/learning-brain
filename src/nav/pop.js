/* "In popular culture" tabs. Item fields: id, title, sub, kind, year, films:[[name,imdbUrl]], verdict:[class,label], desc, right[], wrong[], note:[title,text]?, src, more:[[label,url|null]]? */
function renderPop(POP,tabsId,panelsId){const tabs=document.getElementById(tabsId),panels=document.getElementById(panelsId);
 POP.forEach((f,i)=>{const b=document.createElement('button');b.role='tab';b.id='tab-'+f.id;b.setAttribute('aria-controls','pp-'+f.id);b.setAttribute('aria-selected',i===0);b.tabIndex=i===0?0:-1;b.innerHTML=`${f.title}<small>${f.sub}</small>`;tabs.appendChild(b);
  const p=document.createElement('div');p.className='popp';p.id='pp-'+f.id;p.role='tabpanel';p.setAttribute('aria-labelledby','tab-'+f.id);p.tabIndex=0;p.hidden=i!==0;
  const links=(f.films||[]).map(([n,u])=>`<a href="${u}">${n} on IMDb</a>`).join('');
  p.innerHTML=`<div class="popmeta"><span class="verdictchip ${f.verdict[0]}">${f.verdict[1]}</span><span>${f.kind}</span>${links}</div>
  <p class="popdesc">${f.desc}</p><div class="popcols"><div class="pr"><h3>What it gets right</h3><ul>${f.right.map(x=>`<li>${x}</li>`).join('')}</ul></div><div class="pw"><h3>What it gets wrong</h3><ul>${f.wrong.map(x=>`<li>${x}</li>`).join('')}</ul></div></div>
  ${f.note?`<div class="popnote"><b>${f.note[0]}</b>${f.note[1]}</div>`:''}
  ${f.more?`<div class="popmore"><b>Explore further</b>${f.more.map(([l,u])=>u?`<a href="${u}">${l}</a>`:`<span class="soon">${l} · coming soon</span>`).join('')}</div>`:''}
  <p class="popsrc">Source: ${f.src}</p>`;panels.appendChild(p)});
 const all=()=>[...tabs.querySelectorAll('[role=tab]')];
 function sel(b,focus){all().forEach(x=>{const on=x===b;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute('aria-controls')).hidden=!on});if(focus)b.focus()}
 tabs.addEventListener('click',e=>{const b=e.target.closest('[role=tab]');if(b)sel(b)});
 tabs.addEventListener('keydown',e=>{const L=all(),i=L.indexOf(document.activeElement);if(i<0)return;let j=null;
  if(e.key==='ArrowRight')j=(i+1)%L.length;else if(e.key==='ArrowLeft')j=(i-1+L.length)%L.length;else if(e.key==='Home')j=0;else if(e.key==='End')j=L.length-1;
  if(j!==null){e.preventDefault();sel(L[j],true)}})}
