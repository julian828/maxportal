from django.urls import path, include
from django.conf.urls import url
from timeentry import views
from rest_framework import routers

app_name = 'maxportal'

router = routers.DefaultRouter()
router.register('persons', views.PersonViewSet)
router.register('labors', views.LaborViewSet)
router.register('labtrans', views.LabtransViewSet)

urlpatterns = [
    
    
    #url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('main', views.main, name='main'),
    url('entryrecords/', views.entryrecords, name='entryrecords'),
    url('api/', include(router.urls)),
    
    ]
