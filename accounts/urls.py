from django.urls import path
from .views import profile, login_view,refresh_token_view  
urlpatterns = [
    path('profile', profile, name= 'profile'),
    path('login', login_view, name= 'login'),
    path('refresh_token', refresh_token_view, name='refresh_token')
]