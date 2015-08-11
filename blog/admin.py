# _*_ coding=utf-8 _*_
from django.contrib import admin

from models import Article, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    ordering = ['pub_date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['to_article', 'pub_date', 'title', 'content']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)