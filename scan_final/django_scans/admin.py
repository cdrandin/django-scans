from django.contrib import admin
from django_scans.models import *


# Register your models here.
class ScanAdmin(admin.ModelAdmin):
    readonly_fields = ('entered_datetime', 'last_scan_datetime')

admin.site.register(Scan, ScanAdmin)