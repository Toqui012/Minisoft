from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'login_view.html')