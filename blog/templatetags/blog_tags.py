from django import template
from blog.models import Post
from django.db.models import Count

register = template.Library()

# Custom template tag to get the latest posts
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

    """Return the most commented posts."""
    return Post.published.annotate(num_comments=Count('comments')).order_by('-num_comments')[:count]

@register.simple_tag
def latest_posts(count=3):
    """Return the latest 'count' published posts."""
    return Post.published.all()[:count]

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}