from account.models import Person, Labor
from timeentry.models import Labtrans
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Person
        fields = ('personuid', 'personid', 'firstname', 'lastname',)
        
class LaborSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Labor
        fields =('personid', 'laborid', 'laborcode', 'status', 'portalpwd')
        
class LabtransSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Labtrans
        fields = ('labtransid', 'laborcode', 'enterdate', 'refwo', 'craft', 'regularhrs')