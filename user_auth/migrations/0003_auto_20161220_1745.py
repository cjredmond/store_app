# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adress_city',
            new_name='address_city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='adress_num',
            new_name='address_num',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='adress_state',
            new_name='address_state',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='adress_street',
            new_name='address_street',
        ),
    ]
