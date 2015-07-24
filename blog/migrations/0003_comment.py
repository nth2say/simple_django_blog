# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150721_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('content', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('to_article', models.ForeignKey(to='blog.Article')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
