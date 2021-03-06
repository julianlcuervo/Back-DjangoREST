# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-17 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('idMovie', models.AutoField(primary_key=True, serialize=False)),
                ('Gender', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('Cover', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Name', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.TextField()),
                ('IDUser', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
