import uuid


def uuid5():
    v = uuid.uuid5(uuid.uuid4(), __file__).hex
    return str(v)

# from django_scans_app.settings import SECRET_SCAN_KEY
# print SECRET_SCAN_KEY

SECRET_SCAN_KEY = 'nij]rYt?Jiec&iD}jUv>nOj=byB}In;oNk+yAg^Toc+eiJ(tEy' # uuid5()
