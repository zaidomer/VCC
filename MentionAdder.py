import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from moviepy.editor import *
import getpass

class MentAdder:

    title = ''

    def __init__(self, title):
        self.title = title
        for char in self.title:
            if char in "<>:\"/\\|?*":
                self.title = self.title.replace(char, '')
        self.title = self.title

    def mentionAdder(self):

        checkuser = getpass.getuser()
        video2 = mp.VideoFileClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + '.mp4')
        video1 = video2.resize(height=1080)
        video = video1.fx(afx.audio_normalize).fx(afx.volumex, 0.6)

        ment = (mp.ImageClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + '.png')
                  .set_duration(6)
                  .resize(0.3)
                  .set_position(("left","bottom")))

        ment = vfx.fadein(ment,1, initial_color=[255,255,255])
        ment = vfx.fadeout(ment,1,final_color=[255,255,255])

        final = mp.CompositeVideoClip([video, ment])
        final.write_videofile('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + 'Final.mp4',threads=3,fps=30)
        final.close()

    def getDuration(self,clipTitle):
        for char in clipTitle:
            if char in "<>:\"/\\|?*":
                clipTitle = clipTitle.replace(char, '')
        checkuser = getpass.getuser()
        video = mp.VideoFileClip('C:/Users/' + checkuser + '/Documents/VCC/Today\'s Clips/' + clipTitle + 'Final.mp4')
        dur = video.duration
        video.close()
        return dur
