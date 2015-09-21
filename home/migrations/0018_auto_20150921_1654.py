# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20150919_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post Date', default=datetime.datetime(2015, 9, 21, 23, 54, 13, 54583, tzinfo=utc)),
        ),
    ]
