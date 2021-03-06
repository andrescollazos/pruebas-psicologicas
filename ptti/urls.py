"""ptti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib import admin
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.views import password_change, password_change_done
from django.shortcuts import render
from apps.administrador.views import *

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^administrador/', include('apps.administrador.urls', namespace = "administrador")),
    url(r'^estudiante/', include('apps.estudiante.urls', namespace = "estudiante")),
    url(r'^psicologo/', include('apps.psicologo.urls', namespace = "psicologo")),
    url(r'^$', index, name= "index"),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name = "login"),
    url(r'^logout/$', logout_then_login, name = "logout"),
    url(r'^reset/password_reset', password_reset,
        {'template_name': 'registration/password_reset_form.html',
        'email_template_name':'registration/password_reset_email.html'},
        name = 'password_reset'),
    url(r'^reset/password_reset_done', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name = 'password_reset_confirm'),
    url(r'^reset/done', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name = 'password_reset_complete'),
    url(r'^editar/perfil/(?P<pk>\d+)$', login_required(login_url = '/accounts/login/')(UsuarioEditar.as_view()),
            name='editar_perfil'),
    url(r'^editar/password/$', login_required(login_url = '/accounts/login/')(UsuarioEditarPassword),
            name='editar_password'),

]
