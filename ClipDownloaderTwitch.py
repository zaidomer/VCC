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

        if getpass.getuser()=="zaid":
            self.cDriveLocation = "C:/Users/zaidl"
        else:
            self.cDriveLocation = "C:/Users/" + getpass.getuser()

    # Scrapes the specific clips to get the MP4 url
    def scrapeMP4Url(self):
        if getpass.getuser() == "zaidl":
            driver = webdriver.Chrome(self.cDriveLocation + "/Documents/chromedriver/chromedriver.exe")
        else:
            driver = webdriver.Chrome('C:\\Users\\braul\\OneDrive\\Desktop\\chromedriver.exe')
        driver.get(self.url)
        sleep(5)
        downLink = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div[2]/div/div[2]/div/video')
        self.downloadFile(downLink.get_attribute("src"))
        driver.close()

    # Download the files from the specific mp4 url
    def downloadFile(self,url):
        checkuser = getpass.getuser()
        r = requests.get(url, stream=True)
        with open(self.cDriveLocation + '/Documents/VCC/Today\'s Clips/' + self.title, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    def downloadFirstThumbnail(self,firstVid):
        vidcap = cv2.VideoCapture(self.cDriveLocation + '/Documents/VCC/Today\'s Clips/' + firstVid + '.mp4')
        success,image = vidcap.read()
        cv2.imwrite(self.cDriveLocation + '/Documents/VCC/Today\'s Clips/Thumbnail.png', image)