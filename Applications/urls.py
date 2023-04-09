from django.urls import path
from .views import create_application

urlpattern = [
    path('create_application', create_application, name='application')
    
]