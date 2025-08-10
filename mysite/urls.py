from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog import views as blog_views
from .sitemaps import PostSitemap  # your sitemap class
from django.contrib.auth.views import LogoutView

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Blog URLs
    path('blog/', include('blog.urls', namespace='blog')),

    # Root/home page points to blog home
    path('', blog_views.post_list, name='blog-home'),

    # Accounts and auth
    path('accounts/', include('accounts.urls', namespace='accounts')),  # custom register view
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout/password views
    path('accounts/logout/', LogoutView.as_view(next_page='blog:blog-home'), name='logout'),
    # Sitemap
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]

