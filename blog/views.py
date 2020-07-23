from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages
from .models import Post, Course, Application, About
from .forms import AppicationForm, RawApplicationForm

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/index.html'


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'post/detail.html', {'post': post})


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


def about(request):
    descr = About.objects.all()
    return render(request, 'blog/about.html', {'descr': descr})