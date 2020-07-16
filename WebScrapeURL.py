import praw
from selenium import webdriver
from time import sleep


class ScrapeRT:
    clipLinks = []
    clipTitles = []
    clipAmnt = None

    def __init__(self, num):
        self.clipAmnt = num
        self.clipLinks = []
        self.clipTitles = []

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
        # Chromedriver must be installed
        driver = webdriver.Chrome('C:\\Users\\braul\\OneDrive\\Desktop\\chromedriver.exe')
        driver.get('https://www.twitch.tv/directory/game/VALORANT/clips?range=24hr')
        sleep(10)

        # Scrolls until x clips are loaded
        i = 1
        while i <= self.clipAmnt:
            links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
            titles = driver.find_elements_by_xpath("//h3[@class='tw-ellipsis tw-font-size-5']")
            driver.execute_script('arguments[0].scrollIntoView(true);', titles[len(titles) - 1])
            i += 20
            sleep(2)

        # Finds the list of titles and URLS
        links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
        titles = driver.find_elements_by_xpath("//h3[@class='tw-ellipsis tw-font-size-5']")

        # Gets all the titles and puts it in a list
        for title in titles:
            self.clipTitles.append(title.get_attribute('title'))

        # Gets all the links and puts it in a list
        for link in links:
            self.clipLinks.append(link.get_attribute('href'))

        driver.close()
        self.twitchFilter(self.clipLinks, self.clipTitles)

    # endregion

    # region Filter
    def twitchFilter(self, clipLinks, clipTitles):
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
                clipTi.pop(count)
                clipLinks.pop(count)
                count -= 1
            count += 1

        self.clipTitles = clipTi
        self.clipLinks = clipLinks
    # endregion
