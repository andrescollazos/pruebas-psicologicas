# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
TIPO_DOCUMENTO = (
    ('CC', 'Cedula de Ciudadania'),
    ('TI', 'Tarjeta de Identidad'),
    ('RI', 'Registro Civil')
)

# CLASE ADMINISTRADOR -> TIENE LLAVE FORANEA DE USUARIO
class Administrador(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    cargoInstitucional = models.TextField(max_length = 140, default = '', blank = True)
    tipoDocumento = models.CharField(max_length = 2, choices = TIPO_DOCUMENTO)
    docIdentidad = models.CharField(max_length = 10, primary_key = True)#, unique = True)
    fechaDeNacimiento = models.DateField(null = True, blank = True)
    direccion = models.CharField(max_length = 120)
    telefono = models.CharField(max_length = 10, blank = True)

    def _str_(self):
        return 'Admin. ' + self.user.first_name

    class Meta:
        permissions = (
            ('administrar', 'Puede administrar'),
        )

# CLASE INSTITUCION
class Institucion(models.Model):
    nit = models.CharField(max_length = 20, primary_key = True)
    nombre = models.CharField(max_length = 70, unique = True)
    telefono = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 50)
    paginaWeb = models.URLField(max_length = 200)
    direccion = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

# CLASE PSICOLOGO
class Psicologo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tipoDocumento = models.CharField(max_length = 2, choices = TIPO_DOCUMENTO)
    docIdentidad = models.CharField(max_length = 10, primary_key = True)#, unique = True)
    fechaDeNacimiento = models.DateField(null = True, blank = True)
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 10, blank = True)
    titulo = models.CharField(max_length = 100) # Titulo Universitario
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.user.first_name +' '+ self.user.last_name

    class Meta:
        permissions = (
            ('soypsicologo', 'Puedo ejercer'),
            ("ver_evaluacion_psicologo", "Puede ver las evaluaciones"),
            ("ver_diagnostico_psicologo", "Puede ver los diagnosticos"),
            ("realizar_diagnostico", "Puede realizar un diagnostico")
        )

# CLASE GRUPO
#class Grupo(models.Model):
class Grupo(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE) # Un psicologo puede tener varios grupos
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE)
    JORNADA = (
            ('JM', 'Jornada Mañana'),
            ('JT', 'Jornada Tarde'),
            ('JE', 'Jornada Especial')
            )
    jornada = models.CharField(max_length = 2, choices = JORNADA)
    nombre_grado = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return self.nombre_grado+' '+self.institucion.nombre

# CLASE ESTUDIANTE
class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tipoDocumento = models.CharField(max_length = 2, choices = TIPO_DOCUMENTO)
    docIdentidad = models.CharField(max_length = 10, primary_key = True)#, unique = True)
    fechaDeNacimiento = models.DateField(null = True, blank = True)
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 10, blank = True)
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE, null = True) # Un grupo tiene varios alumnos

    class Meta:
        permissions = (
            ("ver_test_estudiante", "Puede ver los test"),
            ("ver_diagnostico", "Puede ver los diagnosticos")
        )

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

# CLASE TEST (Tipos de test)
class Test(models.Model):
    descripcion = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return self.descripcion

# CLASE TEST ASIGNADO:
class TestAsignado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    #respuestas = models.ForeignKey(Respuestas, on_delete = models.CASCADE)

# CLASE PREGUNTAS
class Pregunta(models.Model):
    pregunta = models.TextField()
    numero = models.CharField(max_length = 10, null = True)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)

    def __str__(self):
        return self.pregunta+' '+str(self.test.id)
