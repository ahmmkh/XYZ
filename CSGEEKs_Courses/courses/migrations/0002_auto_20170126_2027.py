# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.CharField(default='', max_length=200),
        ),
    ]
