# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170130_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='img',
            field=models.ImageField(upload_to='upload/.png'),
        ),
    ]