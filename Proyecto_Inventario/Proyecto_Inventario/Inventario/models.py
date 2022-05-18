from django.db import models
from django.utils import timezone

ESTADO_CHOICES = (
    ("líquido", "líquido"),
    ("sólido" , "sólido"),
)

ALMACENAMIENTO = (
    ("temperatura ambiente", "temperatura ambiente"),
    ("refrigeración", "refrigeración"),
    ("congelación", "congelación"),
    ("vacío", "vacío")
)

class Reactivo(models.Model):
    nombre=models.CharField(max_length=250)
    estado_de_agregacion=models.CharField(
        max_length=20,
        choices= ESTADO_CHOICES,
    )
    cantidad=models.IntegerField()
    almacenamiento=models.CharField(
        max_length=25,
        choices= ALMACENAMIENTO,
    )
    fecha_agregado=models.DateTimeField(default=timezone.now)

    readonly_fields = ('fecha_agregado')

    def __str__(self):
        return self.nombre


PRESENTACION = (
    ("bolsa", "bolsa"),
    ("caja", "caja"),
    ("rack", "rack"),
    ("tubo", "tubo")
)

AREAS = (
    ("cultivo", "cultivo"),
    ("síntesis", "síntesis"),
    ("molecular", "molecular"),
    ("general", "general"),
)

class Consumible(models.Model):
     nombre=models.CharField(max_length=250)
     presentacion=models.CharField(
        max_length=25,
        choices= PRESENTACION,
    )
     cantidad=models.IntegerField()
     area_de_trabajo=models.CharField(
        max_length=25,
        choices= AREAS,
    )
     fecha_agregado=models.DateTimeField(default=timezone.now)

     def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    correo=models.EmailField()
    telefono=models.IntegerField()
    empresa=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nombre}  {self.apellido}  ({self.empresa})"

