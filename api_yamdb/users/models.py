from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLES = (
        ('user', 'Аутентифицированный пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=10,
        null=True
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    )

    role = models.CharField(
        'Роль',
        choices=ROLES,
        default='user',
        max_length=20
    )

    email = models.EmailField(
        'E-mail',
        unique=True, max_length=100
    )
