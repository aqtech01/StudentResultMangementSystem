from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.models import Course, SessionYear, CustomUser, Student


@login_required(login_url="/")
def hod_home(request):
    return render(request, "hod/home.html")


@login_required(login_url="/")
def add_students(request):
    courses = Course.objects.all()
    sessions = SessionYear.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        session_year_id = request.POST.get("session_year_id")
        # print(profile_pic,first_name,last_name,email,username,password,address,gender,course_id,session_year_id)
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already is taken")
            return redirect("add_students")
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already is taken")
            return redirect("add_students")
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,

            )
            user.set_password(password)
            user.save()
            course_id = Course.objects.get(id=course_id)
            session_year = SessionYear.objects.get(id=session_year_id)  #
            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course_id,
                gender=gender

            )
            student.save()
            messages.success(request, "Student are successfully created")
            return redirect("hod_student_view")

    context = {
        'courses': courses,
        'sessions': sessions,

        'title': 'Add Students',
    }

    return render(request, "hod/add-students.html", context)


def hod_student_view(request):
    students = Student.objects.all()
    context = {
        "students": students,
        "title": "View Student",
    }
    return render(request, "hod/view_student.html", context)


def edit_student(request, id):
    students = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    sessions = SessionYear.objects.all()
    if request.method == "POST":
        # CustomUser Model Fields
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Student Model
        address = request.POST.get("address")
        gender = request.POST.get("gender")

        course_id = request.POST.get("course")

        # Session Year Model
        session_year_id = request.POST.get("session_year")

        # Update CustomUser fields
        user = students.admin
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if profile_pic:
            user.profile_pic = profile_pic
        if password:
            user.set_password(password)
        user.save()

        # Update Student fields
        students.address = address
        students.gender = gender
        # Update Course and Session Year
        students.course_id = Course.objects.get(id=course_id)
        students.session_year_id = SessionYear.objects.get(id=session_year_id)

        students.save()
        messages.success(request, "Student was successfully updated")
        return redirect("hod_student_view", id=id)

    context = {
        "students": students,
        "courses": courses,
        "sessions": sessions,
        "title": "Edit Student",
    }
    return render(request, "hod/edit_student.html", context)


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Student was successfully deleted")
    return redirect("hod_student_view")


# Create Course

def add_course(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # Additional course fields can be added here
        course = Course(name=name)  # Create a Course object with the provided name

        # Check for duplicate name
        if Course.objects.filter(name=name).exists():
            messages.error(request, "Course with that name already exists.")
        else:
            course.save()  # Save the course object to the database
            messages.success(request, "Course successfully created!")
            return redirect("view_course")  # Redirect to the HoD home page after successful creation

    return render(request, "hod/add_course.html")


def view_course(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
        "title": "View Course",
    }
    return render(request, "hod/view_course.html", context)


def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        name = request.POST.get("name")

        # Check for duplicate name (excluding the current course)
        if Course.objects.filter(name=name).exclude(id=id).exists():
            messages.error(request, "Course with that name already exists.")
        else:
            course.name = name
            course.save()  # Save the updated course object to the database
            messages.success(request, "Course successfully updated!")
            return redirect("view_course", id=id)  # Redirect back to the edit page after successful update

    context = {
        "course": course,
        "title": "Edit Course",
    }
    return render(request, "hod/edit_course.html", context)



def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    messages.success(request, "Course successfully deleted!")
    return redirect("view_course")  # Redirect to a list of courses or another relevant page
