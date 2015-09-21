# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import datetime
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_subscribepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(max_length=255, default='Gentle Coffee'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post Date', default=datetime.datetime(2015, 9, 16, 11, 46, 26, 479699)),
        ),
    ]
