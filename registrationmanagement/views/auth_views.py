from django.shortcuts import render

from registrationmanagement.forms.auth_forms import FacultyLoginForm, StudentLoginForm


def student_login(request):
    if request.method == "POST":
        pass
    return render(
        request,
        "registrationmanagement/student_login.html",
        {"form": StudentLoginForm()},
    )


def student_registration(request):
    return render(request, "registrationmanagement/student_registration.html")


def faculty_login(request):
    return render(
        request,
        "registrationmanagement/faculty_login.html",
        {"form": FacultyLoginForm()},
    )


def faculty_registration(request):
    return render(request, "registrationmanagement/faculty_registration.html")
