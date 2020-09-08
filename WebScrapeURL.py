import praw
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import getpass
from selenium.webdriver.common.keys import Keys
import requests
import json

class ScrapeRT:
    clipLinks = []
    clipTitles = []
    clipUsers = []
    clipAmnt = None

    def __init__(self):
        self.clipLinks = []
        self.clipTitles = []
        self.clipUsers = []
        self.clipLength = []

        if getpass.getuser()=="zaid":
            self.cDriveLocation = "C:/Users/" + getpass.getuser() + "l"
        else:
            self.cDriveLocation = "C:/Users/" + getpass.getuser()

    # region REDDIT
    def redditScrape(self):
        # Client to get reddit data
        reddit = praw.Reddit(client_id='1Gy4zNNu1JlnIA', client_secret='1GzLnVE1fcIqZ9rrOUYyOP_Kzkk', user_agent='VCC')

        redditLinks = []
        redditTitles = []
        # Get the 20 top posts URLS
        top_posts = reddit.subreddit('ValorantClips').top('day', limit=15)
        for post in top_posts:
            redditLinks.append(post.url)
            redditTitles.append(post.title)

    # endregion

    # region TWITCH

    def twitchScrape(self):
        data = ' '
        count = 0
        while len(str(data))<300:
            response = requests.post('https://gql.twitch.tv/gql', data='[{"operationName":"ClipsCards__Game","variables":{"gameName":"VALORANT","limit":100,"criteria":{"languages":["EN"],"filter":"LAST_DAY"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d8d0eba9fc7ef77de54a7d933998e21ad7a1274c867ec565ac14ffdce77b1f9"}}}]',headers={'Client-ID':'kimne78kx3ncx6brgo4mv6wki5h1ko','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'})
            data = json.loads(response.text)
            sleep(count)
            count+=0.25

        for x in range(len(data[0]['data']['game']['clips']['edges'])):
            self.clipUsers.append(data[0]['data']['game']['clips']['edges'][x]['node']['broadcaster']['displayName'])
            self.clipLinks.append(data[0]['data']['game']['clips']['edges'][x]['node']['url'])

            #Reformat Title
            titleToAdd = repr(data[0]['data']['game']['clips']['edges'][x]['node']['title'])
            for char in titleToAdd:
                if char in "/\\\'":
                    titleToAdd = titleToAdd.replace(char, '')

            if len(str(x)) >= 2:
                self.clipTitles.append(titleToAdd + str(x))
            else:
                self.clipTitles.append(titleToAdd + '0' + str(x))

            self.clipLength.append(data[0]['data']['game']['clips']['edges'][x]['node']['durationSeconds'])

        self.twitchFilter(self.clipLinks, self.clipTitles,self.clipUsers,self.clipLength)
        print(self.clipLinks[0])
    # endregion

    # region Filter
    def twitchFilter(self, clipLinks, clipTitles,clipUsers,clipLength):
        tempLinks = []
        tempTitles = []
        tempUsers = []
        tempLength = []
        # Open and reads the text file and puts each term in a list
        with open('filterTags.txt', "r") as f:
            filterList = f.readlines()
        filterList = [x.strip() for x in filterList]

        clipTi = clipTitles[:]

        count = 0
        for cTitle in clipTitles:
            if any(x.lower() in cTitle.lower() for x in filterList):
                pass
            else:
                tempLinks.append(clipLinks[count])
                tempTitles.append(clipTitles[count])
                tempUsers.append(clipUsers[count])
                tempLength.append(clipLength[count])

                clipTi.pop(count)
                clipLinks.pop(count)
                clipUsers.pop(count)
                clipLength.pop(count)
                count -= 1
            count += 1


        # So we can choose how many clips go through
        self.clipTitles = clipTi[:]
        self.clipLinks = clipLinks[:]
        self.clipUsers = clipUsers[:]
        self.clipLength = clipLength[:]

        currentLength = 0
        for length in clipLength:
            currentLength += length

        count = 0
        while currentLength<600:
            self.clipTitles.append(tempTitles[count])
            self.clipLinks.append(tempLinks[count])
            self.clipUsers.append(tempUsers[count])
            self.clipLength.append(tempLength[count])
            currentLength+=tempLength[count]
            count+=1
    # endregion
