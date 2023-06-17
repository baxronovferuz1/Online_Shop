from django.shortcuts import render

# Create your views here.

#target for view.py
# 1)create My_Cart class

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Shopping_Cart
from .serializers import *
from rest_framework.response import Response
from user_profile.models import UserInformation,UserProfile


class My_Cart(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Shopping_Cart.objects.filter(user=self.request.user, status="on_cart")
    
    serializer_class=ShoppingCartSerializer


class My_Orders(ModelViewSet):
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Shopping_Cart.objects.filter(user=self.request.user, status="on_cart")
    
    serializers={
        'list':ItemInOrderList,
        'retrieve':ItemInOrderDetail,
        'create':Go_To_Confirmation_Step,
        'update':Confirmation,
    }

    
    def get_serializer_class(self):
        return self.serializers.get(self.action)
    

    
    def create(self, request, *args, **kwargs):
        return Response("Tasdiqlash yoki rad etish uchun birorta bo'limni tanlang")
    


    def update(self, request, *args, **kwargs):

        if request.data["status"]=="accept":
            obj=Shopping_Cart.objects.get(pk=int(kwargs["pk"]))
            obj.status="ready_to_payment"
            obj.save()
            return Response({"message":"Hurmatli mijoz mahsulot tasdiqlandi va to'lov olinadi"})
        
    
        else:
            obj=Shopping_Cart.objects.get(pk=int(kwargs["pk"]))
            obj.status="on_cart"
            obj.save()
            return Response({"message":"Javobingiz qabul qilindi"})
        

class Payment(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Shopping_Cart.objects.filter(user=self.request.user, status="ready_to_payment")
    


    serializers={
        "list" : Pay_for_Item
    }

    def create(self, request, *args, **kwargs):
        if request.data["status"]=="accept":
            ordered_item=Shopping_Cart.objects.filter(user=self.request.user, status="ready_to_payed")
            for ordered in ordered_item:
                ordered.status=""
                ordered.item.quantity-=ordered.quantity
                ordered.item.save()
                ordered.save()
                profile=UserProfile.objects.filter(user=self.request.user)
                address=UserInformation.objects.get(user=self.request.data["address"])
            return Response({"message":"Hurmatli mijoz, to'lovingiz muvaffaqiyatli yakunlandi"})
       
        else:
            return Response({"message":"Tolov bekor qilindi"})
        

     
    def get_serializer_class(self):
        return self.serializers.get(self.action)