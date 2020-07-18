from moviepy.editor import VideoFileClip, concatenate_videoclips

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
        for title in self.clipTitles:
            self.clips.append(VideoFileClip('C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\' + title + 'Final.mp4'))

        finalVideo = concatenate_videoclips(self.clips)
        finalVideo.write_videofile('C:\\Users\\braul\\Documents\\VCC\\Today\'s Upload\\Final.mp4')