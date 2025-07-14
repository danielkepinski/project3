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

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )

