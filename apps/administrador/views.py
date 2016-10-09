from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
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


#def profile_create(request):
#    if request.method == 'POST':
#        user_form = UserForm(request.POST , instance = request.user)
#        #profile_form = ProfileForm(request.POST, instance = request.user.profile)
#        if user_form.is_valid():# and profile_form.is_valid():
#            user_form.save()
#            #profile_form.save()
#            #messages.succes(request, _('Your profile was sucefully updated!'))
#            return redirect('administrador:index')
#    else:
#        user_form = UserForm(instance = request.user)
#        #profile_form = ProfileForm(instace = request.user.profile)
#    return render(request, 'administrador/profile_form.html', {'user_form': user_form})#, 'profile_form': profile_form})
