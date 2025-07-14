from django import template
from blog.models import Post

register = template.Library()

# Custom template tag to get the latest posts
@register.simple_tag
def latest_posts(count=3):
    """Return the latest 'count' published posts."""
    return Post.published.all()[:count]

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}