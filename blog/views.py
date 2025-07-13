from django.shortcuts import render, get_object_or_404
from .models import Post

# View to list all published posts
def post_list(request):
    # Retrieve all published posts using the custom manager
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',  # Template path
        {'posts': posts}        # Context dictionary
    )

# View to display a single post's details
def post_detail(request, id):
    # Try to retrieve a single post by ID and status
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',  # Template path
        {'post': post}            # Context dictionary
    )
