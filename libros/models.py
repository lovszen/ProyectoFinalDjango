from django.db import models
from django.urls import reverse
from categorias.models import Categoria 

def get_image_upload_path(instance, filename):
    return f'libros_imagenes/{filename}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) 
    descripcion = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1) 

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def get_absolute_url(self):
        return reverse('libros:detalle', kwargs={'pk': self.pk})