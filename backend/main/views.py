import os
import logging
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from nltk.sentiment.vader import SentiText
from .models import SentimentCheck

logger = logging.getLogger(__file__)


class HomeView(TemplateView):
    """Main page"""

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        try:
            check = SentimentCheck.objects.create(url=request.POST.get("input_url"))
            summary = check.calculate_overall_sentiment()
            check.sentiment = summary
            check.save()
        except Exception as e:
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
        except:
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
            return redirect(request.META["HTTP_REFERER"])

        return redirect(request.META["HTTP_REFERER"])
