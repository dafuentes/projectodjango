#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import Autor, Articulo, Comentario

class AutorAdmin(admin.ModelAdmin):
	list_display = ('username', 'email')

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'fecha_publicacion')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario)
