from rest_framework import serializers, authentication,permissions
from .models import Contact, Job

class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('url', 'idcontact', 'title', 'description', 'location', 'active', )


class ContactSerializer(serializers.HyperlinkedModelSerializer):

    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ('url', 'name','telephone','email', 'jobs',)

