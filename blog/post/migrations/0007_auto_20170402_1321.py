# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170402_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.URLField(default=None, null=True),
        ),
    ]
