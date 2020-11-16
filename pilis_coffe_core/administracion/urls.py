from django.contrib import admin
from django.urls import path
from .views import HomeAdminView, PreciosView

app_name = 'administracion'

urlpatterns = [
    path('administrador/', HomeAdminView.as_view(), name='home'),
    path('precios/', PreciosView.as_view(), name="precios"),
]
