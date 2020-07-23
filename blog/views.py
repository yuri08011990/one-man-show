from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages
from .models import Post, Course, Application
from .forms import AppicationForm, RawApplicationForm

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
    courses = Course.objects.all()
    form = RawApplicationForm(request.GET)
    if request.method == 'POST':
        form = RawApplicationForm(request.POST or None)
        if form.is_valid():
            Application.objects.create(**form.cleaned_data)
            messages.success(request, 'Заявку відправлено! \nОчікуйте дзвінка ;)')
            return redirect('school')
        elif Application.objects.filter(phone=phone, course=course).exists():
            messages.info(request, 'Ви вже подавали заявку на цей курс.')
            return redirect('school')
        else:
            form = RawApplicationForm()
    context = {'form': form, 'courses': courses}
    return render(request, 'blog/school.html', context)


# def school(request):
#     if request.method == "POST":
#         form = AppicationForm(request.POST)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.created = timezone.now()
#             application.save()
#             return redirect('post_list')
#     else:
#         form = AppicationForm()
#     return render(request, 'blog/school.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')