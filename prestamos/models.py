from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import get_user_model 
from libros.models import Libro 
from django.utils import timezone

User = get_user_model()

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha_prestamo']

    def clean(self):
        """Validación adicional a nivel modelo"""
        if not self.pk and self.libro.stock <= 0:
            raise ValidationError(f'No hay stock disponible para el libro "{self.libro.titulo}"')

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.usuario.username}"

    def get_absolute_url(self):
        return reverse('prestamos:detalle', kwargs={'pk': self.pk})

    def marcar_devuelto(self):
        """Método para marcar como devuelto (R5)"""
        if not self.devuelto:
            self.devuelto = True
            self.fecha_devolucion = timezone.now().date()
            self.save()
            self.libro.stock += 1
            self.libro.save()