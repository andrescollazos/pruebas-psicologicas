# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import *

# FORMULARIOS PARA LA CREACION DE PROFILES:

# FORMULARIO PARA LA CREACION DEL OBJETO USER
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo electronico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }

TIPO_DOCUMENTO = (
    ('CC', 'Cedula de Ciudadania'),
    ('TI', 'Tarjeta de Identidad'),
    ('RI', 'Registro Civil')
)

GENERO = (
    ('HOMBRE', 'Hombre'),
    ('MUJER', 'Mujer')
)
# FORMULARIO PARA LA CREACION DEL OBJETO PSICOLGO
class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = [
            'tipoDocumento',
            'docIdentidad',
            'fechaDeNacimiento',
            'direccion',
            'telefono',
            'titulo',
        ]
        labels = {
            'tipoDocumento': 'Tipo de documento (CC-TI-RI)',
            'docIdentidad': 'Documento de Identidad',
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
            'titulo' : 'Titulo Universitario',
        }

# FORMULARIO PARA LA CREACION DEL OBJETO ESTUDIANTE
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'tipoDocumento',
            'docIdentidad',
            'fechaDeNacimiento',
            'direccion',
            'telefono',
            #'grupo',
        ]
        labels = {
            'tipoDocumento': 'Tipo de documento (CC-TI-RI)',
            'docIdentidad': 'Documento de Identidad',
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
            #'grupo' : 'Grupo asignado'
        }

# FORMULARIO PARA LA CREACION DEL OBJETO INSTITUCION
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = [
            'nit',
            'nombre',
            'telefono',
            'email',
            'paginaWeb',
            'direccion',
        ]
        labels = {
            'nit': 'NIT',
            'nombre': 'Nombre de la Institucion',
            'telefono': 'Telefono',
            'email': 'Correo electronico',
            'paginaWeb': 'Sitio Web',
            'direccion': 'Direccion',
        }

# FORMULARIOS PARA LA MODIFICACION DE PROFILES (YA QUE NO SE REQUIEREN TODOS LOS CAMPOS)

# Model User
class UserEditarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo electronico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }
        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'first_name': forms.TextInput(attrs = {'class':'form-control'}),
            'last_name': forms.TextInput(attrs = {'class':'form-control'}),
        }

# Modelo Institucion
class InstitucionEditarForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = [
            'nombre',
            'telefono',
            'email',
            'paginaWeb',
            'direccion',
        ]
        labels = {
            'nombre': 'Nombre de la Institucion',
            'telefono': 'Telefono',
            'email': 'Correo electronico',
            'paginaWeb': 'Sitio Web',
            'direccion': 'Direccion',
        }

# Modelo Psicologo
class PsicologoEditarForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = [
            'fechaDeNacimiento',
            'direccion',
            'telefono',
            'titulo',
        ]
        labels = {
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
            'titulo': 'Titulo Universitario',
        }
        widgets = {
            'fechaDeNacimiento' : forms.DateInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs = {'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs = {'class':'form-control'}),
        }

# Modelo Estudiante
class EstudianteEditarForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'fechaDeNacimiento',
            'direccion',
            'telefono',
            #'grupo',
        ]
        labels = {
            'fechaDeNacimiento': 'Fecha de Nacimiento (yyyy-mm-dd)',
            'direccion': 'Direccion de recidencia',
            'telefono': 'Telefono',
            #'grupo': 'Grupo de Clase'
        }
        widgets = {
            'fechaDeNacimiento' : forms.DateInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs = {'class': 'form-control'}),
            #'grupo' : forms.TextInput(attrs = {'class':'form-control'})
        }
