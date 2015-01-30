# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.PositiveIntegerField()),
                ('research_interest', models.TextField()),
                ('education_background', models.TextField()),
                ('type', models.CharField(max_length=4, choices=[(b'ASSI', b'Associate Professor'), (b'ASSI', b'Assistant Professor'), (b'PROF', b'Professor')])),
                ('website', models.URLField()),
                ('account_id', models.ForeignKey(to='account.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_number', models.PositiveIntegerField()),
                ('degree_level', models.PositiveSmallIntegerField()),
                ('website', models.URLField()),
                ('account_id', models.ForeignKey(to='account.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='professor_id',
            field=models.ForeignKey(blank=True, to='account.Professor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='student_id',
            field=models.ForeignKey(blank=True, to='account.Student', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
