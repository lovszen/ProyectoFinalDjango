from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model 
from libros.models import Libro 

User = get_user_model()

class Prestamo(models.Model):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['-fecha_prestamo'] 

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.usuario.username}"

    def get_absolute_url(self):
        return reverse('prestamos:detalle', kwargs={'pk': self.pk})
