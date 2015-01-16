# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from tweetsearch import views

urlpatterns = patterns('',
    # ex: /search/
    url(r'^$', views.search, name='search'),
)
