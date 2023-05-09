target
1)profile detail class
2)Factor detail class 




from rest_framework import serializers
from django.contrib.auth.models import User 
from user_profile.models import UserProfile
from Shopping_Cart.models import Shopping_Cart




class ProfileDetail(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()

    def get_username(self, profile):
        return profile.user.username
    
    
    def get_email(self, profile):
        return profile.user.emial
    
    class Meta:
        model=UserProfile
        fields=("username","email","phone","address")


class FactorDetail(serializers.ModelSerializer):
    item=serializers.SerializerMethodField()
    quantity=serializers.SerializerMethodField()

    def get_item(self, sh_cart):
        return sh_cart.item.name
    
    def get_quantity(self, sh_cart):
        return sh_cart.quantity
    

    class Meta:
        model=Shopping_Cart
        fields=("item",'quantity')
