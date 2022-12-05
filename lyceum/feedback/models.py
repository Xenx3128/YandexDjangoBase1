from django.db import models


class Feedback(models.Model):
    text = models.TextField('отзыв')
    created_on = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
