from catalog.models import Item
from django.shortcuts import render


def home(request):
    items = Item.objects.published_main()
    context = {
        'items': items,
        'app_name': 'homepage',
    }
    return render(request, 'homepage/index.html', context)
