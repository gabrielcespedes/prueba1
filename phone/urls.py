
from django.contrib import admin
from django.urls import path

from .views import fabricantes_index
from .views import smartphone_create

urlpatterns = [
    path('', fabricantes_index, name='fabricantes'),
    path('smartphone-create', smartphone_create, name='smartphone_create'),
]
