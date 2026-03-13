from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def nucleus(request):
    return HttpResponse("pagina do nucleo!!")
