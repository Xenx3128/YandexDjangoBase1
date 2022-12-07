from django import forms

from .models import Rating


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Rating.RATING_CHOICES,
    )

    class Meta:
        model = Rating
        fields = (
            Rating.text.field.name,
            Rating.email.field.name,
        )
        labels = {
           Rating.text.field.name: 'Ваш отзыв',
           Rating.email.field.name: 'Ваша почта',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
