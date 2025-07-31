from django.urls import path
from django.contrib import admin
from . import views
from .feeds import LatestPostsFeed
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


app_name = 'blog'

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Homepage and post list
    path('', views.post_list, name='blog-home'),         # Homepage
    path('posts/', views.post_list, name='post_list'),   # For tests and direct nav

    # Tag filtering
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # Post detail and actions
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    # RSS Feed
    path('feed/', LatestPostsFeed(), name='post_feed'),


    # Search
    path('search/', views.post_search, name='post_search'),
]