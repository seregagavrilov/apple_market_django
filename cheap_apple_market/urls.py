from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', include('market.urls')),
    path('admin/', admin.site.urls),
]
