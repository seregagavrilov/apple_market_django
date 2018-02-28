from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('market/', include('market.urls')),
    path('admin/', admin.site.urls),
]