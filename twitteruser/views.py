from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification import views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    def get(self, request):
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


class UserView(TemplateView):
    def get(self, request, user_id):
        target_user = TwitterUser.objects.filter(id=user_id).first()
        user_tweets = Tweet.objects.filter(author=target_user).order_by("-date")
        notification_count = views.notification_new_count(request)
        if request.user.is_authenticated:
            following = request.user.following.all()
        else:
            following = []
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
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "redirect_if_referer_not_found"))


def unfollow(request, user_id):
    current_user = request.user
    follow = TwitterUser.objects.filter(id=user_id).first()
    current_user.following.remove(follow)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "redirect_if_referer_not_found"))
