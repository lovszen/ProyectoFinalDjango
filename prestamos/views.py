from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages 
from django.shortcuts import redirect, get_object_or_404
from django.db.models import F 
from django.utils import timezone 
from .models import Prestamo 
from libros.models import Libro 

class PrestamoListado(ListView):
    model = Prestamo
    context_object_name = 'prestamos'
    template_name = 'prestamos/prestamo_listado.html'

class PrestamoDetalle(DetailView):
    model = Prestamo
    context_object_name = 'prestamo'
    template_name = 'prestamos/prestamo_detalle.html'

class PrestamoCrear(CreateView):
    model = Prestamo
    fields = ['libro', 'usuario'] 
    template_name = 'prestamos/prestamo_formulario.html'
    success_url = reverse_lazy('prestamos:listado')

    def form_valid(self, form):
        libro_seleccionado = form.cleaned_data['libro']
        
        if libro_seleccionado.stock > 0:
            response = super().form_valid(form)
            
            Libro.objects.filter(pk=libro_seleccionado.pk).update(stock=F('stock') - 1)
            messages.success(self.request, f'Préstamo registrado. Stock de "{libro_seleccionado.titulo}" descontado.')
            return response
        else:
            messages.error(self.request, f'Error: "{libro_seleccionado.titulo}" no tiene stock disponible para préstamo.')
            return self.form_invalid(form)


class PrestamoEliminar(DeleteView):
    model = Prestamo
    template_name = 'prestamos/prestamo_confirmar_eliminacion.html'
    success_url = reverse_lazy('prestamos:listado')

def marcar_devuelto(request, pk):
    """Marca un préstamo como devuelto y aumenta el stock del libro (R5)."""
    prestamo = get_object_or_404(Prestamo, pk=pk)
    
    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.fecha_devolucion = timezone.now().date()
        prestamo.save(update_fields=['devuelto', 'fecha_devolucion'])
        
        Libro.objects.filter(pk=prestamo.libro.pk).update(stock=F('stock') + 1)
        
        messages.success(request, f'Libro "{prestamo.libro.titulo}" devuelto correctamente. Stock actualizado.')
    
    return redirect('prestamos:listado')