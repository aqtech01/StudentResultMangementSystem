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
    feed_back_history =StaffFeedBack.objects.filter(staff_id=staff_id)
    context = {
        "feed_back_history": feed_back_history,
    }
    return render(request, "staff/feed_back.html",context)


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

