from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    premium = models.BooleanField()
    
    def __str__(self):
        return "Usuario: %s " %(self.nombre)
    

    

