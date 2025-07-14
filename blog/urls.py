from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post list view (using class-based view)
    path('', views.PostListView.as_view(), name='post_list'),  # This should be for the homepage (blog index)

    # Post list filtered by tag
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),  # Post list filtered by tag

    # Post detail view
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),

    # Post share view
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    # Post comment submission view
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
