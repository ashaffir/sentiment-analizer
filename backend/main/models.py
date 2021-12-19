import re
import nltk
import urllib
import requests
from nltk.sentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup


from django.db import models
from django.db.models.base import ModelState

nltk.download("vader_lexicon")


class SentimentCheck(models.Model):
    """Saving information about a URL request from the website"""

    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)
    sentiment = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Sentiment check"
        verbose_name_plural = "Sentiment checks"

    def __str__(self) -> str:
        domain = urllib.parse.urlparse(self.url).netloc
        return f"Created: {self.created}. Root domain: {domain}"

    def get_page_text(self):
        html_doc = requests.get(self.url).content
        soup = BeautifulSoup(html_doc, "html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        return text

    def clean_text(self, text):
        text = (
            text.replace("\n", "").replace("\t", "").replace(":", "").replace(",", "")
        )
        # return re.findall(r'[A-Za-z]+', text)
        sentences = text.split(".")
        return sentences

    def get_sentiment(self, sentences: list):
        sia = SentimentIntensityAnalyzer()
        sentiments = []
        for sentence in sentences:
            senti_dict = sia.polarity_scores(sentence)
            sentiments.append(senti_dict)

        return sentiments

    def calculate_overall_sentiment(self):
        text = self.get_page_text()
        sentences = self.clean_text(text)
        sentiments = self.get_sentiment(sentences)

        negatice = 0.0
        neutral = 0.0
        positive = 0.0
        total = 0.0
        summary = dict()
        for senti in sentiments:
            negatice += senti["neg"]
            neutral += senti["neu"]
            positive += senti["pos"]
            total += senti["compound"]

        summary["negative"] = round((negatice / len(sentiments)) * 100)
        summary["neutral"] = round((neutral / len(sentiments)) * 100)
        summary["positive"] = round((positive / len(sentiments)) * 100)
        summary["total"] = round((total / len(sentiments)) * 100)
        return summary
