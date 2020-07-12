import os
import getpass

checkuser = getpass.getuser()
if checkuser == 'zaid':
    videoPath = r"C:/Users/" + checkuser + 'l/Documents/VCC/Today\'s Video/'
else:
    videoPath = r"C:/Users/" + checkuser + '/Documents/VCC/Today\'s Video/'

print(videoPath)