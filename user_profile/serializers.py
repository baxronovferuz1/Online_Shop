# target
# 1)SignUpSerializer(email,phone,password) >> "def create" funtion
# 2)UpdateProfileSerializer(username,first_name, last_name,email)
# 3)UpdateProfileRetrieve(Meta)

from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile import models
from suppliar.serializers import FactorDetail
from suppliar.models import Suppliar_Check



class SignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    #phone=serializers.CharField(max_length=14)
    password=serializers.CharField(label="password", min_length=4, max_length=80)
    confirm_password = serializers.CharField(min_length=4, max_length=80, write_only=True)
     

    # i'll must work


    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match.")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    class Meta:
        model=User
        fields=("username","email","password","confirm_password")
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

    
class MyPaymentedItemSerializer(serializers.ModelSerializer):

    address = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    factor = FactorDetail()

    def get_username(self , suppliar):
        return suppliar.reciever.username

    def get_email(self , suppliar):
        return suppliar.reciever.email 

    def get_address(self , suppliar):
        return suppliar.address.address    

    class Meta:
        model = Suppliar_Check
        fields = ('username' , 'email' , 'phone' , 'address' , 'factor')