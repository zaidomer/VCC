import os
import getpass
from WebScrapeURL import ScrapeRT
from ClipDownloaderTwitch import DownTwitch
from VideoMentions import VideoMent
from MentionAdder import MentAdder
from MergeVideo import MergeAdder
from RepetitionChecker import RepCheck
from time import sleep

def main():

    checkuser = getpass.getuser()
    if checkuser == 'zaid':
        videoPath = r"/mnt/c/Users/" + checkuser + 'l/Documents'
    else:
        videoPath = r"C:\\Users\\" + checkuser + '\\Documents'

    try:
        os.mkdir(os.path.join(videoPath, 'VCC'))
    except OSError as error:
        pass

    try:
        os.mkdir(os.path.join(videoPath + '/VCC', 'Today\'s Clips'))
    except OSError as error:
        pass

    try:
        os.mkdir(os.path.join(videoPath + '/VCC', 'Today\'s Upload'))
    except OSError as error:
        os.remove(videoPath + '/VCC/Today\'s Upload/Final.mp4')

    generateURL = ScrapeRT(10)
    generateURL.twitchScrape()
    checkRep = RepCheck()
    checkRep.moveClips()

    for x in range(len(generateURL.clipTitles)):

        if (checkRep.checkClips(generateURL.clipTitles[x])):
            pass
        else:
            continue

        print('down')

        downloadMP4 = DownTwitch(generateURL.clipLinks[x],generateURL.clipTitles[x])
        downloadMP4.scrapeMP4Url()

        print('image')

        imageMention = VideoMent(generateURL.clipUsers[x],generateURL.clipTitles[x])
        imageMention.imageEditor()

        print('mention')

        mentionAdd = MentAdder(generateURL.clipTitles[x])
        mentionAdd.mentionAdder()

        print('checking')

    mergeAdd = MergeAdder(generateURL.clipTitles)
    mergeAdd.merger()

    checkRep.writeNewClips(generateURL.clipTitles)


if __name__ == "__main__":
    main()