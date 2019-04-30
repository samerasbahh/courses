from django.contrib import admin


from django.contrib import admin
from .models import Course, Professor, TimeSlot

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(TimeSlot)
