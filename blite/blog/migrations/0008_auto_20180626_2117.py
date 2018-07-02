# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180619_1631'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('posts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
