from catalog.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import RatingForm
from .models import Rating


class RatingView(LoginRequiredMixin, FormView):
    form_class = RatingForm
    template_name = 'rating/rating.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        item = Item.objects.get(pk=self.kwargs['item_id'])
        rating = user.rating.filter(user=user, item=item).first()
        if rating:
            kwargs['rating'] = rating
        return kwargs

    def form_valid(self, form):
        rating = form.cleaned_data['rating']
        user = self.request.user
        item = Item.objects.get(pk=self.kwargs['item_id'])
        Rating.objects.update_or_create(
            user=user,
            item=item,
            defaults={
                'rating': rating,
                'user': user,
                'item': item
            }
        )
        return redirect('users:user_detail', pk=self.request.user.pk)

    def form_invalid(self, form):
        return render(
            self.request,
            self.template_name,
            {'form': form}
        )
