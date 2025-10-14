from django.contrib import admin
from .models import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'usuario', 'fecha_prestamo', 'fecha_devolucion', 'devuelto')
    list_filter = ('devuelto', 'fecha_prestamo', 'usuario')
    search_fields = ('libro__titulo', 'usuario__username')