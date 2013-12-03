#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^autores/', views.autores, name="autores"),
	url(r'^autor/(?P<id_autor>\d+)/$', views.autor, name="autor"),
	url(r'^post/(?P<id_post>\d+)/$', views.detalle, name="detalle"),
)