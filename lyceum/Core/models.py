from django.db import models


class PublishableBaseModel(models.Model):
    is_published = models.BooleanField('опубликовано',
                                       default=True)

    class Meta:
        abstract = True


class NamedBaseModel(models.Model):
    name = models.CharField('название', max_length=150,)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class SluggedBaseModel(models.Model):
    slug = models.SlugField('слаг', max_length=200, unique=True,
                            help_text='Слаг')

    class Meta:
        abstract = True
