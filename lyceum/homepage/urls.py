from django.urls import path, reverse

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home')
]
