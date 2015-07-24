# _*_ coding=utf-8 _*_
from django.db import models

import blog_conf


class Tag(models.Model):
    name = models.CharField(max_length=blog_conf.max_tag_length, unique=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=blog_conf.max_title_length)
    content = models.TextField()
    pub_date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    summary = models.CharField(max_length=blog_conf.max_summary_length)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    to_article = models.ForeignKey(Article)
    title = models.CharField(max_length=200, blank=True)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title + ':' + self.content

    class Meta:
        ordering = ('pub_date',)
