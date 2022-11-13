from django.shortcuts import render

from catalog.models import Item


def home(request):
    items = Item.objects.published_main()
    context = {
        'items': items,
        'app_name': 'homepage',
    }
    return render(request, template_name='homepage/index.html',
                  context=context)
