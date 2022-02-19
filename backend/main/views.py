import os
import requests
import logging
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from nltk.sentiment.vader import SentiText

from .models import SentimentCheck

logger = logging.getLogger(__file__)

SCRAPER_API_URL = "http://scraper:8222"


class HomeView(TemplateView):
    """Main page"""

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info(f'>>>>> {os.environ.get("SQL_DATABASE", "UNDEFINED")=}')
        logger.info(f'>>>>> {os.environ.get("SQL_USER", "UNDEFINED")=}')
        logger.info(f'>>>>> {os.environ.get("SQL_PASSWORD", "UNDEFINED")=}')
        logger.info(f'>>>>> {os.environ.get("SQL_HOST", "UNDEFINED")=}')

        return context

    def post(self, request):
        try:
            query = request.POST.get("input_url")

            if "twitter_search" in request.POST:
                response = requests.get(SCRAPER_API_URL + f"/twitter/tweets/{query}")
                print(f"{response.json()=}")
                check = SentimentCheck.objects.create(query=query)
                check.sentiment = response.json()["tweets_sentiment"]
                check.source = "twitter"
                check.messages_count = response.json()["total_tweets"]
                check.save()
            elif "google_search" in request.POST:
                response = requests.get(SCRAPER_API_URL + f"/google/{query}")
                print(f"{response.json()=}")
                check = SentimentCheck.objects.create(query=query)
                check.sentiment = response.json()
                check.source = "google"
                check.save()
            elif "dailymotion_search" in request.POST:
                response = requests.get(SCRAPER_API_URL + f"/dailymotion/{query}")
                print(f"{response.json()=}")
                check = SentimentCheck.objects.create(query=query)
                check.sentiment = response.json()
                check.source = "dailymotion"
                check.save()
            elif "reddit_search" in request.POST:
                response = requests.get(SCRAPER_API_URL + f"/reddit/{query}")
                print(f"{response.json()=}")
                check = SentimentCheck.objects.create(query=query)
                check.sentiment = response.json()
                check.source = "reddit"
                check.save()
            else:
                check = SentimentCheck.objects.create(url=query)
                summary = check.calculate_overall_sentiment()
                check.sentiment = summary
                check.save()
        except Exception as e:
            logger.error(e)
            messages.error(request, "Failed processing the URL")
            return redirect(request.META["HTTP_REFERER"])

        return redirect("main:results")


class ResultsView(TemplateView):
    template_name = "main/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            check = SentimentCheck.objects.last()
            context["data"] = check
        except Exception as e:
            pass

        return context

    def post(self, request):
        try:
            check = SentimentCheck.objects.create(url=request.POST.get("input_url"))
            summary = check.calculate_overall_sentiment()
            check.sentiment = summary
            check.save()
        except Exception as e:
            messages.error(request, "Failed processing the URL")
            logger.error(e)
            return redirect(request.META["HTTP_REFERER"])

        return redirect(request.META["HTTP_REFERER"])
