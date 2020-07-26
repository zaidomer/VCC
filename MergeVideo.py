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

        if getpass.getuser()=="zaid":
            self.cDriveLocation = "/mnt/c/Users/zaidl"
        else:
            self.cDriveLocation = "C:/Users/" + getpass.getuser()

    def merger(self):
        checkuser = getpass.getuser()
        self.clips.append(VideoFileClip('intro.mp4'))
        for title in self.clipTitles:
            clip = VideoFileClip(self.cDriveLocation +'/Documents/VCC/Today\'s Clips/' + title + 'Final.mp4')
            self.clips.append(clip)
        self.clips.append(VideoFileClip('outro.mp4'))

        finalVideo = concatenate_videoclips(self.clips, method='compose')
        finalVideo.write_videofile(self.cDriveLocation+'/Documents/VCC/Today\'s Upload/Final.mp4',threads=4, bitrate="20000k",fps=30)