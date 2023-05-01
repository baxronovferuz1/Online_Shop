# target for serializers.py

# 1)create ShoppingCartSerializer
# 2)/itemDetail
# 3)Iteminorderlist
# 4)iteminorderDetail

#5)Confirmation


from rest_framework import serializers
import user_profile
from product.models import BaseItem
from .models import Shopping_Cart


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    item=serializers.PrimaryKeyRelatedField(queryset=BaseItem.objects.all())
    item_name=serializers.SerializerMethodField("item_name_function")
    quantity=serializers.IntegerField()
    user_id=serializers.SerializerMethodField("user_id_func")



    def item_name_function(self, obj):
        return obj.item.name


    def user_id_func(self, obj):
        return obj.id
    

class ItemDetail(serializers.ModelSerializer):
    class Meta:
        model=BaseItem
        fields=("name","brand","category","price")


class ItemInOrderList(serializers.HyperlinkedModelSerializer):
    detail=serializers.HyperlinkedIdentityField(view_name="MyOrder-Detail" ,)

    class Meta:
        model=Shopping_Cart
        fields=("detail")

class ItemInOrderDetail(serializers.DjangoModelField):
    item=ItemDetail(many=True)

    class Meta:
        model=Shopping_Cart
        fields=("item","quantity",)




class Confirmation(serializers.ModelSerializer):

    order_choice=(
        ("accept","I accept it, go to payment"),
        ("reject","I reject it, I want to something")
    )


    

    