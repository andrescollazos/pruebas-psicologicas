# coding=utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm

from forms import *
from models import *
# Create your views here.

@permission_required('administrador.administrar', login_url = '/accounts/login/')
def index_administrador(request):
    return render(request, 'administrador/index.html')

# VISTAS RELACIONADAS A TODOS LOS USERS (SIN DISCRIMINACION)

# VIEWS CORRESPONDIENTES AL LISTADO DE MODELOS:

# Modelo estudiante
#@permission_required('administrador.administrar', login_url = '/accounts/login/')
class EstudianteList(ListView):
    model = Estudiante
    template_name = 'administrador/estudiante_list.html'

# Modelo Psicologo
#@permission_required('administrador.administrar', login_url = '/accounts/login/')
class PsicologoList(ListView):
    model = Psicologo
    template_name = 'administrador/psicologo_list.html'

# Modelo Institucion
class InstitucionList(ListView):
    model = Institucion
    template_name = 'administrador/instituciones_list.html'

# VISTAS RELACIONADAS A LA CREACION DE REGISTROS
class InstitucionCrear(CreateView):
    model = Institucion
    template_name = 'administrador/instituciones_form.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('administrador:instituciones_listar')

# Modelo Psicologo
class PsicologoCrear(CreateView):
    try:
        p = Psicologo.objects.filter(fechaDeNacimiento = None)
        p.delete()
    except:
        pass

    model = Psicologo
    template_name = 'administrador/psicologo_form.html'
    form_class = PsicologoForm
    second_form_class = UserForm
    success_url = reverse_lazy('administrador:psicologo_listar')

    def get_context_data(self, **kwargs):
        context = super(PsicologoCrear, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            grupo = Group.objects.get(name = 'psicologos')
            psicologo = form.save(commit = False)
            psicologo.user = form2.save()
            psicologo.user.groups.add(grupo)
            psicologo.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

# Modelo Estudiante
class EstudianteCrear(CreateView):
    try:
        p = Estudiante.objects.filter(fechaDeNacimiento = None)
        p.delete()
    except:
        pass

    model = Estudiante
    template_name = 'administrador/estudiante_form.html'
    form_class = EstudianteForm
    second_form_class = UserForm
    success_url = reverse_lazy('administrador:estudiante_listar')

    def get_context_data(self, **kwargs):
        context = super(EstudianteCrear, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            grupo = Group.objects.get(name = 'estudiantes')
            estudiante = form.save(commit = False)
            estudiante.user = form2.save()
            estudiante.user.groups.add(grupo)
            estudiante.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

# VIEWS RELACIONADAS A LA EDICION DE LOS REGISTROS
# Modelo User
class UsuarioEditar(UpdateView):
    model = User
    template_name = 'editar.html'
    form_class = UserEditarForm
    success_url = reverse_lazy('index')

@login_required(login_url = '/accounts/login/')
def UsuarioEditarPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'editar_password.html', {'form': form})

# Modelo Psicologo
class PsicologoEditar(UpdateView):
    model = Psicologo
    second_model = User
    template_name = 'administrador/psicologo_editar_form.html'
    form_class = PsicologoEditarForm
    second_form_class = UserEditarForm
    success_url = reverse_lazy('administrador:psicologo_listar')

    def get_context_data(self, **kwargs):
        context = super(PsicologoEditar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        psicologo = self.model.objects.get(docIdentidad = pk)
        user = self.second_model.objects.get(id = psicologo.user_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2'not in context:
            context['form2'] = self.second_form_class(instance = user)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_profile = kwargs['pk']
        psicologo = self.model.objects.get(docIdentidad = id_profile)
        user = self.second_model.objects.get(id = psicologo.user_id)

        form = self.form_class(request.POST, instance = psicologo)
        #print "FORM: ", form
        form2 = self.second_form_class(request.POST, instance = user)
        #print "\n\nFORM2", form2

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            #print "ALGO FALLO"
            return HttpResponseRedirect(self.get_success_url())

# Modelo Estudiante
class EstudianteEditar(UpdateView):
    model = Estudiante
    second_model = User
    template_name = 'administrador/estudiante_editar_form.html'
    form_class = EstudianteEditarForm
    second_form_class = UserEditarForm
    success_url = reverse_lazy('administrador:estudiante_listar')

    def get_context_data(self, **kwargs):
        context = super(EstudianteEditar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        estudiante = self.model.objects.get(docIdentidad = pk)
        user = self.second_model.objects.get(id = estudiante.user_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2'not in context:
            context['form2'] = self.second_form_class(instance = user)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_profile = kwargs['pk']
        estudiante = self.model.objects.get(docIdentidad = id_profile)
        user = self.second_model.objects.get(id = estudiante.user_id)

        form = self.form_class(request.POST, instance = estudiante)
        #print "FORM: ", form
        form2 = self.second_form_class(request.POST, instance = user)
        #print "\n\nFORM2", form2

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            #print "ALGO FALLO"
            return HttpResponseRedirect(self.get_success_url())

# VIEWS RELACIONADAS A LA ELIMINACION DE REGISTROS

# Modelo Psicologo
@permission_required('administrador.administrar', login_url = '/accounts/login/')
def PsicologoEliminar(request, pk):
    psicologo = Psicologo.objects.get(docIdentidad = pk)
    if request.method == 'POST':
        psicologo.user.is_active = 0
        psicologo.save()
        psicologo.delete()
        return HttpResponseRedirect(reverse_lazy('administrador:psicologo_listar'))
    return render(request, 'administrador/psicologo_eliminar.html', {'psicologo':psicologo})

# Modelo Estudiante
@permission_required('administrador.administrar', login_url = '/accounts/login/')
def EstudianteEliminar(request, pk):
    estudiante = Estudiante.objects.get(docIdentidad = pk)
    if request.method == 'POST':
        estudiante.user.is_active = 0
        estudiante.save()
        estudiante.delete()
        return HttpResponseRedirect(reverse_lazy('administrador:estudiante_listar'))
    return render(request, 'administrador/estudiante_eliminar.html', {'estudiante': estudiante})

# NO SE HARA USO DE LA CLASE DeleteView YA QUE SOLO QUEEREMOS HACER UN BORRADO LOGICO:
# SE ELIMINA DE LA TABLA DE Profile, PERO NO DE LA TABLA DE User, EN DICHA TABLA SOLO
# SE PONE COMO INACTIVA LA CUENTA
