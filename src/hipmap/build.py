t=open('hipmap/template.html').read()
nav=open('nav/nav.html').read().replace('__CURRENT__','hipmap')
t=t.replace('__POPCSS__',open('nav/pop.css').read()).replace('__POPJS__',open('nav/pop.js').read())
t=t.replace('__COLLCSS__',open('nav/coll.css').read()).replace('__COLLJS__',open('nav/coll.js').read())
srt=open('hipmap/srt.json').read() if __import__('os').path.exists('hipmap/srt.json') else '""'
t=t.replace('__CSS__',open('hipmap/shared.css').read()).replace('__SRT__',srt).replace('__BRAIN__',open('shared/brain.js').read()).replace('__NAV__',nav)
open('hipmap/index.html','w').write(t)
