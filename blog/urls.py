from django.urls import path
from .views import create_category, get_all_category,update_category_details, delete_category, create_blog_details
urlpatterns = [
    path('create_category', create_category, name='category'),
    path('get_category', get_all_category, name='get_category'),
    path('update_category/<int:pk>', update_category_details, name='update_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
    # blog
    path('create_blog', create_blog_details, name='create_blog')
    path('fetch_blogs', get_all_blogs, name='fetch_blogs')
    
]