from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.CategoriaListado.as_view(), name='listado'),
    path('crear/', views.CategoriaCrear.as_view(), name='crear'),
    path('<int:pk>/', views.CategoriaDetalle.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.CategoriaEditar.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.CategoriaEliminar.as_view(), name='eliminar'),
]