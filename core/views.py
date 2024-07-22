from django.shortcuts import render
from core.email_back_end import EmailBackend
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def home(request):
    return render(request, "base.html")


def signin(request):
    context = {
        "title": "Login"
    }
    return render(request, "login.html", context)


def doLogin(request):
    return  Pass
