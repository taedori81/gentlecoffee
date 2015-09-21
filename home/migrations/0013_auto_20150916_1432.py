# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150916_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post Date', default=datetime.datetime(2015, 9, 16, 14, 32, 1, 908230)),
        ),
    ]
