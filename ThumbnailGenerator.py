from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFilter
import getpass
import random
import os

class ThumbnailGenerator:

    characterNames = ["breach", "brimstone", "cypher", "jet", "omen", "phoenix", "raze", "reyna", "sage", "sova", "viper"]
    maps = ["ascent", "bind", "haven", "split"]
    ranks = ["diamond", "immortal", "platinum", "radiant"]

    def __init__(self):
        print("Starting thumbnail generation...")

    def createThumbnail(self, thumbnailTitle, urlGenerator):
        #Open base images
        checkuser = getpass.getuser()
        baseImage = Image.open("C:/Users/"+checkuser+"/Documents/VCC/Today\'s Clips/Thumbnail.png")
        baseImageCopy = baseImage.resize((1117, 626))
        baseImageCopy = baseImageCopy.filter(ImageFilter.BLUR)
        baseImageWidth, baseImageHeight = baseImageCopy.size

        #Add Secondary image on thumbnail (either map or rank)
        mapName = False
        rank = False
        for i in range (len(urlGenerator.clipTitles)):
            for j in range(len(ThumbnailGenerator.maps)):
                if ThumbnailGenerator.maps[j].upper() in urlGenerator.clipTitles[i].upper() and mapName==False:
                    mapName = True
                    selectedMap = ThumbnailGenerator.maps[j]
            if mapName == False:
                for j in range(len(ThumbnailGenerator.ranks)):
                    if ThumbnailGenerator.ranks[j].upper() in urlGenerator.clipTitles[i].upper() and rank==False:
                        rank = True
                        selectedRank = ThumbnailGenerator.ranks[j]
        secondaryImageSelect = random.randint(0,1)

        if mapName:
            secondaryImage = Image.open(os.getcwd() + "\\ThumbnailResources\\maps\\" + selectedMap + ".png")
            secondaryImageWidth, secondaryImageHeight = secondaryImage.size
            resizedSecondaryImage = secondaryImage.resize((int(secondaryImageWidth*0.70), int(secondaryImageHeight*0.70)))
            resizedSecondaryImageWidth, resizedSecondaryImageHeight = resizedSecondaryImage.size
            baseImageCopy.paste(resizedSecondaryImage, (15, baseImageHeight-resizedSecondaryImageHeight-15), resizedSecondaryImage.convert('RGBA'))
        elif rank:
            secondaryImage = Image.open(os.getcwd() + "\\ThumbnailResources\\ranks\\" + selectedRank + ".png")
            secondaryImageWidth, secondaryImageHeight = secondaryImage.size
            rotatedSecondaryImage = secondaryImage.rotate(10)
            baseImageCopy.paste(rotatedSecondaryImage, (15, int((baseImageHeight-secondaryImageHeight)/2)), rotatedSecondaryImage.convert('RGBA'))
        elif secondaryImageSelect == 0:
            secondaryImage = Image.open(os.getcwd() + "\\ThumbnailResources\\maps\\" + ThumbnailGenerator.maps[random.randint(0,(len(ThumbnailGenerator.maps)-1))] + ".png")
            secondaryImageWidth, secondaryImageHeight = secondaryImage.size
            resizedSecondaryImage = secondaryImage.resize((int(secondaryImageWidth*0.70), int(secondaryImageHeight*0.70)))
            resizedSecondaryImageWidth, resizedSecondaryImageHeight = resizedSecondaryImage.size
            baseImageCopy.paste(resizedSecondaryImage, (15, baseImageHeight-resizedSecondaryImageHeight-15), resizedSecondaryImage.convert('RGBA'))
        else:
            secondaryImage = Image.open(os.getcwd() + "\\ThumbnailResources\\ranks\\" + ThumbnailGenerator.ranks[random.randint(0,(len(ThumbnailGenerator.ranks)-1))] + ".png")
            secondaryImageWidth, secondaryImageHeight = secondaryImage.size
            rotatedSecondaryImage = secondaryImage.rotate(10)
            baseImageCopy.paste(rotatedSecondaryImage, (15, int((baseImageHeight-secondaryImageHeight)/2)), rotatedSecondaryImage.convert('RGBA'))

        #Add character
        characterName = False
        for i in range (len(urlGenerator.clipTitles)):
            for j in range(len(ThumbnailGenerator.characterNames)):
                if ThumbnailGenerator.characterNames[j].upper() in urlGenerator.clipTitles[i].upper() and characterName==False:
                    characterName = True
                    selectedCharacter = ThumbnailGenerator.characterNames[j]

        if characterName:
            characterImage = Image.open(os.getcwd() + "\\ThumbnailResources\\characters\\" + selectedCharacter + ".png")
        else:
            characterImage = Image.open(os.getcwd() + "\\ThumbnailResources\\characters\\" + ThumbnailGenerator.characterNames[random.randint(0,(len(ThumbnailGenerator.characterNames)-1))] + ".png")
        characterImageWidth, characterImageHeight = characterImage.size
        baseImageCopy.paste(characterImage, (int(baseImageWidth-characterImageWidth), int(0)), characterImage.convert('RGBA'))

        #Add Clickbait Arrow/Thumbnail
        clickbaitSelect = random.randint(0, 1)
        if clickbaitSelect == 0:
            clickbaitImage = Image.open(os.getcwd() + "\\ThumbnailResources\\clickbait\\circles\\circle" + str(random.randint(1,4)) + ".png")
        else:
            clickbaitImage = Image.open(os.getcwd() + "\\ThumbnailResources\\clickbait\\arrows\\arrow" + str(random.randint(1,4)) + ".png")

        clickbaitImageWidth, clickbaitImageHeight = clickbaitImage.size
        resizedClickbaitImage = clickbaitImage.resize((int(clickbaitImageWidth*0.6), int(clickbaitImageHeight*0.6)))
        resizedClickbaitImageWidth, resizedClickbaitImageHeight = resizedClickbaitImage.size
        baseImageCopy.paste(resizedClickbaitImage, (random.randint(0, (baseImageWidth-resizedClickbaitImageWidth)), random.randint(0, (baseImageHeight-resizedClickbaitImageHeight))), resizedClickbaitImage.convert('RGBA'))

        #Add text
        draw = ImageDraw.Draw(baseImageCopy)
        font = ImageFont.truetype("Calibri Regular.ttf", 125)
        draw.text((50,60), thumbnailTitle.upper(), (111,255,255), font=font)

        #Save Thumbnail
        print("Saving Thumbnail...")
        baseImageCopy.save("C:/Users/"+checkuser+"/Documents/VCC/Today\'s Upload/FinalThumbnail.png")
        print("Thumbnail Created!")
