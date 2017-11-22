# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:24
from __future__ import unicode_literals

from django.db import migrations


def copy_attrs(apps, schema_editor):
    current_database = schema_editor.connection.alias
    SentFullReport = apps.get_model('delivery.SentFullReport')
    NewSentFullReport = apps.get_model('delivery.NewSentFullReport')
    for instance in SentFullReport.objects.using(current_database):
        NewSentFullReport.objects.create(
            report_id=instance.report_id,
            sent=instance.sent,
            to_address=instance.to_address,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0024_newsentfullreport'),
    ]

    operations = [
        migrations.RunPython(
            copy_attrs,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
