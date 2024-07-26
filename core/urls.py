from core.hod_views import *
from core.staff_views import *
from core.views import *
from core.student_views import *
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
    path("hod/staff_leave/", staff_leave_view, name="staff_leave_view"),
    path("hod/staff_leave/approve/<str:id>", staff_leave_approve, name="staff_leave_approve"),
    path("hod/staff_leave/approve/<str:id>", staff_leave_disapprove, name="staff_leave_disapprove"),
    path("hod_staffeed_back/", staff_feedback_reply, name="hod_staff_feedback_reply"),
    path("hod_staffeed_back/save", staff_feedback_reply_save, name="hod_staff_feedback_reply_save"),
    path("hod_student_feed_back/", student_feedback_reply, name="student_feedback_reply"),
    path("hod_student_feed_back/save/", student_feedback_reply_save, name="student_feedback_reply_save"),
    path("hod/student_leave/", student_leave_view, name="student_leave_view"),
    path("hod/student_leave/approve/<int:id>/", student_leave_approve, name="student_leave_approve"),
    path("hod/student_leave/disapprove/<int:id>/", student_leave_disapprove, name="student_leave_disapprove"),
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

    path("staff/home/", staff_home, name="staff_home"),
    path("hod/staff_notification", staff_send_notification, name="staff_send_notification"),
    path("hod/staff/save_notification", save_staff_notification, name="save_staff_notification"),
    path("hod/staff/notification", staff_view_notification, name="staff_view_notification"),
    path("staff/mark_done/notification<str:status>", mark_done, name="mark_done"),
    path("staff/apply_leave/", staff_apply_leave, name="staff_apply_leave"),
    path("staff/apply_leave/save", staff_leave_save, name="staff_leave_save"),
    path("staff/feedback/", staff_feedback, name="staff_feedback"),
    path("staff/feedback/save/", staff_feedback_save, name="staff_feedback_save"),
    path("staff/take/attendance/", staff_take_attendance, name="staff_take_attendance"),
    path("staff/save/attendance/", staff_save_attendance, name="staff_save_attendance"),
    path("staff/view/attendance/", staff_view_attendance, name="staff_view_attendance"),

    # StudentURL

    path("student/home", student_home, name="student_home"),
    path('send-notification/', student_send_notification, name='student_send_notification'),
    path('send-notification/save', student_send_notification_save, name='student_send_notification_save'),
    path("student/notification/", student_notification, name="student_notification"),
    path('notifications/mark-done/<int:notification_id>/', mark_done, name='mark_done'),
    path("student/feedback",student_feedback,name="student_feedback"),
    path("student/feedback/save", student_feedback_save, name="student_feedback_save"),
    path("student/apply_leave/", student_apply_leave, name="student_apply_leave"),
    path("student/apply_leave/save/", student_leave_save, name="student_leave_save"),
]
