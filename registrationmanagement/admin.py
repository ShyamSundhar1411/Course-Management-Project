from django.contrib import admin

from registrationmanagement.utils.admin_builders import CustomUserAdmin

from .models import Course, CourseRegistration, Faculty, Student, User

admin.site.register(Course)
admin.site.register(User, CustomUserAdmin)
admin.site.register(CourseRegistration)
admin.site.register(Student)
admin.site.register(Faculty)
