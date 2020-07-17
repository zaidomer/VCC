import moviepy.editor as mp
import moviepy.video.fx.all as vfx

class MentAdder:

    title = ''

    def __init__(self, title):
        self.title = title
        for char in self.title:
            if char in "<>:\"/\\|?*":
                self.title = self.title.replace(char, '')
        self.title = self.title

    def mentionAdder(self):
        video = mp.VideoFileClip('C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\' + self.title + '.mp4')

        ment = (mp.ImageClip('C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\' + self.title + '.png')
                  .set_duration(6)
                  .resize(0.3)
                  .set_position((0.05,0.75), relative=True))

        ment = vfx.fadein(ment,1, initial_color=[255,255,255])
        ment = vfx.fadeout(ment,1,final_color=[255,255,255])

        final = mp.CompositeVideoClip([video, ment])
        final.write_videofile('C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\' + self.title + 'Final.mp4',threads=4, bitrate="20000k",logger=None)