from django.contrib import messages
from django.shortcuts import redirect, render

from registrationmanagement.forms.auth_forms import (
    FacultyLoginForm,
    FacultySignUpForm,
    StudentLoginForm,
    StudentSignUpForm,
)
from registrationmanagement.services.auth_service import AuthService
from registrationmanagement.utils.auth_response_message import AuthResponseMessage


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
    if request.method == "POST":
        student_signup_form = StudentSignUpForm(request.POST)
        if student_signup_form.is_valid():
            _, error = AuthService.register_student(
                request, student_signup_form.cleaned_data
            )
            if error:
                messages.error(
                    request, AuthResponseMessage.REGISTRATION_UNSUCCESSFUL.value
                )
                return render(
                    request,
                    "registrationmanagement/student_registration.html",
                    {"form": student_signup_form},
                )

            messages.success(request, AuthResponseMessage.REGISTRATION_SUCCESSFUL.value)
            return redirect("home")
        return render(
            request,
            "registrationmanagement/student_registration.html",
            {"form": student_signup_form},
        )
    return render(
        request,
        "registrationmanagement/student_registration.html",
        {"form": StudentSignUpForm()},
    )


def faculty_login(request):
    if request.method == "POST":
        faculty_login_form = FacultyLoginForm(request.POST)
        if faculty_login_form.is_valid():
            _, error = AuthService.login_faculty(
                request, faculty_login_form.cleaned_data
            )
            if error:
                messages.error(request, error)
                return render(
                    request,
                    "registrationmanagement/faculty_login.html",
                    {"form": faculty_login_form},
                )
            messages.success(request, "Login successful")
            return redirect("home")
        return render(
            request,
            "registrationmanagement/faculty_login.html",
            {"form": faculty_login_form},
        )
    return render(
        request,
        "registrationmanagement/faculty_login.html",
        {"form": FacultyLoginForm()},
    )


def faculty_registration(request):
    if request.method == "POST":
        faculty_signup_form = FacultySignUpForm(request.POST)
        if faculty_signup_form.is_valid():
            _, error = AuthService.register_faculty(
                request, faculty_signup_form.cleaned_data
            )
            if error:
                messages.error(
                    request, AuthResponseMessage.REGISTRATION_UNSUCCESSFUL.value
                )
                return render(
                    request,
                    "registrationmanagement/faculty_registration.html",
                    {"form": faculty_signup_form},
                )

            messages.success(request, AuthResponseMessage.REGISTRATION_SUCCESSFUL.value)
            return redirect("home")
        return render(
            request,
            "registrationmanagement/faculty_registration.html",
            {"form": faculty_signup_form},
        )
    return render(
        request,
        "registrationmanagement/faculty_registration.html",
        {"form": FacultySignUpForm()},
    )
