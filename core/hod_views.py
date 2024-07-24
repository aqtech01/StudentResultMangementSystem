from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.models import Course, SessionYear, CustomUser, Student, Staff, Subject, StaffNotification


@login_required(login_url="/")
def hod_home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male = Student.objects.filter(gender="Male").count()
    student_gender_female = Student.objects.filter(gender="Female").count()

    context = {
        "student_count": student_count,
        "staff_count": staff_count,
        "course_count": course_count,
        "subject_count": subject_count,
        "student_gender_male": student_gender_male,
        "student_gender_female": student_gender_female,
        "title": "Home",

    }
    return render(request, "hod/home.html", context)


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


# Staff Views

def add_staff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")

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
                user_type=2,

            )
            user.set_password(password)
            user.save()
            #
            staff = Staff(
                admin=user,
                address=address,
                gender=gender

            )
            staff.save()
            messages.success(request, "Staff successfully created")
            return redirect("add_staff")

    context = {
        'title': 'Add Students',
    }

    return render(request, "hod/add_staff.html", context)


def view_staff(request):
    staff = Staff.objects.all()
    context = {
        "staff": staff,
        "title": "View Staff"
    }
    return render(request, "hod/view_staff.html", context)


def edit_staff(request, id):
    staff = get_object_or_404(Staff, id=id)

    if request.method == "POST":
        # Fetch and update staff details
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        profile_pic = request.FILES.get("profile_pic")
        address = request.POST.get("address")
        gender = request.POST.get("gender")

        # Update CustomUser fields
        user = staff.admin
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if profile_pic:
            user.profile_pic = profile_pic
        if password:
            user.set_password(password)
        user.save()

        # Update Staff fields
        staff.address = address
        staff.gender = gender
        staff.save()

        messages.success(request, "Staff was successfully updated!")
        return redirect("view_staff", id=id)

    context = {
        "staff": staff,
    }
    return render(request, "hod/edit_staff.html", context)


def delete_staff(request, id):
    staff = get_object_or_404(Staff, id=id)

    # Example: Handle related records before deletion
    # Update or delete related records here
    # e.g., related_model.objects.filter(staff=staff).delete()

    try:
        # This will delete the associated CustomUser as well
        staff.delete()
        messages.success(request, "Staff was successfully deleted!")
    except IntegrityError:
        transaction.rollback()
        messages.error(request, "Cannot delete staff due to related records.")

    return redirect("staff_list")


def add_subject(request):
    courses = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        subject = Subject(
            name=name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subjects are Successfully added")
        return redirect("view_subject")

    context = {
        "courses": courses,
        "staff": staff,
        "title": "Add Subject",
    }
    return render(request, "hod/add_subject.html", context)


def view_subject(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects,
        "title": "View Subjects",
    }
    return render(request, "hod/view_subject.html", context)


def edit_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    courses = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")

        course = Course.objects.get(id=course_id)
        staff_member = Staff.objects.get(id=staff_id)

        subject.name = name
        subject.course = course
        subject.staff = staff_member
        subject.save()

        messages.success(request, "Subject updated successfully!")
        return redirect("view_subject")  # Assuming you have a view to list subjects

    context = {
        "subject": subject,
        "courses": courses,
        "staff": staff,
        "title": "Edit Subject",
    }
    return render(request, "hod/edit_subject.html", context)


def delete_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    # This will delete the associated CustomUser as well
    subject.delete()
    messages.success(request, "Staff was successfully deleted!")
    return redirect("view_subject")


# Add function
def add_session_year(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        if session_start and session_end:
            new_session = SessionYear(session_start=session_start, session_end=session_end)
            new_session.save()
            messages.success(request, "Session Created Successfully")

            return redirect('view_session_year')
        else:
            messages.error(request, "something wrong")

    return render(request, 'hod/add_session.html')


# View function
def view_session_year(request):
    sessions = SessionYear.objects.all()
    context = {
        "sessions": sessions,
        "title": "Session Year",
    }
    return render(request, "hod/view_session.html", context)


# Update function
def update_session_year(request, id):
    sessions = get_object_or_404(SessionYear, id=id)

    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        # Check for duplicate name (excluding the current course)

        sessions.session_start = session_start
        sessions.session_end = session_end
        sessions.save()  # Save the updated course object to the database
        messages.success(request, "Course successfully updated!")
        return redirect("view_session_year")  # Redirect back to the edit page after successful update

    context = {
        "sessions": sessions,
        "title": "Edit Session Year",
    }
    return render(request, "hod/edit_session.html", context)


# Delete function
def delete_session_year(request, id):
    session = get_object_or_404(SessionYear, id=id)
    # This will delete the associated CustomUser as well
    session.delete()
    messages.success(request, "Staff was successfully deleted!")
    return redirect("view_session_year")


def save_staff_notification(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        message = request.POST.get("message")
        staff = Staff.objects.get(admin=staff_id)

        notification = StaffNotification(
            staff_id = staff,

            message=message
        )
        notification.save()
        messages.success(request,"Notification send Successfully")
        return redirect("staff_send_notification")


def staff_leave_view(request):
    return render(request, "hod/staff_leave.html")
