# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-22 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classe_de_fanie', '0002_eleve_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eleve',
            old_name='courriel_mere',
            new_name='courriel_parents_1',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='courriel_pere',
            new_name='courriel_parents_2',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='nom_mere',
            new_name='nom_parents_1',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='nom_pere',
            new_name='nom_parents_2',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='prenom_mere',
            new_name='prenom_parents_1',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='prenom_pere',
            new_name='prenom_parents_2',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='telephone_mere',
            new_name='telephone_parents_1',
        ),
        migrations.RenameField(
            model_name='eleve',
            old_name='telephone_pere',
            new_name='telephone_parents_2',
        ),
    ]
