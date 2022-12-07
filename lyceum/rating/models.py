from catalog.models import Item
from users.models import User
from django.db import models


class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    )
    rating = models.IntegerField(
        'оценка',
        help_text='1- \'Ненависть\','
                  '2 - \'Неприязнь\','
                  '3 - \'Нейтрально\','
                  '4 -\'Обожание\','
                  '5 - \'Любовь\'',
        choices=RATING_CHOICES,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        null=True
    )
    item = models.ForeignKey(
        Item,
        verbose_name='товар',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Рейтинг'
        constraints = (
            models.UniqueConstraint(
                fields=("user", "item"),
                name='user_item_unique',
            ),
        )
