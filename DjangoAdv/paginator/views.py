from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'paginator_tpl/index.html', {'page_posts': page_posts})