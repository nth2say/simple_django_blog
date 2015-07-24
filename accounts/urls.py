# _*_ coding=utf-8 _*_
__author__ = 'lib.o'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout'),
    url(r'^register/$', 'accounts.views.register'),
]
