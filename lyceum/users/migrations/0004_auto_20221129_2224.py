# Generated by Django 3.2.16 on 2022-11-29 17:24

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221128_2355'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, help_text='Не более 254 символов', max_length=254, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, help_text='Не более 254 символов', max_length=254, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Не более 254 символов', max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Не более 150 символов', max_length=150, verbose_name='Имя пользователя'),
        ),
    ]
