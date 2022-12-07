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
            Rating.rating.field.name,
        )
        labels = {
           Rating.rating.field.name: 'Ваша оценка',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
