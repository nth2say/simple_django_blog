# _*_ coding=utf-8 _*_
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.forms import UserCreationForm
from django.template import  RequestContext
# Create your views here.


def register(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/list')
    return HttpResponseBadRequest()
