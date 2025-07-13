from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # List of all published posts
    path('<int:id>/', views.post_detail, name='post_detail'),  # Single post detail page
]
