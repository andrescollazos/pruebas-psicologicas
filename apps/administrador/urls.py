from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required
from views import *


urlpatterns = [
    url(r'^$', index_administrador, name = 'index'),
    url(r'^listar/psicologos$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoList.as_view()),
        name = 'psicologo_listar'),
    url(r'^listar/estudiantes$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteList.as_view()),
        name = 'estudiante_listar'),
    url(r'^crear/psicologos$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoCrear.as_view()),
        name = 'psicologo_crear'),
    url(r'^crear/estudiantes$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteCrear.as_view()),
        name = 'estudiante_crear'),
    url(r'^editar/perfil/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(UsuarioEditar.as_view()),
        name='editar_perfil'),
    url(r'^editar/psicologos/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoEditar.as_view()),
        name = 'psicologo_editar'),
    url(r'^editar/estudiantes/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteEditar.as_view()),
        name = 'estudiante_editar'),
    url(r'^eliminar/psicologos/(?P<pk>\d+)$', PsicologoEliminar, name = 'psicologo_eliminar'),
    url(r'^eliminar/estudiantes/(?P<pk>\d+)$', EstudianteEliminar, name = 'estudiante_eliminar'),
]
