# coding=utf-8

from django import forms
from ..administrador.models import *

# FORMULARIO PARA LA ASIGNACIÓN DE TEST
class TestAsignadoForm(forms.ModelForm):
    class Meta:
        model = TestAsignado
        fields = [
            'estudiante',
            'test',
        ]
        labels = {
            'estudiante' : 'Asignar al estudiante',
            'test' : 'Tipo de Test',
        }
