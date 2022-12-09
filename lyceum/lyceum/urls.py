from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('feedback/', include('feedback.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('rating/', include('rating.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
