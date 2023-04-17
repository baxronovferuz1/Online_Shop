# Target
# 1)UserSignupApiview
# 2)UpdateProfile

from django.shortcuts import render
from user_profile import serializers , models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserSignUPAPIView(APIView):
    serializer_class=serializers.SignUpSerializer


    def post(self, request):

        serializer=serializers.SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'You are successfuly signup dear {}'}.format(request.data["username"]))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)