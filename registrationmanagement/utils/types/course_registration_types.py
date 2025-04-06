from typing import Optional

from django.db.models import QuerySet

from registrationmanagement.models import CourseRegistration

CourseRegistrationType = Optional[CourseRegistration]
CourseRegistrationQuerySetType = QuerySet[CourseRegistration]
