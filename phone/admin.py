from django.contrib import admin

# Register your models here.
from .models import Fabricante
from .models import Smartphone

admin.site.register(Fabricante)
admin.site.register(Smartphone)

