from django.contrib import admin

from posts.models import Post, Comment
from users.models import User


class PostInline(admin.TabularInline):
    """Инлайн для отображения публикаций в объекте пользователя"""
    model = Post
    readonly_fields = (
        'date_posted',
        'title',
        'content',
        'picture'
    )
    show_change_link = True
    can_delete = False
    extra = 0


class CommentInline(admin.TabularInline):
    """Инлайн для отображения комментариев в объекте пользователя"""
    model = Comment
    readonly_fields = (
        'date_posted',
        'post',
        'content',
    )
    show_change_link = True
    can_delete = False
    extra = 0
    show_full_result_count = True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение списка пользователей"""
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
    )
    list_display_links = ('username',)
    list_filter = ('groups',)
    inlines = [PostInline, CommentInline]
    readonly_fields = (
        'password',
        'date_joined',
        'last_login',
        'date_of_creation',
        'date_of_edition'
    )

