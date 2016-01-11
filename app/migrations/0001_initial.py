# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.model_field_custom
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthentication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', app.models.model_field_custom.EmailFieldCaseInsensitive(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=70, blank=True)),
                ('last_name', models.CharField(max_length=70, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=45)),
                ('project_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=100)),
                ('points', models.PositiveSmallIntegerField()),
                ('stage', models.CharField(max_length=100)),
                ('project', models.ForeignKey(related_name='stories', to='app.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
                ('story', models.ForeignKey(to='app.Story')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_level', models.PositiveSmallIntegerField()),
                ('project', models.ForeignKey(related_name='team_members', to='app.Project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', app.models.model_field_custom.CharFieldCaseInsensitive(unique=True, max_length=70)),
                ('full_name', models.CharField(max_length=90, blank=True)),
                ('user_type', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(to='app.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(to='app.User'),
        ),
        migrations.AddField(
            model_name='member',
            name='org',
            field=models.ForeignKey(to='app.User'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userauthentication',
            name='profile',
            field=models.ForeignKey(related_name='pro', to='app.User'),
        ),
    ]
