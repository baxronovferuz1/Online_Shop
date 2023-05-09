from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Suppliar_Check
from .serializers import Suppliar_Factor,CheckOrdersDetail

class Factor(ModelViewSet):
    permission_classes=[IsAdminUser]
    queryset=Suppliar_Check.objects.filter(status='')

    def get_serializer_class(self):
        if self.action=="list":
            return Suppliar_Factor
        else:
            return CheckOrdersDetail
        
    

