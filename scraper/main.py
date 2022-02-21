from datetime import datetime

from fastapi import FastAPI, status

from db import db_init

import twitter
from models import TwitterQuery
from utils import logger, calculate_total_sentiment
import web
import dailymotion
import reddit

app = FastAPI()

twitter_collection = db_init.twitter_collection

# Home/welcome route
@app.get("/")
def read_root():
    return "Main Scraper API Root"


# get single tweeter user
@app.post("/twitter/track_username/{username}", status_code=status.HTTP_201_CREATED)
async def get_user(username: str):
    """Getting Twitter user using username

    Args:
        username (str):

    Returns:
        user (str):
    """
    if username:
        try:
            user = twitter_collection.find_one({"twitter_user.screen_name": username})
        except Exception as e:
            return e.args
        if user:
            return f'{user["twitter_user"]["screen_name"]} already in DB'
        else:
            try:
                user, user_id = await twitter.get_user_data(username)
                try:
                    twitter_collection.insert_one(
                        {"_id": int(user.id), "twitter_user": user._json}
                    )
                except Exception as e:
                    logger.error(f"{e}")
                return {"user": user._json}
            except Exception as e:
                logger.error(f"{e}")


@app.get("/twitter/followers/{username}")
async def get_followers(username):
    if username != "null":
        try:
            followers = await twitter.get_user_followers(username)
            return followers
        except Exception as e:
            return e.args


@app.get("/twitter/tweets/{query}")
async def get_tweets(query):
    """Tweets realted to a particular topic.

    Args:
        query (str):

    Returns:
        bool: True/False (done/error)

    Processing information results:
    1- Total number of tweets
        1.1 Total tweets over time (if enough data)
    2- Sentiment score for the topic
        2.2- Sentiment over time
    3- Users' stats
        3.1- Total users active
            3.1.1- Total active users over time (shows interest in the topic)
        3.2- Users' followers distribution
        3.3- Top 3 active users
        3.4- Top 3 active users' sentiments

    """
    twitter_pages = await twitter.get_tweets(query)

    tweets = []
    total_followers = 0
    total_favorits = 0
    total_retweets = 0

    users = []

    for page in twitter_pages:
        try:
            # in case of a re-tweeted tweet
            total_followers += page._json["retweeted_status"]["user"]["followers_count"]
            total_favorits += page._json["retweeted_status"]["favorite_count"]
            total_retweets += page._json["retweeted_status"]["retweet_count"]
            tweets.append({"tweet": page._json["retweeted_status"]})

            users.append(page._json["retweeted_status"]["user"])

        except:
            total_followers += page._json["user"]["followers_count"]
            total_favorits += page._json["favorite_count"]
            total_retweets += page._json["retweet_count"]
            tweets.append({"tweet": page._json})

            users.append(page._json["user"])

    # Check sentiments of the tweets - get summary back
    tweets_sentiment = calculate_total_sentiment(
        tweets, total_followers, total_favorits, total_retweets
    )

    # Sort and filter the users that made the tweets. Return users list, their followers count
    # Store/Create/Update the leading users. Return "success"

    query_obj = TwitterQuery(
        created=datetime.now(),
        query_text=query,
        tweets_count=len(tweets),
        tweets=tweets,
        sentiment_score=tweets_sentiment,
        users=users,
    )
    try:
        twitter_collection.insert_one({"twitter_query": dict(query_obj)})
    except Exception as e:
        logger.error(f"{e}")

    return {
        "query": query,
        "total_tweets": len(tweets),
        "tweets_sentiment": tweets_sentiment,
    }


@app.get("/google/{query}")
async def google_search(query):
    """Google search query. 10 results sentiment"""
    google_sentiment = web.google_search(search_term=query)
    return google_sentiment


@app.get("/dailymotion/{query}")
async def dailymotion_search(query):
    """Access Dailymotion videos sentiment"""
    dailymotion_sentiment = dailymotion.get_dailymotion(query)
    return dailymotion_sentiment


@app.get("/reddit/{query}")
def reddit_search(query):
    """Access Reddit posts and subreddits for sentiment"""
    reddit_sentiment = reddit.get_reddit(query)
    return reddit_sentiment
