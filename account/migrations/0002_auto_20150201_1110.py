# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='professor_email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='account_id',
            field=models.ForeignKey(blank=True, to='account.Account', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='education_background',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='research_interest',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='telephone',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='type',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'ASSI', b'Associate Professor'), (b'ASSI', b'Assistant Professor'), (b'PROF', b'Professor')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='website',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='account_id',
            field=models.ForeignKey(blank=True, to='account.Account', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='degree_level',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='website',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
