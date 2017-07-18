=====
Usage
=====

To use django-curriculum in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_curriculum.apps.DjangoCurriculumConfig',
        ...
    )

Add django-curriculum's URL patterns:

.. code-block:: python

    from django_curriculum import urls as django_curriculum_urls


    urlpatterns = [
        ...
        url(r'^', include(django_curriculum_urls)),
        ...
    ]
