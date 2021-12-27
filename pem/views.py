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
        
        if not monto:
            messages.Error(request, 'El monto es requerido')
        return render(request, 'pem/home.html', context)
    
    return render(request, 'pem/home.html', context)

def categoria(request):
    pass
    return render(request, 'pem/categoria.html')