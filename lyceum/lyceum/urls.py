from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    re_path('catalog/(?P<pk>^[1-9]+$)/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('admin', admin.site.urls),
]
