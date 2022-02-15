"""
DailyMotion interaction model

API Docs: https://developer.dailymotion.com/api/#global-parameters

Dashboard: https://www.dailymotion.com/partner/x2mmbqp/channel/advanced
alfreds@actappon.com
10001
"""
import requests

from utils import blob_sentiment

DAILYMOTION_API_KEY = "585232c535cd4ab4c204"
DAILYMOTION_API_SECRET = "533e50389c0d06f1e516f619072d6664c5e7e869"


def get_dailymotion(query):
    daily_motion_url = f"https://api.dailymotion.com/videos?fields=id,created_time,description,title&search={query}&limit=100"
    response = requests.get(daily_motion_url)
    videos = response.json()["list"]
    contents = [video["description"] for video in videos]
    sentiment = blob_sentiment(contents)
    return sentiment
