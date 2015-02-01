# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20150131_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeitem',
            name='coefficient',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
