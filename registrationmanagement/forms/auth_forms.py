from django import forms


class StudentLoginForm(forms.Form):
    registration_number = forms.CharField(label="Registration Number", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        fields = ["registration_number", "password"]


class FacultyLoginForm(forms.Form):
    employee_id = forms.CharField(label="Employee ID", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        fields = ["employee_id", "password"]
