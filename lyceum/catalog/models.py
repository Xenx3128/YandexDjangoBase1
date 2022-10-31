from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from Core.models import CatalogBaseModel
from .validators import validate_words


slug_regex_validator = RegexValidator(r'^[0-9a-zA-Z\-_]*$',
                                      'Разрешены только цифры, буквы латиницы,'
                                      'символы \'-\' и \'_\'')


class Tag(CatalogBaseModel):
    slug = models.CharField('Слаг', max_length=200, unique=True,
                            help_text='Слаг тега',
                            validators=[slug_regex_validator])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(CatalogBaseModel):
    slug = models.CharField('Слаг', max_length=200, unique=True,
                            help_text='Слаг категории',
                            validators=[slug_regex_validator])
    weight = models.IntegerField(default=100,
                                 help_text='Вес категории',
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(32766)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(CatalogBaseModel):
    text = models.TextField('Описание', default='Sample Text',
                            help_text='Описание товара',
                            validators=[
                                validate_words('превосходно', 'роскошно')])
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 help_text='Категория товара',
                                 on_delete=models.CASCADE, null=True,
                                 related_name='items')
    tags = models.ManyToManyField(Tag, verbose_name='Теги',
                                  help_text='Теги товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# python manage.py makemigrations
# CRUD - create read update delete
# CASCADE, SET_NULL
