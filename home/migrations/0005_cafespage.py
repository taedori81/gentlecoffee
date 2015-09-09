# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0004_auto_20150907_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafesPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='wagtailcore.Page')),
                ('header', models.CharField(max_length=255, default='Find your Gentle Coffee Cafes')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
