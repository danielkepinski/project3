from django.urls import path, include
from django.contrib import admin
from . import views
from .feeds import LatestPostsFeed
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # <-- you must import Post for add_comment


# Add comment view (you might want to keep or move this to views.py)
def add_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()
    # You should return a response in the 'else' case, example:
    return render(request, 'your_comment_form_template.html', {'form': form})


app_name = 'blog'


urlpatterns = [
    # Remove admin path from here!

    # Your app URLs:
    path('', views.home, name='blog-home'),

    # Post views
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    # RSS feed
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # Search
    path('search/', views.post_search, name='post_search'),

    # You can enable comment adding here if needed
    # path('post/<int:post_pk>/comment/', add_comment, name='add_comment'),
]
