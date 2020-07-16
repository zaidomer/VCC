from redvid import Downloader

def downloadReddit(url):
    reddit = Downloader()
    reddit.overwrite = True
    reddit.max = True
    reddit.path = 'C:\\Users\\braul\\Documents\\VCC\\Today\'s Clips\\'
    reddit.url = url
    reddit.download()

downloadReddit('https://www.reddit.com/r/ValorantClips/comments/hrqqyi/the_lads_are_not_fans_of_the_new_elderflame_skin/')
