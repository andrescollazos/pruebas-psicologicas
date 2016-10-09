from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# CLASE USUARIO
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    TIPO_DOCUMENTO = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
        ('RI', 'Registro Civil')
    )
    tipoDocumento = models.CharField(max_length = 2, choices = TIPO_DOCUMENTO)
    docIdentidad = models.CharField(max_length = 10, primary_key = True)#, unique = True)
    fechaDeNacimiento = models.DateField(null = True, blank = True)
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


# CLASE ADMINISTRADOR -> TIENE LLAVE FORANEA DE USUARIO
class Administrador(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    informacionPersonal = models.TextField(max_length = 140, default = '', blank = True)

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
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100) # Titulo Universitario
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, null = True)

    #def __str__(self):
    #    return self.user

# CLASE GRUPO
#class Grupo(models.Model):
class Grupo(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE) # Un psicologo puede tener varios grupos
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE)
    JORNADA = (
            ('JM', 'JornadaManana'),
            ('JT', 'JornadaTarde'),
            ('JE', 'JornadaEspecial')
            )
    jornada = models.CharField(max_length = 2, choices = JORNADA)

# CLASE ESTUDIANTE
class Estudiante(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    #institucion = models.ForeignKey(Institucion) # Una institucion tiene varios alumnos
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE, null = True) # Un grupo tiene varios alumnos
