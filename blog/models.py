# _*_ coding=utf-8 _*_
from django.db import models

import blog_conf


class Tag(models.Model):
    name = models.CharField(max_length=blog_conf.max_tag_length)

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
