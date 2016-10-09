from django.conf.urls import url, include
from views import index_administrador

urlpatterns = [
    url(r'^$', index_administrador),
]
