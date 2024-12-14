from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Producto
from .forms import ProductoForm
# Create your views here.

def redirigir_a_productos(request):
    return redirect('Gestor:lista_producto')

def lista_producto(request):
    productos= Producto.objects.all()
    return render(request, 'productos/lista_producto.html', {'productos':productos})

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