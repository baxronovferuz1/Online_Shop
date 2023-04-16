# target
# 1)SignUpSerializer(email,phone,password) >> "def create" funtion
# 2)

from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=14)
    password=serializers.CharField(label="password", min_length=4, max_length=80, style={"input_type":"password"})


    class Meta:
        model=User
        fields=("username","email","phone","password")
        write_only_fields=("password" ,) #fielddan kyn "," qo'yilsa keyin typlega aylanadi
