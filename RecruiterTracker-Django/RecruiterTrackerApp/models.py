from django.db import models

# Create your models here.

class Contact(models.Model):
    idcontact = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    dateadded = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'contact'

    def __str__(self):
        return self.name



class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Job(models.Model):
    idjob = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    idcontact = models.ForeignKey(Contact, models.DO_NOTHING, db_column='idcontact',verbose_name="Contact")

    class Meta:
        managed = False
        db_table = 'job'

    def __str__(self):
        return self.title
