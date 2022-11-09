# Generated by Django 3.2.16 on 2022-11-09 13:58

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='Sample Text', help_text='Описание товара', validators=[catalog.validators.validate_words], verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='SecondaryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/%Y/%m')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Галерея изображений товара',
            },
        ),
    ]
