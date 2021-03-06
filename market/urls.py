from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('market/', views.index, name='index'),
    path('market/<int:product_id>/', views.product, name='product'),
]