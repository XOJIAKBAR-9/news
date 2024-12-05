from django.contrib import admin
from django.contrib.auth.models import User, Group

from main.models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Gallery)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContentInline(admin.StackedInline):
    model = Content
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'reading_time', 'category', 'views', 'comments', 'published', 'created_at')
    search_fields = ('title', 'category_name', 'tags__name')
    list_filter = ('category', 'tags', 'published')
    inlines = (ContentInline, CommentInline)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at',)
    search_fields = ('author', 'text',)
    list_filter = ('author',)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'message',)
    search_fields = ('full_name', 'email',)
    list_filter = ('email', 'phone_number', 'subject',)


