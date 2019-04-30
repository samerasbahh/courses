from django.contrib.auth.models import User
from rest_framework import serializers

from courses.models import *


# TODO: Make sure of Validation


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email')


class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Professor
    fields = ('url', 'name',)


class TimeSlotSerializer(serializers.ModelSerializer):
  start_time = serializers.TimeField(required=True)
  end_time = serializers.TimeField(required=True)


  def validate(self, data):
    """
    Check that start is before end.
    """
    if data['start_time'] > data['end_time']:
      raise serializers.ValidationError("End time must be after start time")
    return data

  class Meta:
    model = TimeSlot
    fields = ('url', 'course', 'start_time', 'end_time')


class CourseSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=30, required=True)
  cost = serializers.FloatField(required=True)

  timeslots = TimeSlotSerializer(read_only=True, source='timeslot_set', many=True)
  professor = ProfessorSerializer(read_only=True)

  class Meta:
    model = Course
    fields = ('url', 'id', 'name', 'cost', 'professor', 'timeslots')
