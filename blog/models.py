from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('чорновик', 'Чорновик'),
        ('опубліковано', 'Опубліковано'),
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', verbose_name='Автор', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Текст допису')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Час публікації')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title
