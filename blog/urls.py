from django.urls import path, include
from django.contrib import admin
from . import views
from .feeds import LatestPostsFeed
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


app_name = 'blog'

urlpatterns = [
    urlpatterns = [
    path('', views.post_list, name='blog-home'),
    path('posts/', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]