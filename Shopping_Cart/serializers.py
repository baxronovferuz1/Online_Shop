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
    
    def create(self , validated_data):

        user = self.context['request'].user
        item = validated_data['item']
        quantity = validated_data['quantity']

        if item.quantity >= quantity:
            user_good = Shopping_Cart.objects.filter(user = user , item = item , status = 'on_cart')
            if len(user_good) == 0:
                user_good = Shopping_Cart.objects.create(user = user , item = item ,  quantity = quantity , status = 'on_cart')
                user_good.save()

            else:
                user_good = user_good[0]
                user_good.quantity += quantity
                user_good.save()

            return user_good

        else:
            raise serializers.ValidationError("There isn't sufficient quantity for this item")

    def update(self , instance , validated_data):

        item = validated_data['item']
        quantity = validated_data['quantity']

        Shopping_Cart.objects.filter(pk = instance.id).update(item = item , quantity = quantity)

        obj = Shopping_Cart.objects.get(pk = instance.id)
        return obj
    

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

    status=serializers.ChoiceField(choices=order_choice)


class Go_To_Confirmation_Step(serializers.ModelSerializer):

    visit_choices=(
        ("action","I want to take an action")
    )
    
    order=serializers.ChoiceField(choices=visit_choices)



class Pay_for_Item(serializers.ModelSerializer):
    item=ItemDetail(many=True)
    class Meta:
        model=Shopping_Cart
        fields=("item","quantity")