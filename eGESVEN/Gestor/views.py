from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductoForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm




# Create your views here.

def redirigir_a_productos(request):
    return redirect('Gestor:lista_producto')

def lista_producto(request):
    productos= Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Gestor:lista_producto')
    else:
        form = ProductoForm()
    return render(request, 'productos/lista_producto.html', {'productos':productos, 'form':form})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Gestor:detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/detalle_producto.html',{'producto':producto, 'form': form})

def eliminar_producto(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('Gestor:lista_producto')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Gestor:home')  
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')  
    else:
        form = LoginForm()  

    return render(request, 'productos/login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  
            user.save()

            messages.success(request, 'Cuenta creada correctamente. Ahora puedes iniciar sesión.')
            return redirect('Gestor:login')  
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RegisterForm()

    return render(request, 'productos/register.html', {'form': form})