# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app2', '0006_delete_blogapp2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogApp2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
