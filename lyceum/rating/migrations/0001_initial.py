# Generated by Django 3.2.16 on 2022-12-07 14:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0041_alter_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, help_text="1- 'Ненависть',2 - 'Неприязнь',3 - 'Нейтрально',4 -'Обожание',5 - 'Любовь'", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='оценка')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
    ]
