# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spot_id', models.IntegerField(unique=True)),
                ('timestamp', models.DateTimeField()),
                ('reporter', models.CharField(max_length=100)),
                ('reporter_grid', models.CharField(max_length=6)),
                ('snr', models.IntegerField()),
                ('frequency', models.DecimalField(max_digits=10, decimal_places=5)),
                ('call_sign', models.CharField(max_length=6)),
                ('grid', models.CharField(max_length=6)),
                ('power', models.IntegerField()),
                ('drift', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('azimuth', models.IntegerField()),
                ('band', models.IntegerField()),
                ('version', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
