# Generated by Django 3.2.16 on 2022-12-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default='example@yandex.ru', max_length=254),
        ),
    ]
