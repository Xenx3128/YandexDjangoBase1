from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .validators import validate_words


class Tag(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    weight = models.IntegerField(default=100,
                                 help_text='Вес категории',
                                 validators=(MinValueValidator(1),
                                             MaxValueValidator(32766)))

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


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


class Item(PublishableBaseModel, NamedBaseModel):

    text = models.TextField('описание', default='Sample Text',
                            help_text='Описание товара',
                            validators=(validate_words('превосходно',
                                                       'роскошно'),))
    category = models.ForeignKey(Category, verbose_name='категория',
                                 help_text='Категория товара',
                                 on_delete=models.CASCADE, null=True,
                                 related_name='items')
    is_on_main = models.BooleanField('на главной странице',
                                     default=False)

    tags = models.ManyToManyField(Tag, verbose_name='теги',
                                  help_text='Теги товара')
    main_image = models.ImageField('изображение',
                                   upload_to='images/%Y/%m',
                                   null=True,
                                   blank=True)

    objects = ItemManager()

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

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


class SecondaryImage(NamedBaseModel):
    image = models.ImageField('Картинка',
                              upload_to='images/%Y/%m',
                              null=True)
    item = models.ForeignKey(Item, verbose_name='товар',
                             on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'картинка товара'
        verbose_name_plural = 'галерея'

    def __str__(self):
        return self.name

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
