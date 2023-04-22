from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
# Create your views here.

from .models import Television,Computer,Book,Stationery,Mobile
from .serializers import *
from rest_framework import filters



class ShowTelevisions(ReadOnlyModelViewSet):

    queryset = Television.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : TelevisionListSerializer ,
        'retrieve' : TelevisionDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)
    


class ShowComputer(ReadOnlyModelViewSet):

    queryset = Computer.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : Com,
        'retrieve' : TelevisionDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)