from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Categoria 

class CategoriaListado(ListView):
    model = Categoria
    template_name = 'categorias/categoria_listado.html' 
    context_object_name = 'categorias'
    ordering = ['nombre'] 

class CategoriaDetalle(DetailView):
    model = Categoria
    template_name = 'categorias/categoria_detalle.html'
    context_object_name = 'categoria'
    
class CategoriaCrear(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/categoria_formulario.html'
    success_url = reverse_lazy('categorias:listado')

class CategoriaEditar(UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/categoria_formulario.html'
    def get_success_url(self):
        return reverse_lazy('categorias:detalle', kwargs={'pk': self.object.pk})

class CategoriaEliminar(DeleteView):
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('categorias:listado')