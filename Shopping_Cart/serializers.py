# target for serializers.py

# 1)create ShoppingCartSerializer
# 2)


from rest_framework import serializers
import user_profile
import product
from .models import Shopping_Cart


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
