from django.conf.urls import url, include
from views import *


urlpatterns = [
    url(r'^$', index_administrador, name = 'index'),
    url(r'^listar$', ProfileList.as_view(), name = 'profile_listar'),
    url(r'^listarEstudiante$', EstudianteList.as_view(), name = 'estudiante_listar'),
    url(r'^listarPsicologo$', PsicologoList.as_view(), name = 'psicologo_listar'),
    url(r'^CrearProfile$', ProfileCrear.as_view(), name = 'profile_crear')
    #url(r'^nuevo$', profile_create, name = 'profile_create'),
]
