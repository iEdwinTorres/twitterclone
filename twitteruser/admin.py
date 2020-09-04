from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser

admin.site.register(TwitterUser, UserAdmin)