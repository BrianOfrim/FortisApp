# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panelpage', '0002_auto_20150827_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpanel',
            name='panelSublocation',
            field=models.CharField(max_length=2, default='', blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')]),
        ),
    ]
