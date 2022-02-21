import time
import tweepy  # https://docs.tweepy.org/en/stable/
from decouple import config
from utils import logger

consumer_key = config("TWITTER_CONSUMER_KEY")
consumer_secret = config("TWITTER_CONSUMER_SECRET")
access_token = config("TWITTER_ACCESS_TOKEN")
access_token_secret = config("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = config("TWITTER_BEARER_TOKEN")

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


async def get_public_tweets_gen():
    public_tweets = api.home_timeline()
    return public_tweets


async def get_user_data(username):
    user = api.get_user(screen_name=username)
    return user, user.id_str


async def get_user_followers(username):
    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.get_follower_ids, screen_name=username).pages():
        if page_count > 1:
            break
        ids.extend(page)
        time.sleep(0.1)
        page_count += 1
    return ids


async def get_tweets(query: str):
    pages = []
    page_count = 0
    for page in tweepy.Cursor(
        api.search_tweets, q=query, count=5, tweet_mode="extended"
    ).pages():
        if page_count > 2:
            break

        pages.extend(page)
        logger.info(f"{page_count=}")
        time.sleep(0.1)
        page_count += 1

    return pages
