from django.urls import path
from .views import create_category, get_all_category
urlpatterns = [
    path('create', create_category, name='category'),
    path('get_category', get_all_category, name='get_category'),
    
]