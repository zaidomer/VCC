from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, transfx
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
        self.clips.append(VideoFileClip('intro.mp4'))
        for title in self.clipTitles:
            clip = VideoFileClip('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + title + 'Final.mp4')
            self.clips.append(clip)
        self.clips.append(VideoFileClip('outro.mp4'))

        #finalCLip = [CompositeVideoClip([clip.fx(transfx.slide_in, 0.2, 'bottom')]) for clip in self.clips]
        finalVideo = concatenate_videoclips(self.clips, method='compose')
        finalVideo.write_videofile('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Upload/Final.mp4',threads=3,fps=30)
        finalVideo.close()
