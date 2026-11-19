import json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro('/tmp/tts/kokoro-v1.0.onnx','/tmp/tts/voices-v1.0.bin')
VOICE='am_michael'
# (scene id, sentences, extra silent hold after narration in seconds)
S = [
 ("title", ["Perception is a best guess."], 1.2),
 ("board", ["Here's a checkerboard, with a cylinder standing on it.", "The cylinder casts a shadow across the board.", "Look at the two squares marked A and B."], 0.4),
 ("ask",   ["Which one is lighter?", "Decide before we go on."], 3.4),
 ("most",  ["Most people say B.", "It looks much lighter than A."], 0.5),
 ("cover", ["Now let's cover everything except the two squares.", "Without the board and the shadow, A and B look the same.", "Because they are the same.", "Exactly the same grey."], 1.0),
 ("bars",  ["Bring the scene back, and join the squares with a bar of that same grey.", "Follow the bar from A to B.", "There's no edge where the colour changes."], 1.0),
 ("still", ["Even now that you know, B probably still looks lighter.", "Knowing the answer doesn't switch the effect off."], 1.0),
 ("why",   ["The same amount of light reaches your eye from both squares.", "But your brain sees that B is in shadow.", "So it infers that B is a light square in dim light, and A is a dark square in bright light.", "It reports what the surfaces are probably like, not how much light reaches your eye."], 1.0),
 ("guess", ["That's perception.", "A best guess, built from context, and from what usually happens in the world.", "Usually, it's a very good guess."], 0.8),
 ("class", ["Your students make guesses like this whenever they look at a new diagram or graph.", "You already know what matters.", "Their eyes are still guessing.", "So tell them what to look at."], 1.0),
 ("end",   ["Based on Edward Adelson's checker-shadow illusion, from 1995."], 1.8),
]
SR=24000; LEAD=0.6; SGAP=0.28; SCGAP=0.45
def trim(s):
    win=int(.02*SR); e=np.convolve(np.abs(s),np.ones(win)/win,'same'); th=0.02*e.max(); nz=np.where(e>th)[0]
    return s[max(0,nz[0]-int(.03*SR)):nz[-1]+int(.08*SR)]
t=LEAD; audio=[np.zeros(int(SR*LEAD),np.float32)]; scenes=[]
for sid,sents,hold in S:
    t0=0 if not scenes else t-SCGAP/2; lines=[]
    for i,x in enumerate(sents):
        s,sr=k.create(x,voice=VOICE,speed=0.97,lang='en-us'); assert sr==SR
        s=trim(s.astype(np.float32)); d=len(s)/SR
        lines.append(dict(text=x,start=round(t,3),end=round(t+d,3)))
        audio+=[s]; t+=d
        g=SGAP if i<len(sents)-1 else hold+SCGAP
        audio.append(np.zeros(int(SR*g),np.float32)); t+=g
    scenes.append(dict(id=sid,t0=round(t0,3),lines=lines))
for i,s in enumerate(scenes): s['t1']=scenes[i+1]['t0'] if i+1<len(scenes) else round(t,3)
sf.write('/tmp/p01v/audio/voice.wav',np.concatenate(audio),SR)
json.dump(dict(total=round(t,3),scenes=scenes),open('/tmp/p01v/timeline.json','w'),indent=1)
for s in scenes: print(s['id'],s['t0'],s['t1'])
print('total',round(t,2))
