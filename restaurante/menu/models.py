from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class Pago (models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.nombre_cliente} - {self.plato.nombre}"