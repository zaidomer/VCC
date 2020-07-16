from selenium import webdriver
import requests
from time import sleep

def downloadTwitch(url):
    driver = webdriver.Chrome('C:\\Users\\braul\\OneDrive\\Desktop\\chromedriver.exe')
    driver.get(url)
    sleep(10)
    downLink = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div[2]/div/div[2]/div/video')
    download_file(downLink.get_attribute("src"))

def download_file(url,title):
    r = requests.get(url, stream=True)
    with open('C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\' + title, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

downloadTwitch('https://www.twitch.tv/masayoshi/clip/JollyOptimisticLouseNomNom','test.mp4')