# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20171114_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='contributors',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='owner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='recipients',
            field=models.TextField(),
        ),
    ]
