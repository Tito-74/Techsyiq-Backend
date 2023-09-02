from django.urls import path
from .views import get_all_category,update_category_details, delete_category, create_blog_details,get_all_blogs, get_single_blog_details, update_blog_details, delete_blog_details,categoryView, add_author_details, get_all_authors, get_single_author_details, delete_author_details, update_author_details
urlpatterns = [
    # path('create_category', create_category, name='category'),
    path('create_category', categoryView.as_view()),
    path('get_category', get_all_category, name='get_category'),
    path('update_category/<int:pk>', update_category_details, name='update_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
    # blog
    path('create_blog', create_blog_details, name='create_blog'),
    path('fetch_blogs', get_all_blogs, name='fetch_blogs'),
    path('fetch_blog/<int:pk>', get_single_blog_details, name='fetch_blog'),
    path('update_blog/<int:pk>', update_blog_details, name='update_blog'),
    path('delete_blog/<int:pk>', delete_blog_details, name='delete_blog'),

    # author
    path('add_author_detail', add_author_details, name='add_author'),
    path('fetch_all_author',get_all_authors , name='fetch_authors'),
    path('fetch_single_author/<int:pk', get_single_author_details, name='single_author'),
    path('delete_author/<int:pk>',delete_author_details, name='delete_author'),
    path('update_author_details/<int:pk>', update_author_details, name="update_author"),


]