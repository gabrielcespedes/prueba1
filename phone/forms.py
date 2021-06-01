from django import forms
from .models import Smartphone
from .models import Fabricante

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        fields = ['nombre', 'fabricante', 'ram', 'almacenamiento', 'tamaño_pantalla']

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nombre', 'pais', 'fecha', 'link']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }