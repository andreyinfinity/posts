from django.contrib import admin
from posts.models import Post, Comment


class CommentInline(admin.TabularInline):
    """Инлайн для отображения комментариев в объекте публикации"""
    model = Comment
    readonly_fields = (
        'date_posted',
        'author',
        'content'
    )
    show_change_link = True
    can_delete = False
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Отображение списка публикаций"""
    list_display = (
        'id',
        'title',
        'author',
        'content',
        'date_posted',
        'date_modified'
    )
    list_display_links = ('title',)
    list_filter = ('date_posted',)
    inlines = [CommentInline]
    readonly_fields = (
        'date_posted',
        'date_modified',
        'author'
    )
