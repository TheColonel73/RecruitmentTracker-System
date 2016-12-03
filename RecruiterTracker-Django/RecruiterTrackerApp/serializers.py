from rest_framework import serializers, authentication,permissions
from .models import Contact, Job


class ContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact
        fields = ('name','telephone','email',)

"""
    idjob = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    idcontact = models.ForeignKey(Contact, models.DO_NOTHING, db_column='idcontact')
"""
class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('title', 'description')