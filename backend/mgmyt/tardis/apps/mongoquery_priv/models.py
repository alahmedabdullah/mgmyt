from django.db import models

# Create your models here.
from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    collection_user = models.CharField(max_length=50)
    collection_pass = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    port_number = models.IntegerField()
    database_name = models.CharField(max_length=100)
    authsource_database = models.CharField(max_length=100)
    collection_description = models.CharField(max_length=600)
    collection_uri = models.CharField(max_length=600, blank=True, null=True)
    collection_rowcount = models.IntegerField(blank=True, null=True)
    collection_querylink = models.CharField(max_length=1, blank=True, null=True)
    collection_querylimit = models.IntegerField(default=0,blank=True, null=True)

    def __str__(self):
       return self.collection_name

class UserCollection(models.Model):
    tardis_user = models.CharField(max_length=50)
    collection = models.ManyToManyField(Collection)

    def __str__(self):
       return self.tardis_user

class Job(models.Model):
    JOB_STATUS = (
        ('N','New'),
        ('R','Running'),
        ('C','Completed'),
        ('S','Success'),
        ('F','Failed'),
    )
    query_text = models.CharField(max_length=1000)
    status = models.CharField(max_length=1, choices=JOB_STATUS)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
       return self.collection + ':' + str(self.query_text)
