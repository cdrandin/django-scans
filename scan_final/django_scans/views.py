from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django_scans.models import Scan
from django_scans.settings import SECRET_SCAN_KEY
import json


def home(request):
    return HttpResponse("Hello World")


def scan(request):
    payload = {'status': 'nok'}
    if request.method == 'POST':
        if request.POST.has_key('scan_id_input'):
            meta_data = {}

            if Scan.objects.filter(scan_id=request.POST['scan_id_input']).count() > 0:
                payload['reason'] = 'Scan ID already exist in system.'
            else:
                if request.POST.has_key('meta_data_input'):
                    try:
                        json_obj = json.loads(request.POST['meta_data_input'])
                        meta_data = json_obj

                        scan = Scan.objects.create(
                            scan_id=request.POST['scan_id_input'], meta_data=meta_data)
                    except Exception, e:
                        meta_data = {}

                scan = Scan.objects.create(
                    scan_id=request.POST['scan_id_input'], meta_data=meta_data)
                scan.update_last_scan_datetime()
                payload['status'] = 'ok'
        else:
            payload['reason'] = 'Missing post field "scan_id_input".'
    else:
        payload['reason'] = 'GET not accepted.'

    return JsonResponse(payload)

@csrf_exempt
def scan_csrf_exempt(request):
    payload = {'status': 'nok'}
    if request.method == 'POST':
        if request.POST.has_key('SECRET_SCAN_KEY') and request.POST['SECRET_SCAN_KEY'] == SECRET_SCAN_KEY:
            if request.POST.has_key('scan_id_input'):
                meta_data = {}

                if Scan.objects.filter(scan_id=request.POST['scan_id_input']).count() > 0:
                    payload['reason'] = 'Scan ID already exist in system.'
                else:
                    if request.POST.has_key('meta_data_input'):
                        try:
                            json_obj = json.loads(request.POST['meta_data_input'])
                            meta_data = json_obj

                            scan = Scan.objects.create(
                                scan_id=request.POST['scan_id_input'], meta_data=meta_data)
                        except Exception, e:
                            meta_data = {}

                    scan = Scan.objects.create(
                        scan_id=request.POST['scan_id_input'], meta_data=meta_data)
                    scan.update_last_scan_datetime()
                    payload['status'] = 'ok'
            else:
                payload['reason'] = 'Missing post field "scan_id_input".'
        else:
            payload['reason'] = 'Failed validation.'
    else:
        payload['reason'] = 'GET not accepted.'

    return JsonResponse(payload)
