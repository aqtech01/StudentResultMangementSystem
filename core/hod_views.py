from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def hod_home(request):
    return render(request, "hod/home.html")


@login_required(login_url="/")
def add_students(request):
    return render(request, "hod/add-students.html")
