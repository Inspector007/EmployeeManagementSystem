# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=50)),
                ('empEmail', models.EmailField(max_length=50)),
                ('empPan', models.CharField(max_length=50)),
            ],
        ),
    ]
