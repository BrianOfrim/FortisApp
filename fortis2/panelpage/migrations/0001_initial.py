# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterPanel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('panelName', models.CharField(max_length=120)),
                ('shipment', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], max_length=2)),
                ('panelLocation', models.CharField(choices=[('Assembly Table', 'Assembly Table'), ('Framing Table', 'Framing Table'), ('Sheathing Table', 'Sheathing Table'), ('ABV Table', 'ABV Table'), ('South Wall', 'South Wall'), ('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'), ('R5', 'R5'), ('R6', 'R6'), ('R7', 'R7'), ('R8', 'R8'), ('RS1', 'RS1'), ('RS2', 'RS2'), ('RS3', 'RS3'), ('T002', 'T002'), ('T006', 'T006'), ('T007', 'T007'), ('T007', 'T007'), ('T008', 'T008'), ('T016', 'T016'), ('T021', 'T021'), ('Overflow 1', 'Overflow 1'), ('Overflow 2', 'Overflow 2'), ('Overflow 3', 'Overflow 3'), ('Overflow 4', 'Overflow 4'), ('Overflow 5', 'Overflow 5'), ('Overflow 6', 'Overflow 6'), ('Overflow 7', 'Overflow 7'), ('Overflow 8', 'Overflow 8'), ('Overflow 9', 'Overflow 9'), ('Overflow 10', 'Overflow 10'), ('Site', 'Site')], max_length=15)),
                ('generalNotes', models.CharField(max_length=200, null=True)),
                ('crewInfo', models.CharField(max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
