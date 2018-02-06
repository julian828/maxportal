from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from timeentry.models import Labtrans
from account.models import Person, Labor
from timeentry.serializers import PersonSerializer, LaborSerializer, LabtransSerializer
from timeentry import urls

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class LaborViewSet(viewsets.ModelViewSet):
    
    queryset = Labor.objects.all()
    serializer_class = LaborSerializer
    filter_fields = ('laborcode',)
    
class LabtransViewSet(viewsets.ModelViewSet):
    
    queryset = Labtrans.objects.all()
    serializer_class = LabtransSerializer
    filter_fields = ('laborcode', 'labtransid',)
    ordering_fields = '__all__'
    
    '''
    def get_queryset(self):
        queryset = Labtrans.objects.all()
        slaborcode = self.request_query_param.get('laborcode', None)
        if slaborcode is not None:
            queryset = queryset.filter(laborcode = slaborcode)
        return queryset
    '''
    
def main(request):
    
    return render(request, 'main.html')

def entryrecords(request):
    
    return render(request, 'entryrecords.html')