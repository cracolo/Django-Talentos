from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'alumnos/index.html', context)   
def nosotros(request):
    return render(request, 'alumnos/html/nosotros.html')
def contacto(request):
    return render(request, 'alumnos/html/contacto.html')
def musica(request):
    return render(request, 'alumnos/html/musica.html')