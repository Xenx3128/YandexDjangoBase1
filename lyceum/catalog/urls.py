from django.urls import path, re_path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ItemView.as_view(), name='item_list'),
    re_path(r'^(?P<pk>[1-9][0-9]*)/$', views.ItemDetailView.as_view(),
            name='item_detail')
]
