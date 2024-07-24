from django.shortcuts import render
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
    
    return render(request, "staff/notification.html")
