# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_username', models.CharField(max_length=256)),
                ('twitter_key', models.CharField(max_length=256)),
                ('avatar', sorl.thumbnail.fields.ImageField(upload_to=users.models.get_image_path)),
                ('job_title', models.CharField(max_length=256)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
