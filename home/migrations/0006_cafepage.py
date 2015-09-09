# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0005_cafespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
                ('cafe_name', models.CharField(default='Location Name', max_length=100)),
                ('cafe_description', wagtail.wagtailcore.fields.RichTextField()),
                ('cafe_address_line_1', models.CharField(max_length=100)),
                ('cafe_address_line_2', models.CharField(max_length=100)),
                ('cafe_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
