from django.contrib import admin

from .models import Course, CourseRegistration, Faculty, Student, User

# Register your models here.

admin.site.register(Course)
admin.site.register(User)
admin.site.register(CourseRegistration)
admin.site.register(Student)
admin.site.register(Faculty)
