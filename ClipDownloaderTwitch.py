from selenium import webdriver
import requests
from time import sleep
import getpass
import cv2

class DownTwitch:

    url = None
    title = None

    def __init__(self, link, vidTitle):
        self.url = link
        self.title = vidTitle
        for char in self.title:
            if char in "<>:\"/\\|?*":
                self.title = self.title.replace(char, '')
        self.title = self.title + '.mp4'

    # Scrapes the specific clips to get the MP4 url
    def scrapeMP4Url(self):
        driver = webdriver.Chrome('C:\\Users\\braul\\OneDrive\\Desktop\\chromedriver.exe')
        driver.get(self.url)
        sleep(5)
        downLink = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div[2]/div/div[2]/div/video')
        self.downloadFile(downLink.get_attribute("src"))
        self.downloadFirstThumbnail(self.title)
        driver.close()

    # Download the files from the specific mp4 url
    def downloadFile(self,url):
        checkuser = getpass.getuser()
        r = requests.get(url, stream=True)
        with open('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + self.title, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    def downloadFirstThumbnail(self,firstVid):
        checkuser = getpass.getuser()
        vidcap = cv2.VideoCapture('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/' + firstVid)
        success,image = vidcap.read()
        cv2.imwrite('C:/Users/'+checkuser+'/Documents/VCC/Today\'s Clips/Thumbnail.png', image)