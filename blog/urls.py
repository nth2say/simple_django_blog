# _*_ coding=utf-8 _*_
__author__ = 'lib.o'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index),
]
