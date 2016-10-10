# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-10 06:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('cargoInstitucional', models.TextField(blank=True, default='', max_length=140)),
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad'), ('RI', 'Registro Civil')], max_length=2)),
                ('docIdentidad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fechaDeNacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad'), ('RI', 'Registro Civil')], max_length=2)),
                ('docIdentidad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fechaDeNacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jornada', models.CharField(choices=[('JM', 'JornadaManana'), ('JT', 'JornadaTarde'), ('JE', 'JornadaEspecial')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('nit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('paginaWeb', models.URLField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad'), ('RI', 'Registro Civil')], max_length=2)),
                ('docIdentidad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fechaDeNacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Institucion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Institucion'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='psicologo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Psicologo'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Grupo'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
