from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    fecha = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.nombre

class Smartphone(models.Model):
    nombre = models.CharField(max_length=200)
    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.CASCADE,
    )
    ram = models.IntegerField()
    almacenamiento = models.IntegerField()
    tamaño_pantalla = models.FloatField()

    def __str__(self):
        return f'{self.nombre} de {self.fabricante.nombre}'