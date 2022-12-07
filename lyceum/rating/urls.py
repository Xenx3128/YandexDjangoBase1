from django.urls import re_path

from . import views

app_name = 'rating'

urlpatterns = [
    re_path(
        r'^rating/(?P<pk>[1-9][0-9]*)/$',
        views.RatingView.as_view(),
        name='rating'
    ),
]
