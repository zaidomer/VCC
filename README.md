# VCC

Automated YouTube Channel for Valorant Clips

## Getting Started

This will create folders to store the data, and it will use chromedriver.exe to have automated control of the webpages
[Valorant Clip Compilation](https://www.youtube.com/channel/UC5LvIuwCmRVFSEea194HS0A)

### Prerequisites

Libraries:

Libraries (Braullio):

```
pip install selenium
```
```
pip install requests
```
```
pip install pillow
```
```
pip install moviepy
```
```
https://chromedriver.chromium.org/downloads
```

Libraries (Zaid):
```
pip install --upgrade google-api-python-client
```
```
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```
```
pip install argparse
```
```
pip install python-http-client
```
```
pip3 install --upgrade oauth2client
```
```
pip install opencv-python
```
```
pip install google-auth-oauthlib
```
Install FFmpeg and follow https://github.com/elmoiv/redvid


## Running the tests

The code will display which function is currently being ran in order:

* Reset Folders
* Scrape Clip information
* Download Clips
* Create channel mention
* Add Mention to Clips
* Create timestamps
* Generate a title
* Generate a thumbnail
* Merge clips together
* Upload to YouTube
* Repeat

## Deployment

This was launched 8/8/20 as version 1.0. We had a few errors with repetition and resolution and version 1.1 is the current one that went live on 8/9/20

## Built With

* [Python V3.8.5](https://www.python.org/downloads/) - The language used to code it
* [Windows Server 2019](https://www.microsoft.com/en-ca/windows-server) - Server ran from the saftey of our home


## Contributing

[Braulio Carrion Corveira](https://github.com/Carr-23)
[Zaid Omer](https://github.com/zaidomer)

## Versioning

Currently on version 1.1
