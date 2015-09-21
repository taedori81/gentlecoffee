# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0015_auto_20150918_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CoffeePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MerchandisePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 18, 23, 49, 43, 488430, tzinfo=utc), verbose_name='Post Date'),
        ),
    ]
