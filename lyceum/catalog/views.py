from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    items = Item.objects.published_by_category()
    context = {
        'items': items,
        'app_name': 'catalog',
    }
    return render(request, template_name='catalog/item_list.html',
                  context=context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk, is_published=True)
    context = {
        'item': item,
        'app_name': 'catalog',
    }
    return render(request, template_name='catalog/item_detail.html',
                  context=context)
