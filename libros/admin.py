from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'stock', 'isbn')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'autor', 'isbn')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'autor', 'categoria', 'descripcion', 'imagen')
        }),
        ('Información de Inventario', {
            'fields': ('isbn', 'stock'),
            'classes': ('collapse',)
        }),
    )