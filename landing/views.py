from django.shortcuts import render, redirect
from .forms import AnimalForm, AyudaForm
from .models import Animal

# Registrar un animal
def registrar_mascota(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directorio_mascota')
    else:
        form = AnimalForm()
    
    return render(request, 'mascotas/registrar_mascota.html', {'form': form})

# Registrar una ayuda
def registrar_ayuda(request):
    if request.method == 'POST':
        form = AyudaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directorio_mascota')
    else:
        form = AyudaForm()
    
    return render(request, 'mascotas/registrar_ayuda.html', {'form': form})

# Listar animales
def directorio_mascota(request):
    mascota = Animal.objects.all()
    return render(request, 'mascotas/directorio_mascota.html', {'mascota': mascota})

def index(request):
    
    return render(request, 'mascotas/index.html')
