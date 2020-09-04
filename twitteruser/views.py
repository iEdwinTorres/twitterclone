from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification import views


@login_required
def index_view(request):
    user_tweets = Tweet.objects.filter(author=request.user)
    following_tweets = Tweet.objects.filter(author__in=request.user.following.all())
    tweet_feed = user_tweets | following_tweets
    tweet_feed = tweet_feed.order_by("-date")
    notification_count = views.notification_new_count(request)
    return render(
        request,
        "index.html",
        {"tweet_feed": tweet_feed, "notification_count": notification_count},
    )


def user_view(request, user_id):
    target_user = TwitterUser.objects.filter(id=user_id).first()
    user_tweets = Tweet.objects.filter(author=target_user).order_by("-date")
    notification_count = views.notification_new_count(request)
    following = request.user.following.all()
    return render(
        request,
        "user_view.html",
        {
            "target_user": target_user,
            "user_tweets": user_tweets,
            "following": following,
            "notification_count": notification_count,
        },
    )


def follow(request, user_id):
    current_user = request.user
    follow = TwitterUser.objects.filter(id=user_id).first()
    current_user.following.add(follow)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def unfollow(request, user_id):
    current_user = request.user
    follow = TwitterUser.objects.filter(id=user_id).first()
    current_user.following.remove(follow)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
