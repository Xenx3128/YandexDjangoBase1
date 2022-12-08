from django.shortcuts import get_object_or_404, render
from django.db.models import Avg, Count

from .models import Item


def item_list(request):
    items = Item.objects.published_by_category()
    context = {
        'items': items,
    }
    return render(request, 'catalog/item_list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk, is_published=True)
    rating_avg = item.rating.aggregate(Avg('rating'))
    rating_count = item.rating.aggregate(Count('rating'))
    context = {
        'item': item,
        'rating_avg': rating_avg,
        'rating_count': rating_count,
    }
    return render(request, 'catalog/item_detail.html', context)
