from django.shortcuts import render

# Create your views here.

#target for view.py
# 1)create My_Cart class

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Shopping_Cart
from .serializers import ShoppingCartSerializer


class My_Cart(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Shopping_Cart.objects.filter(user=self.request.user, status="on_cart")
    
    serializer_class=ShoppingCartSerializer