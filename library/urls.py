"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views
from borrowing import views as borrowing_views
from django.contrib.auth import views as auth_views
from borrowing.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Catalog
    path('', catalog_views.carro_list, name='carro_list'),
    path('add-book/', catalog_views.add_carro, name='add_carro'),

    # Borrowing
    path('alugado/', borrowing_views.carro_alugado, name='carro_alugado'),
    path('return/<int:pk>/', borrowing_views.return_carro, name='return_carro'),
    path('meus-carros/', borrowing_views.meu_carros, name='meus_carros'),
    path('vencido/', borrowing_views.data_vencida, name='data_vencida'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]
