# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resources',
            new_name='Resource',
        ),
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, to='course.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='teacher_assistants',
            field=models.ManyToManyField(related_name='course_teacher_assistants', null=True, to='account.Student', blank=True),
            preserve_default=True,
        ),
    ]
