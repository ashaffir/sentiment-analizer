import requests
import re
import emoji
from logging.config import dictConfig
import logging
from log_config import LogConfig
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

dictConfig(LogConfig().dict())
logger = logging.getLogger("scraper")


def clean_sentance(text: str):
    remove_emoji = emoji.demojize(text)
    clean_text = " ".join(re.findall(r"\w+", remove_emoji))
    return clean_text


def get_sentiment(sentence: str):
    sia = SentimentIntensityAnalyzer()
    sentance_sentiment = sia.polarity_scores(sentence)
    return sentance_sentiment


def calculate_total_sentiment(tweets, total_followers, total_favorits, total_retweets):

    tweets_sentiments = []

    for tweet in tweets:
        text = tweet["tweet"]["full_text"]
        user_followers = tweet["tweet"]["user"]["followers_count"]
        favorite_count = tweet["tweet"]["favorite_count"]
        retweet_count = tweet["tweet"]["retweet_count"]

        clean_text = clean_sentance(text)
        sentiment = get_sentiment(clean_text)

        # Weighted sentiment calculation
        followers_weight = (total_followers - user_followers) / total_followers
        favorite_weight = (total_favorits - favorite_count) / total_favorits
        retweet_weight = (total_retweets - retweet_count) / total_retweets

        weights_average = (followers_weight + favorite_weight + retweet_weight) / 3

        sentiment.update((k, v * (1 - weights_average)) for k, v in sentiment.items())
        tweets_sentiments.append(sentiment)

    negatice = 0.0
    neutral = 0.0
    positive = 0.0
    total = 0.0
    summary = dict()
    for senti in tweets_sentiments:
        negatice += senti["neg"]
        neutral += senti["neu"]
        positive += senti["pos"]
        total += senti["compound"]

    summary["negative"] = round((negatice / len(tweets_sentiments)) * 1000)
    summary["neutral"] = round((neutral / len(tweets_sentiments)) * 1000)
    summary["positive"] = round((positive / len(tweets_sentiments)) * 1000)
    summary["total"] = round((total / len(tweets_sentiments)) * 1000)
    return summary


def blob_sentiment(messages: list):
    clean_text = ""

    for message in messages:
        clean_sen = clean_sentance(message)
        clean_text += clean_sen

    senti = {k: 100 * v for k, v in get_sentiment(clean_text).items()}
    sentiment = {
        "negative": senti["neg"],
        "neutral": senti["neu"],
        "positive": senti["pos"],
        "total": senti["compound"],
    }
    return sentiment
