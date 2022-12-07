import os

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from .forms import FeedbackForm
from .models import Feedback

load_dotenv()


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        email = form.cleaned_data['email']
        Feedback.objects.create(
            text=text,
            email=email,
        )
        send_mail(
            'Спасибо за Отзыв',
            f'Спасибо, мы получили ваш отзыв:\n {text} \n С вашей '
            'помощью, мы становимcя лучше. \n Resupply ',
            os.environ.get('SUPPORT_EMAIL', 'noreply@test.com'),
            [email],
            fail_silently=False,
        )
        send_mail(
            'Новый Отзыв',
            f'Получен новый отзыв:\n {text} \n'
            f'Почта отправителя:\n {email} \n',
            os.environ.get('SUPPORT_EMAIL', 'noreply@test.com'),
            [os.environ.get('SUPPORT_EMAIL', 'noreply@test.com')],
            fail_silently=False,
        )
        return redirect(request.path)

    context = {
        'form': form,
    }
    return render(request, 'feedback/feedback.html', context)
