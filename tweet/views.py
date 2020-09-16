from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.forms import TweetForm
from .models import Tweet, TwitterUser
from notification.models import Notification
from notification.views import notification_new_count
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import re


class NewTweetFormView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        form = TweetForm()
        return render(request, "new_tweet_view.html", {"form": form})

    def post(self, request):
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
        else:
            return render(request, "new_tweet_view.html", {"form": form})


class TweetView(TemplateView):
    def get(self, request, tweet_id):
        tweet_detail = Tweet.objects.filter(id=tweet_id).first()
        return render(
            request,
            "tweet_view.html",
            {
                "tweet_detail": tweet_detail,
                "panel": "Use Info Panel",
            },
        )
