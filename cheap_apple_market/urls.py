from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('market/', include('market.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns