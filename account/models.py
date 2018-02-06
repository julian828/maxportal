from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    personuid = models.IntegerField(primary_key=True)
    personid = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=50, null=True)
    
    
    class Meta:
        db_table = 'person'
    
    
    def __unicode__(self):
        return self.personid
    
#class Person_ext(models.Model):
#    ownerid = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
#    aln1 = models.CharField(max_length=50, null=True)
#    
#    
#    class Meta:
#        db_table = 'person_ext'
#        
#    def __unicode__(self):
#        return self.aln1

class Labor(models.Model):
    
    laborid = models.IntegerField(primary_key=True)
    laborcode = models.CharField(max_length=8, unique=True)
    status = models.CharField(max_length=12, null=True)
    portalpwd = models.CharField(max_length=50, null=True)
    personid = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='personid', to_field='personid')
    
    class Meta:
        db_table = 'labor'
        
    def __unicode__(self):
        return self.laborcode
    
















    
    
    
    
    