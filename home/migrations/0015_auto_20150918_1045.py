# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20150916_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 18, 17, 45, 8, 655958, tzinfo=utc), verbose_name='Post Date'),
        ),
    ]
