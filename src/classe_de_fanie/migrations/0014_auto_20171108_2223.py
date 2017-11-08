# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-08 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe_de_fanie', '0013_eleve_enseignant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='enseignant',
        ),
        migrations.AddField(
            model_name='eleve',
            name='non_enseignant',
            field=models.BooleanField(default=True),
        ),
    ]