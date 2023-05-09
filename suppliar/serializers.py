# target
# 1)profile detail class
# 2)Factor detail class 




from rest_framework import serializers
from django.contrib.auth.models import User 
from user_profile.models import UserProfile
from Shopping_Cart.models import Shopping_Cart
from .models import Suppliar_Check




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


class CheckOrdersDetail(serializers.ModelSerializer):

    status_choices=(
        ("ready","ready"),
        ("on_process","on_process"),
    )

    status=serializers.ChoiceField(choices=status_choices)


class Suppliar_Factor(serializers.ModelSerializer):
    address=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()
    factor=FactorDetail


    def get_address(self, suppliar):
        return suppliar.address.address
    
    def get_email(self, suppliar):
        return suppliar.recipient.email
    
    def get_username(self,suppliar):
        return suppliar.recipient.username
    
    class Meta:
        model=Suppliar_Check
        fields=("username","address","email","factor","phone")
  