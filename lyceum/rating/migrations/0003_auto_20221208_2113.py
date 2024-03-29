# Generated by Django 3.2.16 on 2022-12-08 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0043_alter_item_text'),
        ('rating', '0002_auto_20221207_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='catalog.item', verbose_name='товар'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Ненависть'), (2, '2 - Неприязнь'), (3, '3 - Нейтрально'), (4, '4 - Обожание'), (5, '5 - Любовь')], help_text="1- 'Ненависть',2 - 'Неприязнь',3 - 'Нейтрально',4 -'Обожание',5 - 'Любовь'", null=True, verbose_name='оценка'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='user_item_unique'),
        ),
    ]
