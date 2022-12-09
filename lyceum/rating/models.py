from catalog.models import Item
from django.db import models
from users.models import User


class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 - Ненависть'),
        (2, '2 - Неприязнь'),
        (3, '3 - Нейтрально'),
        (4, '4 - Обожание'),
        (5, '5 - Любовь'),
    )
    rating = models.IntegerField(
        'оценка',
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
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'
        default_related_name = 'ratings'
        constraints = (
            models.UniqueConstraint(
                fields=("user", "item"),
                name='user_item_unique',
            ),
        )

    def __str__(self):
        return self.rating
