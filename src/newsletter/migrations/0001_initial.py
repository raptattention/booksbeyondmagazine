# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('maintext', models.TextField(null=True, blank=True)),
                ('event1', models.CharField(max_length=200, null=True, blank=True)),
                ('event1text', models.TextField(null=True, blank=True)),
                ('event2', models.CharField(max_length=200, null=True, blank=True)),
                ('event2text', models.TextField(null=True, blank=True)),
                ('bookrecommendationtitle', models.CharField(max_length=200, null=True, blank=True)),
                ('bookrecommendationpicture', models.ImageField(upload_to=b'')),
                ('bookrecommendationdescription', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(max_length=120, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
