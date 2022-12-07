import os

from django import forms
from django.core.mail import send_mail

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        fields = (
            Feedback.text.field.name,
            Feedback.email.field.name,
        )
        labels = {
           Feedback.text.field.name: 'Ваш отзыв',
           Feedback.email.field.name: 'Ваша почта',
        }

    def save(self):
        instance = super().save()
        instance.text = self.cleaned_data['text']
        instance.email = self.cleaned_data['email']
        instance.save()
        return instance

    def send_mails(self):
        text = self.cleaned_data['text']
        email = self.cleaned_data['email']
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
