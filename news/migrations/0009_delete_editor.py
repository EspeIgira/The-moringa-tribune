# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190320_1342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
