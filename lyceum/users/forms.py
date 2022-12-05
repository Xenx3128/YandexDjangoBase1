from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(required=False, widget=DateInput())

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            'password1',
            'password2',
            User.birthday.field.name,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.birthday.field.name,
        )
        widgets = {
            'birthday': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial['birthday']:
            self.initial['birthday'] = self.instance.birthday.isoformat()
