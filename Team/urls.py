from django.urls import path
from .views import add_team_member, get_members

urlpatterns = [
    path('add', add_team_member, name='add'),
    path('fetch', get_members, name='fetch'),
]
