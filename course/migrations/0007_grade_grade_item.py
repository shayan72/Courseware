# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20150131_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade_item',
            field=models.ForeignKey(blank=True, to='course.GradeItem', null=True),
            preserve_default=True,
        ),
    ]
