# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0006_cafepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cafepage',
            name='cafe_logo_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='cafepage',
            name='area',
            field=models.ForeignKey(related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='home.Area'),
        ),
    ]
