# Generated by Django 4.0.5 on 2025-04-08 12:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
