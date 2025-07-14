from django import template
from blog.models import Post

register = template.Library()

# Custom template tag to get the latest posts
@register.simple_tag
def latest_posts(count=3):
    """Return the latest 'count' published posts."""
    return Post.published.all()[:count]