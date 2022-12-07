from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from .forms import RatingForm
from .models import Rating


class RatingView(LoginRequiredMixin, FormView):
    template_name = 'rating/rating.html'
    form_class = RatingForm

    def get_initial(self):
        initial = super().get_initial()
        rating = Rating.objects.get(user=self.request.user)
        if rating:
            initial['rating'] = rating
        return initial

    def get_success_url(self):
        return reverse_lazy(
            'users:user_detail',
            kwargs={'pk': self.request.user}
        )

    def form_valid(self, form):
        rating = form.cleaned_data['rating']
        user = self.request.user
        context = self.get_context_data()
        item = context['item_id']
        Rating.objects.create(
            rating=rating,
            user=user,
            item=item,
        )
        return super(RatingView, self).form_valid(form)
