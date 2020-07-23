from django.contrib import admin
from .models import Post, Course, Application

admin.site.site_header = 'Адміністрування One Man Show'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')

admin.site.register(Course, CourseAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'email', 'phone', 'created')
    list_filter = ('course', 'created')
    date_hierarchy = 'created'

admin.site.register(Application, ApplicationAdmin)
