import argparse
import http.client
import httplib2
import os
import random
import time
import sys
import googleapiclient.discovery
import googleapiclient.errors

# import videoDetails

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client.tools import argparser, run_flow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.http import MediaFileUpload

from oauth2client import client 
from oauth2client import tools 
from oauth2client.file import Storage 

class YoutubeAPICommands:
  # Explicitly tell the underlying HTTP transport library not to retry, since
  # we are handling retry logic ourselves.
  httplib2.RETRIES = 1

  # Maximum number of times to retry before giving up.
  MAX_RETRIES = 10

  # Always retry when these exceptions are raised.
  RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
    http.client.IncompleteRead, http.client.ImproperConnectionState,
    http.client.CannotSendRequest, http.client.CannotSendHeader,
    http.client.ResponseNotReady, http.client.BadStatusLine)

  RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

  CLIENT_SECRETS_FILE = "client_secrets.json"

  YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"

  # This variable defines a message to display if the CLIENT_SECRETS_FILE is
  # missing.
  MISSING_CLIENT_SECRETS_MESSAGE = """
  WARNING: Please configure OAuth 2.0

  To make this sample run you will need to populate the client_secrets.json file
  found at:

    %s

  with information from the API Console
  https://console.developers.google.com/

  For more information about the client_secrets.json file format, please visit:
  https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
  """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    CLIENT_SECRETS_FILE))

  VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

  def __init__(self):
    print("Youtube API Starting...")

  def __getAuthenticatedService(self,args):
    flow = flow_from_clientsecrets(YoutubeAPICommands.CLIENT_SECRETS_FILE,
      scope=YoutubeAPICommands.YOUTUBE_UPLOAD_SCOPE,
      message=YoutubeAPICommands.MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
      credentials = run_flow(flow, storage, args)

    return build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
      http=credentials.authorize(httplib2.Http()))

  def __initializeUpload(self,youtube, options):
    tags = None
    if options.keywords:
      tags = options.keywords.split(",")

    body=dict(
      snippet=dict(
        title=options.title,
        description=options.description,
        tags=tags,
        categoryId=options.category
      ),
      status=dict(
        privacyStatus=options.privacyStatus
      )
    )

    insert_request = youtube.videos().insert(
      part=",".join(body.keys()),
      body=body,
      media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    self.__resumableUpload(insert_request)

  # This method implements an exponential backoff strategy to resume a
  # failed upload.
  def __resumableUpload(self,insert_request):
    response = None
    error = None
    retry = 0
    while response is None:
      try:
        print ("Uploading file...")
        status, response = insert_request.next_chunk()
        if response is not None:
          if 'id' in response:
            print ("Video id '%s' was successfully uploaded." % response['id'])
            YoutubeAPICommands.VIDEO_ID = response['id']
          else:
            exit("The upload failed with an unexpected response: %s" % response)
      except HttpError as e:
        if e.resp.status in YoutubeAPICommands.RETRIABLE_STATUS_CODES:
          error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                              e.content)
        else:
          raise
      except RETRIABLE_EXCEPTIONS as e:
        error = "A retriable error occurred: %s" % e

      if error is not None:
        print(error)
        retry += 1
        if retry > MAX_RETRIES:
          exit("No longer attempting to retry.")

        max_sleep = 2 ** retry
        sleep_seconds = random.random() * max_sleep
        print ("Sleeping %f seconds and then retrying..." % sleep_seconds)
        time.sleep(sleep_seconds)

  def __uploadThumbnail(self, videoPath, youtubeAuthenticator):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    print("Uploading Thumbnail...")

    request = youtubeAuthenticator.thumbnails().set(
        videoId=YoutubeAPICommands.VIDEO_ID,
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload(videoPath + "/VCC/Today\'s Upload/FinalThumbnail.png")
    )
    response = request.execute()

    print(response)
    print("\nThumbnail Uploaded!")

  def __createVideoDescription(self, urlGenerator, timeStamps):
    description = "Thank you for watching! Our videos wouldn't be possible without the clips we used. If you own a clip we have used and would not like your content to be used by us, contact us and we will prevent it from happening again. Thank you to all the streamers on Twitch who made this possible. \n\nHere are links to all the clips we've used: \n"
    count = 0
    for i in range (len(urlGenerator.clipLinks)):
      minutes = round(timeStamps[count]/60)
      seconds = round(timeStamps[count]%60)
      secondsString = str(seconds)

      if len(secondsString) < 2:
        secondsString = "0" + secondsString

      description += ("[" + str(minutes) + ":" + secondsString + "] " "\"" + urlGenerator.clipTitles[i] + "\" Content by Twitch streamer \"" + urlGenerator.clipUsers[i].capitalize() + "\" at " + urlGenerator.clipLinks[i] + "\n")
      count+=1
    description += "\nThis channel is fully automated, from creating the videos to the description you are reading right now. The entire process is controlled by our code. Special thanks to Gloomshot for the inspiration.\n\n"
    description += "INTRO AND OUTRO \nCredit to tiziano12122 for our into template at https://panzoid.com/creations/335902 \nCredit to KrissirK for our outro template at https://panzoid.com/creations/334842\n\n"
    description += "MUSIC LINKS \nintro: https://youtu.be/QF08nvtHHCY \noutro: https://youtu.be/tHP9cOnS1nQ"
    return description

  #This is the only function that should ever need to be used from main
  def uploadVideo(self, videoPath, urlGenerator, timeStamps):
    description = self.__createVideoDescription(urlGenerator, timeStamps)

    episodeNumberFile = open("EpisodeNumber.txt", "r+")
    episodeNumber = int(episodeNumberFile.read())

    print(videoPath+r"/VCC/Today's Upload/Final.mp4")
    argparser.add_argument("--file", help="Video file to upload", default=(videoPath+r"/VCC/Today's Upload/Final.mp4"))
    argparser.add_argument("--title", help="Video title", default=("Valorant Highlights Episode #" + str(episodeNumber+1)))
    argparser.add_argument("--description", help="Video description",default=description)
    argparser.add_argument("--category", default="22",help="Numeric video category. " +"See https://developers.google.com/youtube/v3/docs/videoCategories/list")
    argparser.add_argument("--keywords", help="Video keywords, comma separated",default="Valorant, gaming, Valorant Highlights")
    argparser.add_argument("--privacyStatus",default=YoutubeAPICommands.VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
    args = argparser.parse_args()

    if not os.path.exists(args.file):
      exit("Please specify a valid file using the --file= parameter.")

    youtube = self.__getAuthenticatedService(args)
    try:
      print("Video description: \n" + description + "\n\n")
      self.__initializeUpload(youtube, args)
      self.__uploadThumbnail(videoPath, youtube)
      episodeNumberFile.close()
      episodeNumberFile = open("EpisodeNumber.txt", "w")
      episodeNumberFile.write(str(episodeNumber+1))
      episodeNumberFile.close()
    except HttpError as e:
      print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))