# _*_ coding=utf-8 _*_
__author__ = 'lib.o'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'content', 'pub_date']

        widgets = {
            #'to_article': forms.TextInput(attrs={'hidden': True}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }