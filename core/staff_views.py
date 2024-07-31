from django.contrib import messages
from django.shortcuts import render, redirect
from core.models import *


def staff_home(request):
    return render(request, "staff/home.html")


def staff_send_notification(request):
    staff = Staff.objects.all()
    see_notification = StaffNotification.objects.all().order_by('id')
    context = {
        "staff": staff,
        "title": "Staff Notifation",
        "see_notification": see_notification,
    }
    return render(request, "staff/staff_send_notification.html", context)


def staff_view_notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = StaffNotification.objects.filter(staff_id=staff_id)

        context = {
            "notification": notification,
            "Title": "View Notification",
        }
    return render(request, "staff/notification.html", context)


def mark_done(request, status):
    notification = StaffNotification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect("staff_view_notification")


def staff_apply_leave(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = StaffLeave.objects.filter(staff_id=staff_id)
        context = {
            "staff_leave_history": staff_leave_history
        }
    return render(request, "staff/apply_leave.html", context)


def staff_leave_save(request):
    if request.method == "POST":
        date = request.POST.get("date")
        message = request.POST.get("message")
        staff_id = Staff.objects.get(admin=request.user.id)
        leave = StaffLeave(
            staff_id=staff_id,
            date=date,
            message=message

        )
        leave.save()
        messages.success(request, "Apply Successfully")
        return redirect("staff_apply_leave")

    # return render(request, "staff/apply_leave.html")


def staff_feedback(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feed_back_history = StaffFeedBack.objects.filter(staff_id=staff_id)
    context = {
        "feed_back_history": feed_back_history,
    }
    return render(request, "staff/feed_back.html", context)


def staff_feedback_save(request):
    if request.method == "POST":
        feed_back = request.POST.get("feed_back")
        staff_id = Staff.objects.get(admin=request.user.id)
        feedBack = StaffFeedBack(
            staff_id=staff_id,
            feed_back=feed_back,
            feed_back_reply="",
        )
        feedBack.save()
        messages.success(request, "feedback sent successfully")
        return redirect(("staff_feedback"))


def staff_take_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    session_year = SessionYear.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            session_year_id = request.POST.get("session_year_id")
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = SessionYear.objects.get(id=session_year_id)
            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
    context = {
        "subject": subject,
        "session_year": session_year,
        "title": "Take Attendance",
        "get_subject": get_subject,
        "get_session_year": get_session_year,
        "action": action,
        "students": students
    }
    return render(request, "staff/take_attendance.html", context)


def staff_save_attendance(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = SessionYear.objects.get(id=session_year_id)
        attendace = Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year,

        )
        attendace.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)
            p_students = Student.objects.get(id=int_stud)
            attendace_report = AttendanceReport(
                student_id=p_students,
                attendance_id=attendace,
            )
            attendace_report.save()
    return redirect("staff_take_attendance")

def staff_view_attendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = SessionYear.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            attendance_date= request.POST.get('attendance_date')
            get_subject= Subject.objects.get(id = subject_id)
            get_session_year = SessionYear.objects.get(id = session_year_id)

    context = {
        "subject":subject,
        "session_year":session_year,
        "action" : action,
        "get_subject":get_subject,
        "get_session_year":get_session_year,
        "attendance_date":attendance_date

    }

    return render(request, "staff/view_attendance.html",context)