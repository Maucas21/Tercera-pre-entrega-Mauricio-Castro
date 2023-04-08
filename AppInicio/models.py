from django.db import models

# Create your models here.

    
class Usuario(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} "
    

class Profesional(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} "