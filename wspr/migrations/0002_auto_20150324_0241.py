# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wspr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='day',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='hour',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
