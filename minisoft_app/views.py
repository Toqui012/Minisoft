from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto
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
    return render(request,'bodega.html')