# Generated by Django 3.2.16 on 2022-11-13 14:35

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20221113_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='На главной странице'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', help_text='Описание товара', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
    ]
