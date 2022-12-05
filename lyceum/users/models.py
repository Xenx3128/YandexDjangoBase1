from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models
from django.urls import reverse


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Имя пользователя', max_length=150,
                                help_text='Не более 150 символов')
    email = models.EmailField('Электронная почта', max_length=254, unique=True,
                              help_text='Не более 254 символов')

    first_name = models.CharField('Имя', max_length=254, blank=True, null=True,
                                  help_text='Не более 254 символов')
    last_name = models.CharField('Фамилия', max_length=254, blank=True,
                                 null=True, help_text='Не более 254 символов')
    birthday = models.DateField('День рождения', null=True, blank=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
