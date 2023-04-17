# target
# 1)SignUpSerializer(email,phone,password) >> "def create" funtion
# 2)UpdateProfileSerializer(username,first_name, last_name,email)
# 3)UpdateProfileRetrieve(Meta)

from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile import models



class SignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=14)
    password=serializers.CharField(label="password", min_length=4, max_length=80, style={"input_type":"password"})
     

    # i'll must work
    

    class Meta:
        model=User
        fields=("username","email","phone","password")
        write_only_fields=("password" ,) #fielddan kyn "," qo'yilsa keyin typlega aylanadi


class UpdateProfileRetrieve(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields='__all__'


class UpdateProfileSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=40)
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    email=serializers.CharField(max_length=60)



class AddressesDetail(serializers.ModelSerializer):
    class Meta:
        model=models.UserInformation
        fields=('address', )



class ShowProfileserializer(serializers.Serializer):
    user=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    phone=serializers.SerializerMethodField()



    def get_user(self, user):  #i will must work
        return user.username
    

    
    def get_email(self, user):
        return user.email
    

    def get_phone(self, user):
        return user.users.phone
    
    class Meta:
        model=User
        fields=('user','email','phone','id')

    
