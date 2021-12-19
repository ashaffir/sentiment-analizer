from django.contrib import admin
from .models import SentimentCheck


@admin.register(SentimentCheck)
class SentimentCheckAdmin(admin.ModelAdmin):
    list_fields = (
        "created",
        "url",
    )
