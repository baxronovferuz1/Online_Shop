target
1)profile detail class




from rest_framework import serializers
from django.contrib.auth.models import User 
from user_profile.models import UserProfile




class ProfileDetail(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()

    def get_username(self, profile):
        return profile.user.username
    
    
    def get_email(self, profile):
        return profile.user.emial
    
    class Meta:
        models=UserProfile
        fields=("username","email","phone","address")