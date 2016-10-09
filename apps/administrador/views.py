from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User

from forms import *
from models import *
# Create your views here.

def index_administrador(request):
    return render(request, 'administrador/index.html')

class UserList(ListView):
    model = Profile
    template_name = 'administrador/profile_list.html'

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'administrador/estudiante_list.html'

class PsicologoList(ListView):
    model = Psicologo
    template_name = 'administrador/psicologo_list.html'


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
