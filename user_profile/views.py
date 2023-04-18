# Target
# 1)UserSignupApiview
# 2)UpdateProfile

from django.shortcuts import render
from user_profile import serializers , models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserSignUPAPIView(APIView):
    serializer_class=serializers.SignUpSerializer


    def post(self, request):

        serializer=serializers.SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'You are successfuly signup dear {}'}.format(request.data["username"]))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(ModelViewSet):

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
    
    serializer={
        'retrieve':serializers.UpdateProfileSerializer,
        'update':serializers.UpdateProfileSerializer,
        'partial_update':serializers.UpdateProfileSerializer,
    }


    def create(self, request):
        return Response({'message' : 'Please enter you id at the end of your url to update your profile'})