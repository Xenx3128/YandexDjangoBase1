from django.db import models


class Feedback(models.Model):
    text = models.TextField('Отзыв')
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
