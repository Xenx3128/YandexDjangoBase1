from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg, Count

from .models import Item


class ItemView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published_by_category()


class ItemDetailView(DetailView):
    model = Item
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.object.rating.aggregate(
            rating_avg=Avg('rating')
        ))
        context.update(self.object.rating.aggregate(
            rating_count=Count('rating')
        ))
        if self.request.user.is_authenticated:
            user = self.request.user
            item = Item.objects.get(pk=self.kwargs['pk'])
            context['user_rating'] = user.rating.filter(
                user=user,
                item=item
                ).first()
        return context

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs['pk'])
