from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse('HOME')

def contato(rquest):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')