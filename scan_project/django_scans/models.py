from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

import datetime
import collections
import json


class Scan(models.Model):
    scan_id = models.CharField(max_length=60, primary_key=True)
    meta_data = JSONField(
        # load_kwargs={'object_pairs_hook': collections.OrderedDict}, 
        null=True, blank=True,
        help_text='Make sure valid JSON. Verify at <a href="http://jsonlint.com/" target="_blank">http://jsonlint.com/</a>')
    entered_datetime = models.DateTimeField(auto_now_add=True)
    last_scan_datetime = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # First time ONLY
        if not self.pk:
            if self.scan_id is None or self.scan_id == '':
                raise Exception("scan_id cannot be empty")

            if self.meta_data:
                if type(self.meta_data) is str:
                    self.meta_data = json.loads(self.meta_data)

        super(Scan, self).save(*args, **kwargs)

    def update_last_scan_datetime(self):
        self.last_scan_datetime = datetime.datetime.now()
        self.save()

    #
    # Pacific Standard Time (PST) is 8 hours behind Coordinated Universal Time.
    # https://www.timeanddate.com/time/zones/pst
    #
    def clean_entered_datetime(self, offset_from_UTC=0, _24_hour_clock=False):
        datetime_format = ("%x", "%H:%M") if _24_hour_clock else (
            "%x", "%I:%M %p")
        local_datetime = self.entered_datetime - \
            datetime.timedelta(hours=offset_from_UTC)
        return (local_datetime.strftime(datetime_format[0]), local_datetime.strftime(datetime_format[1]))

    #
    # Pacific Standard Time (PST) is 8 hours behind Coordinated Universal Time.
    # https://www.timeanddate.com/time/zones/pst
    #
    def clean_last_scan_datetime(self, offset_from_UTC=0, _24_hour_clock=False):
        datetime_format = ("%x", "%H:%M") if _24_hour_clock else (
            "%x", "%I:%M %p")
        local_datetime = self.last_scan_datetime - \
            datetime.timedelta(hours=offset_from_UTC)
        return (local_datetime.strftime(datetime_format[0]), local_datetime.strftime(datetime_format[1]))

    def __str__(self):
        return 'scan ID #: %s' % (self.scan_id)

    def __repr__(self):
        return 'scan ID #: %s' % (self.scan_id)

    def __unicode__(self):
        return 'scan ID #: %s' % (self.scan_id)
