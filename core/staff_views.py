from django.shortcuts import render


def staff_home(request):
    return render(request, "staff/home.html")