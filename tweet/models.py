from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    body = models.TextField(max_length=140, default="")
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.body