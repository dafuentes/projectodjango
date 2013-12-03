#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Autor(models.Model):
	username = models.CharField("Username", max_length=75)
	nombre = models.CharField("Nombre", max_length=255)
	apellido = models.CharField("Apellido", max_length=255)
	email = models.EmailField("Email", max_length=255)
	info = models.TextField("Informacion del Autor")
	imagenAutor = models.ImageField(upload_to="images")

	def obtener_nombre_completo(self):
		return '%s %s' % (self.nombre, self.apellido)

	nombre_completo = property(obtener_nombre_completo)

	def image_tag():
		return '<img src="%s" />' % self.imagenAutor.url

	image_tag.short_description = 'Imagen'
	image_tag.allow_tags = True

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.apellido)


class Articulo(models.Model):
	autor = models.ForeignKey(Autor)
	titulo = models.CharField("Titulo", max_length=255)
	subtitulo = models.CharField("subtitulo",max_length=255,blank=True)
	fecha_publicacion = models.DateTimeField(auto_now=True)
	contenido = models.TextField()
	portada = models.ImageField(upload_to="images")

	def __unicode__(self):
		return self.titulo


class Comentario(models.Model):
	articulo = models.ForeignKey(Articulo)
	nombre = models.CharField('Nombre', max_length=255)
	comentario = models.TextField()
	fecha_publicacion = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.comentario
		