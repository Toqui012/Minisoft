from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto

# Create your views here.


def index(request):
    list = Producto.objects.all()
    return render(request,'index.html',{'list':list})

def login_view(request):
    return render(request,'login_view.html')