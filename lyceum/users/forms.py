from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(required=False, widget=DateInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birthday')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'birthday')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birthday'].widget = DateInput()
        if self.initial['birthday']:
            self.initial['birthday'] = self.instance.birthday.isoformat()
