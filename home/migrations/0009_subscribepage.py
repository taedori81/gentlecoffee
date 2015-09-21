# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0008_blogindexpage_blogpage_brewguidepage_eventindexpage_eventpage_faqpage_learnpage_ourstorypage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
