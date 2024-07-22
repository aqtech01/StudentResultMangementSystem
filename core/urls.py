from django.urls import path
from core.views import *
from core.hod_views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("", signin, name="login"),
    path("dologin/", doLogin, name="doLogin"),
    path("dologout/", doLogout, name="logout"),

    # Profile Update
    path("profile/", profile, name="profile"),
    path("profile_update",profile_update, name= "profile_update"),

    # HoD Panel URL

    path("hod/home/", hod_home, name="hod_home"),
    path("add/students/", add_students, name="add_students"),

]