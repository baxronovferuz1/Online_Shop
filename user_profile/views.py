# Target
# 1)UserSignupApiview
# 2)UpdateProfile

from django.shortcuts import render
from user_profile.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from Shopping_Cart.models import *
from Shopping_Cart.serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet


class UserSignUPAPIView(APIView):
    serializer_class=SignUpSerializer


    def post(self, request):
            
        serializer = SignUpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Your are successfuly singup dear {}'.format(request.data['username'])}) 
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST) #elseni o'rniga

class UpdateProfileView(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
    
    serializer={
        'list':ShowProfileserializer,
        'retrieve':UpdateProfileSerializer,
        'update':UpdateProfileSerializer,
    }
    



    def update(self,request, *args, **kwargs):

        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']

        user_obj = User.objects.get(pk = int(kwargs['pk']))
        user_obj.username = username
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.email = email
        user_obj.save()

        return Response({'message' : 'Your profile was updated dear {0} {1}'.format(first_name , last_name)}) 
    

    

    
    def get_serializer_class(self):
        return self.serializer.get(self.action)




class ShowMyShoppingCartView(ReadOnlyModelViewSet):

    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Shopping_Cart.objects.filter(user = self.request.user , status = 'on_cart')

    serializer = {
        'list' : ShoppingCartSerializer,
        'retrieve' : ItemInOrderDetail
    }  

    def get_serializer_class(self):
        return self.serializer.get(self.action)