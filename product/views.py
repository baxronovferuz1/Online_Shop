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
        'list' : ComputerListSerializer,
        'retrieve' : ComputerDetailserializer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)
    

class ShowMobile(ReadOnlyModelViewSet):


    queryset = Mobile.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : MobileListSerializer,
        'retrieve' : MobileDetailSerializer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)
    


class ShowBook(ReadOnlyModelViewSet):


    queryset = Book.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serialzers = {
        'list' : BookListSerializer,
        'retrieve' : BookDetailSerializer
    }

    def get_serializer_class(self):
        return self.serialzers.get(self.action)
    
class ShowStationery(HyperlinkedModelSerializer):
    queryset=Stationery.objects.all()

    lookup_field='slug'

    filter_backends=(filters.SearchFilter ,)

    search_fields=('name','brand','category')

    serializers={
        'list': StationeryListSerializer,
        'retrieve':StationeryDetailSerializer
    }


    