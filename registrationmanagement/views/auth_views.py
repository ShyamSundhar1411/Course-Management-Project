from django.contrib import messages
from django.shortcuts import redirect, render

from registrationmanagement.forms.auth_forms import FacultyLoginForm, StudentLoginForm
from registrationmanagement.services.auth_services import AuthService


def student_login(request):
    if request.method == "POST":
        student_login_form = StudentLoginForm(request.POST)
        if student_login_form.is_valid():
            _, error = AuthService.login_student(
                request, student_login_form.cleaned_data
            )
            if error:
                messages.error(request, error)
                return render(
                    request,
                    "registrationmanagement/student_login.html",
                    {"form": student_login_form},
                )
            messages.success(request, "Login successful")
            return redirect("home")
        return render(
            request,
            "registrationmanagement/student_login.html",
            {"form": student_login_form},
        )
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
