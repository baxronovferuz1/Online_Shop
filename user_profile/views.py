# Target
# 1)UserSignupApiview
# 2)UpdateProfile

from django.shortcuts import render
from user_profile import serializers , models
from rest_framework.views import APIView

class UserSignUPAPIView(APIView):
    serializer_class=serializers.SignUpSerializer


    def post(self, request):

        serializer=serializers.SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()