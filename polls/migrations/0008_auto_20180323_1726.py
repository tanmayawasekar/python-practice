# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180323_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['question_text'], name='polls_quest_questio_13fa43_idx'),
        ),
    ]