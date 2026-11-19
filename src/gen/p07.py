import sys;sys.path.insert(0,'gen')
from pkit import *
from memjs import grid
o=pbase(7,'Hearing With Your Eyes: Lips, the McGurk Effect and Captions','Hearing','with your eyes',
'Speech perception isn’t just hearing. The brain combines the sound with what it sees on the speaker’s face, so strongly that a mismatched face can change the sound you hear. That matters in every lecture hall.',
'<span><a href="#brT">Predict the findings</a></span>')
o['hero_aria'],o['hero_js']=hero(['tem','v1'],{'tem':([300,770],'left'),'v1':([960,-60],'right')},'Drawing of the side of the brain with the temporal lobe, at the side, which processes speech sounds, and the visual cortex, at the back, glowing orange and labelled.')

# The student activity is a YouTube demonstration of the McGurk effect (chosen by the course author).
YT='2k8fHR9jKVM'
student=f'''        <div class="ytwrap">
          <iframe src="https://www.youtube-nocookie.com/embed/{YT}?rel=0&amp;cc_load_policy=1" title="Video: the McGurk effect" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
        </div>
        <ol class="ytsteps">
          <li><b>Watch and listen.</b> What sound does the speaker make?</li>
          <li><b>Play it again with your eyes closed.</b> Does the sound change?</li>
          <li><b>Open your eyes partway through.</b> Can you stop your eyes changing what you hear?</li>
        </ol>
        <p class="ytlink">Video not loading? <a href="https://www.youtube.com/watch?v={YT}">Watch it on YouTube</a>.</p>'''

