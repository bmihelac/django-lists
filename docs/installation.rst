============
Installation
============

Installation
------------

::

    pip install django-lists

Configuration
-------------

For using `django-lists` templatetags, make sure
``TEMPLATE_CONTEXT_PROCESSORS`` settings.py variable includes request
context processor::

    TEMPLATE_CONTEXT_PROCESSORS = (
        #...
        "django.core.context_processors.request"
    )
