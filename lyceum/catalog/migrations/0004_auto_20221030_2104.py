# Generated by Django 3.2.16 on 2022-10-30 16:04

import catalog.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20221030_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\-_]*$', "Разрешены только цифры, буквы латиницы,символы '-' и '_'")], verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\-_]*$', "Разрешены только цифры, буквы латиницы,символы '-' и '_'")], verbose_name='Слаг'),
        ),
    ]
