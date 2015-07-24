# _*_ coding=utf-8 _*_
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from .models import Article,Comment
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url

import forms
import datetime


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
        article = super(ArticleDetailView, self).get_object()
        # Return the object
        return article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = forms.CommentForm()
        return context

def index(request):
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
