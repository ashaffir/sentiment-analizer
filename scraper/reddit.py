"""
Reddit search API

Reference: https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/

"""
import re
import praw
import requests
from bs4 import BeautifulSoup as bs
from utils import blob_sentiment

REDDIT_CLIENT_ID = "s-_tD8jWv0TsaERqGeqG4g"
REDDIT_SECRET = "KMd_KBNKVnE2TWFnKPIlac6v70V-lw"
REDDIT_USER = "rookastle"

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER,
)


def get_reddit(query):
    url = f"https://www.reddit.com/search/?q={query}&t=day&sort=relevance"
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    posts = soup.find_all("div", {"class": "Post"})
    subreddits_names = []
    for post in posts:
        subreddits_names.append(
            post.find("a", {"href": re.compile("^/r/")})["href"].split("/")[2]
        )

    all_headlines = []

    for sub in subreddits_names:
        headlines = set()
        for submission in reddit.subreddit(sub).new(limit=20):
            headlines.add(submission.title)

        all_headlines += list(headlines)

    sentiment = blob_sentiment(all_headlines)
    return sentiment
