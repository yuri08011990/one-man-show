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
        verbose_name_plural = 'Пости'
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва курсу')
    description = models.TextField(verbose_name='Опис курсу')
    start = models.CharField(max_length=100, verbose_name='Дата початку курсу')
    end = models.CharField(max_length=100, verbose_name='Дата закінчення курсу')

    class Meta:
        verbose_name_plural = 'Курси'

    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я")
    email = models.EmailField(max_length=75, verbose_name="Email")
    phone = models.CharField(max_length=13, verbose_name="Номер телефону")
    course = models.CharField(max_length=100, verbose_name="Курс")
    comment = models.CharField(max_length=250, verbose_name="Коментар")
    created = models.DateTimeField(default=timezone.now, verbose_name='Додано')

    class Meta:
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.email


