# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 19:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_auto_20170103_1911'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'product')]),
        ),
    ]
