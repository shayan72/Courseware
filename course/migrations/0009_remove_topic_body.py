# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20150131_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='body',
        ),
    ]
