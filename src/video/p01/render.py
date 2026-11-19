import sys,subprocess,time,json,os
from playwright.sync_api import sync_playwright
W,H,FPS=1920,1080,30; wk=int(sys.argv[1]); nw=int(sys.argv[2]); port=8800+wk
TL=json.load(open('/tmp/p01v/timeline.json')); sc=TL['scenes']
srv=subprocess.Popen(['python3','-m','http.server',str(port),'--bind','127.0.0.1'],cwd='/tmp/p01v',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':W,'height':H})
    pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_function('window.ready===true'); pg.evaluate('document.fonts.ready')
    for i,s in enumerate(sc):
      if i%nw!=wk: continue
      f0=round(s['t0']*FPS); f1=round(s['t1']*FPS); out=f'/tmp/p01v/out/{i:02d}_{s["id"]}.mp4'; tmp=out.replace('.mp4','.tmp.mp4')
      ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-c:v','mjpeg','-framerate',str(FPS),'-i','-','-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p','-r',str(FPS),tmp],stdin=subprocess.PIPE)
      for f in range(f0,f1):
        pg.evaluate(f'renderFrame({f/FPS})'); ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
      ff.stdin.close(); rc=ff.wait()
      if rc==0: os.rename(tmp,out)
      print(s['id'],f1-f0,rc,flush=True)
    b.close()
finally: srv.kill()
