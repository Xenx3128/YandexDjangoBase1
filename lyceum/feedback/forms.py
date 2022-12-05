from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        labels = {
           Feedback.text.field.name: 'Ваш отзыв',
        }
        help_texts = {
            'text': 'Текст вашего отзыва',
        }