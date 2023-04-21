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


