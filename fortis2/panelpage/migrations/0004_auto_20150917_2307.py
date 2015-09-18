# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panelpage', '0003_auto_20150827_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageOptions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('pageChoice', models.CharField(choices=[('office', 'office'), ('worker', 'worker')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='enterpanel',
            name='panelSublocation',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='  ', max_length=2, blank=True),
        ),
    ]
