from django.conf.urls import url, include
from django.contrib.auth.decorators import permission_required
from views import *

urlpatterns = [
    url(r'^$', index_psicologo, name = 'index'),
    url(r'^listar/grupos/(?P<pk>\d+)$$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoGrupoList),
        name = 'grupo_listar'),
    url(r'^listar/estudiante/(?P<grupo_id>\d+)$$', permission_required('administrador.soypsicologo', login_url = '/accounts/login/')(psicologoEstudianteList),
        name = 'estudiante_listar'),
]
