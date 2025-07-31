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
    return render(request, 'your_comment_form_template.html', {'form': form})


app_name = 'blog'

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='blog-home'),

    # ✅ Added post list route to support tests and navigation
    path('posts/', views.post_list, name='post_list'),

    # Tag-based post filtering
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # Post detail and related actions
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    # RSS feed
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # Search
    path('search/', views.post_search, name='post_search'),

    # Optional: Direct comment form endpoint (currently unused)
    # path('post/<int:post_pk>/comment/', add_comment, name='add_comment'),
]
