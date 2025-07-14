from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.db.models import Count  # Importing Count for similar posts
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Post

from taggit.models import Tag

from .forms import CommentForm

# function for the share view
def post_share(request, post_id):
    # Retrieve the post by its ID
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    
    # Handle the form submission (for example, sharing via email)
    # (You could also implement a URL to share, or social media integration)
    
    # Placeholder for sharing functionality: send email with the post link
    if request.method == 'POST':
        # Assuming the form includes a field for email
        email = request.POST.get('email')
        if email:
            subject = f"Check out this post: {post.title}"
            message = f"Here's a link to the post: {post.get_absolute_url()}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            return render(request, 'blog/post/share_done.html', {'post': post})
    
    # Render the share form (you can create a simple form in the template for email submission)
    return render(request, 'blog/post/share.html', {'post': post})


# Class-based view to list posts with pagination
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# Function-based view to list posts with optional tag filtering and pagination
def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'tag': tag
        }
    )


# View to display a single post’s details
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    # List of active comments for the post
    comments = post.comments.filter(active=True)
    # Form for users to comment on the post
    form = CommentForm()

    # List of similar posts based on shared tags
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=post_tags_ids
    ).exclude(id=post.id)

    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')
    ).order_by('-same_tags', '-publish')[:4]

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form,
            'similar_posts': similar_posts  # Adding similar posts to the context
        }
    )


# View to handle a submitted comment
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )
