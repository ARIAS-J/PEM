from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Registro, Categoria, User

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        passwordconfirm = request.POST['passwordconfirm']
        
        if not email:
            messages.error(request, 'El email es requerido.')
        else:
            if not User.objects.filter(email = email).exists() and password == passwordconfirm:
                
                User.objects.create(name = nombre, apellido = apellido, email = email, password = password)
                messages.success(request, 'Cuenta registrada correctamente!')
                return render(request, 'registration/login.html')
            else: 
                messages.error(request, 'Ya existe una cuenta con este email o la contraseña no coincide.')
                return render(request, 'pem/register.html')
    return render(request, 'pem/register.html')

def loginpage(request):
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # user = authenticate(username = email, password = password)
        user = authenticate(email = email, password = password)
        print("User aqui ====>>>>>", user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email incorrecto o contraseña incorrecta.')
            return redirect('login')
        
    return render(request, 'registration/login.html')


def logoutpage(request):
    return redirect('login')


@login_required
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


@login_required
def categoria(request):
    
    if request.method == 'POST':
        categoria = request.POST['addcategorias']
        Categoria.objects.create(nombre = categoria)
    
    return render(request, 'pem/categoria.html')


@login_required
def historial(request):
    historials = Registro.objects.all()
    
    # print(historials[0].categoria)
    context = {'historials': historials}
    
    return render(request, 'pem/historial.html', context)