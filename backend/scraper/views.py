from http.client import HTTPResponse
from django.http import JsonResponse
import requests
from django.db import reset_queries
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

SCRAPER_API_URL = "http://localhost:8222"


class SourceScrape(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(f"Processing data source {request.data}...")
        return Response("ok", status=status.HTTP_200_OK)


class GetTwitter(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, query, **kwargs):
        response = requests.get(SCRAPER_API_URL + f"/twitter/tweets/{query}")
        return JsonResponse(response.json(), safe=False)
