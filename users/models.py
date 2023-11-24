from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    email_verified = models.BooleanField(default=False, verbose_name='статус верификаций')
    verification_token = models.CharField(max_length=255, blank=True, null=True, verbose_name='токен верификаций')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
