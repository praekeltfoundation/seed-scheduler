# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-12 20:10
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import scheduler.models


class Migration(migrations.Migration):

    dependencies = [("scheduler", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="celery_cron_definition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djcelery.CrontabSchedule",
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="celery_interval_definition",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djcelery.IntervalSchedule",
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedules_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="cron_definition",
            field=models.CharField(
                blank=True,
                max_length=500,
                null=True,
                validators=[scheduler.models.validate_crontab],
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="interval_definition",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                validators=[scheduler.models.validate_interval],
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="payload",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default={}, null=True
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedules_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
