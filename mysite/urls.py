"""
URL configuration for mysite project.
For more information see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap  # Ensure sitemaps.py exists with PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Ensure blog/urls.py exists
    path('account/', include('django.contrib.auth.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]

