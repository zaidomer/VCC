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
    videoPath = r"C:/Users/" + checkuser + '/Documents'

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
        try:
            os.remove(videoPath + '/VCC/Today\'s Upload/Final.mp4')
        except OSError as error:
            pass

    for filename in os.listdir(videoPath + '/VCC/Today\'s Clips'):
       file_path = os.path.join(videoPath + '/VCC/Today\'s Clips', filename)
       os.remove(file_path)

    timeStamps= []
    timeStamps.append(7)

    generateURL = ScrapeRT(10)
    generateURL.twitchScrape()
    checkRep = RepCheck()
    checkRep.moveClips()

    updatedTitles = generateURL.clipTitles[:]
    count = 0

    thumbnailDone = True
    thumbnailTitle = ""

    for x in range(len(generateURL.clipTitles)):

        if (checkRep.checkClips(generateURL.clipTitles[x])):
            count+=1
        else:
            updatedTitles.pop(count)
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

        timeStamps.append(round(timeStamps[x] + mentionAdd.getDuration(generateURL.clipTitles[x]),2))

        if thumbnailDone and len((generateURL.clipTitles[x]).split())<5:
            downloadMP4 = DownTwitch(generateURL.clipLinks[x], generateURL.clipTitles[x])
            downloadMP4.downloadFirstThumbnail(generateURL.clipTitles[x])
            thumbnailTitle = generateURL.clipTitles[x]
            thumbnailDone = False

    mergeAdd = MergeAdder(updatedTitles)
    mergeAdd.merger()

    checkRep.writeNewClips(updatedTitles)

    print(timeStamps)


if __name__ == "__main__":
    main()