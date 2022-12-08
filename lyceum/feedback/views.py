from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import FeedbackForm


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def form_valid(self, form):
        form.save()
        form.send_mails()
        return redirect('feedback:feedback')

    def form_invalid(self):
        return render(self.request, self.template_name,
                      {'form': FeedbackForm()})

    def get_form(self):
        return FeedbackForm(self.request.POST or None)
