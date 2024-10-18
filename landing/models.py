from django.db import models

class Animal(models.Model):
    VULNERABILIDAD_CHOICES = [
        ('Abandono', 'Abandono'),
        ('Enfermedad', 'Enfermedad'),
        ('Maltrato', 'Maltrato'),
        ('Otros', 'Otros')
    ]
    
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    tipo_vulnerabilidad = models.CharField(max_length=50, choices=VULNERABILIDAD_CHOICES)
    descripcion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Ayuda(models.Model):
    TIPO_AYUDA_CHOICES = [
        ('Alimentos', 'Alimentos'),
        ('Adopción', 'Adopción'),
        ('Hogar de paso', 'Hogar de paso'),
        ('Medicamentos', 'Medicamentos'),
        ('Otros', 'Otros')
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='ayudas')
    tipo_ayuda = models.CharField(max_length=50, choices=TIPO_AYUDA_CHOICES)
    descripcion = models.TextField()
    oferente = models.CharField(max_length=100)  # Nombre de quien ofrece la ayuda
    fecha_ofrecimiento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_ayuda} para {self.animal.nombre}"
