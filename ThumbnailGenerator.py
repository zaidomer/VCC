from PIL import Image, ImageDraw, ImageFont
import getpass
import random

class ThumbnailGenerator:
    
    characterNames = ["breach", "brimstone", "cypher", "jet", "omen", "phoenix", "raze", "reyna", "sage", "sova", "viper"]

    def __init__(self, clipThumbnailPath):
        print("Thumbnail generating...")
        self.title = "Today\'s Upload"
        for char in self.title:
            if char in "<>:\"/\\|?*":
                self.title = self.title.replace(char, '')
        self.title = self.title + '.png'

    def createThumbail(self):
        checkuser = getpass.getuser()
        clipThumbnailPath = selectClipThumbnail()
        baseImage = Image.open(clipThumbnailPath)
        characterImage = Image.open(characterNames[random.randint(0,10)] + ".png")

    def selectClipThumbnail(self):
        clipThumbnailPath
        return clipThumbnailPath


