# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="base.html")),
    url(r'^api/', include(router.urls)),
]
