from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.db.models import Count  # Importing Count for similar posts
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.postgres.search import SearchVector

from taggit.models import Tag

from .forms import CommentForm, SearchForm  # Don't forget to import your SearchForm

# Function for the share view
def post_share(request, post_id):
    

# Class-based view to list posts with pagination
class PostListView(ListView):
    

# Function-based view to list posts with optional tag filtering and pagination
def post_list(request, tag_slug=None):
    

# View to display a single post’s details
def post_detail(request, year, month, day, post):
   

# View to handle a submitted comment
@require_POST
def post_comment(request, post_id):
    

# **New Search View**
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # build a weighted search vector
            search_vector = (
                SearchVector('title', weight='A') +
                SearchVector('body',  weight='B')
            )
            search_query  = SearchQuery(query)
            # annotate each Post with a rank and filter/order by it
            results = (
                Post.published
                    .annotate(search=search_vector, rank=SearchRank(search_vector, search_query))
                    .filter(rank__gte=0.3)
                    .order_by('-rank')
            )

    return render(
        request,
        'blog/post/search.html',  
        {
            'form': form,
            'query': query,
            'results': results,
        }
    )
