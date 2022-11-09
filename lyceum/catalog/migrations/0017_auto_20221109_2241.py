# Generated by Django 3.2.16 on 2022-11-09 17:41

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', help_text='Описание товара', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='secondaryimage',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m', verbose_name='Картинка'),
        ),
    ]
