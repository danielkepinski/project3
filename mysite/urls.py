from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog import views as blog_views
from .sitemaps import PostSitemap  # your sitemap class

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', blog_views.home, name='home'),  # root URL points to blog's home view
    path('account/', include('django.contrib.auth.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
