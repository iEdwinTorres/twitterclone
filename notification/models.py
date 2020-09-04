from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    n_receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="receiver")
    tracked_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tracked")
    notification_read = models.BooleanField(default=False)
