# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_shoppage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=models.CharField(max_length=255, default='Get our favorite coffees, brewing equipment, merchandise, accessories, and more.'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(max_length=50, default='Shop'),
        ),
    ]
