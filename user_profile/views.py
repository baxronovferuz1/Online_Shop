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


class UserSignUPAPIView(APIView):
    serializer_class=SignUpSerializer


    def post(self, request):
            
        serializer = SignUpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Your are successfuly singup dear {}'.format(request.data['username'])}) 
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
    
    serializer={
        'retrieve':UpdateProfileSerializer,
        'update':UpdateProfileSerializer,
        'partial_update':UpdateProfileSerializer,
    }


    def create(self, request):
        return Response({'message' : 'Please enter you id at the end of your url to update your profile'})
    

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
