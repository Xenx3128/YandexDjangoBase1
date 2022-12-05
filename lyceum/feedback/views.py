from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data['text']
        Feedback.objects.create(
            text=text,
        )
        send_mail('Спасибо за Отзыв',
                  f'Спасибо, мы получили ваш отзыв:\n {text} \n С вашей '
                  'помощью, мы становимcя лучше. \n Resupply ',
                  'noreply@example.com',
                  ['user@example.com'],
                  fail_silently=False)

        return redirect(request.path)

    context = {
        'form': form,
    }
    return render(request, 'feedback/feedback.html', context)
