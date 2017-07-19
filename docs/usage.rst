=====
Usage
=====

To use django-curriculum in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'curriculum',
        ...
    )

Create migrations and run migrations: ::

    python manage.py makemigrations curriculum
    python manage.py migrate curriculum


Add django-curriculum's URL patterns:

.. code-block:: python


    urlpatterns = [
        ...
        url(r'^api/curriculum/', include('curriculum.urls')),
        ...
    ]
