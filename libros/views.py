from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.core.paginator import Paginator

from .models import Libro
from categorias.models import Categoria
from django.contrib.messages.views import SuccessMessageMixin

class LibroListado(ListView):
    model = Libro
    template_name = 'libros/libro_listado.html'
    context_object_name = 'object_list'
    paginate_by = 5 
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('titulo')

        categoria_id = self.request.GET.get('categoria_id')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(autor__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categorias_con_conteo'] = Categoria.objects.annotate(
            num_libros=Count('libro') 
        ).order_by('nombre')
        context['current_category_id'] = self.request.GET.get('categoria_id', '')
        context['current_query'] = self.request.GET.get('q', '')

        return context

class LibroDetalle(DetailView):
    model = Libro
    template_name = 'libros/libro_detalle.html'
    context_object_name = 'libro'

class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    template_name = 'libros/libro_formulario.html'
    fields = ['titulo', 'autor', 'categoria', 'descripcion', 'isbn', 'fecha_publicacion', 'imagen', 'stock']
    success_url = reverse_lazy('libros:listado')
    success_message = "El libro '%(titulo)s' fue creado exitosamente"
    
class LibroActualizar(SuccessMessageMixin, UpdateView):
    model = Libro
    template_name = 'libros/libro_formulario.html'
    fields = ['titulo', 'autor', 'categoria', 'descripcion', 'isbn', 'fecha_publicacion', 'imagen', 'stock']
    success_url = reverse_lazy('libros:listado')
    success_message = "El libro '%(titulo)s' fue actualizado exitosamente"

class LibroEliminar(DeleteView):
    model = Libro
    template_name = 'libros/libro_confirmar_eliminacion.html'
    success_url = reverse_lazy('libros:listado')