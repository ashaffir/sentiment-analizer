from unicodedata import name
from django.urls import path

from . import views

app_name = "scraper"

urlpatterns = [
    path("source-process/", views.SourceScrape.as_view(), name="source-process"),
    path("twitter/<str:query>/", views.GetTwitter.as_view(), name="twitter"),
]
