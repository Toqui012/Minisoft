from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto,Strike
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


# Create your views here.


def index(request):
    list = Producto.objects.all()
    return render(request,'index.html',{'list':list})

def login_view(request):
    status = ''
    if request.method == 'POST':
        username = request.POST.get('txtRut')
        password = request.POST.get('txtPassword')
        print("El texto primero es: ",username)
        print("La contraseña recibida es: ",password)
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            status = 'OK'
            return HttpResponseRedirect(reverse('index'))
        else:
            status = 'ERROR'
            messages.error(request,'Error al iniciar sesión')
    variables = {'status':status}
    return render(request,'login_view.html',variables)

@login_required(login_url = 'login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')


def bodega(request):
    list = Producto.objects.all()
    status = ''
    if request.method == 'POST':
        try:
            familiaBusca = request.POST.get('selectorFamilia')
            colorBusca = request.POST.get('txtColorBusca')
            if Producto.objects.all().filter(familia = familiaBusca, color = colorBusca):
                status = 'SEARCH'
                list = Producto.objects.all().filter(familia = familiaBusca, color = colorBusca)
            
            elif Producto.objects.all().filter(familia = familiaBusca):
                status = 'SEARCHFamilia'
                list = Producto.objects.all().filter(familia = familiaBusca)
            
            elif Producto.objects.all().filter(color = colorBusca):
                status = 'SEARCHColor'
                list = Producto.objects.all().filter(color = colorBusca)
                
            else:
                status = 'NOTSEARCH'
                list = Producto.objects.all()
        except:
            status = 'NOTSEARCH'
    variables = {'status':status,
                 'list':list}
    return render(request,'bodega.html',variables)


def mermas(request):
    list = Producto.objects.all()
    status = ''
    if request.method == 'POST':
        try:
            nombreProducto = request.POST.get('txtNombreProducto')
            if Producto.objects.all().filter(nombre = nombreProducto) and Producto.objects.all().filter(merma = True):
                status = 'SEARCH'
                list = Producto.objects.all().filter(nombre = nombreProducto)
            else:
                status = 'NOTSEARCH'
                list = Producto.objects.all().filter(merma = True)
        except:
            status = 'ERROR'
    print(status)    
    variables = {'status':status,
                 'list':list}
    return render(request,'mermas.html',variables)


def strikes(request):
    status = ''
    try:
        status = 'OK'
        list = Strike.objects.all();
    except:
        status = 'ERROR'
    
    variables = {'status':status,
                 'list':list}
    return render(request,'strikes.html',variables)

def add_strike(request):
    status = ''
    if request.method == 'POST':
        try:
            nuevoStrike = Strike()
            nuevoStrike.rut = request.POST.get('txtRut')
            print(request.POST.get('txtRut'))
            nuevoStrike.nombre = request.POST.get('txtNombre')
            print(request.POST.get('txtNombre'))
            nuevoStrike.apellido = request.POST.get('txtApellido')
            print(request.POST.get('txtApellido'))
            nuevoStrike.correo = request.POST.get('txtCorreo')
            print(request.POST.get('txtCorreo'))
            nuevoStrike.cantidad = request.POST.get('txtCantidad')
            print(request.POST.get('txtCantidad'))
            if int(nuevoStrike.cantidad) <= 3 and int(nuevoStrike.cantidad) >= 1:
                nuevoStrike.save()
                status = 'OK'
            else:
                status = 'ERROR'
        except:
            status = 'ERROR'
    return render(request,'add_strike.html',{'status':status})

def update_strike(request):
    return render(request,'update_strike.html')

def delete_strike(request,id):
    status = 'NO_CONTENT'
    try:
        list = Strike.objects.all()
        Strike.objects.get(pk = id).delete()
        status = 'DELETED'
    except:
        status = 'ERROR'
    
    variables = {'status':status,
                 'list':list}
    return render(request,'strikes.html',variables)