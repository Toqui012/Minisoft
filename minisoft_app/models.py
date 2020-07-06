from django.db import models

# Create your models here.
load_family = [
    ('Hogar','Hogar'),
    ('Viaje','Viaje'),
    ('Jugueteria','Jugueteria'),
    ('Salud y Belleza','Salud y Belleza'),
    ('Deportes','Deportes'),
    ('Licencia','Licencia'),
]


class Producto(models.Model):

    num_cuenta = models.BigIntegerField(null=False)
    nombre = models.CharField(max_length=255, null=False)
    familia = models.CharField(max_length=255, null=False, choices=load_family, default='Hogar')
    color = models.CharField(max_length=255, null=False)
    descripcion = models.CharField(max_length=255, null=False)
    cantidad = models.BigIntegerField(null=False)
    merma = models.BooleanField(null=False)
    precio = models.BigIntegerField(null=False)

    def __str__(self):
        return str(self.pk)

