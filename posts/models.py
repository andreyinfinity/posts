from django.db import models
from users.models import User


class Post(models.Model):
    """Публикация"""
    title = models.CharField(
        max_length=200,
        verbose_name='заголовок',
    )
    content = models.TextField(
        verbose_name='текст'
    )
    picture = models.ImageField(
        upload_to='posts/',
        verbose_name='изображение',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='дата редактирования'
    )

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Комментарий"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='публикация',
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор')
    content = models.TextField(
        verbose_name='текст'
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='дата редактирования'
    )

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.content
