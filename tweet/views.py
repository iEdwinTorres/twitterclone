from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from notification.views import notification_new_count
import re


@login_required(login_url="login")
def new_tweet_view(request):
    notification_count = notification_new_count(request)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body=data.get("body"),
                author=request.user,
            )
            mentions = re.findall(r"@(\w+)", data.get("body"))
            if mentions:
                for mention in mentions:
                    matched_user = TwitterUser.objects.get(username=mention)
                    if matched_user:
                        Notification.objects.create(
                            n_receiver=matched_user,
                            tracked_tweet=new_tweet,
                        )
            return HttpResponseRedirect(reverse("homepage"))

    form = TweetForm()
    return render(
        request,
        "new_tweet_view.html",
        {
            "form": form,
            "notification_count": notification_count,
        },
    )


def tweet_view(request, tweet_id):
    tweet_detail = Tweet.objects.filter(id=tweet_id).first()
    # notification_count = notification_new_count(request)
    return render(
        request,
        "tweet_view.html",
        {
            "tweet_detail": tweet_detail,
            "panel": "Use Info Panel",
            # "notification_count": notification_count,
        },
    )