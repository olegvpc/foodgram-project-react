from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель Пользователя."""
    username = models.CharField(
        max_length=100, unique=True,
        blank=True, verbose_name='Ник-нейм пользователя')
    email = models.EmailField(blank=False,
                              unique=True,
                              verbose_name='Электронная почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower', verbose_name='Подписчик')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following', verbose_name='Автор')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_list'),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='self_following'
            )
        ]
