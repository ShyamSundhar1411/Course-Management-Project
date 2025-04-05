from django.urls import path

from registrationmanagement.views import base_views

urlpatterns = [path("", base_views.home, name="home")]
