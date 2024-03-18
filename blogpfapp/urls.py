# blogp_app/urls.py
from django.urls import path
from .views import blog_list, delete_blog, web2db, frontpage, edit_blog
from . import views
urlpatterns = [
    path('blog/list/', blog_list, name='blog_list'),
    path('blog/<int:blog_id>/delete/', delete_blog, name='delete_blog'),
    path('web2db/', web2db, name='web2db'),
    path('', frontpage, name='frontpage'),
    path('blog/<int:blog_id>/edit/', edit_blog, name='edit_blog'),  # Add this line
    path('blogs/', views.blog_list, name='blog_list'),
]
