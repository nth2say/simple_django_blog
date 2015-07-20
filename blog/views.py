# _*_ coding=utf-8 _*_
from django.http import HttpResponse


# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

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
    return HttpResponse("this is index")
