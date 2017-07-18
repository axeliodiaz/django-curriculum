# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_curriculum.urls import urlpatterns as django_curriculum_urls

urlpatterns = [
    url(r'^', include(django_curriculum_urls, namespace='django_curriculum')),
]
