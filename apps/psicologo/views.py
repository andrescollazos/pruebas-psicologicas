from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_psicologo(request):
    return HttpResponse("Soy la pagina principal de Un psicologo")
