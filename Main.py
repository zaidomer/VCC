from WebScrapeURL import ScrapeRT

def main():
    generateURL = ScrapeRT()
    generateURL.redditScrape()
    generateURL.twitchScrape()
if __name__ == "__main__":
    main()