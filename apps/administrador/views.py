from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_administrador(request):
    return render(request, 'administrador/index.html')
