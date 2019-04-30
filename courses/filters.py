import django_filters

from courses.models import Course


class CourseFilter(django_filters.FilterSet):

  class Meta:
    model = Course
    fields = {
      'name': ['icontains'],
      'cost': ['exact'],
      'professor__name': ['icontains'],
      'timeslot__start_time':['exact'],
      'timeslot__end_time':['exact']
    }
