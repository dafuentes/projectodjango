#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Autor, Articulo

def index(request):
	articulos = Articulo.objects.all()
	return render_to_response('index.html', {'titulo':'Lista de Articulos', 'posts':articulos}, context_instance=RequestContext(request))

def autores(request):
	lista = Autor.objects.all()
	return render_to_response('autores.html', {'titulo': 'Lista de Autores','listado':lista}, context_instance=RequestContext(request))

def autor(request, id_autor):
	detalle_autor = get_object_or_404(Autor, pk=id_autor)
	return render_to_response('detalle_autor.html', {'titulo':detalle_autor.username, 'autor':detalle_autor}, context_instance=RequestContext(request))

def detalle(request, id_post):
	try:
		single = Articulo.objects.get(pk=id_post)
	except Exception, e:
		raise Http404
	return render_to_response('detail.html', {'titulo':single.titulo,'post':single}, context_instance=RequestContext(request))
