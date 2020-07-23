from moviepy.editor import VideoFileClip, concatenate_videoclips
import getpass

class MergeAdder:

    clips = []
    clipTitles = []

    def __init__(self, titles):
        self.clipTi = titles[:]
        self.clipTitles = []
        ti = ''
        for title in self.clipTi:
            ti = title
            for char in ti:
                if char in "<>:\"/\\|?*":
                    ti = ti.replace(char, '')
            self.clipTitles.append(ti)
        self.clips = []

    def merger(self):

        checkuser = getpass.getuser()
        print(self.clipTitles)
        for title in self.clipTitles:
            clip = VideoFileClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + title + 'Final.mp4')
            self.clips.append(clip)

        finalVideo = concatenate_videoclips(self.clips, method='compose')
        finalVideo.write_videofile('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Upload/Final.mp4',threads=4, bitrate="20000k",logger=None,fps=30)