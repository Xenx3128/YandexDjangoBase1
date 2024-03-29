# Generated by Django 3.2.16 on 2022-10-30 18:36

import catalog.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(related_name='Теги', to='catalog.Tag'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
    ]
