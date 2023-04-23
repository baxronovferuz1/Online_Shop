from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet , ModelViewSet , ViewSet
# Create your views here.

from .models import Television,Computer,Book,Stationery,Mobile
from .serializers import *
from rest_framework import filters
from rest_framework.decorators import action
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.reverse import NoReverseMatch, reverse
from rest_framework.response import Response


class APIRootView(APIView):

    _ignore_model_permissions = True
    schema = None  # exclude from schema
    api_root_dict = None

    def get(self, request, *args, **kwargs):
        # Return a plain {"name": "hyperlink"} response.
        ret = OrderedDict()
        namespace = request.resolver_match.namespace
        for key, url_name in self.api_root_dict.items():
            if namespace:
                url_name = namespace + ':' + url_name
            try:
                ret[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get('format', None)
                )
            except NoReverseMatch:
                # Don't bail out if eg. no list routes exist, only detail routes.
                continue
        
        list_of_categories = []
        dict1_of_categories = {}
        dict2_of_categories = {}
        dict3_of_categories = {}

        dict1_of_categories['Home_appliance'] = [{'Refrigerator' : ret['Refrigerator']} , {'TV' : ret['TV']}]
        dict2_of_categories['Digital_Products'] = [{'Laptob' : ret['Laptob']} , {'Mobile' : ret['Mobile']}]
        dict3_of_categories['Educational'] = [{'Book' : ret['Book']} , {'Stationery' : ret['Stationery']}]

        list_of_categories.append(dict1_of_categories)
        list_of_categories.append(dict2_of_categories)
        list_of_categories.append(dict3_of_categories)

        return Response(list_of_categories)




class ShowTelevisions(ReadOnlyModelViewSet):

    queryset = Television.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serializers = {
        'list' : TelevisionListSerializer ,
        'retrieve' : TelevisionDetailSerilizer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)
    



class ShowComputer(ReadOnlyModelViewSet):

    queryset = Computer.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serializers = {
        'list' : ComputerListSerializer,
        'retrieve' : ComputerDetailserializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)
    

class ShowMobile(ReadOnlyModelViewSet):


    queryset = Mobile.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serializers = {
        'list' : MobileListSerializer,
        'retrieve' : MobileDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)
    


class ShowBook(ReadOnlyModelViewSet):


    queryset = Book.objects.all()

    lookup_field = 'slug'

    filter_backends = (filters.SearchFilter , )
    search_fields = ('name' , 'brand' , 'category')

    serializers = {
        'list' : BookListSerializer,
        'retrieve' : BookDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)
    
    
class ShowStationery(ReadOnlyModelViewSet):
    queryset=Stationery.objects.all()

    lookup_field='slug'

    filter_backends=(filters.SearchFilter ,)

    search_fields=('name','brand','category')

    serializers={
        'list': StationeryListSerializer,
        'retrieve':StationeryDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)
    



    