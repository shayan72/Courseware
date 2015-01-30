# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choosed_Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(to='course.Choice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('course_number', models.PositiveIntegerField()),
                ('credit', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.SmallIntegerField()),
                ('description', models.TextField(null=True, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('professors', models.ManyToManyField(to='account.Professor')),
                ('teacher_assistants', models.ManyToManyField(to='account.Student', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.PositiveIntegerField()),
                ('student', models.ForeignKey(to='account.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GradeItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('max_grade', models.PositiveIntegerField()),
                ('coefficient', models.PositiveIntegerField()),
                ('assignment', models.ForeignKey(blank=True, to='course.Assignment', null=True)),
                ('course_instance', models.ForeignKey(to='course.CourseInstance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('anonymous', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.ForeignKey(to='account.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=2, choices=[(b'SA', b'Saturday'), (b'SU', b'Sunday'), (b'MO', b'Monday'), (b'TU', b'Tuesday'), (b'WE', b'Wednesday'), (b'TH', b'Thursday'), (b'FR', b'Friday')])),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('is_ta', models.BooleanField(default=False)),
                ('course_instance', models.ForeignKey(to='course.CourseInstance')),
                ('room_id', models.ForeignKey(to='course.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('grading_policy', models.TextField(null=True, blank=True)),
                ('course_instance', models.ForeignKey(to='course.CourseInstance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('semester', models.CharField(max_length=2, choices=[(b'FA', b'Fall'), (b'SP', b'Spring'), (b'SU', b'Summer')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('view_num', models.IntegerField(default=0)),
                ('locked', models.BooleanField(default=False)),
                ('anonymous', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('course_instance', models.ForeignKey(to='course.CourseInstance')),
                ('created_by', models.ForeignKey(to='account.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UploadedAssignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField()),
                ('assignment', models.ForeignKey(to='course.Assignment')),
                ('student', models.ForeignKey(to='account.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='text_books',
            field=models.ManyToManyField(to='course.TextBook', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='course.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='poll',
            name='topic',
            field=models.OneToOneField(to='course.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='term',
            field=models.ForeignKey(to='course.Term'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choosed_choice',
            name='poll',
            field=models.ForeignKey(to='course.Poll'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choosed_choice',
            name='voted_by',
            field=models.ForeignKey(to='account.Account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(to='course.Poll'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendar',
            name='course_instance',
            field=models.ForeignKey(to='course.CourseInstance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='course_instance',
            field=models.ForeignKey(to='course.CourseInstance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='created_by',
            field=models.ForeignKey(to='account.Account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='course_instance',
            field=models.ForeignKey(to='course.CourseInstance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='created_by',
            field=models.ForeignKey(to='account.Account'),
            preserve_default=True,
        ),
    ]
