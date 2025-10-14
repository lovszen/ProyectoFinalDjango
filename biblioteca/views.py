from django.shortcuts import render

def inicio(request):
    """
    Renderiza la página de inicio del proyecto.
    El template se llama 'index.html' (página principal de la biblioteca).
    """
    return render(request, 'index.html')