from django import forms

from .models import Rating


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        label='Ваша оценка',
        widget=forms.RadioSelect,
        choices=Rating.RATING_CHOICES,
    )

    class Meta:
        model = Rating
        fields = (
            Rating.rating.field.name,
        )

    def __init__(self, *args, **kwargs):
        init_rating = kwargs.pop('rating', None)
        super().__init__(*args, **kwargs)
        if init_rating:
            print(init_rating)
            self.fields['rating'].initial = init_rating.rating
