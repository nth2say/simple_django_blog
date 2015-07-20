# _*_ coding=utf-8 _*_
__author__ = 'lib.o'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.ArticleListView.as_view(), name='article-list'),
]
