=====
Django Scans
=====

Quick start
-----------

1. Add "django_scans" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_scans',
    )

2. Include 

	urlpatterns = patterns('',
	    url(r'^django_scans/', include('django_scans.urls')),
	)

	into your root project's(not the app) urls.py inside urlpatterns
	(or anywhere if you want)

3. Run `python manage.py makemigrations django_scans` to create scan table

4. Run `python manage.py migrate` to create the django_scans models.

5. 1 view for scanning with csrf is found at django_scans.views.scan, whereas, scanning with csrf exempt then use
	django_scans.views.scan_csrf_exempt.
	if scan_csrf_exempt is used make sure to include SECRET_SCAN_KEY. This is a simple form of validation.
	
	POST to http://127.0.0.1:8000/django_scans/scan_csrf_exempt OR in a template {% url 'django_scans.views.scan_csrf_exempt' %} to insert scan item.
	POST should include {SECRET_SCAN_KEY: SECRET_SCAN_KEY, scan_id_input: '' [, meta_data_input: '']}
	(omit secret key for scan with csrf)
   --------------
   [] is optional

   SECRET_SCAN_KEY can be retrieved by 
   `from django_scans.settings import SECRET_SCAN_KEY`

6. Visit http://127.0.0.1:8000/admin/ and checkout scan that was created.

--------------

If you want to handle your own creation of scan objects.

# make sure to catch error for duplicate scan ids. They aren't allowed. meta_data is option. The datetime fields manage themselves.

scan = Scan.objects.create(scan_id=request.POST['scan_id_input'], meta_data=equest.POST['meta_data_input'])
scan.save() # always make sure to save right after
