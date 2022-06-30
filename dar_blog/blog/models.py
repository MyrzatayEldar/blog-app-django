from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    surname = models.CharField(max_length=255, verbose_name='Отчество')
    image = models.ImageField(upload_to='user_pictures/', verbose_name='Фото профиля')


class Post(models.Model):
    author = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Тема поста')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')
    text = models.TextField(verbose_name='Текст поста')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    image = models.ImageField(upload_to='post_pictures/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост {self.author}. Дата написания: {self.published_date}.'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.name}'
