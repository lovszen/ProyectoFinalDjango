from django.urls import path
from .views import (
    PrestamoListado,
    PrestamoDetalle,
    PrestamoCrear,
    PrestamoEliminar,
    marcar_devuelto 
)

app_name = 'prestamos'

urlpatterns = [
    path('', PrestamoListado.as_view(), name='listado'),
    path('crear/', PrestamoCrear.as_view(), name='crear'),
    path('detalle/<int:pk>/', PrestamoDetalle.as_view(), name='detalle'),
    path('eliminar/<int:pk>/', PrestamoEliminar.as_view(), name='eliminar'),
    path('devolver/<int:pk>/', marcar_devuelto, name='devolver'),
]
