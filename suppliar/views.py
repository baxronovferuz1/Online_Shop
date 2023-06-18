from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Suppliar_Check
from .serializers import Suppliar_Factor,CheckOrdersDetail
from rest_framework.response import Response

class Factor(ModelViewSet):
    permission_classes=[IsAdminUser]
    queryset=Suppliar_Check.objects.filter(status='')

    def get_serializer_class(self):
        if self.action=="list":
            return Suppliar_Factor
        else:
            return CheckOrdersDetail
        
    def create(self, request, *args, **kwargs):
        if request.data["status"]==["ready"]:
            not_sended_factor=self.queryset
            for i in not_sended_factor:
                i.status="ready"
                i.save()
            return Response({"message":"All factors sent to contributed part"})


