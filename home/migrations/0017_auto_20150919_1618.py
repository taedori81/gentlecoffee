# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20150918_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post Date', default=datetime.datetime(2015, 9, 19, 23, 18, 11, 930140, tzinfo=utc)),
        ),
    ]
