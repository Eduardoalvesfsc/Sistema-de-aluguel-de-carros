from .import views
from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views
from borrowing import views as borrowing_views
from django.contrib.auth import views as auth_views
from borrowing.views import register_view

urlpatterns = [
    path('meus_carros/', views.meus_carros, name='meus_carros')
]