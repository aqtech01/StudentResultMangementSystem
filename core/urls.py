from django.urls import path
from core.views import *

urlpatterns = [
    path("home", home, name="home"),
    path("", signin, name="login"),
    path("dologin/", doLogin, name="doLogin")
]