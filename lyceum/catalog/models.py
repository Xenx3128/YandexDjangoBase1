from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

from Core.models import PublishableBaseModel
from .validators import validate_words


slug_regex_validator = RegexValidator(r'^[0-9a-zA-Z\-_]*$',
                                      'Разрешены только цифры, буквы латиницы,'
                                      'символы \'-\' и \'_\'')


class Tag(PublishableBaseModel):
    slug = models.CharField('Слаг', max_length=200, unique=True,
                            help_text='Слаг тега',
                            validators=[slug_regex_validator])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(PublishableBaseModel):
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


class ItemManager(models.Manager):
    def published_main(self):
        return (
            self.get_queryset()
                .filter(is_published=True, is_on_main=True)
                .select_related('category')
                .order_by('name')
                .prefetch_related(
                    models.Prefetch('tags', queryset=Tag.objects.all())
                )
        )

    def published_by_category(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .select_related('category')
                .order_by('category__name', 'name')
                .prefetch_related(
                    models.Prefetch('tags', queryset=Tag.objects.all())
                )
        )


class Item(PublishableBaseModel):
    objects = ItemManager()

    text = models.TextField('Описание', default='Sample Text',
                            help_text='Описание товара',
                            validators=[validate_words('превосходно',
                                                       'роскошно')])
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 help_text='Категория товара',
                                 on_delete=models.CASCADE, null=True,
                                 related_name='items')
    is_on_main = models.BooleanField(verbose_name='На главной странице',
                                     default=False)

    tags = models.ManyToManyField(Tag, verbose_name='Теги',
                                  help_text='Теги товара')
    main_image = models.ImageField(upload_to='images/%Y/%m',
                                   verbose_name='Изображение',
                                   null=True,
                                   blank=True)

    def get_absolute_url(self):
        return reverse('catalog:item_detail', kwargs={"pk": self.pk})

    @property
    def get_img(self):
        return get_thumbnail(self.main_image, '300x300', crop='center',
                             quality=50)

    def image_tmb(self):
        if self.main_image:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Главное изображение'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class SecondaryImage(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, null=True)
    image = models.ImageField(upload_to='images/%Y/%m',
                              verbose_name='Картинка',
                              null=True)
    item = models.ForeignKey(Item, verbose_name='Товар',
                             on_delete=models.CASCADE, null=True)

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center',
                             quality=50)

    def sec_image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return 'Нет изображения'

    sec_image_tmb.short_description = 'Галерея'
    sec_image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.name
