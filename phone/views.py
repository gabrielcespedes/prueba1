from django.shortcuts import render
from django.shortcuts import redirect

from .models import Fabricante
from .forms import SmartphoneForm
from .forms import FabricanteForm

# Create your views here.

def fabricantes_index(request):
    fabricantes = Fabricante.objects.all()
    context = {'fabricantes': fabricantes}
    return render(request, 'phone/fabricantes.html', context)

def smartphone_create(request):
    if request.method == 'POST':
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fabricantes')
    else:
        form = SmartphoneForm()
    context = {'form': form}

    return render(request, 'phone/smartphone_create.html', context)

def fabricante_create(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fabricantes')
    else:
        form = FabricanteForm()
    context = {'form': form}

    return render(request, 'phone/fabricante_create.html', context)




