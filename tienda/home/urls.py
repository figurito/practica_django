from django.urls import path
from .import views

urlpatterns = [
    path('lista_producto', views.lista_producto),
]