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

2. Include the polls URLconf in your project urls.py like this::

    url(r'^django_scans/', include('django_scans.urls')),

3. Run `python manage.py migrate` to create the django_scans models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. POST to http://127.0.0.1:8000/django_scans/scan to insert scan item.
   POST should include {SECRET_SCAN_KEY: SECRET_SCAN_KEY, scan_id_input: '', meta_data_input*: ''}
   
   SECRET_SCAN_KEY can be retrieved by 
   `from django_scans.settings import SECRET_SCAN_KEY`

   * is optional
