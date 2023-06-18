# Generated by Django 4.2.2 on 2023-06-16 12:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="community",
            name="category",
            field=models.ManyToManyField(blank=True, to="api.category"),
        ),
        migrations.AlterField(
            model_name="community",
            name="membors",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
