class RepCheck:

    def moveClips(self):

        today = open("Today.txt", "r")
        yesterday = open("yesterday.txt", "w+")

        yesterday.write(today.read())

        today.close()
        yesterday.close()

    def writeNewClips(self,clipTitles):

        today = open("Today.txt", "w+")

        for title in clipTitles:
            today.write(title + '\n')

        today.close()

    def checkClips(self,todayClip):

        yesterday = open("yesterday.txt", "r")
        if ((todayClip + '\n') in (yesterday.readlines())):
            return False
        else:
            return True

        yesterday.close()


