# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 10:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0004_auto_20190316_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
