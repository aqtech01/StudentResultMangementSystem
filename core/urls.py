from core.hod_views import *
from core.views import *
from django.urls import path

urlpatterns = [
    path("home/", home, name="home"),
    path("", signin, name="login"),
    path("dologin/", doLogin, name="doLogin"),
    path("dologout/", doLogout, name="logout"),

    # Profile Update
    path("profile/", profile, name="profile"),
    path("profile_update", profile_update, name="profile_update"),

    # HoD Panel URL

    path("hod/home/", hod_home, name="hod_home"),
    path("add/students/", add_students, name="add_students"),
    path("hod/student/view/", hod_student_view, name="hod_student_view"),
    path("hod/student/edit/<str:id>", edit_student, name="edit_student"),
    path('hod/delete_student/<str:id>/', delete_student, name='delete_student'),
    path('hod/add_course/', add_course, name='add_course'),
    path('hod/view_course/', view_course, name='view_course'),
    path('edit_course/<int:id>/', edit_course, name='edit_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),

]
