from django.urls import path
from .views import add_team_member, get_members, update_member_details,delete_member_details

urlpatterns = [
    path('add', add_team_member, name='add'),
    path('fetch', get_members, name='fetch'),
    path('update/<int:pk>', update_member_details, name='update'),
    path('delete/<int:pk>', delete_member_details, name='delete'),
]
