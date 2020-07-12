import os
import getpass
from WebScrapeURL import ScrapeRT

def main():
    generateURL = ScrapeRT()
    generateURL.redditScrape()
    generateURL.twitchScrape()
    checkuser = getpass.getuser()
    if checkuser == 'zaid':
        videoPath = r"C:/Users/" + checkuser + 'l/Documents/VCC/Today\'s Video/'
    else:
        videoPath = r"C:/Users/" + checkuser + '/Documents/VCC/Today\'s Video/'

    print(videoPath)


if __name__ == "__main__":
    main()
