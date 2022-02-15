from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    followers: int
    space: Optional[str]
    tracked: Optional[bool] = True


# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
class TwitterQuery(BaseModel):
    created: datetime
    query_text: str
    tweets_count: int = 0
    tweets: list
    sentiment_score: dict
    users: list


# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
class TwitterUser(BaseModel):
    created: datetime
    twitter_id: str
    screen_name: str
    followers_count: int
    statuses_count: int
