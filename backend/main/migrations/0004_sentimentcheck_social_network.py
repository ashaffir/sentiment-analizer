# Generated by Django 4.0 on 2022-02-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_sentimentcheck_query_alter_sentimentcheck_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentimentcheck',
            name='social_network',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]