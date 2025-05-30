from typing import Optional

from django.db.models import QuerySet

from registrationmanagement.models import Course

CourseType = Optional[Course]
CourseQuerySetType = QuerySet[Course]
