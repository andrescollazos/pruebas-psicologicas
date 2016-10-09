from django.conf.urls import url, include
from views import index_psicologo

urlpatterns = [
    url(r'^index$', index_psicologo),
]
