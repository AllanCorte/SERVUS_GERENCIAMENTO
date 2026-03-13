from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ministries(request):
    return HttpResponse("pagina de ministerios!")
