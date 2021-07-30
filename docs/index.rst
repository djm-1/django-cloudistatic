.. django-cloudistatic documentation master file, created by
   sphinx-quickstart on Fri Jul 30 20:42:07 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-cloudistatic's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


===================
django-cloudistatic
===================

django-cloudistatic is a Django app to upload your staticfiles to Cloudinary and serve from there.
Cloudinary serves files using CDN, which will reduce the load on django server and pages will load 
faster.

`Github Repo<https://github.com/djm-1/django-cloudistatic>`
`PYPI page<https://pypi.org/project/django-cloudistatic/>`

Quick start
-----------

1. Add "djangocloudistatic" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djangocloudistatic',
    ]

2. Declare the following settings variables (you will get them from Cloudinary dashboard) ::

      CLOUDI_NAME = <Cloud name>
      CLOUDI_API_KEY = <API Key>
      CLOUDI_API_SECRET = <API Secret> 

3. Include ``STATICFILES_DIRS`` and ``STATIC_ROOT`` in settings.py file (Should be included before ``STATIC_URL``)
   of your project. You may refer to https://docs.djangoproject.com/en/3.2/howto/static-files/ for details.

4. Modify the ``STATIC_URL`` like this::

      STATIC_URL=f'https://res.cloudinary.com/{CLOUDI_NAME}/raw/upload/v1/{STATIC_ROOT}/' 

5. Now run ``python manage.py collectstatic`` command to collect all staticfiles to STATIC_ROOT
   of your project. 

6. Finally, run ``python manage.py cloudistatic`` to upload staticfiles to Cloudinary. Wait for a few minutes
   and your staticfiles will be ready to be served from there. If you want to delete your local STATIC_ROOT (staticfiles will not be served from here now) after
   uploading to cloud, then you should run ``python manage.py cloudistatic --deletelocal`` instead of 
   ``python manage.py cloudistatic``.