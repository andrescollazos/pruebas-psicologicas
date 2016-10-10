from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
# Create your views here.


@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def index_psicologo(request):
    return render(request, 'psicologo/index.html')
    #return HttpResponse("Soy la pagina principal de Un psicologo")
