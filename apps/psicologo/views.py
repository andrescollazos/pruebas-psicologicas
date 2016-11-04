from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from ..administrador.models import *
from forms import *
# Create your views here.


@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def index_psicologo(request):
    return render(request, 'psicologo/index.html')
    #return HttpResponse("Soy la pagina principal de Un psicologo")

# VISTAS PARA EL LISTADO DE ELEMENTOS

# Listar los grupos que tiene asignado un psicologo:
@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def psicologoGrupoList(request, pk):
    # Buscar el objeto psicologo, con el id que tiene el usuario activo actual
    psicologo = Psicologo.objects.get(user_id = pk)
    # Filtrar los resultador por el psicologo
    grupos_list = Grupo.objects.order_by('nombre_grado').filter(psicologo = psicologo.docIdentidad)
    context = {'grupos_list':grupos_list, 'psicologo':psicologo.docIdentidad}
    return render(request, 'psicologo/grupo_list.html', context)

# Listar los alumnos que tienen los grupos asociados al psicologo
@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def psicologoEstudianteList(request, grupo_id):
    estudiante_list = Estudiante.objects.order_by('docIdentidad').filter(grupo = grupo_id)
    context = {'estudiante_list':estudiante_list, 'grupo':grupo_id}
    return render(request, 'psicologo/estudiante_list.html', context)

# Listar los test que tiene asignado un estudiante
@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def psicologoEstudianteTestList(request, est_id):
    estudiante = Estudiante.objects.get(docIdentidad = est_id)
    testAsignado_list = TestAsignado.objects.filter(estudiante = est_id)
    context = {'testAsignado_list':testAsignado_list, 'estudiante':estudiante}
    return render(request, 'psicologo/estudiante_test_list.html', context)

# Asignar test a un estudiante
@permission_required('administrador.soypsicologo', login_url='/accounts/login/')
def psicologoAsignarTest(request, est_id):
    estudiante = Estudiante.objects.get(docIdentidad = est_id)
    if request.method == 'POST':
        form = TestAsignadoForm(request.POST)
        print "DATOS INGRESADOS---------->"
        print form
        if form.is_valid():
            form.save()
            return psicologoEstudianteTestList(request, est_id)
    else:
        form = TestAsignadoForm()
    return render(request, 'psicologo/asignar_test_form.html', {'form':form, 'estudiante':estudiante})
