# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 04:51
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_图片'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='发布时间',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='图片',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]