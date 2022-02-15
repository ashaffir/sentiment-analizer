from django.db import models


class DataSource(models.Model):
    """Data source from which to scrape data"""

    name = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"
