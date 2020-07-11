import praw
from selenium import webdriver
from time import sleep

# Client to get reddit data
reddit = praw.Reddit(client_id='1Gy4zNNu1JlnIA', client_secret='1GzLnVE1fcIqZ9rrOUYyOP_Kzkk', user_agent='VCC')

# Get the 20 top posts URLS
top_posts = reddit.subreddit('ValorantClips').top('day',limit=20)
for post in top_posts:
    print(post.url)

# Chromedriver must be installed
driver = webdriver.Chrome('C:\\Users\\braul\\OneDrive\\Desktop\\chromedriver.exe')
driver.get('https://www.twitch.tv/directory/game/VALORANT/clips?range=24hr')
sleep(10)

i = 1
while i <= 100:
    links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
    titles = driver.find_elements_by_xpath("//h3[@class='tw-ellipsis tw-font-size-5']")
    driver.execute_script('arguments[0].scrollIntoView(true);', titles[len(titles)-1])
    #driver.execute_script('arguments[0].scrollIntoView(true);', links[len(links)-1])
    i+=20
    sleep(2)


links = driver.find_elements_by_xpath("//a[@data-a-target='preview-card-image-link']")
titles = driver.find_elements_by_xpath("//h3[@class='tw-ellipsis tw-font-size-5']")

clipLinks = []
clipTitles = []

for title in titles:
    clipLinks.append(title.get_attribute('title'))

for link in links:
    clipLinks.append(link.get_attribute('href'))

print(clipLinks)
print((clipTitles))
