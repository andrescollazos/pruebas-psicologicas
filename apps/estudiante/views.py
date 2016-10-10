from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('administrador.ver_test_estudiante', login_url='/accounts/login/')
def index_estudiante(request):
    return render(request, 'estudiante/index.html')
    #return HttpResponse("Soy la pagina principal de Estudiante")
