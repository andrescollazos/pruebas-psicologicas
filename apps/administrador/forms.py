# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'username': 'Nombre de Usuario',
            'email': 'Correo electronico',
            'password': 'Contraseña',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'tipoDocumento',
            'docIdentidad',
            'fechaDeNacimiento',
            'direccion',
            'telefono',
        ]
        labels = {
            'tipoDocumento': 'Tipo de documento',
            'docIdentidad': 'Documento de Identidad',
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
        }
