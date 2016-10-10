from django.conf.urls import url, include
from views import *


urlpatterns = [
    url(r'^$', index_administrador, name = 'index'),
    url(r'^listar/psicologos$', PsicologoList.as_view(), name = 'psicologo_listar'),
    url(r'^listar/estudiantes$', EstudianteList.as_view(), name = 'estudiante_listar'),
    url(r'^crear/psicologos$', PsicologoCrear.as_view(), name = 'psicologo_crear'),
    url(r'^crear/estudiantes$', EstudianteCrear.as_view(), name = 'estudiante_crear'),
    url(r'^editar/psicologos/(?P<pk>\d+)$', PsicologoEditar.as_view(), name = 'psicologo_editar'),
    url(r'^editar/estudiantes/(?P<pk>\d+)$', EstudianteEditar.as_view(), name = 'estudiante_editar'),
    url(r'^eliminar/psicologos/(?P<pk>\d+)$', PsicologoEliminar, name = 'psicologo_eliminar'),
    url(r'^eliminar/estudiantes/(?P<pk>\d+)$', EstudianteEliminar, name = 'estudiante_eliminar'),
]
