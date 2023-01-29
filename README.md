# Twitter-Scraping
My first project as bignner data scientist (still in the course) to create a simple GUI used to scarpe twitter data with given keyword and limit and downloading it into file.

# Table of Contents
* Using Snscrape to scapr data from twitter
* Using Streamlit to create a simple GUI
* Bacis Workflow

## Snscrape
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.  For reference:https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721

The following services are currently supported:

* Facebook: user profiles, groups, and communities (aka visitor posts)
* Instagram: user profiles, hashtags, and locations
* Mastodon: user profiles and toots (single or thread)
* Reddit: users, subreddits, and searches (via Pushshift)
* Telegram: channels
* Twitter: users, user profiles, hashtags, searches, tweets (single or surrounding thread), list posts, and trends
* VKontakte: user profiles
* Weibo (Sina Weibo): user profiles

### Requirements
snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.

### Installation
    pip3 install snscrape

If you want to use the development version:

    pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

### Usage
#### CLI
The generic syntax of snscrape's CLI is:

    snscrape [GLOBAL-OPTIONS] SCRAPER-NAME [SCRAPER-OPTIONS] [SCRAPER-ARGUMENTS...]

`snscrape --help` and `snscrape SCRAPER-NAME --help` provide details on the options and arguments. `snscrape --help` also lists all available scrapers.

The default output of the CLI is the URL of each result.

Some noteworthy global options are:

* `--jsonl` to get output as JSONL. This includes all information extracted by snscrape (e.g. message content, datetime, images; details vary by scraper).
* `--max-results NUMBER` to only return the first `NUMBER` results.
* `--with-entity` to get an item on the entity being scraped, e.g. the user or channel. This is not supported on all scrapers. (You can use this together with `--max-results 0` to only fetch the entity info.)

##### Examples
Collect all tweets by Jason Scott (@textfiles):

    snscrape twitter-user textfiles

It's usually useful to redirect the output to a file for further processing, e.g. in bash using the filename `twitter-@textfiles`:

```bash
snscrape twitter-user textfiles >twitter-@textfiles
```

To get the latest 100 tweets with the hashtag #archiveteam:

    snscrape --max-results 100 twitter-hashtag archiveteam

#### Library
It is also possible to use snscrape as a library in Python, but this is currently undocumented.

### Issue reporting
If you discover an issue with snscrape, please report it at <https://github.com/JustAnotherArchivist/snscrape/issues>. If possible please run snscrape with `-vv` and `--dump-locals` and include the log output as well as the dump files referenced in the log in the issue. Note that the files may contain sensitive information in some cases and could potentially be used to identify you (e.g. if the service includes your IP address in its response). If you prefer to arrange a file transfer privately, just mention that in the issue.

### License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.


## Streamlit
Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our Community Cloud platform to deploy, manage, and share your app!
 For reference: https://docs.streamlit.io/library/get-started


## Basic WorkFlow
* First Install the requirements present in the requirements.txt using pip install -r requirements.txt
* Using snscrape we write a code to scrape data from twitter using keyword/hastag and number of tweets limit by user as input
![snscrape](https://user-images.githubusercontent.com/119933313/215355502-c19c1e1a-e2a3-40f0-9565-4d45a92a66d5.png)

* Then we use streamlit to create a simple GUI where we take data from user and show that data on the same page
![form](https://user-images.githubusercontent.com/119933313/215355501-f347a39c-05ee-4006-a27e-30a2914dfa00.png)

* We also create a download button for downloading the data in cvs and json file format.
![download_button](https://user-images.githubusercontent.com/119933313/215355500-ea7b1528-1bfe-45af-a461-7eb81ef56806.png)


###*Then run the program and it will take you to a streamlit GUI page in the web browser.
* You will see a form which will require you to fill the keyword/hastag you want to search and the number of tweets and how your downloaded file name.
![front](https://user-images.githubusercontent.com/119933313/215357417-a31ea015-b299-46bb-92f5-1098807b223f.png)

* Then *click* on the submit button and in a few sec you will be able to see your data below.
![datacapture](https://user-images.githubusercontent.com/119933313/215357414-1e104699-67dd-407a-9f84-683f0acad816.png)

* You can also download the data file in json and csv by clicking in the dowload option at the botom.
![download_option](https://user-images.githubusercontent.com/119933313/215357416-7b5b9de8-f4bc-4d55-9d01-5a72b6561172.png)









