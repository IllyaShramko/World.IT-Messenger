# Generated by Django 5.2 on 2025-06-11 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_remove_customabstractuser_request_friends_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customabstractuser',
            name='friend_requests',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='FriendRequests',
        ),
    ]
