import os
import getpass
# from WebScrapeURL import ScrapeRT
#import YoutubeAPICommands

def main():

    checkuser = getpass.getuser()
    if checkuser == 'zaid':
        videoPath = r"C:/Users/" + checkuser + 'l/Documents'
    else:
        videoPath = r"C:/Users/" + checkuser + '/Documents'

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

    #generateURL = ScrapeRT()
    #generateURL.redditScrape()
    #generateURL.twitchScrape()


    print(videoPath)


if __name__ == "__main__":
    main()
