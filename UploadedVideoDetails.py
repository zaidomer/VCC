import os
import getpass


class UploadedVideoDetails:
    checkuser = getpass.getuser()
    videoPath = 'C:\Users\\' + checkuser + '\Documents\VCC\Today\'s Video\\'

    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "public"
