# Generated by Django 4.0 on 2022-02-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_sentimentcheck_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentimentcheck',
            name='query',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sentimentcheck',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]