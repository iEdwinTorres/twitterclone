from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification


@login_required
def notification_view(request):
    notifications = Notification.objects.filter(n_receiver=request.user)
    notification_count = 0
    new_notifications = []
    for notification in notifications:
        if notification.notification_read == False:
            notification_count += 1
            new_notifications.append(notification.tracked_tweet)
            notification.notification_read = True
            notification.save()
    return render(
        request,
        "notifications_view.html",
        {
            "new_notifications": new_notifications,
            "notification_count": notification_count,
        },
    )


def notification_new_count(request):
    notifications = Notification.objects.filter(n_receiver=request.user)
    notification_count = 0
    for notification in notifications:
        if notification.notification_read == False:
            notification_count += 1
    return notification_count
