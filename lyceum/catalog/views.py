from django.shortcuts import render

from .models import Item


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, template_name='catalog/item_list.html',
                  context=context)


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, template_name='catalog/item_detail.html',
                  context=context)
