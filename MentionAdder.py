import moviepy.editor as mp
import moviepy.video.fx.all as vfx
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
        video = mp.VideoFileClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + '.mp4')

        ment = (mp.ImageClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + '.png')
                  .set_duration(6)
                  .resize(0.3)
                  .set_position(("left","bottom")))

        ment = vfx.fadein(ment,1, initial_color=[255,255,255])
        ment = vfx.fadeout(ment,1,final_color=[255,255,255])

        final = mp.CompositeVideoClip([video, ment])
        final.write_videofile('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title + 'Final.mp4',threads=4, bitrate="20000k",logger=None,fps=30)