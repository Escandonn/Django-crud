from asyncio import Task
from collections import defaultdict
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task,ProductoComprado,ProductoVenta

from api.forms import TaskForm,ProductoCompradoForm,ProductoVentaForm


def home(request):
    return render(request, 'home.html')



## REGISTRO DE USARIO
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
                
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def list_product(request):
    productos_comprados = ProductoComprado.objects.all()
    return render(request, 'list_product.html', {"productos_comprados": productos_comprados})


def list_venta(request):
    productos_vendidos = ProductoVenta.objects.all()
    return render(request, 'list_venta.html', {"productos_vendidos": productos_vendidos})


def tasks(request):
    return render(request, 'tasks.html', {"tasks": tasks})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')

def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})

def create_product(request):
    if request.method == "GET":
        return render(request, 'create_product.html', {"form": ProductoCompradoForm})
    else:
        try:
            form = ProductoCompradoForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_task.html', {"form": ProductoCompradoForm, "error": "Error creating task."})


def create_venta(request):
    if request.method == "GET":
        return render(request, 'create_venta.html', {"form": ProductoVentaForm})
    else:
        try:
            form = ProductoVentaForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_task.html', {"form": ProductoVentaForm, "error": "Error creating task."})


def product_detail(request, product_id):
    product = get_object_or_404(ProductoComprado, id=product_id)
    if request.method == 'POST':
        form = ProductoCompradoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductoCompradoForm(instance=product)
    return render(request, 'product_detail.html', {'product': product, 'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(ProductoComprado, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_product')
    return render(request, 'product_detail.html', {'product': product})

def update_product(request, product_id):
    product = get_object_or_404(ProductoComprado, id=product_id)
    if request.method == 'POST':
        form = ProductoCompradoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductoCompradoForm(instance=product)
    return render(request, 'product_detail.html', {'product': product, 'form': form})


def venta_detail(request, venta_id):
    venta = get_object_or_404(ProductoVenta, id=venta_id)
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('list_venta')
    else:
        form = ProductoVentaForm(instance=venta)
    return render(request, 'venta_detail.html', {'venta': venta, 'form': form})

def delete_venta(request, venta_id):
    venta = get_object_or_404(ProductoVenta, pk=venta_id)
    
    if request.method == 'POST':
        venta.delete()
        return redirect('list_venta')  # Redirigir a la lista de productos vendidos
    
    return render(request, 'delete_venta.html', {'venta': venta})

def update_venta(request, venta_id):
    venta = get_object_or_404(ProductoVenta, id=venta_id)
    if request.method == 'POST':
        form = ProductoVentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('list_venta')
    else:
        form = ProductoVentaForm(instance=venta)
    return render(request, 'venta_detail.html', {'venta': venta, 'form': form})

def complete_compra(request, product_id):
    compra = get_object_or_404(ProductoComprado, pk=product_id)
    
    if request.method == 'POST':
        compra.fecha_importacion = timezone.now()
        compra.save()
        return redirect('list_product')  # Redirigir a la lista de productos comprados
    
    return render(request, 'complete_compra.html', {'compra': compra})


def fechas_productos_comprados(request):
    productos_comprados = ProductoComprado.objects.all()
    fecha_contador = defaultdict(int)

    for producto in productos_comprados:
        fecha = producto.fecha_importacion.strftime('%Y-%m-%d')
        fecha_contador[fecha] += 1

    fechas_importacion = [{'fecha': fecha, 'cantidad': cantidad} for fecha, cantidad in fecha_contador.items()]

    return render(request, 'fechas_productos_comprados.html', {'fechas_importacion': fechas_importacion})

def fechas_productos_vendidos(request):
    productos_vendidos = ProductoVenta.objects.all()
    fecha_contador = defaultdict(int)

    for producto in productos_vendidos:
        fecha = producto.fecha_venta.strftime('%Y-%m-%d')
        fecha_contador[fecha] += producto.cantidad

    fechas_ventas = [{'fecha': fecha, 'cantidad': cantidad} for fecha, cantidad in fecha_contador.items()]

    return render(request, 'fechas_productos_vendidos.html', {'fechas_ventas': fechas_ventas})



def fechas_dinero_invertido(request):
    ventas = ProductoVenta.objects.all()
    fecha_contador = defaultdict(int)

    for venta in ventas:
        fecha = venta.fecha_venta.strftime('%Y-%m-%d')
        # Sumar el precio_total de todas las ventas para la misma fecha
        fecha_contador[fecha] += int(venta.precio_total)

    fechas_dinero_invertido = [{'fecha': fecha, 'dinero_invertido': dinero} for fecha, dinero in fecha_contador.items()]

    return render(request, 'fechas_dinero_invertido.html', {'fechas_dinero_invertido': fechas_dinero_invertido})


