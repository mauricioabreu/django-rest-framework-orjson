djangorestframework-orjson
======================================

|build-status-image| |pypi-version|

Overview
--------

Provides parser and renderer support for orjson library

Requirements
------------

-  Python (3.5, 3.6, 3.7)
-  Django (1.11, 2.0, 2.1)
-  Django REST Framework (3.6, 3.7, 3.8, 3.9)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install djangorestframework-orjson

Example
-------

You can use this library by adding the following lines to your settings file:

.. code:: python

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_orjson.renderers.ORJSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework_orjson.parsers.ORJSONParser',
        ),
    }

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/mauricioabreu/django-rest-framework-orjson.svg?branch=master
   :target: http://travis-ci.org/mauricioabreu/django-rest-framework-orjson?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-orjson.svg
   :target: https://pypi.python.org/pypi/djangorestframework-orjson
