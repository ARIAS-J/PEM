from django.core.checks import messages
from django.shortcuts import render
from .models import Registro, Categoria

# Create your views here.

def home(request):
    categorias = Categoria.objects.all()
    
    context = {
        'categorias': categorias
    }
    
    if request.method == 'POST':
        monto = request.POST['monto']
        descripcion = request.POST['descripcion']
        fecha = request.POST['datetime']
        nombre_categoria = request.POST['categoria']
        
        try:
            categoria = Categoria.objects.get(nombre = nombre_categoria)
        except Categoria.DoesNotExist:
            categoria = None

        if not monto:
            messages.Error(request, 'El monto es requerido')
        else:
            Registro.objects.create(monto = monto, descripcion = descripcion, fecha = fecha, categoria = categoria)
        return render(request, 'pem/home.html', context)
    
    return render(request, 'pem/home.html', context)

def categoria(request):
    
    if request.method == 'POST':
        categoria = request.POST['addcategorias']
        Categoria.objects.create(nombre = categoria)
    
    return render(request, 'pem/categoria.html')

def historial(request):
    historials = Registro.objects.all()
    
    # print(historials[0].categoria)
    context = {'historials': historials}
    
    return render(request, 'pem/historial.html', context)

def Constante_registro(request):
    
    return render(request, 'pem/home.html')