from django.urls import path
from .views import create_application,get_all_application_details

urlpatterns = [
    path('create_application', create_application, name='application'),
    path('fetch_application', get_all_application_details, name='fetch_application')
]