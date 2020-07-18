import os
import getpass


class UploadedVideoDetails:

    title = "test title"
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "public"
    videosPath = None

    def __init__(videosPathFromMain):
        videosPath = videosPathFromMain

    def getFileName():
        for file in os.listdir(videosPath+"/Today's Upload"):
            return file
            break

