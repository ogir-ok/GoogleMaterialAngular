# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 12:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCredentials',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='google_credential', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
            ],
        ),
    ]