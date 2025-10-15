from django.shortcuts import render
from libros.models import Libro
from categorias.models import Categoria
from django.core.paginator import Paginator
from django.db.models import Count

def inicio(request):
    libros_list = Libro.objects.all().order_by('-id')
    categorias = Categoria.objects.annotate(num_libros=Count('libro'))
    
    paginator = Paginator(libros_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'index.html', {
        'page_obj': page_obj,
        'categorias': categorias
    })