import uuid
from django.db import models
from django.db.models import Model

# Create your models here.

class Family(Model):
    name = models.CharField('Nombre', max_length=140)

    def __str__(self):
        return(self.name)
    
    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"
    

class Person(Model):
    family = models.ManyToManyField(Family)
    first_name = models.CharField(
        'Nombre',
        max_length=35
        )
    last_name = models.CharField(
        'Apellido',
        max_length=30
        )
    age = models.IntegerField(
        'Edad',
        default=18,
        help_text="Introduce un número en el formulario"
        )
    dni = models.CharField(
        'DNI',
        max_length=9,
        unique=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ["age"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"