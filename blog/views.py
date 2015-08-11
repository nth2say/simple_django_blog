# _*_ coding=utf-8 _*_

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render_to_response, resolve_url, get_object_or_404
from django.template import RequestContext
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)

import forms
import datetime
import blog_conf
from .models import Article,Comment


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


def login(request):
    redirect_to = request.POST.get(REDIRECT_FIELD_NAME,
                                   request.GET.get(REDIRECT_FIELD_NAME, ''))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url('/list/')

            auth_login(request, form.get_user())
            return HttpResponseRedirect(redirect_to)
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form,
        REDIRECT_FIELD_NAME: redirect_to,
    }

    return render_to_response('blog/index.html', context=context, context_instance=RequestContext(request))


def add(request):
    return HttpResponse("add new artilce!!")


def show_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(to_article=pk)
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.to_article = article
            new_comment.save()
            return HttpResponseRedirect('', {'pk': article.pk})
        else:
            raise HttpResponseBadRequest
    else:
        comment_form = forms.CommentForm(initial={'pub_date': datetime.datetime.now(), 'to_article': article.pk})
    return render_to_response('blog/show_article.html', context={'object': article, 'comments': comments, 'form': comment_form}, context_instance=RequestContext(request))
