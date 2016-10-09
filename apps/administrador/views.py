from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from forms import *
from models import *
# Create your views here.

def index_administrador(request):
    return render(request, 'administrador/index.html')

class ProfileList(ListView):
    model = Profile
    template_name = 'administrador/profile_list.html'

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'administrador/estudiante_list.html'

class PsicologoList(ListView):
    model = Psicologo
    template_name = 'administrador/psicologo_list.html'

class ProfileCrear(CreateView):
    model = Profile
    template_name = 'administrador/profile_form.html'
    form_class = ProfileForm
    second_form_class = UserForm
    success_url = reverse_lazy('administrador:profile_listar')

    def get_context_data(self, **kwargs):
        context = super(ProfileCrear, self).get_context_data(**kwargs)
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
            profile = form.save(commit = False)
            profile.user = form2.save()
            profile.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

class ProfileEditar(UpdateView):
    model = Profile
    second_model = User
    template_name = 'administrador/profile_editar_form.html'
    form_class = ProfileForm
    second_form_class = UserForm
    success_url = reverse_lazy('administrador:profile_listar')

    def get_context_data(self, **kwargs):
        context = super(ProfileEditar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        profile = self.model.objects.get(docIdentidad = pk)
        user = self.second_model.objects.get(id = profile.user_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2'not in context:
            context['form2'] = self.second_form_class(instance = user)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_profile = kwargs['pk']
        profile = self.model.objects.get(docIdentidad = id_profile)
        user = self.second_model.objects.get(id = profile.user_id)

        form = self.form_class(request.POST, instance = profile)
        print "FORM: ", form
        form2 = self.second_form_class(request.POST, instance = user)
        print "\n\nFORM2", form2

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            #print "ALGO FALLO"
            return HttpResponseRedirect(self.get_success_url())
