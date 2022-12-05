from catalog.models import Category, Item, SecondaryImage, Tag
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

admin.site.register(Category)
admin.site.register(Tag)


class SecondaryImageInline(AdminImageMixin, admin.StackedInline):
    model = SecondaryImage
    extra = 1


@admin.register(Item)
class ItemAdmin(AdminImageMixin, SummernoteModelAdmin):
    summernote_fields = 'text'
    list_display = (
        'name',
        'is_published',
        'image_tmb',
        'is_on_main',
    )
    list_editable = (
        'is_published',
        'is_on_main',
    )
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
    readonly_fields = ('image_tmb',)
    inlines = (SecondaryImageInline,)


@admin.register(SecondaryImage)
class SecondaryImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sec_image_tmb',
        'item',
    )
    readonly_fields = ('sec_image_tmb',)
