# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150130_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='course_instance',
            field=models.OneToOneField(to='course.CourseInstance'),
            preserve_default=True,
        ),
    ]
