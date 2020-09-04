from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from tweet.models import Tweet

admin.site.register(Tweet)
