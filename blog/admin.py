from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    raw_id_fields = ['posts']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'published_at', 'author']
    readonly_fields = ['published_at']
    list_filter = ['author', 'published_at']
    raw_id_fields = ['likes', 'tags', 'author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'published_at']
    raw_id_fields = ['post', 'author']
    readonly_fields = ['published_at']
