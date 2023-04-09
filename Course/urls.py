from django.urls import path
from .views import *

urlpatterns = [
    path('add', add_course_details, name='add'),
    path('fetch_course', get_all_course, name='fetch_course'),
    path('update/<int:pk>', update_course_details, name='update'),
    path('delete/<int:pk>', delete_course_details, name='delete'),
]