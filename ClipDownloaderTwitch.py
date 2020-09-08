from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

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
            self.cDriveLocation = "C:/Users/" + getpass.getuser() + "l"
        else:
            self.cDriveLocation = "C:/Users/" + getpass.getuser()

    # Scrapes the specific clips to get the MP4 url
    def scrapeMP4Url(self):
        if getpass.getuser() == "zaidl":
            driver = webdriver.Chrome(self.cDriveLocation + "/Documents/chromedriver/chromedriver")
        else:
            driver = webdriver.Chrome('C:\\Users\\' + getpass.getuser() + '\\Documents\\chromedriver.exe')

        while True:
            driver.get(self.url)
            sleep(5)
            try:
                element_present = EC.presence_of_element_located((By.ID, 'main'))
                WebDriverWait(driver,5).until(element_present)
            except TimeoutException:
                pass
            finally:
                break

        downLink = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/video')
        self.downloadFile(downLink.get_attribute("src"))
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

        for char in firstVid:
            if char in "<>:\"/\\|?*":
                firstVid = firstVid.replace(char, '')

        vidcap = cv2.VideoCapture('C:/Users/' + checkuser + '/Documents/VCC/Today\'s Clips/' + firstVid + '.mp4')
        success,image = vidcap.read()
        cv2.imwrite('C:/Users/' + checkuser + '/Documents/VCC/Today\'s Clips/Thumbnail.png', image)
