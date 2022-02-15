from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("results/", views.ResultsView.as_view(), name="results"),
    path("scraper/", include("scraper.urls")),
]