o.update(body=tabs('Hear it with your eyes','A short video of the McGurk effect. Watch it, then listen again with your eyes closed.',student,
 'About 10 minutes, plus an optional live demo',
 ['Play the video once and ask everyone to write down the sound they heard, without discussing it. Then play it again with eyes closed and compare.',
  'Live demo: silently mouth “bat”, “pat” and “mat” in random order and ask the class to call out which. Then mouth “fan” and “pan”.',
  'Discuss which sounds the lips show (where the mouth closes) and which they hide (whether the voice is on).',
  'Connect to your room: where do you stand when you speak? What happens when you talk while writing on the board?'],
 ['Why did the sound change when you closed your eyes?',
  'Why can you tell “fan” from “pan” by the lips, but not “bat” from “pat”?',
  'What does hearing add that the lips can’t?',
  'Who in this room depends most on seeing your face, or on captions?'],
 'Face the room when you speak, don’t talk while writing on the board, use a microphone when you have one, and turn on captions for video. Seeing the speaker helps everyone, and it helps most when the room is noisy.',
 'The effect usually works even when you know about it. Not everyone experiences it, and its strength varies from person to person.')+'''
  <div class="col lede">
    <p>In 1976, Harry McGurk and John MacDonald dubbed the sound of someone saying “ba” onto a film of a woman’s face saying “ga”. Adults watching it reported hearing “da”: neither the sound nor the lips, but a blend. With their eyes closed, they heard “ba” correctly.</p>
    <p>The McGurk effect shows that speech perception combines what we hear and what we see. The brain doesn’t keep them separate; it makes one best guess from both.</p>
  </div>

  <div class="wide">
    <div class="facts" role="list">
      <div role="listitem"><strong>“da”</strong><span>heard when a “ba” sound is dubbed onto lips saying “ga”</span></div>
      <div role="listitem"><strong>1954</strong><span>first experiments showing that seeing the face helps people understand speech in noise</span></div>
      <div role="listitem"><strong>Noise</strong><span>is where seeing the speaker adds the most</span></div>
      <div role="listitem"><strong>100+</strong><span>studies on same-language captions, in one 2015 review</span></div>
    </div>
  </div>

  <div class="col">
    <h2 class="sec"><span class="n">In noise</span>The face fills in what the ear misses</h2>
    <p>William Sumby and Irwin Pollack tested how well people understood spoken words in noise, with and without seeing the speaker’s face. Seeing the face helped across noise levels, and because there is so much more to recover when the sound is poor, the face added the most in the noisiest conditions.</p>
    <h2 class="sec"><span class="n">What lips show</span>Where, not whether</h2>
    <p>The lips show where in the mouth a sound is made: “p”, “b” and “m” all close the lips; “f” and “v” put the teeth on the lip. They can’t show whether the voice is on, which is the difference between “p” and “b”. Hearing supplies that. That is why “fan” and “pan” look different on the lips, but “bat” and “pat” don’t.</p>
    <h2 class="sec"><span class="n">Captions</span>A large literature, with caveats</h2>
    <p>In a 2015 review, Morton Ann Gernsbacher listed more than 100 studies reporting that same-language captions improve comprehension of, attention to and memory for videos. Captions are especially helpful for people watching in a second language, people learning to read, and people who are deaf or hard of hearing. Critics note that much of this evidence comes from those groups, and that well-controlled studies with typical hearing students are fewer. For many students, though, captions are essential, and they are required for accessibility in most educational settings.</p>
  </div>

'''+pgrid_html(),
tips_h='Let students see you speak.',
tips='''      <li><b>Face the room</b><span>Don’t talk to the board or the screen.</span></li>
      <li><b>Captions on</b><span>For every video. Essential for some students, useful for many.</span></li>
      <li><b>Cut the noise</b><span>Use the microphone; the noisier the room, the more the face matters.</span></li>''',
sources='''        <li><a href="https://doi.org/10.1038/264746a0">McGurk, H., &amp; MacDonald, J. (1976). Hearing lips and seeing voices. <i>Nature, 264</i>, 746–748.</a></li>
        <li><a href="https://doi.org/10.1121/1.1907309">Sumby, W. H., &amp; Pollack, I. (1954). Visual contribution to speech intelligibility in noise. <i>Journal of the Acoustical Society of America, 26</i>(2), 212–215.</a></li>
        <li><a href="https://doi.org/10.1177/2372732215602130">Gernsbacher, M. A. (2015). Video captions benefit everyone. <i>Policy Insights from the Behavioral and Brain Sciences, 2</i>(1), 195–202.</a></li>''',
foot='The video is hosted on YouTube. The brain drawing is a simplified illustration.',
css='.ytwrap{position:relative;aspect-ratio:16/9;max-width:860px;margin:0 auto;background:#000;border-radius:8px;overflow:hidden}.ytwrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.ytsteps{max-width:860px;margin:18px auto 0;padding-left:1.4em;font-size:18px;line-height:1.5}.ytsteps li{margin:6px 0}.ytlink{max-width:860px;margin:10px auto 0;font-size:16px}.ytlink a{color:inherit}',
quiz='''[
 {q:'In the McGurk effect, a “ba” sound on lips saying “ga” is usually heard as…',o:['“da”','“ba”','“ga”'],a:0,f:'A blend of sound and sight.'},
 {q:'Seeing the speaker’s face helps understanding most when…',o:['The room is noisy','The room is silent','The speaker is far away'],a:0,f:'Sumby and Pollack, 1954.'},
 {q:'Why can’t you tell “bat” from “pat” by lips alone?',o:['Both close the lips; the difference is the voice','They’re spelled differently','You can, easily'],a:0,f:'Lips show where, not whether the voice is on.'}]''',
js=r'''
'''+grid('''[
 ['A “ba” sound dubbed onto a face saying “ga” was usually heard as…',['“da”','“ba”','“ga”'],0,'McGurk and MacDonald, 1976.'],
 ['With their eyes closed, the same listeners heard…',['“ba”, correctly','“da”','Nothing clear'],0,'So the lips changed what they heard.'],
 ['In Sumby and Pollack’s experiments, seeing the speaker helped most when…',['The noise was loudest','There was no noise','The words were familiar'],0,'There was most to recover.'],
 ['How many studies on captions did Gernsbacher’s 2015 review list?',['More than 100','About 10','About 1,000'],0,'Reporting benefits for comprehension, attention and memory.'],
 ['Critics of “captions benefit everyone” point out that much of the evidence comes from…',['Second-language learners, deaf viewers and self-report','Only children','Brain scans'],0,'Studies with typical-hearing college students are fewer.']]''','The pattern: we hear with our eyes too, and the face matters most when the sound is poor.'))
write(o)
