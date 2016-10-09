# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo electronico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'password': 'Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'first_name': forms.TextInput(attrs = {'class':'form-control'}),
            'last_name': forms.TextInput(attrs = {'class':'form-control'}),
            'password' : forms.PasswordInput(attrs = {'class':'form-control'}),
        }

TIPO_DOCUMENTO = (
    ('CC', 'Cedula de Ciudadania'),
    ('TI', 'Tarjeta de Identidad'),
    ('RI', 'Registro Civil')
)

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
            'tipoDocumento': 'Tipo de documento (CC-TI-RI)',
            'docIdentidad': 'Documento de Identidad',
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
        }
        widgets = {
            'tipoDocumento': forms.TextInput(attrs = {'class': 'form-control'}),#CheckboxInput(),
            'docIdentidad': forms.TextInput(attrs = {'class': 'form-control'}),
            'fechaDeNacimiento' : forms.DateInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs = {'class': 'form-control'}),
        }
