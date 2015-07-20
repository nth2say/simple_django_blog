# _*_ coding=utf-8 _*_


# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext

import blog_conf
from .models import Article


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(ArticleDetailView, self).get_object()
        # Return the object
        return object

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def index(request):
    title = blog_conf.title
    second_title = blog_conf.second_title

    current_page = 1
    count = Article.objects.count()
    page_count = (count + blog_conf.article_num_per_page - 1) / blog_conf.article_num_per_page
    pk_range = ((current_page - 1) * blog_conf.article_num_per_page, current_page * blog_conf.article_num_per_page)

    article = Article.objects.filter(pk__range=pk_range)

    context = {
        'title': title,
        'second_title': second_title,
        'article': article,
        'page_count': page_count,
        'current_page': current_page,
    }

    return render_to_response("blog\index.html", context=context, context_instance=RequestContext(request))
