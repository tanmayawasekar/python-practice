# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
