# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180626_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
