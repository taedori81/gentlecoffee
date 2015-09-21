# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150916_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock((('first_name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('last_name', wagtail.wagtailcore.blocks.CharBlock(required=True))), icon='user'))), blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post Date', default=datetime.datetime(2015, 9, 16, 12, 36, 6, 103744)),
        ),
    ]
