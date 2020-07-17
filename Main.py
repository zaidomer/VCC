import os
import getpass
from WebScrapeURL import ScrapeRT
from ClipDownloaderTwitch import DownTwitch
from VideoMentions import VideoMent
from MentionAdder import MentAdder
from time import sleep

def main():

    checkuser = getpass.getuser()
    if checkuser == 'zaid':
        videoPath = r"C:\\Users\\" + checkuser + 'l\\Documents'
    else:
        videoPath = r"C:\\Users\\" + checkuser + '\\Documents'

    try:
        os.mkdir(os.path.join(videoPath, 'VCC'))
    except OSError as error:
        pass

    try:
        os.mkdir(os.path.join(videoPath + '\\VCC', 'Today\'s Clips'))
    except OSError as error:
        pass

    try:
        os.mkdir(os.path.join(videoPath + '\\VCC', 'Yesterday\'s Clips'))
    except OSError as error:
        pass

    try:
        os.mkdir(os.path.join(videoPath + '\\VCC', 'Today\'s Upload'))
    except OSError as error:
         pass

    generateURL = ScrapeRT(10)
    generateURL.twitchScrape()

    for x in range(len(generateURL.clipTitles)):
        downloadMP4 = DownTwitch(generateURL.clipLinks[x],generateURL.clipTitles[x])
        downloadMP4.scrapeMP4Url()

        print('image')

        imageMention = VideoMent(generateURL.clipUsers[x],generateURL.clipTitles[x])
        imageMention.imageEditor()

        print('mention')

        mentionAdd = MentAdder(generateURL.clipTitles[x])
        mentionAdd.mentionAdder()

        print('down')



if __name__ == "__main__":
    main()
