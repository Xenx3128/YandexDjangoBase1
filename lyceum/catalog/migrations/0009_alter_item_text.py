# Generated by Django 3.2.16 on 2022-11-09 13:26

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20221109_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', help_text='Описание товара', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
    ]