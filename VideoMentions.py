from PIL import Image, ImageDraw, ImageFont
import getpass

class VideoMent:

    username = ''
    title = ''

    def __init__(self, user, ti):
        self.title = ti
        self.username = user
        for char in self.title:
            if char in "<>:\"/\\|?*":
                self.title = self.title.replace(char, '')
        self.title = self.title + '.png'

    def imageEditor(self):
        checkuser = getpass.getuser()
        image = Image.open('Twitch Shoutout Label.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('DIMIS___.TTF', size=125)
        (x, y) = (430, 82)
        color = 'rgb(108, 36, 152)'
        draw.text((x, y), self.username, fill=color, font=font)
        image.save('C:\\Users\\'+ checkuser +'\\Documents\\VCC\\Today\'s Clips\\' + self.title )
