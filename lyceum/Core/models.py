from django.db import models


class CatalogBaseModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150,)
    is_published = models.BooleanField(verbose_name='Опубликовано',
                                       default=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name
