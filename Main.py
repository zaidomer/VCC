import os
import getpass
import time
from WebScrapeURL import ScrapeRT
from datetime import datetime
from ClipDownloaderTwitch import DownTwitch
from VideoMentions import VideoMent
from MentionAdder import MentAdder
from MergeVideo import MergeAdder
from RepetitionChecker import RepCheck
import time
from ThumbnailGenerator import ThumbnailGenerator
from TitleGenerator import TitleGen
from YoutubeAPICommands import YoutubeAPICommands

def main():

    print('Starting...')

    startTime = time.time()
    checkuser = getpass.getuser()
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
        try:
            os.remove(videoPath + '/VCC/Today\'s Upload/Final.mp4')
        except OSError as error:
            pass

    for filename in os.listdir(videoPath + '/VCC/Today\'s Clips'):
        file_path = os.path.join(videoPath + '/VCC/Today\'s Clips', filename)
        os.remove(file_path)

    timeStamps= []
    timeStamps.append(6)

    generateURL = ScrapeRT()
    generateURL.twitchScrape()
    checkRep = RepCheck()
    checkRep.moveClips()

    finishedTitlesList = []
    finishedLinksList = []
    finishedUsersList = []

    print('Number of Clips' + str(len(generateURL.clipTitles)))

    thumbnailDone = True
    thumbnailTitle = ""

    for x in range(len(generateURL.clipTitles)):

        print('Check repetition')

        #if (checkRep.checkClips(generateURL.clipTitles[x])):
        #    pass
        #else:
        #    continue

        print('Downloading')

        downloadMP4 = DownTwitch(generateURL.clipLinks[x],generateURL.clipTitles[x])
        downloadMP4.scrapeMP4Url()

        print('Image Maker')

        imageMention = VideoMent(generateURL.clipUsers[x],generateURL.clipTitles[x])
        imageMention.imageEditor()

        print('Mention Adder')

        mentionAdd = MentAdder(generateURL.clipTitles[x])
        mentionAdd.mentionAdder()

        timeStamps.append(round(timeStamps[x] + mentionAdd.getDuration(generateURL.clipTitles[x]),2))

        print('Timestamp: ' + str(timeStamps[x+1]))


        print('TXitle gen')

        if thumbnailDone:
            tiGen = TitleGen()
            if tiGen.twoWords(generateURL.clipTitles[x]) != '_':
                downloadMP4 = DownTwitch(generateURL.clipLinks[x], generateURL.clipTitles[x])
                downloadMP4.downloadFirstThumbnail(generateURL.clipTitles[x])
                thumbnailTitle = tiGen.twoWords(generateURL.clipTitles[x])
                thumbnailDone = False
            else:
                pass


        finishedTitlesList.append(generateURL.clipTitles[x])
        finishedLinksList.append(generateURL.clipLinks[x])
        finishedUsersList.append(generateURL.clipUsers[x])

        if timeStamps[x+1] >= 600:
            break


    generateURL.clipTitles = finishedTitlesList
    generateURL.clipLinks = finishedLinksList
    generateURL.clipUsers = finishedUsersList

    if thumbnailDone:
        for x in range(len(finishedTitlesList)):
            if thumbnailDone:
                tiGen = TitleGen()
                if tiGen.oneWord(generateURL.clipTitles[x]) != '_':
                    downloadMP4 = DownTwitch(generateURL.clipLinks[x], generateURL.clipTitles[x])
                    downloadMP4.downloadFirstThumbnail(generateURL.clipTitles[x])
                    thumbnailTitle = tiGen.oneWord(generateURL.clipTitles[x])
                    thumbnailDone = False

    if thumbnailDone:
        downloadMP4 = DownTwitch(generateURL.clipLinks[2], generateURL.clipTitles[2])
        downloadMP4.downloadFirstThumbnail(generateURL.clipTitles[2])
        tiGen = TitleGen()
        thumbnailTitle = tiGen.fullRNG()

    print('Title: ' + thumbnailTitle)

    generateThumbnail = ThumbnailGenerator()
    generateThumbnail.createThumbnail(thumbnailTitle, generateURL)

    print('Final merge')
    mergeAdd = MergeAdder(finishedTitlesList)
    mergeAdd.merger()

    checkRep.writeNewClips(finishedTitlesList)
    videoUploader = YoutubeAPICommands()
    videoUploader.uploadVideo(videoPath, generateURL, timeStamps,finishedTitlesList)

    print('Time elapsed: ' + str(time.time() - startTime))
    #end time
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    print("Video Process Completed at " + currentTime + ". Going back to idle mode...")

if __name__ == "__main__":
    startTime = "04:45"
    print("Program started, currently on idle. Will start video process at " + startTime + "...")
    while True:
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        if currentTime == startTime:
            main()
        time.sleep(55)
