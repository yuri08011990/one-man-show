from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Course, Application, About

admin.site.site_header = 'Адміністрування One Man Show'

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    summernote_fields = 'body'

admin.site.register(Post, SummernoteModelAdmin)


class CourseAdmin(SummernoteModelAdmin):
    list_display = ('title', 'start', 'end')
    summernote_fields = '__all__'

admin.site.register(Course, SummernoteModelAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'email', 'phone', 'created')
    list_filter = ('course', 'created')
    date_hierarchy = 'created'

admin.site.register(Application, ApplicationAdmin)


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(About, AboutAdmin)