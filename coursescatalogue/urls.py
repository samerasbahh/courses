"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from courses import views
from courses.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'timeslots', views.TimeSlotViewSet)
# courses_table = CourseViewSet.as_view({'get': 'list'})
# router.register(r'courses_table', courses_table)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    # path('', views.index, name="index"),
  url(r'^$',
      TemplateView.as_view(template_name='index.html'),
      name='uHome'
      ),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
urlpatterns += staticfiles_urlpatterns()
