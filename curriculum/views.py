from rest_framework import viewsets
from django.utils.translation import ugettext_lazy as _

from .models import Overview


class OverviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Overview.objects.all().order_by('-created')
    serializer_class = ProjectSerializer
