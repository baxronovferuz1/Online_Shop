from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer , SerializerMethodField 

from .models import BaseItem,Television,Computer,Mobile,Book,Stationery



class TelevisionListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Television
        fields = ('name' , 'brand' , 'category' , 'price' , 'quantity' , 'image' , 'detail')
        lookup_field = 'slug'
        extra_kwargs = {'detail': {'lookup_field': 'slug'}}




class TelevisionDetailSerilizer(ModelSerializer):
    class Meta:
        model = Television
        fields = '__all__'



class ComputerListSerializer(HyperlinkedModelSerializer):
    model=Computer
    fields=('name' , 'brand' , 'category' , 'price' , 'quantity' , 'image' , 'detail')
    lookup_field='slug'
    extra_kwargs={'detail':{'lookup_field':'slug'}}



class ComputerDetailserializer(ModelSerializer):
    class Meta:
        model=Computer
        fields='__all__'



class MobileListSerializer(HyperlinkedModelSerializer):
    model=Mobile
    fields=('name' , 'brand' , 'category' , 'price' , 'quantity' , 'image' , 'detail')
    lookup_field='slug'
    extra_kwargs={'detail':{'lookup_field':'slug'}}


class MobileDetailSerializer(ModelSerializer):
    class Meta:
        model=Mobile
        fields='__all__'




class BookListSerializer(HyperlinkedModelSerializer):
    model=Book
    fields=('name' , 'brand' , 'category' , 'price' , 'quantity' , 'image' , 'detail')
    lookup_field='slug'
    extra_kwargs={'detail':{'lookup_field':'slug'}}


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'



class StationeryListSerializer(HyperlinkedModelSerializer):
    model=Stationery
    fields=('name' , 'brand' , 'category' , 'price' , 'quantity' , 'image' , 'detail')
    lookup_field='slug'
    extra_kwargs={'detail':{'lookup_field':'slug'}}


class StationeryDetailSerializer(ModelSerializer):
    class Meta:
        model=Stationery
        fields='__all__'