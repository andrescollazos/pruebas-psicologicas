from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import password_change, password_change_done
from views import *


urlpatterns = [
    url(r'^$', index_administrador, name = 'index'),
    url(r'^listar/psicologos$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoList.as_view()),
        name = 'psicologo_listar'),
    url(r'^listar/estudiantes$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteList.as_view()),
        name = 'estudiante_listar'),
    url(r'^listar/instituciones$', permission_required('administrador.administrar', login_url = '/accounts/login/')(InstitucionList.as_view()),
        name = 'instituciones_listar'),
    url(r'^listar/grupo$', permission_required('administrador.administrar', login_url = '/accounts/login/')(GrupoList.as_view()),
        name = 'grupo_listar'),
    url(r'^listar/test$', permission_required('administrador.administrar', login_url = '/accounts/login/')(TestList.as_view()),
        name = 'test_listar'),
    url(r'^listar/preguntas/(?P<test_id>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PreguntaList),
        name = 'pregunta_listar'),

    url(r'^crear/psicologos$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoCrear.as_view()),
        name = 'psicologo_crear'),
    url(r'^crear/estudiantes$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteCrear.as_view()),
        name = 'estudiante_crear'),
    url(r'^crear/instituciones$', permission_required('administrador.administrar', login_url = '/accounts/login/')(InstitucionCrear.as_view()),
        name = 'instituciones_crear'),
    url(r'^crear/grupo$', permission_required('administrador.administrar', login_url = '/accounts/login/')(GrupoCrear.as_view()),
        name = 'grupo_crear'),
    url(r'^crear/test$', permission_required('administrador.administrar', login_url = '/accounts/login/')(TestCrear.as_view()),
        name = 'test_crear'),
    url(r'^crear/preguntas/(?P<test_id>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PreguntaCrear),
        name = 'pregunta_crear'),

    url(r'^editar/psicologos/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoEditar.as_view()),
        name = 'psicologo_editar'),
    url(r'^editar/estudiantes/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteEditar.as_view()),
        name = 'estudiante_editar'),
    url(r'^editar/instituciones/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(InstitucionEditar.as_view()),
        name = 'instituciones_editar'),
    url(r'^editar/grupo/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(GrupoEditar.as_view()),
        name = 'grupo_editar'),
    url(r'^editar/test/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(TestEditar.as_view()),
        name = 'test_editar'),
    url(r'^editar/pregunta/(?P<pre_id>\d+)/(?P<test_id>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PreguntaEditar),
        name = 'pregunta_editar'),

    url(r'^eliminar/psicologos/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(PsicologoEliminar),
        name = 'psicologo_eliminar'),
    url(r'^eliminar/estudiantes/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(EstudianteEliminar),
        name = 'estudiante_eliminar'),
    url(r'^eliminar/instituciones/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(InstitucionEliminar),
        name = 'instituciones_eliminar'),
    url(r'^eliminar/grupo/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(GrupoEliminar),
        name = 'grupo_eliminar'),
    url(r'^eliminar/test/(?P<pk>\d+)$', permission_required('administrador.administrar', login_url = '/accounts/login/')(TestEliminar),
        name = 'test_eliminar'),
]
