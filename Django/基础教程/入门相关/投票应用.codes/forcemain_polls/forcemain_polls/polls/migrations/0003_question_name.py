# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-11 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_question_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
