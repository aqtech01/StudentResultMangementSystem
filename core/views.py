from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.email_back_end import EmailBackend
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from core.models import CustomUser

# Create your views here.
login_required(login_url="login")


def home(request):
    return render(request, "base.html")


def signin(request):
    context = {
        "title": "Login"
    }
    return render(request, "login.html", context)


def doLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == CustomUser.HOD:
                return redirect("hod_home")  # Replace with your actual URL name
            elif user_type == CustomUser.STAFF:
                return redirect("staff_home")  # Replace with your actual URL name
            elif user_type == CustomUser.STUDENT:
                return HttpResponse("Student")
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, "login.html")


def doLogout(request):
    logout(request)
    return redirect("login")


login_required(login_url="login")


def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        user: "user",
        "title": "Profile",
    }
    return render(request, "profile.html", context)


login_required(login_url="login")


def profile_update(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        profile_pic = request.FILES.get("profile_pic")
        password = request.POST.get("password")

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if profile_pic:
                customuser.profile_pic = profile_pic

            if password:
                customuser.set_password(password)
                update_session_auth_hash(request, customuser)  # Prevents logout after password change

            customuser.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")

        except CustomUser.DoesNotExist:
            messages.error(request, "User does not exist")
        except Exception as e:
            messages.error(request, f"Failed to update profile: {str(e)}")

    return render(request, "profile.html")
