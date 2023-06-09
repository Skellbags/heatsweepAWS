# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2023-04-01 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heatsweep', '0003_auto_20230401_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='a_start',
        ),
        migrations.RemoveField(
            model_name='game',
            name='b_start',
        ),
        migrations.RemoveField(
            model_name='game',
            name='hotspot',
        ),
        migrations.AddField(
            model_name='game',
            name='a_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='a_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='b_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='b_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='hotspot_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='hotspot_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tile',
            name='a_revealed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tile',
            name='b_revealed',
            field=models.BooleanField(default=False),
        ),
    ]
