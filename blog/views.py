from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/index.html'


# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 3)  # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'post/list.html', {'page': page, 'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'post/detail.html', {'post': post})


# def index(request):
#     return render(request, 'blog/index.html')


def school(request):
    return render(request, 'blog/school.html')

def about(request):
    return render(request, 'blog/about.html')