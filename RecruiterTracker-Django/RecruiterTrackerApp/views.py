
from rest_framework import viewsets,authentication,permissions

from .serializers import ContactSerializer, JobSerializer
from .models import Contact, Job

# Create your views here.

class DefaultsMixin(object):
    """Default settings for view authentication, permissions,filtering and pagination."""
    authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ContactViewset(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint for listing and creating contacts."""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class JobViewset(DefaultsMixin, viewsets.ModelViewSet):
    """ API endpoint for listing and creating jobs."""
    queryset = Job.objects.all()
    serializer_class = JobSerializer