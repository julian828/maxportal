from django.db import models
from django.conf import settings
from account.models import Person, Labor

# Create your models here.

class Labtrans(models.Model):
    
    labtransid = models.IntegerField(primary_key=True)
    laborcode = models.ForeignKey(Labor, on_delete=models.CASCADE, db_column='laborcode', to_field='laborcode')
    refwo = models.CharField(max_length=10, null=True)
    craft = models.CharField(max_length=8, null=True)
    regularhrs = models.FloatField(null=True)
    enterdate = models.DateField(null=True)
    
    class Meta:
        db_table = 'labtrans'
        
    def __unicode__(self):
        return self.labtransid
