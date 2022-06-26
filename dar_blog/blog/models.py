from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    surname = models.CharField(max_length=255, verbose_name='Отчество')
    image = models.ImageField(upload_to='user_pictures/', verbose_name='Фото профиля')
