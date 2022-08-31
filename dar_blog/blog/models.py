from django.contrib.auth.models import AbstractUser, User
from django.db import models
import os


gender_choices = (
    ('М', 'Мужской'),
    ('Ж', 'Женский'),
    ('ХЗ', 'Другое')
)


class User(AbstractUser):
    surname = models.CharField(max_length=255, verbose_name='Отчество')
    image = models.ImageField(upload_to='user_pictures/', verbose_name='Фото профиля')
    gender = models.CharField(max_length=30, choices=gender_choices, null=True, verbose_name='Пол')
    birthday = models.DateField(verbose_name='Днюха', null=True)
    who_for_me = models.CharField(max_length=255, verbose_name='Кто ты Эльдару?', null=True)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор')
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


class Music(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(null=True, upload_to='my_music/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def get_size(self):
        return str(os.path.getsize(self.file.name) / 1000000)+' мб'

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'
