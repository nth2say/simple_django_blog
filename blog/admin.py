# _*_ coding=utf-8 _*_
from django.contrib import admin

from models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    ordering = ['pub_date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
