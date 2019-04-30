from django.db import models


class Professor(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)


class Course(models.Model):
  name = models.CharField(max_length=30)
  cost = models.FloatField()
  professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

  def __str__(self):
    return 'Name: %s \nCost: %s' % (self.name, self.cost)

  class Meta:
    ordering = ('name', 'cost','professor')


class TimeSlot(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  start_time = models.TimeField()
  end_time = models.TimeField()

  def __str__(self):
    return 'Course: %s \nStartTime: %s EndTime: %s' % (self.course.name, self.start_time, self.end_time)

  class Meta:
    ordering = ('start_time', 'end_time')
