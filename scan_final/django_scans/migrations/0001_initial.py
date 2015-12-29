# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('scan_id', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('meta_data', jsonfield.fields.JSONField(help_text=b'Make sure valid JSON. Verify at <a href="http://jsonlint.com/" target="_blank">http://jsonlint.com/</a>', null=True, blank=True)),
                ('entered_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_scan_datetime', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
