from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required
from views import *

urlpatterns = [
    url(r'^$', index_psicologo, name = 'index'),
    url(r'^listar/grupos/(?P<pk>\d+)$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoGrupoList),
        name = 'grupo_listar'),
    url(r'^listar/(?P<grupo_id>\d+)/estudiantes$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoEstudianteList),
        name = 'estudiante_listar'),
    url(r'^listar/(?P<est_id>\d+)/tests$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoEstudianteTestList),
        name = 'estudiante_test_listar'),

    url(r'^asignar/(?P<est_id>\d+)/tests$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoAsignarTest),
        name = 'asignar_test'),
]
