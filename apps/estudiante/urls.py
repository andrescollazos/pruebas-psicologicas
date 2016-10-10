from django.conf.urls import url, include
from views import index_estudiante

urlpatterns = [
    url(r'^$', index_estudiante, name = 'index'),
]
