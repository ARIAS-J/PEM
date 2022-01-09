from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Registro, Categoria, User

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordconfirm = request.POST.get('passwordconfirm')
        
        #encrypt password
        password_encrypt = make_password(password)
        
        if not email:
            messages.error(request, 'El email es requerido.')
        else:
            if not User.objects.filter(email = email).exists() and password == passwordconfirm:
                
                User.objects.create(name = nombre, apellido = apellido, email = email, password = password_encrypt)
                messages.success(request, 'Cuenta registrada correctamente!')
                return render(request, 'accounts/login.html')
            else: 
                messages.error(request, 'Ya existe una cuenta con este email o la contraseña no coincide.')
                return render(request, 'accounts/register.html')
    return render(request, 'accounts/register.html')


def loginpage(request):
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        print('aqui esta el email ===>> ', email)
        password = request.POST.get('password')
        print('aqui esta el password ===>> ', password)
        customers = authenticate(request, email = email, password = password)
        print('aqui esta el user =====>>>',customers)
        if customers is not None:
            login(request, customers)
            return redirect('home')
        else:
            messages.info(request, 'Email incorrecto o contraseña incorrecta.')
            return redirect('login')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutpage(request):
    logout(request)
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