from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TwitterUser(AbstractUser):
    following = models.ManyToManyField("self", symmetrical=False)
