from django.contrib import messages
from django.shortcuts import render, redirect

from core.models import *


def student_home(request):
    return render(request, "student/home.html")


def student_notification(request):
    try:
        student = Student.objects.get(admin=request.user.id)
        notifications = StudentNotification.objects.filter(student_id=student.id)

        context = {
            "notifications": notifications,
            "title": "View Notifications",
        }
        return render(request, "student/notification.html", context)
    except Student.DoesNotExist:
        messages.error(request, "No student found for the current user.")
        return redirect('home')


def mark_done(request, notification_id):
    try:
        notification = StudentNotification.objects.get(id=notification_id, student_id__admin=request.user.id)
        notification.status = 1
        notification.save()
        messages.success(request, "Notification marked as done.")
    except StudentNotification.DoesNotExist:
        messages.error(request, "Notification not found or you do not have permission to mark it as done.")
    return redirect('student_notification')


def student_feedback(request):
    student_id = Student.objects.get(admin=request.user.id)
    feed_back_history = StudentFeedBack.objects.filter(student_id=student_id)
    context = {
        "feed_back_history": feed_back_history,
    }
    return render(request, "student/student_feedback.html", context)

    # return render(request, "student/student_feedback.html")


def student_feedback_save(request):
    if request.method == "POST":
        feed_back = request.POST.get("feed_back")
        student_id = Student.objects.get(admin=request.user.id)
        feedBack = StudentFeedBack(
            student_id=student_id,
            feed_back=feed_back,
            feed_back_reply="",
        )
        feedBack.save()
        messages.success(request, "feedback sent successfully")
        return redirect("student_feedback")
