from django import forms
from .models import Smartphone
from .models import Fabricante

class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        fields = ['nombre', 'fabricante', 'ram', 'almacenamiento', 'tamaño_pantalla']

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nombre', 'pais', 'fecha', 'link']