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

2. Run `python manage.py makemigrations django_scans` to create scan table

3. Run `python manage.py migrate` to create the django_scans models.

4. POST to http://127.0.0.1:8000/django_scans/scan to insert scan item.
   POST should include {SECRET_SCAN_KEY: SECRET_SCAN_KEY, scan_id_input: '', meta_data_input*: ''}

   SECRET_SCAN_KEY can be retrieved by 
   `from django_scans.settings import SECRET_SCAN_KEY`

   * is optional

5. Visit http://127.0.0.1:8000/admin/ and checkout scan that was created.