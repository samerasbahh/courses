from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action, list_route
from rest_framework.response import Response

from courses.filters import CourseFilter
from courses.serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
  return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Professor.objects.all()
  serializer_class = ProfessorSerializer


class TimeSlotViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = TimeSlot.objects.all()
  serializer_class = TimeSlotSerializer


class CourseViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
  filterset_class = CourseFilter

  search_fields = ('name', 'professor__name')
  ordering_fields = ('name', 'cost','professor')
  ordering = ('name',)


  @list_route()
  def table_attr(self, request):
    data = {
      'filters': [
        {
          'name': 'name',
          'type': 'text',
          'label': 'Name',

        },
        {
          'name': 'cost',
          'type': 'number',
          'label': 'Cost',
        },
        {
          'name': 'professor__name',
          'type': 'text',
          'label': 'Professor',
        },
        {
          'name': 'timeslot__start_time',
          'type': 'time',
          'label': 'Start Time',
        },
        {
          'name': 'timeslot__end_time',
          'type': 'time',
          'label': 'End Time',
        }
      ],
      'headers': [
        {'name': 'name', 'label': 'Name', 'sortable': True},
        {'name': 'cost', 'label': 'Cost', 'sortable': True},
        {'name': 'professor', 'label': 'Professor', 'sortable': True},
        {'name': 'timeslots', 'label': 'TimeSlots', 'sortable': False},
      ]
    }
    return Response(data)
