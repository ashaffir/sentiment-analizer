from django.contrib import admin

from .models import DataSource


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    field_list = (
        "name",
        "url",
        "active",
    )

    ordered = "-name"

    search_fields = (
        "name",
        "url",
    )

    list_filter = (
        "name",
        "active",
    )
