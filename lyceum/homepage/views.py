from catalog.models import Item
from django.views.generic.list import ListView


class HomeView(ListView):
    model = Item
    template_name = 'homepage/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published_main()
