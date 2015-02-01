# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20150131_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='student_number',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gradeitem',
            name='grade_type',
            field=models.CharField(default=b'OT', max_length=2, choices=[(b'EX', b'Exam'), (b'AS', b'Assignment'), (b'PR', b'Project'), (b'FI', b'Final'), (b'OT', b'OT')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, to='account.Student', null=True),
            preserve_default=True,
        ),
    ]
