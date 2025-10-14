from django.urls import path
from .views import LibroListado, LibroDetalle, LibroCrear, LibroActualizar, LibroEliminar

app_name = 'libros'

urlpatterns = [
    path('', LibroListado.as_view(), name='listado'),
    path('crear/', LibroCrear.as_view(), name='crear'),
    path('<int:pk>/detalle/', LibroDetalle.as_view(), name='detalle'),
    path('<int:pk>/editar/', LibroActualizar.as_view(), name='editar'),
    path('<int:pk>/eliminar/', LibroEliminar.as_view(), name='eliminar'),
]