from core.hod_views import *
from core.staff_views import *
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
    # HOD Students URLS
    path("add/students/", add_students, name="add_students"),
    path("hod/student/view/", hod_student_view, name="hod_student_view"),
    path("hod/student/edit/<str:id>", edit_student, name="edit_student"),
    path('hod/delete_student/<str:id>/', delete_student, name='delete_student'),
    # HOD Course URLS
    path('hod/add_course/', add_course, name='add_course'),
    path('hod/view_course/', view_course, name='view_course'),
    path('edit_course/<int:id>/', edit_course, name='edit_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
    # HOD STAFF URLS
    path('hod/add_staff/', add_staff, name='add_staff'),
    path('hod/view_staff/', view_staff, name='view_staff'),
    path('edit_staff/<int:id>/', edit_staff, name='edit_staff'),
    path('delete_staff/<int:id>/', delete_course, name='delete_staff'),


    # Subjects
    path("hod/add/subject/", add_subject, name="add_subject"),
    path('hod/view_subject/', view_subject, name='view_subject'),
    path('edit_subject/<int:id>/', edit_subject, name='edit_subject'),
    path('delete_subject/<int:id>/', delete_subject, name='delete_subject'),

    # Session URLS
    path('hod/add/', add_session_year, name='add_session_year'),
    path('hod/view/', view_session_year, name='view_session_year'),
    path('hod/update/<int:id>/', update_session_year, name='update_session_year'),
    path('hod/delete/<int:id>/', delete_session_year, name='delete_session_year'),


    # This is Staff Urls

    path("staff/home/", staff_home, name="staff_home")

]
