# Generated by Django 4.0.5 on 2022-06-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='user_pictures/', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=255, verbose_name='Отчество'),
        ),
    ]
