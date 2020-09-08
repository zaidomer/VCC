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

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
