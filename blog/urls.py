from django.urls import path
from .views import create_category
urlpatterns = [
    path('', create_category, name='category'),
]