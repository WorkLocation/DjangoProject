# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170307_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='email',
            field=models.CharField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
