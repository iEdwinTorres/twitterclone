"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as twitteruser
from tweet import views as tweet
from authentication import views as authentication
from notification import views as notification


urlpatterns = [
    path('', twitteruser.IndexView.as_view(), name="homepage"),
    path('login/', authentication.LoginView.as_view(), name="login"),
    path('signup/', authentication.SignUpView.as_view()),
    path('logout/', authentication.logout_view),
    path('user/<int:user_id>/', twitteruser.UserView.as_view()),
    path('tweet/<int:tweet_id>/', tweet.TweetView.as_view()),
    path('newtweet/', tweet.NewTweetFormView.as_view()),
    path("follow/<int:user_id>/", twitteruser.follow),
    path("unfollow/<int:user_id>/", twitteruser.unfollow),
    path("notifications/", notification.notification_view),
    path('admin/', admin.site.urls),
]
