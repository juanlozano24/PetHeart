from django import forms
from .models import Animal, Ayuda

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'ubicacion', 'tipo_vulnerabilidad', 'descripcion']

class AyudaForm(forms.ModelForm):
    class Meta:
        model = Ayuda
        fields = ['animal', 'tipo_ayuda', 'descripcion', 'oferente']
