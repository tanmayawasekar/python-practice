# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='votes',
        ),
    ]
