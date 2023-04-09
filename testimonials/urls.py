from django.urls import path
from .views import *

urlpattern = [
    path('add', add_testimonial_details, name='add'),
    path('fetch', get_all_testimonial, name='fetch'),
    path('delete/<int:pk>', delete_testimonial_details, name='delete')
]