from django.urls import path
from .views import create_category, get_all_category,update_category_details
urlpatterns = [
    path('create', create_category, name='category'),
    path('get_category', get_all_category, name='get_category'),
    path('update_category/<int:pk>', update_category_details, name='update_category')
]