# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_access_token', models.TextField(help_text='Click on "Get Access Token" and you will be redirected to             Instagram, then follow the instructions. Remember to log in with             the account that you want to show on the web page.', verbose_name='Access token')),
            ],
            options={
                'verbose_name': 'Django Instagram Configuration',
                'verbose_name_plural': 'Django Instagram Configuration',
            },
        ),
    ]
