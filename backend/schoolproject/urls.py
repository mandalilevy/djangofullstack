from django.contrib import admin
from django.urls import re_path  

from StudentApp import views

urlpatterns = [
    re_path(r'^student$',views.studentApi),
    re_path(r'^student$',views.studentApi),
    re_path(r'^student/([0-9]+)$',views.studentApi),
    re_path('admin/', admin.site.urls),
]