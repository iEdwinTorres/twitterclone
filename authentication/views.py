from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from authentication import forms
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(TemplateView):
    def get(self, request):
        form = forms.SignupForm()
        return render(request, "signup_form.html", {"headline": "Sign Up to TwitterClone", "form": form})

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "signup_form.html", {"headline": "Sign Up to TwitterClone", "form": form})


class LoginView(TemplateView):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "login_form.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
            else:
                return render(request, "login_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))