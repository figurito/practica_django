from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

def lista_producto(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'lista_productos.html', context)
