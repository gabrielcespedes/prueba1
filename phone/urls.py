
from django.contrib import admin
from django.urls import path

from .views import fabricantes_index
from .views import smartphone_create
from .views import fabricante_create

from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', fabricantes_index, name='fabricantes'),
    path('smartphone-create', smartphone_create, name='smartphone_create'),
    path('fabricante-create', fabricante_create, name='fabricante_create'),
    path('register', register, name='register'),
    path('login', LoginView.as_view(template_name='phone/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='phone/logout.html'), name='logout'),
]
