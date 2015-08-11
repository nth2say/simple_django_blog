# _*_ coding=utf-8 _*_
__author__ = 'lib.o'

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^archive/$', views.ArticleListView.as_view(), name='archive'),
    url(r'^ar/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^show/(?P<pk>[0-9]+)/$', views.show_article, name='show_article'),
    url(r'^add/$', views.add, name='add'),
    url(r'^login/$', views.login, name='login'),
]
