from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь"""
    phone_number = models.CharField(
        max_length=11,
        verbose_name='номер телефона',
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(
        verbose_name='дата рождения',
        blank=True,
        null=True
    )
    date_of_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    date_of_edition = models.DateTimeField(
        auto_now=True,
        verbose_name='дата редактирования'
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
