# target for serializers.py

# 1)create ShoppingCartSerializer
# 2)


from rest_framework import serializers
import user_profile
from product.models import BaseItem
from .models import Shopping_Cart


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    item=serializers.PrimaryKeyRelatedField(queryset=BaseItem.objects.all())
    item_name=serializers.SerializerMethodField("item_name_function")



    def item_name_function(self, obj):
        return obj.item.name

