# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpserver', '0008_remove_task_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='timeout',
            field=models.IntegerField(default=300),
        ),
    ]
